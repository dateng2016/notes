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

---

Sabbir

Main UI is the QuesttagBackend
QT-data responseible for business logic, new projects does not depend on it very much
shipday-localization, responsible for language mapping
qt-notification -> send notification to customers, emails, SMS. Currently moving this service to another one

auth -> manage all the authentication stuff. all of the services use this.
shipday-mq-model -> Make sure the json schema produced and consumed match
qt-dispatch -> API service, most the things that we migrate from QuesttagBackend is put here. two functions: serves API to frontend, and external API.
report-services ->
driver-app-api -> (fourth most important )
shipday-plan -> responsible for maintaining subscripition plans

report, api, play project are the three cores

etaautodispatch-> auto-assign happends in this service, (through manual logic)
payment service -> handles all the payment and subscriptoin related stuff

(CHECK OUT THE PARTNER PORTAL)
partner gets 10% cut after getting us a number of customers (payment service)

qt-notification->dependency issue
notification service -> all other services send message to rabbitmq, notification service consume those messages and handles them from there
internal-tool -> for the admin portal page, the frontend for that is admin-portal
external-order-form -> separate domains, gives custom forms
analytic-service -> calculation result put into a separate DB.
customer-tracking-> customers can see the tracking of the drivers

review-analytics -> call openai api for, everytime use submit review, we submit to rabbit mq, review-analytic consumes the message, get the keyword from the review and store it in the databse
order-insertion-service -> all other services that rquire order insertion will call this service
orderupdatesender -> other services send to rabbit mq, orderupdater consumes the message, do the webhook stuff
shpday-chat-js -> handles all the chat (frontend)
real-time-service-> backedn for tha chat

Integration service
upstream orders created on other sites, send the order to us
downstream order created at shipday, we send the order back to them.

TALK TO MOTAHER

---

Shaon

Upstream orders comes from other like squarespace, orders come FROM other platfrom TO shipday
downstream integration like doordash, uber, skipcart..., orders come FROM shipday TO other platforms

Shaon mainly work for downstream integration. Third party delivery services.
on-demand delivery is for third-party delivery.
Estimation / quotation will be performed before assignment
Before estimating you need to call the availability API

Shipday integration lib, provides many functions used for integration. responsbile for calling the API and get the response. (API services will call these funciotns)

When calling the external API, API services will respond

Auto-assignment (in dispatch setting) -> User can choose different algorithms or implement their own rules
We have in-house auto-assignment AND third-party auto-assignment. (lowest estimate / earliest pickup)
hybrid auto-dispatch -> first try in-house -> if failed -> then try third party

ETA-auto-dispatch service -> scheduler called every 30 seconds (with a cron job running)

third-party billing (third party usage) for usage like uber, doordash, roadie, -> Two methods: Bank account or credit card

shipday-wallet -> we can buy credits -> can be used for monthly subscription billing AND third party (Only in USD)-> gets charged before credit card and other payment methods

shiday connect

TODO: Boxfuse

---

Motaher
when user place AN order from merchant page. Some systems we need to fetch the order. For most systems, we wait for notificatoins.

For order related update, we need to notifiy the original platform.
we also send the driver relateed info to the platform so that they can manage it themselves.

AI agent chat -> (review-analytics github repo)

We have some functions defined at OpenAI.
