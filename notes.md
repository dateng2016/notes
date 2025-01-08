# dispatch.shipday.com

---

## Sign Up Process

### Notes

The website takes in the following information
during signing up:

- name
- business name
- email
- phone number
- password
- promo code (optional)
- country
- city
- phone number

After completing the necessary info, you have the option to choose your role:

- Merchant
- Delivery company
- Developer
- Driver

I choose merchant

After that, choose type of merchant you are

- Restaurant
- Meal prep delivery
- Grocery
- Pharmacy
- Florist
- Other

I choose Restaurant

Next specify if you have driver

I choose YES

Next it asks number of deliveries per month

I choose 100 - 1000

Shipday offers the following services:

- Real time delivery tracking for my customers
- Automatically assign drivers to deliveries
- Use 3rd party delivery service providers (Uber & Doordash)
- Gather feedback and boost Google reviews

Finally -> FREE TRIAL

During the signing up process. If you attempt to sign up multiple times, the website will ask you to verify that you are a human to prevent malicious operation. However, the verification process on my computer was impossible to get through after multiple attempts.

### Suggestion

- Ask the user to input the password TWICE to prevent error and confirm user intent.
- Add email and/or phone number syntax verificatoin.
- Add email and/or phone number verification process to confirm ownership of email and prevent spam/fake account.
- Improve the CAPTCHA process to better the user experience.

---

MAIN PAGE

## Team Chat

### NOTES

- There is one conversation that says `Announcement`.
- I assume that this is where the merchant can talk to the drivers.

### Suggestions

- There might be some bugs on this one. When I type something and send the message. There appears to be some blank messages in the chatbox.
- The bug disappears after I send the second message and everything becomes normal.

## Shipday AI

### NOTES

Pre-made prompts:

- Connect Shipday with my POS system
- Assign orders to 3rd party delivery services
- See orders on the Map
- etc...

The AI Model is pre-trained with a lot of specific information about how Shipday works.

The model is very familiar with usage of Shipday App from the user's perspective and provides helpful guidance on various steps such API documentation, integration, and where to find useful resources.

### Suggestions

- The first chat messages appears to be blank before I send my first message
- After sending the second message, the conversation becomes normal.

## Dispatch Page

### NOTES

This part gives live information to the merchant. The merchant can look at their orders and the order progress on the map.

- The middle pane is organized by drivers
- The merchant is able to see the **source, destintation, and driver locations**
- The map is colored (I assume that it gives the merchant some idea about the traffic condition)
- On the top the merchant can also see some preformance information on the order.

### Suggestions

- Sometimes when the window is smaller, some elements overlap and can not be clicked. (The performance bar and the driver pane overlaps when the browser window is too small)

## Order Page

### Notes

In the order page, there are many sub-tabs: Current, Scheduled, Completed, Incomplete, History

- Current:
  - This tab contains the orders that just came in and waiting to be completed
  - It contains more comprehensive information about the orders
    - Order No.
    - C.name
    - C.address
    - Distance
    - Req. pickup time
    - Req. delivery time
    - Driver
    - Status
    - Tracking
  - The page can be ordered in various methods based on the user's need such as `order number, status, req. delivery time`
  - The merchant can upload CSV file to create new orders in batch. The merchant can use a sample file as reference.
  - The search bar searches keyword based on all attributes of the orders
  - in `+ New order`, there is a Map API for user to search for locations based on Map.
  - The merchant can perform operations on orders in batch such as `assign driver`, `send ETA`, `print label`, `delete`.
  - On the tracking page, the merchant can see the locations and call or text the driver if needed.
- Scheduled
  - Not sure how orders could appear there
  <!-- TODO: Find out -->
- Completed
  - This tab contains orders that have been completed by the driver.
- Incomplete
  - This part contains the orders that were placed but not completed within 48 hours
- History
  - Not sure what this tab is about
  <!-- TODO: Find out -->

### Suggestions

- N/A

## Driver Page

### NOTES

- This tab shows the information about each driver that works for the merchant and their payment information

### Suggestions

- N/A

## Map Page

### NOTES

- This page shows locations including `merchant`, `driver`, `destination with pick up time
- Merchant can adjust map pin filters at the top right corner.
- Merchants can also view the performance stats on top

## Review Page

### NOTES

In this page, the merchant can see the information about their order reviews.

- On top there are overall info about order reviews and driver reviews.
- On the right there will be AI generated insights about the reviews that the merchant has.
- The merchant can apply various filters and sorting methods to their reviews.
- The merchant can respond to the reviews

### Suggestions

- N/A

## Report Page

### NOTES

This page contains reports of various types including: sales, drivers, performance, extended, analytics, heatmap, third-party delivery services, success report (beta).

- Sales Report
  - It gives imformation about `Order From`, `Number of Orders`, `Total Order Value`, and `Average Order Size`.
  - The merchant can export the report.
- Drivers Report
  - The page gives information about driver's online hours, performance, and payments info
  - In the performance tab, the merchant can view earnings of different drivers in a graph
  - At the bottom it provides detailed info on the driver's work history
- Performance Report
  - On-time deliveries tab provides two graphs to show performance on pick up time and delivery time
  - The two graphs contains info on both percentage within a certain interval and cumulative percentages
  - At the bottom, there are detailed statistics on performance data ordered by date
  - The delivery time tab shows performance data based on specific orders.
- Extended Report
  - This part offers more detailed reports by order and pick up location
- Analytics Report
  - This part uses many charts to give more insights to trends.
  - By clicking on different metrics, it gives the graph of that performance metric ordered by date.
  - At the bottom it provides info mainly on driver's on-time delivery percentages.
- Heatmap
  - I assume that this part shows the frequency of ordering from customers by different coloring.
  <!-- TODO: Find out -->
- Third party delivery services
  - This gives insights to third-party delivery operations and essential key metrics.

### Suggestions

- N/A

## Integrations

### NOTES

---

<!-- TODO: -->

NOTE: Drivrer update needs to go offline and online to reflect changes

- Start playing with APIs
