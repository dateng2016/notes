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
-   Keep track of user require the do not call
-   Keep track on how we ended the conversation
-   Keep summary of the call.
-   Explore whether to use SDK or REST
    -   
-   Make sure to give the necessary info of the customer to the agent
