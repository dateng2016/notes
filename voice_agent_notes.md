#Retell AI
500ms latency???

## Features

-   Auto-Sync Knowledge Base -> Webpages + Documents
-   Call Transfer between multiple agents (We are currently only focusing on SDRs??)
-   Appointment Booking
-   Naviagte IVR
-   Branded Call ID
-   Batch Calling
-   Verified Phone Number (No Spam Label)
-   Multilingual Support
-   Post-Call Analysis
-   Websites for knowledge base (this gives most updated info)

### Call Transfer

-   Warm/Cold Transfer

### Knowledge Base

-   Upload Webpage
-   Single page or entire website
-   Real-Time Update
-
-   Upload Document

-   Test the knowledge in the playground

### Book Appointment

-   check availability function and book appointment function

### Post-Call Analysis

-   Can integrate the analysis data into our own work flow

Conversation Flow Features gives custom control to user on how the conversation should go.

Multi prompt option gives a much more fine-grained control on the prompt for the model.

# VAPI

## Features

-   Multilingual
-   API-Native
-   Automated Testing
-   Bring your own models
-   Tool calling (plug in your own APIs as tools)
-   File upload for providing context for assistants
-   provider keys configuration
-   Offers custom LLM(Fine-tuned LLM), Voices, Transcribers...
-   Default tooloing -> transfer calls, end call, dial keypad,
-   Also has workflows that controls the flow of the conversation.

Call transfer -> warm / cold

# Synthflow

MORE RESEARCH TO BE DONE

# BLAND AI

# Play AI

# Comparison

Comparison Points: Latency, Integration, Concurrency, Custom Telephony, Knowledge Base, Special Feature?

## Retell AI

Pay-as-you-go users can have 20 concurrent calls. This can be adjusted with cost.

Latency varies from 500-900ms

Use GPT-4o or custom LLM models (lack of choices)

Did not find any info on TTS and STT models they use (less flexible)

Comprehensive post-call analysis: have analysis on user sentiments, disconnect reason, call success rate, pickup rate, call transfer rate, etc.

Offers multi-prompt agent for more fine-grained tasks

Pricing -> TBD

multilingual

## Vapi

Latency (~900ms)

Highly Customizable: Many models to choose from multiple providers. Can choose LLM models, voice, transcribers. (OpenAI, DeepSeek, Deepgram, 11Labs, etc.)

Extensive ingegration options: AWS S3, Langfuse, Cloudflare R2, etc.

Multi-language support

Pricing -> TBD (Pricing page down??) Complex pricing structure

Call-analysis -> TBD

Concurrency -> TBD???

telephony: Twilio Vonage, Telnyx

Squads -> Multi-assistant Conversations

Slightly lower uptime on their API (Still 99.952% uptime)

## Bland

Rate Limit: By default 100 calls per day.

Multi language support

Pathway Generation(conversation flow) by AI (Multi-prompt support) Can choose to use prompt or exact language.

Fine-tuning examples to train the AI on handling edge-cases during the dialogue

Analytics: (fewer analysis compared to Retell AI) number of calls, call pickups, transferred (more focus on numeric analysis)

Unknown models (choices between CORE vs TURBO)

## Synthflow

latency -> TBD

Single prompt agent

No Multilingual Support

pricing -> TBD

concurrency limit -> 10 for starter can be adjusted

Lack of uptime info

Offers third party integrations: including twilio, eleven labs, Zapier, GoHighLevel, Stripe, OpenAI, Cal.com, HubSpot, etc.
