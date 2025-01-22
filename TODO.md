# 1/22

## Shahriar

### Model Deployment

-   [ ] Set up the analytic-service with Shahriar. Get the service up and running
-   [ ] From yesterday's notes, here is the flow -> After our models make the prediction, we will store the data(LEAD SCORE) into the `Analytic-Service` DB. We will create a new API to for the frontend retrieve this `LEAD SCORE`. (I believe we need to work with Zahid on this one correct?)
-   [ ] Where EXACTLY should I store this lead score? (Which SQL table of which DB?)
-   [ ] What will the flow be like? Where should I obtain the data for the model to make the prediction? Will I be consuming RabbitMQ messages for this one? (If so, is there any sample code for RabbitMQ message retrieval in python?)
-   [ ] What will be the format of the data? (I need to convert this into designated format.) I would like to get some sample data to start working on.
-   [ ] Where should I deploy the model?
-   [ ] I believe that we also need to add the `LEAD SCORE` field in the `New Sign-Up Email`. Can you tell me a bit about the flow for email notification?
-   [ ] What config information should I obtain such as DB, RabbitMQ and stuff?
-   [ ] I believe I also need authentication stuff to be able to use the service. Can you help me set that up? A new account needed?
-   [ ] What are the deployment process? Should I just create a merge request and leave it there? Who should review the code?
-   [ ] (Ensure everything is up and running properly such as rabbitmq and all the DB)

### Internal Dashboard

-   [ ] Ask Shahriar to create a new account for the internal dashboard
-   [ ] What will be the flow for this? Where should I get the data needed to produce the table?
-   [ ] Are you familiar with the `Internal Dashboard` backend code as well? Who should I talk to for this service?
