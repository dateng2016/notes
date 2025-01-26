import os
import logging
from typing import List, Dict
import pandas as pd
from openai import OpenAI
import json
from dataclasses import dataclass
import psycopg2
from psycopg2.extras import DictCursor
from logging.handlers import RotatingFileHandler


@dataclass
class DatabaseConfig:
    host: str
    database: str
    user: str
    password: str
    port: int


def setup_logging(log_file: str = "review_analyzer.log"):
    """Configure logging with both file and console handlers."""
    logger = logging.getLogger("ReviewAnalyzer")
    logger.setLevel(logging.INFO)

    # Create formatters
    file_formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(funcName)s:%(lineno)d - %(message)s"
    )
    console_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

    # File handler with rotation
    file_handler = RotatingFileHandler(
        log_file, maxBytes=10 * 1024 * 1024, backupCount=5
    )
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(file_formatter)

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(console_formatter)

    # Add handlers
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger


class ReviewAnalyzer:
    def __init__(self, db_config: DatabaseConfig, openai_api_key: str):
        self.db_config = db_config
        self.client = OpenAI(api_key=openai_api_key)
        self.logger = setup_logging()
        self.logger.info("Initializing ReviewAnalyzer")
        self.review_evalution_prompt = """You are a specialist LLM for evaluating driver performance.
      
       Given the following **input** in JSON format:
       - A **customer review** (free-form text)
       - An **order rating** (numeric)
       - A **driver rating** (numeric)
 
       **Task**:
       - Analyze the review and ratings
       - Determine each factor's rating: "positive", "negative", or "neutral"
       - Provide **details** for each factor in **<= 10 words**
       - Generate a **summary** in **1–2 sentences**
 
       ###Most important Guideline
       Never hallucinate the sentiment of the factors. Only mark:
       - 'positive' if specifically praised
       - 'negative' if specifically criticized
       - 'neutral' if not mentioned"""

        self.review_schema: Dict[str, str] = {
            "name": "DriverPerformanceEvaluation",
            "strict": True,
            "schema": {
                "type": "object",
                "$defs": {},
                "required": [
                    "summary",
                    "manner",
                    "manner_details",
                    "communication",
                    "communication_details",
                    "address_correctness",
                    "address_correctness_details",
                    "order_completeness",
                    "order_completeness_details",
                    "timeliness",
                    "timeliness_details",
                    "instruction_following",
                    "instruction_following_details",
                ],
                "properties": {
                    "summary": {
                        "type": "string",
                        "description": "A concise summary of the driver's overall performance.",
                    },
                    "manner": {
                        "type": "string",
                        "enum": ["positive", "negative", "neutral"],
                        "description": "Evaluation of driver's manner or professionalism.",
                    },
                    "manner_details": {
                        "type": "string",
                        "description": "Specifics (<= 10 words) describing the manner rating.",
                    },
                    "communication": {
                        "type": "string",
                        "enum": ["positive", "negative", "neutral"],
                        "description": "Evaluation of driver's communication.",
                    },
                    "communication_details": {
                        "type": "string",
                        "description": "Specifics (<= 10 words) describing the communication rating.",
                    },
                    "address_correctness": {
                        "type": "string",
                        "enum": ["positive", "negative", "neutral"],
                        "description": "Evaluation of driver's address correctness.",
                    },
                    "address_correctness_details": {
                        "type": "string",
                        "description": "Specifics (<= 10 words) describing address correctness rating.",
                    },
                    "order_completeness": {
                        "type": "string",
                        "enum": ["positive", "negative", "neutral"],
                        "description": "Evaluation of how complete the orders were.",
                    },
                    "order_completeness_details": {
                        "type": "string",
                        "description": "Specifics (<= 10 words) describing the order completeness rating.",
                    },
                    "timeliness": {
                        "type": "string",
                        "enum": ["positive", "negative", "neutral"],
                        "description": "Evaluation of driver's timeliness.",
                    },
                    "timeliness_details": {
                        "type": "string",
                        "description": "Specifics (<= 10 words) describing the timeliness rating.",
                    },
                    "instruction_following": {
                        "type": "string",
                        "enum": ["positive", "negative", "neutral"],
                        "description": "Evaluation of how well the driver followed instructions.",
                    },
                    "instruction_following_details": {
                        "type": "string",
                        "description": "Specifics (<= 10 words) describing the instruction-following rating.",
                    },
                },
                "additionalProperties": False,
            },
        }

    def fetch_reviews(self, carrier_id: str) -> List[Dict]:
        self.logger.info(f"Fetching reviews for carrier_id: {carrier_id}")
        try:
            with psycopg2.connect(**vars(self.db_config)) as conn:
                with conn.cursor(cursor_factory=DictCursor) as cur:
                    cur.execute(
                        """
                       SELECT r.rating as order_rating, r.driver_rating, r.review
                       FROM review r
                       WHERE r.carrier_id = %s
                       ORDER BY order_id DESC
                       LIMIT 100
                       """,
                        (carrier_id,),
                    )
                    results = [dict(row) for row in cur.fetchall()]
                    self.logger.info(f"Successfully fetched {len(results)} reviews")
                    return results
        except psycopg2.Error as e:
            self.logger.error(f"Database error while fetching reviews: {str(e)}")
            raise
        except Exception as e:
            self.logger.error(f"Unexpected error while fetching reviews: {str(e)}")
            raise

    def analyze_review(self, review_data: Dict) -> Dict:
        self.logger.debug(f"Analyzing review: {review_data.get('review')[:100]}...")
        try:
            input_json = {
                "review": review_data["review"],
                "order_rating": review_data["order_rating"],
                "driver_rating": review_data["driver_rating"],
            }

            completion = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": self.review_evalution_prompt},
                    {"role": "user", "content": json.dumps(input_json)},
                ],
                response_format={
                    "type": "json_schema",
                    "json_schema": self.review_schema,
                },
            )
            analysis = json.loads(completion.choices[0].message.content)
            self.logger.debug(
                f"Successfully analyzed review. Summary: {analysis.get('summary')}"
            )
            return analysis
        except Exception as e:
            self.logger.error(f"Error analyzing review: {str(e)}")
            raise

    def process_reviews(self, reviews: List[Dict]) -> None:
        self.logger.info(f"Processing {len(reviews)} reviews")
        factors = [
            "manner",
            "communication",
            "address_correctness",
            "order_completeness",
            "timeliness",
            "instruction_following",
        ]

        for i, review_data in enumerate(reviews, 1):
            try:
                self.logger.info(f"Processing review {i}/{len(reviews)}")
                analysis = self.analyze_review(review_data)
                analysis["review"] = review_data["review"]
                analysis["order_rating"] = review_data["order_rating"]
                analysis["driver_rating"] = review_data["driver_rating"]

                # CSV operations with error handling
                try:
                    pd.DataFrame([analysis]).to_csv(
                        "driver_evaluation.csv",
                        mode="a",
                        header=not os.path.exists("driver_evaluation.csv"),
                        index=False,
                    )
                    self.logger.debug("Successfully appended to driver_evaluation.csv")
                except Exception as e:
                    self.logger.error(
                        f"Error writing to driver_evaluation.csv: {str(e)}"
                    )
                    raise

                # Aggregation operations
                try:
                    self._update_aggregation_counts(analysis, factors)
                    self.logger.debug("Successfully updated aggregation counts")
                except Exception as e:
                    self.logger.error(f"Error updating aggregation counts: {str(e)}")
                    raise

            except Exception as e:
                self.logger.error(f"Error processing review {i}: {str(e)}")
                continue

    def _update_aggregation_counts(self, analysis: Dict, factors: List[str]) -> None:
        try:
            pos_counts = (
                pd.read_csv("positive_aggregation.csv")
                if os.path.exists("positive_aggregation.csv")
                else pd.DataFrame([{factor: 0 for factor in factors}])
            )
            neg_counts = (
                pd.read_csv("negative_aggregation.csv")
                if os.path.exists("negative_aggregation.csv")
                else pd.DataFrame([{factor: 0 for factor in factors}])
            )

            for factor in factors:
                if analysis[factor] == "positive":
                    pos_counts[factor].iloc[0] += 1
                elif analysis[factor] == "negative":
                    neg_counts[factor].iloc[0] += 1

            pos_counts.to_csv("positive_aggregation.csv", index=False)
            neg_counts.to_csv("negative_aggregation.csv", index=False)
        except Exception as e:
            self.logger.error(f"Error in _update_aggregation_counts: {str(e)}")
            raise


def main():
    logger = setup_logging()
    logger.info("Starting review analysis process")

    try:
        db_config = DatabaseConfig(
            host="",
            database="",
            user="",
            password="",
            port=5432,
        )

        analyzer = ReviewAnalyzer(
            db_config=db_config,
            openai_api_key="",
        )

        carrier_ids = [244467, 71480]
        for carrier_id in carrier_ids:
            logger.info(f"Processing carrier_id: {carrier_id}")
            reviews = analyzer.fetch_reviews(carrier_id)
            analyzer.process_reviews(reviews)
            logger.info(f"Completed processing for carrier_id: {carrier_id}")

        logger.info("Review analysis process completed successfully")
    except Exception as e:
        logger.error(f"Fatal error in main process: {str(e)}")
        raise


if __name__ == "__main__":
    main()
