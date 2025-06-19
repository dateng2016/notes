# Hadi 6/12

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






