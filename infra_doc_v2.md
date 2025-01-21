# Questtagbackend

This was the primary backend service previously used for the project, developed using the Play framework. We are currently in the process of migrating away from this service as part of an ongoing update.

# QT-dispatch

This is the current API service that handles order-related operations and serves as the main backend service at present. It plays a major role in managing and processing orders within the system.

It mainly contains two types of API's -> API used for frontend, external API

# Integration Service

The Integration Service is responsible for handling orders coming from external platforms via webhooks. It ensures communication between different systems by processing incoming orders.

There are two types of integrations:

-   Upstream
    -   Upstream orders come FROM other platforms TO shipday
-   Downstream (Shaon mainly work on this downstream integrations, third-party delivery services)
    -   Downstream orders come FROM shipday TO other platforms such `DoorDash`, `Uber`, `SkipCart`, etc.
    -   On-demand delivery is also for third-party delivery.
    -   Estimation/Quotation will be performed before assignment.
    -   Before estimating, we also need to call the availability API to confirm availability.

# Shipday Integration Lib

This library provides many functions used for integration. It is responsible for calling the API and get the responses. (API services will call these functions)

# Route Service

This service is for routing (TODO: need to talk to Razin for more details)

# Analytic Service

The Analytic Service is responsible for processing data and generating reports, heatmaps, and performance analysis for users. It supplies data for various reports found under the "report" tab in the dispatch.shipday.com portal. Reports such as "sales" and metrics like "completed order," "current order," and "incomplete order" all rely on the Analytic Service for accurate and up-to-date information.

# Driver APP API's

This service handles all API interactions related to drivers. It is designed to manage the communication and functionality for the driver mobile application.

(Fourth most important API after Questtagbackend, API service, Report Service)

# Order update sender

The Order Update Sender service listens for events from the `RabbitMQ` middleware. It then uses webhooks to send order updates to users’ preferred public URLs. This service is event-driven and is responsible for managing the flow of real-time order updates.

# Real-time Service

The Real-time Service enables live communication between drivers, dispatchers, and customers. It provides a chat functionality.

# QT-data

This used to be responsible for many business logic. New projects do not depend on this very much.

# Shipday-localization

This service is responsible for language mapping to ensure services function well for specific locations.

# QT-notification

This service is responsible for sending notifications via emails or SMS to customers. We are currently moving this service to another one due to some dependency-related issues.

# Auth

This service manages all the authentication-related tasks. All of the services use this one.

# Shipday-mq-model

This service makes sure that the json schemas produced and the json schemas consumed should match.

# Shipday-plan

This service is designed to maintain all the subscription plans for the users.

# ETA-auto-dispatch

Driver auto-assignment happens in this service. There are a variety of logic we can choose for how we want to assign the orders (such as choosing the nearest driver or the driver with the minimum number of orders). We have BOTH in-house driver assignment AND third-party driver assignments. In addition, we also have hybrid auto-dispatch, where we first try in-house assignment and then go for third-party driver assignment if the in-house assignment does not work.

In this service, the scheduler will be called every 30 seconds to check if there are orders that need to be assigned.

# Payment-service

This service handles all the payment-related tasks such as subscription payments.

# Notification-service

All other services send messages to RabbitMQ, notification service consumes those messages and handles them from there.

# Internal-tool

This service is the backend for the admin portal page. The frontend is `admin-portal`

# Customer-tracking

This service is used for customers to be able to see real-time tracking of their items.

# Review-Analytics

Every time users submit reviews, we submit to RabbitMQ. Review-analytic will consume the message, get the keyword from the review and store them into the DB.

# Order-Insertion service

All other services that will require order insertions will call this service.

# Order Update Sender

Other services send messages to RabbitMQ. Order updater will consume those messages. It will send out order update notifications through webhooks that users provide.

# Shipday-chat-js

This is the frontend of the chat services. The backend of this is `real-time service`

# Third-party billing

This is for usage like `Uber`, `DoorDash`, `Roadie`, etc. We currently have two methods for payments: Bank account and credit card. (Bank accounts tend to be cheaper since credit cards typically require transaction fee of certain amount).

# Shipday-wallet

Users can buy shipday credits that can be used for monthly subscription billing and/or third party payment. Currently we are only supporting USD payment. When payment occurs, the credit will get charged before credit cards or bank accounts.
