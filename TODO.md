free -> professional -> branded premium -> branded elite -> business -> 

-   What is the deployment process
-   Walk through how to gather data for each columns for the  Churn Model??? -> DOne
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






