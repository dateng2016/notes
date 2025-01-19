<!-- TODO: Focus on DB, and microservice structures -->

- Dispatch
- CRUD operations on orders
- Drivers
- Routes
- Reviews
- Reports
- Integrations

What does everyone work on

Shammo -> Integration and AI

Integration comes with support tickets

Applications

1. Dispatch Dashboard (web application)
2. Dispatch APP(Mobile APP)
3. Driver APP(Mobile APP)

Services

1. API services (Shaon) (use cases and stuff)
   1. External APIs
   2. Authentication
   3. 3rd party delivery integration (doordash uber)
2. Integration Service (external facing service) (Contact Shammo after)
   1. Receive order data
   2. Mappers of different integration
   3. Example flow:
      1. Platform sends us a webhook(json payload) -> data preprocessing (some times we need to decrypt) -> figure out which company is issuing the order -> Map the data into Shipday compatible data -> publishes the message of order data in a MQ
3. Order insertion service:
   1. Consumes the order payload with company mapping from the MQ -> stores order into database (By storeing in the MQ, the data does not lose due to service downtime)
4. Order update sender service
   1. Driver updates order state -> Deterimine where to send the webhook(integrations/customer endpoints(self-hosting URL)) -> send the order status update

---

Shahriar

Backend(QuesttagBackend) used to be the Main Service, used Play framework
We are currently working on migrating this project to other ones

Everythign on dispatch/dashboard from the main service

QT-dispatch repo is the api-service (order-related), right now is the main backend

Two apis for csv and indiivual order

Integration Service is responseible for taking orders from other sites through use of webhook

order-insergtion service(repo)

Route-service -> for routing ASK RAZIN.
Analytic-service this is for analyziing to geenrate report for users, heapmaps, performance
Sales comes from report service, order completed,current, historical, incomplted comes from report service
Driver APP APIs->
Order update sender (repo) WEBHOOK manages the order update and send them to the user's preferred url
, this service is event-based, it listens to the events from rabbit mq and then decide what to do based on the spefic evernt

real-time-service is the chat service (chat with driver, dispatchers, customers)

AWS contains everything infra like db redis, mq
how to deploy things?

try logistic
