## Questions

-   For "Industry Filter", how to do the filter?
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
-   Try to get rid of cost info in the post-call summary? (minor issue)
-   Use the assistant ID during the API call
-   use webhook-receiver repo to set up webhook. Base URL -> https://webhook.shipday.com/
-   Use integration-scheduler repo to set up scheduler. This is a single instance server. It runs scheduler every 15 minutes. This service will only to find out the companies. (Do not do the filter)
-   task-executor -> Do the heavy lifting. -> Check the time, initiate the phone call.

## Sabbir notes 6/10

MY TASK:
task executor -> service -> takes in phone number, json object, return the call ID -> DONE

webhook -> only the ended -> get the call-state (boolean that indicate whether it is picked up by human or not) + call-id, publish to rabbit

store the state -> when it is ended -> store whether it is picked up -> when

## Adem notes 6/13

Expose more info to the voice agent.



## Sabbir whole flow 6/13

DB schema -> 
1. failed_order_alert_agent_settings
2. voice_agent_call (also include the future voice agents)
	request_id -> this is the UUID
	

task-executor
failedOrdernotifylistenr.java -> failedorderalertservice.java


TODO: add the long_order_number change requested by Adem. 


redrop -> reinsert it 

based on the conversation to judge 

Agent will say I will redrop and that is it. 

Make sure to implement the last 4 digit thing

Pause at the beginning. 


## 6.18
third party -> 
Check the refund request -> third_party_refund_request


## 6.19

Call end customer -> order info, customer info, replacement order/ refund -> then ask merchant 


## 6.19 Voice Agent Implementation

Send in Redis for rate limit -> ratelimit service. -> add new method 

Make sure the date in UTC time

whitelist -> add another col in the voiceagent setting table -> 

Create a new queue -> Shaon create queues. 



## 6.22 Shaon

What kind of orders will trigger calls?

what is is_internal field mean?

If only third party will trigger, then all the calls for orders can be refunded?

How can I fail an order other than driver failing


Why are we only selecting from third party order table

what is external third party and internal third party/connect

For third party orders, fail via webhook 

shpiday connect -> fail -> delivery company uses driver app. 


##
Default ON


Block third party driver



## Questions 6.29

Should I use API or MQ for this?

Is there existing tables

Do we have existing Google Sheet?

What info should be saved in the DB

Solution:
id
company_id
carrier_id -> ?????
reason
order_id
third_party_delivery_order_id -> What is this, where do I find this in the DB?
remarks
status -> Any Enum for this?
request_type -> ENUM?
time -> (request time?) bigint type??????

What info should be sent to the support team?

Everything Above?

shipday connect -> manage merchant -> add merchant -> (account email is the import one) -> 


merchant -> setting -> third-party-delivery -> get 


## Outreach Agent for Old Lead 

### Flow

1. Run a scheduler to get the old lead -> Gather info about the user (phone,  -> Publish event 
2. Make outbound calls
3. If needed, send meeting invitation link via SMS
4. Discount code (Need to discuss with the team)

NOTE: Phone number need to be in E164, suggest that we only call the US customer for now.




## 7.5

-   Where should the API to send the schedule link be?
-   Where and how to set up scheduler to find out the company to call
-   Currently have 20 concurrency. Will not be calling everyone at the same time. Need to design.
-   How to design the calling again part? Similar to the previous voice agent with 3 trials?
-   How to generate the discount code

**Current outreach agent flow**

Scan the DB -> call the customer -> Book appointment -> send appointment link via SMS -> Send discount code -> send via SMS



## Talk with kamarul
qt dispatch -> companyInfoController -> line 28 Do NOT publish event, enter to a DB table to log which account to make the call

Time restriction 

Run a scheduler -> 5 phone calls per ten minutes

Task executor will implement the features. 

Ask Adem about time restriction for SMS and Phone Calls

Need to figure out something else if restriction is needed.

in scheudler project

Pick a time that is not conflict others

for discount go to company_info table -> 

redirect to the sales team. 25% if they upgrade this week. 

Can send email to both support and sales


## 7.11 AI Receptionist

Take their info -> name address phone

Check for voice selection 

Operating hours




## 7.14 Oliver Google Maps Sync

User will add business phone -> We will pull the info from google. -> When the pulling is completed, the user will see their public info. Next the user will preview the agent voice. -> 


## 7.15 Adem AI Receptionist


If need to send sms to manager to feedback complaints or compliments. 

If catering is needed -> name phone -> email / sms

## 7.15 Initial Flow Design

Customer picks up the call 

1. Check the time -> normal greeting / after-hour greeting 

2. Check intention 

3. Functionalities:
    - General questions (store hours, policy check, etc)
    - Order status check -> API call
    - Transfer to live agent for any necessary issues
    - Place an order 
        - `supportPhoneOrder` == true -> Phone call
        - `supportPhoneOrder` == false -> Send link after the call
    - Reservation 
        - if catering -> transfer
        else
        - `supportReservation` == true -> Phone Call
        - `supportReservation` == false -> Reject
    - Direction
        - We can give the address as per request
        - We can also send out SMS with a Google Map URI
    - Taking complaints or Kudos 
        - Go to email/SMS???.

4 Webhook

    - Initial webhook -> fetch dynamic variable.
    
    - API for order status check

    - End-call webhook
        - Complaints, Kudos?
        - Send user order URL?
        - Send user Map URL?

5. DB Design
    - AI_receptionist_agent_settings
        - company_id, agent_phone_number, transfer number
        - agent_phone_number(this can be used as primary key), company_id, transfer_number, created_at, updated_at, active_status. 
    - google_business_info_for_ai_receptionist (This should be updated daily)
        - TBD

inbound webhook -> webhook server.

Rate limiting at webhook server. -> Let Adem decide.


Google Map



Manual Input:

1. Menu (Link or actual menu?)
2. Phone number
3. Order URL
4. Store Name
5. Phone order policy
6. Reservation policy
7. Whether the store supports catering order
8. Specific plicy regarding reserving should be manulaly input (reservable or not is in google)
9. standard/after-hour greeting
10. transfer-number (e164 format)




From Google:
1. address
2. payment option
3. reserable
4. 

Make sure to add the phoneReseravation flag


## 7/30

- Edit opening hours?
- Add accept_dine_in
- Modify the payment options based on what I sent you (NFC, cashonly) -> ADEM
- add reservable
- Phone order checkbox?
- Modify the initial business details -> we don't have photos of the store. Display Name + Address + Google Map URL -> ADEM

without picture -> current fields are good

- Do we need agent name? The only time we mention this is at the beginning -> ADEM
YES
- You have catering, takeout, delivery, dinein,  selection twice -> ADEM

Only keep the second one

- Reservation link should be optional -> ADEM



- Should we split the takeout + delivery policies into 2 text boxes? -> ADEM
- Takeout and Delivery policy? Is that necessary? -> ADEM
- Dine in policy? Is that necessary? -> ADEM

hide it for now

- after-hour greeting -> end the call? -> ADEM

end the call logic.


TODO: 
- add accept event boolean field
- Add catering policy
- Add accept dine in


