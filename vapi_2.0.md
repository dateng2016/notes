## Vapi 2.0 Update

### Update

-   More model (100+) integrations on LLM, transcription, and voice.
-   Added integrations for things like observability tools (langfuse), native hooks into calendars, CRMs, etc.
-   Embedded tools: Turn-taking orchestration (handles interruptions, end-of-speech detection, backchanneling by adding things like 'uh-huh', 'sure' that makes conversations natural), noise cancellation, voicemail detection, test environment for simulating complex call flows.
-   More customization: support for persistent memory, dynamic variables, real-time endpointing, multilingual output, openAI's speech-to-speech model (currently in BETA), etc.
-   Infra at scale 44 million with <500ms (Although I checked at their dashboard, web latency is at around 900ms, Twilio is around 1400ms and Vonage is around 1200ms). Handles long calls (60+ mins)

### New Features

-   Query tool for knowledge base. (Although at their docs website, it mentions that Currently, the Query Tool only supports Google as a provider with the gemini-1.5-flash model for knowledge base retrieval.). Although Vapi has integration with Trieve allowing users to use Trieve API key to import existing Trieve datasets into Vapi.
-   Assistant Tools: call transfers, hang-up, data retrieval, keypad dialing, etc.
-   Observability: integrated with Langfuse. Can see transcripts, call outcomes, engagement metrics, quality ratings, etc.
-   Added 10+ new voices.
