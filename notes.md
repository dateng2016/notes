# dispatch.shipday.com

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

- Add email verification during signing up and ask the user to input the password TWICE to prevent error and confirm user intent.
- Add email and/or phone number syntax verificatoin.
- Add email and/or phone number verification process to confirm ownership of email and prevent spam/fake account.
- Improve the CAPTCHA process to better the user experience.

---

MAIN PAGE

## Team Chat

### NOTES

- There is one conversation that says `Announcement`.
- Assume that this is where the merchant can talk to the drivers.

### Suggestions

- There might be bugs on this one. When I type something and send the message. There appears to be some blank messages in the chatbox.
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
  - order information includes:
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
  - in `+ New order`, there is a Map API for user to search for locations based on Map.
- Chat Assitant (DOESNOT WORK???)

### Suggestions

<!-- TODO: -->

NOTE: Drivrer update needs to go offline and online to reflect changes

- Start playing with APIs
