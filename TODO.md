-   Where to store the CSV file?  -> AWS S3
-   Server access for ml-service？
-   Can we enable the scheduler? 
-   What is the deal with the carrier count?
-   We should probably get number of drivers logged in???
-   For the internal dashboard API, should I write on the current function or should I write ANOTHER one myself???
-   pkl file for Ensemble???


Daily
Active Integration (TODO:)  -> platform(if not null -> True)&order_source(if not null -> True, need to figure our whether order source is a valid platform) in the order_info table

Payment Type                -> payment_source from monthly billing table (Stripe/Shopify)  (company&month are primary keys)
Plan Type                   -> company_info table
Orders Inserted             -> order_info table
Orders Completed            -> order_info_historical
Logged In Web               -> daily usage track table
Logged In App               -> daily usage track table
Driver Log Ins              -> daily usage track table (probably should not be boolean???)
Reports Usage               -> daily usage track table
Notification click in App   -> daily usage track table
Read reviews                -> daily usage track table
Responded to review         -> get from chat DB, (Ask access)
Time active on web          -> TBD from daily usage track table
Time active on app          -> TBD from daily usage track table
Used Driver List            -> daily usage track table
In-house completed          -> order_info table, third_party_assigned
Third Party Completed       -> order_info table  
Takeout Orders              -> pickup_order table
Reviews Received            -> reivew_analysis table








Talk to Adem about the components on the status page

See if we can hide the incidents 

Work on the deprecated warning for the securityConfiguration.java



Hadi notes:

we fetch orders from the other sites like Shopify, Square, etc.

First explore their sites,

POLLING their orders, we call the API every interval, 
WEBHOOK -> We create an app in their place with secrets, we create a client at shopify, we will provide the endpoint to shopify. 

Map it to our order_info table


Ecommerce -> customer places the order themselves. 
PoS system -> Need a phone call or be present before hte cashier and tell the staff to create the order for them. 






<!-- TODO: Focus on component right now -->
// * Integration -> Most important
// * Dispatcher APP (delivery management) -> to assign third party delivery services -> at least the delivery is working

//* Insertion services -> most important
//*
//* SDR sales development representative


Do a deeper dive on the voice and the pricing of the agents
