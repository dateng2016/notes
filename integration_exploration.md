## Foodhub (Webhook??)

Only has one controller -> /foodhub/order

In short, the delegateOrder method processes an incoming Foodhub event, checks if the order is valid, fetches the order data from Foodhub, dispatches the order, and logs the outcome. It handles different event types (order placed, accepted, or cancelled) and ensures that duplicate or invalid orders aren't processed. It also interacts with various services like logging, caching, and order management.



