# Questtagbackend

This was the primary backend service previously used for the project, developed using the Play framework. We are currently in the process of migrating away from this service as part of an ongoing update.

# QT-dispatch

This is the current API service that handles order-related operations and serves as the main backend service at present. It plays a major role in managing and processing orders within the system

# Integration Service

The Integration Service is responsible for handling orders coming from external platforms via webhooks. It ensures communication between different systems by processing incoming orders.

# Route Service

This service is for routing (TODO: need to talk to Razin for more details)

# Analytic Service

The Analytic Service is responsible for processing data and generating reports, heatmaps, and performance analysis for users. It supplies data for various reports found under the "report" tab in the dispatch.shipday.com portal. Reports such as "sales" and metrics like "completed order," "current order," and "incomplete order" all rely on the Analytic Service for accurate and up-to-date information.

# Driver APP API's

This service handles all API interactions related to drivers. It is designed to manage the communication and functionality for the driver mobile application.

# Order update sender

The Order Update Sender service listens for events from the `RabbitMQ` middleware. It then uses webhooks to send order updates to users’ preferred public URLs. This service is event-driven and is responsible for managing the flow of real-time order updates.

# Real-time Service

The Real-time Service enables live communication between drivers, dispatchers, and customers. It provides a chat functionality.

# QT-data

This used to be responsible for many buisiness logic. New projects do not depend on this very much.

# Shipday-localization

This service is responsible for language mapping to ensure services function well for specific locations.

# QT-notification

This service is responsible for sending notifications via emails or SMS to customers. We are current moving this service to another one.
