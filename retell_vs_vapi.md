## Latency and Stability

#### Retell AI

Estimated latency shows to be around 900-1300ms during testing. Actual latency can go above 1300ms at times.

During testing, retell AI had stable and good performance.

#### Vapi

It claims to be around 1000ms according to dashboard

During testing, Vapi has good performance for both latency and stability.

**NOTE**: During testing there are no notable differences between Retell and Vapi in terms of performance.

## Pricing

#### Retell AI

Pricing depends on the models and services that you select.

Pay-as-you-go: 0.07-0.31/min. Enterprise: as low as 0.03/min.

Example: GPT-4o + 11labs + telephony + 1 knowledge base -> $0.14/min

We should expect to pay around \$0.14/min if using pay-as-you-go option

Retell AI Pricing Page: https://www.retellai.com/pricing

#### Vapi

Pay-as-you-go: bring in our own Voice + LLM, the only fee they charge is the orchestration fee of \$0.05/min, total round up to \$0.15/min. (According to their support team)

Agency (coming soon): \$400/month for 4000 minutes + \$0.14/min for bundled minute overage

Startup (coming soon): \$800/month for 10000 minutes + \$0.12/min for bundled minute overage

Enterpise (Custom): Need to contact their support team to set up.

They have startup program for eligible applicants: free 100,000 mins every month for the first 10 months.

Vapi Pricing Page: https://vapi.ai/pricing

## Model Customization

## Retell AI

LLM: OpenAI, Claude, Gemini, or your own custom model. Nothing for TTS or STT. Cannot bring in your own API key.

TTS (Text to Speech): Elevenlabs, PlayHT, OpenAI

## Vapi

LLM: OpenAI, Claude, Gemini, Together-AI, or your own custom model.

STT (Speech to Text): Deepgram, Azure

TTS (Speech to Text): Vapi, Deepgram, 11Labs, Azure, PlayHT, etc

Highly Customizable. We can bring in our own api keys for all the TTS, STT, LLM models. i.e. 11labs, openai, anthropic, deepgram, etc

## Post-call Analytics

#### Retell AI

-   Call counts
-   Call duration
-   Call latency
-   Successful call counts
-   User sentiment analysis
-   Disconnection reason analysis
-   Call picked up rate
-   Call successful rate
-   Call transfer rate
-   Voicemail rate
-   Use of LLM to analyze the call information
-   Webhooks for further analysis after the call to extract info

#### Vapi

-   Call counts
-   Call Duration
-   Successful call counts
-   Disconnection reason
-   Call transfer count
-   Success evaluation (using LLM)
-   Structured data extraction (using LLM)
-   Custom LLM analysis
-   Post-call webhooks

## Concurrency

#### Retell AI

20 concurrencies for free + \$8 per concurrency per month

#### Vapi

Pay-as-you-go: 10 concurrencies for free + \$10 / line / month
Agency: 50 concurrencies for free + \$10 / line / month
Start-up: 100 concurrencies for free + \$10 / line / month

## Knowledge Base

#### Retell AI

File upload + webpages (URL)

#### Vapi

File upload

## Integration

Both have extensive integrations

#### Retell AI

Twilio, Vonage, Telnyx, Cal.com, Stripe, Azure, Hubspot, etc.

#### Vapi

Twilio, Vonage, Telnyx, AWS S3, Supabase, Langfuse, etc

## Conversation Flow

In terms of conversation flow customization, both services provide similar level of customization

Both services provide common functionalities. You have a conversation flow graph of nodes connected by edges.

Nodes can perform tasks such as conversation (where you prompt the LLM with specific tasks), logic split (condition check), digit press, call transfer, call end, functions, API queries, etc.

## Special Feature

Vapi has **Squads**, where you can connect multiple assistants into one conversation flow.
