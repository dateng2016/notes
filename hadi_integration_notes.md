# Hadi 6/12

platform_token and restaurant_mapping are the two Main mapping tables in MySQL

## MONGO

### External_order_log 
collection for incoming webhook for integration projects
Any event that comes up, we just dump it here. 
origin -> platform that it comes from
timestamp -> when the order comes to our system
logtimestamp -> time when it starts processing
(example -> square -> webhook timestamp corresponds to timestamp.when the order comes, it hands off to a separate thread pool in a queue, it won't execute immediately, logtimestamp means the time that we start processing the order. 

### Order_event_log
when we only have the order_id and do not have exact order info, we will need to look at the order_event_log
external order log is the parent of order_event_log
mapping between the order_event_log with external_order_log -> order_event.requestId = external_order_log._id
We can use the aggregation pipeline during search. (Hadi will send samples for aggregation pipeline)
To know the exact origin name, check the code. (dumpLog method call), We have a list of origin names in the Index.java
uuid -> order_event_log -> requestId (this is the external_order_log._id)   This uuid is only created once. 

## NEXT STEP
SQUARE -> In a separate package
squareintegraionservicenew.java

For onboarding process, go to dispatch dashboard, check the integration there. Most of the times is the authcontroller that controls the onboarding process. 



## 6/17
### Square
merchant email -> company id

If the new_state is PROPOSED, we discard. (customer add into the cart), we only care about new_state that is OPEN. Search using regex -> OPEN. (Basically make the data field contains the string "new_state\":\"OPEN") (fixed the escape as needed)

Order's GUID -> Square id 

When order event comes -> we cache the order task -> orderGuid(order id from Square) -> Check if the order GUID already exisits in Redis, if it already exists, we  discard. If not we cache the GUID in the Redis. -> We retrieve the order details from SQUARE for other necessary information. -> After fetching the order detail, we add the details into the order_event_log. 

In order to insert into the order_info -> Map the order detail from the third party to our own structure -> after the mapping -> we publish to the MQ for the order-insertion service to consume -> when url is '/publish-to-rabbit' (DATA EXCHANGE): We are sending to rabbitMQ, from this point integration-service's task is DONE. -> after the order-insertion service completes, it will publish back to the MQ, the integration will listen to that response, then it will add the log for "ORDER_CREATED" event. Then this will be cached into Redis again in case for cancelling event. (key: value = squareGUID: ourOrderId). 

For the url fields, they don't necessarily share the same Base Url. 

#### Onboarding Flow for Square
When you click the connect on our dispatch website -> api.shipday.com/square/connect -> redirects to square endpoint -> connectionsquareup.com/oarth2/authorize?..... 

for square we use platform_token table in the DB, if it is revoked, then that means the connection is deleted. 


upstream (both polling and webhook) -> we are receiving order vs downstream (we are assigning order to third party driver uber or doordash)

square is a ecommerce site -> each restaurant has their own dedicated website. 

## Uber Eats
This is a marketplace -> single APP -> different restaurants (no dedicated websites for each restaurant)

Order comes from webhook

UbereatsController.java (only one endpoint)

When order comes in -> dump log to the `external_order_log` -> Will fetch the order via API call (add `order_event_log`) 

the inital order event will contains whether you should use API v1 or v2(in the resourceHref). 

(DTO -> data tranfer object -> use this to transfer from one strcuture to another structure)

We will validate the order data -> if fails -> throws EXCEPTION -> if success -> rabbit MQ -> 

If we get the same event as before, we throw exceptions because it means that this event is already processed. 

If validation succeeds -> we will cache the order to Redis. (This means that this task is successfully processed)

How to diagnose a problem -> from email get company_id -> 

NOTE: Only valid order types are inserted, we discard ones that are not valid. 

fulfillmentType(v1) / type(v2) -> only allow DELIVERY_BY_RESTAURANT DELIVERY_BY_MERCHANT (depends on the version of API) or PICKUP (v1) PICK_UP (v2). (We don't care about deliveries by Ubereats and such) 

If no tax -> set it to 0

After the order-insertion service successfully inserted order, it will send back a message to the MQ and give the Order ID. -> THEN the integration service will add ORDER CREATE in the order_event_log MongoDB. 


Ubereats has 2 mapping table -> ubereats_mapping + platform_token

platform_token mainly contains access_token + refresh_token

ubereat_mapping contains additional info like address, phone number, etc.

Our merchant might have multiple stores at UberEats. 

When we receive the webhook from UberEats -> It contains store GUID (it will be the 'user_id' in the JSON object)


When we receive 


## 6.23

Some merchants have their own platforms, they use external API to insert their orders. They will have their platform names to be null.

We will not see any code for A-Team, last_app and xxx??? -> They use external API for integration

## Shopify

We have an app published on shopify. We use webhooks. 

We have a nodejs app called shopify-app-rewrite. This app receives the order, validates (Shopify requires node js app?) -> pushes the order to rabbit MQ to integration project -> We have a listener at integration project, and handles from there. -> 


###  Inside nodejs project 
gdpr.js 
APP_UNINSTALLED -> when the merchant do not want us anymore. 

ORDER_CREATE -> Do validations such as allowed delivery methods and such -> send order to MQ

During the test of order creation, there will be logs -> It will using incoming_webhook_logs (PLURAL!!).

### Integration project

Receives the order message from nodejs. ShopifyService.java handleOrderInsert. 

Initially it will dump the log to the external order log -> this will be the same as incoming_webhook_logs -> uuid is created in the nodejs application -> (the records in the two logs are exactly the same)

We pretty much do not need incoming_webhook_logs -> Just need external order logs.

TODO: Next week -> GLORIA

## Gloria

This is done through webhook. 

Mapping in a very primitive way

When parsing the payload to mapper -> json object helper?

GlobalFoodIntegrationMapper -> help for mapping -> MappedToOrderInfo is the helper function 

IntegratorHelper.java -> Doing the insertion in DB. Input is JsonData from the mapper, output is insertion of the order in DB.

Insert delivery order -> done by carrier

pickup order -> No carrier, done by the customer. 

insertDeliveryOrder -> insert it to DB -> 

Check integration controller. -> creating + update 

U -> means update  (the first 2 methods) 
P -> Means creation 


Onboarding -> Done from gloria food. Place the api key from shipday wizard. (inside the gloria platform) 

User account mapping through our API key.



## Lightspeed

2 integration: x-series (e-commerce), k-series (restaurant)


### K-series

LightKController.java

receive webhook

first we get mapping. We have a separate table for mapping. light_k_mapping. 

For mongo:
notification type: (inside data in the mongo log)
CLOSE, UPDATE, OPEN

account: 

businessLocationId is used for mapping the restaurant.


On-boarding process: like square. Initiated from our side. we initiate, light speed send us one-time token.(refresh token) We get the refresh token, business location ID. 

When we connect, we send the api key of the shipday to light speed. /oauth/authorize   After the user logs in. light speed will then send the code / token to us. 

2 tables -> light_k_mapping & light_k_token (parent table)

for every merchant, one entry in the token table 

for the mapping tables, one merchant can have multiple entries. 

different business_location_id means different stores 

During onboarding. the merchant selects what kind of profiles they want to import to shipday. (active profiles). Inside the data payload in mongo -> there wiill be info for that -> accountProfileName + accountProfielId

When the webhook comes in, we check if the profile matches the active profiels recrod that we have on hand. if not, we discard. 

If the active_profile = null -> we are allowing all orders. 

When we receive the event, we log to external_order_log, we got all the info needed, we do not need to call the external API again to fetch extra info. 



## Polling

We periodically fetch orders from the platform. We only have 3 or 4 that use polling. Adelo Adora Odoo. 

There is a separate project for polling service. Currently under migration to integration-scheduler + task-executor. 

ingegration-scheduler -> task executor -> integration project

Every once a while -> sync -> get the mapping -> send the poll reuest to the task-executor 

At the task-executor there are listeners. First there is a order_poll_log. This is the first log that comes in.

Then do the actual fetch order by calling the external API. 

### Odoo

The overlap window is 24 hours, 12 hours before the current and 12 hours after. We have this due to timezone differences. (To accomedate different timezones for different customers.)

Check if it has order in the payload. 

Check the cache repo. Check if the order is already there. 

If the order is not already there, we will send it to integration project and cache it to the cache repository.

In the integration project, there is a listener OdooListner, First dump it to external_order_event. Then the rest is the same structure with other ones. Odoo only has delivery order, no pickup order. 


### Aldelo 

NOTE: Listener either listens to polling project or task-executor project, 

The structure is pretty much the same. 

This also uses order_poll_log for the inital event. 

The restaurant mapping table is in cache for aldelo. The cache is populated at start time from DB. From then on, it will only fetch from cache. If a new mapping comes in -> there is a cache resync event. (Restaurant_sync listener)

Overlap for aldelo is only 15 minutes. 

### Adora

this also uses order_poll_log. It's in capital -> ADORA

In the API call, it fetches all the order for a single day. Based on the UTC date. 

During the polling, we need to put the offset into consideration. Check the operational_area table. We need to use the customer's time zone eventually. 

The rest should follow the similar structure with the other 2. 


### 7.21 Motaher Toast:

They send webhooks for any event.

Back then we used json objects -> currently trying to do the migration to the integration service for insertion.

ToastController.java

webhook/order/restaruantguid is for polling, we do not use it anymore

/webhook/order is for the webhook


/order/poll is for when our system is down, we will do some polling for a time range and then insert the orders. 

### On boarding flow

Use install shipday app on their app. they provide their api key. we will receive at the /webhook/restaurant controller. Then it goes to toastmapping table. `restaurantGuid` is the key field

/synAllCompany  controller, this is called by the integration-scheduler project.

It does NOT send to the order-insertion service.

For toast it uses the JSONObject not order info stuff. 


## 6.22 Motaher Adora Driver Sync

employee sync is similar to toast. There is no order update api for adora.

order-polling-service project

AdoraService.java

For adora we only have date option for order fetching. 

If the order is assigned to driver -> integration service. 

They use our system to assign orders to drivers. But for adora they assign carriers at Adora site. 

Checkout AdoraOrderAPICallerNew.java 

When they assign driver at their site, the event comes to us and the we assign it in the background to the same driver. There is a driver mapping table to make sure that we assign to the same driver. 

If the order is not assigned (scheduled for later) -> we will save it to redis. we start processing the item shortly before the scheduled the time.(90 minutes) we process orders that is going to happen within the next 90 minutes.

in the assignment-polling, we sync every 15 seconds. it's faster. The goal is to assign driver / change driver in time. 

entry -> AdoraService.java from the order-polling-service
entry -> assignment-polling project -> 
entry for employee sync -> integration-scheduler -> AdoraDriverSync.java


If the order is 

Toast reservation look into it.

