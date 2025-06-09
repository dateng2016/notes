## Questions

-   Where should we get the knowledge base for this agent?
-   For "Industry Filter", how to do the filter?
-   Can we get the name of the user from the DB?
-   What should we do about the reactivation discount or extended trial?
-

### For Vahag

-   What is the phone number to transfer to?
-

## Flow Design

-   Run a scheduler to check on customers (from the Payment DB subscription table?)?
-   Create a table to keep track of the users that we have called already
    -   Call Log
    -   id, company_id, success (boolean), do_not_call(boolean, default false),
    -

## NOTES from Kamarul

-   Need to keep track reactivation discount, need to store it.
-   Keep track of users that require the "do not call"
-   Keep track on how we ended the conversation
-   Keep summary of the call.
-   Explore whether to use SDK or REST
-   Make sure to give the necessary info of the customer to the agent

---

-   how to design the agent
    -   DONE -> Create an agent (Create on the go)
    -   TODO: Add knowledge base to the assistant (Need to get the knowledge base file from someone (Kamarul????))
    -   DONE -> Design the prompt (TODO: Refine)
    -   DONE -> Make the call
-   How to initiate a phone call to a particular customer via this agent - feed information regarding the particular customer
    -   TODO: Feed info via system prompt?
-   DONE -> how to get the summary of the phone call once it's ended
-   TODO: Get the structured output

## Notes 6/5 Kamarul

-   Use customer phone number for the phone call to identify customers
-   Http request/respnose body max limit (should this be a concern?) should be fine
-   Try to get rid of cost info in the post-call summary? (minor issue)
-   Use the assistant ID during the API call
-   use webhook-receiver repo to set up webhook. Base URL -> https://webhook.shipday.com/
-   Use integration-scheduler repo to set up scheduler. This is a single instance server. It runs scheduler every 15 minutes. This service will only to find out the companies. (Do not do the filter)
-   task-executor -> Do the heavy lifting. -> Check the time, initiate the phone call.

## Notes 6/9 Shaon and Sabbir

When is call picked up, when is NOT picked up, when the call is completed. Explore

Just get the payload

## My Work 6/9
