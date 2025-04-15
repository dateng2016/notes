## Questions

Explain the internal dashboard rules?

Only show one account at time

Chcek need action. We can  delete the account. create account

We need to edit priority, sort by priority

Make sure the isCatering field is true.

Create tables/columns about priority. 1 - 5



status (filter by?>?????)

Add a drop down for this.

tracking link? ( Example????) 

Check with Shahriar. 3rd party tracking(optional) + our own tracking


What is modal window? is it the page that shows after you click the row???


Why both magic links in the table and the modal window?

What is order Log? 

What is API key?


other tools integration logs -> order logs.
third party tools order logs -> third party logs


order log end point -> https://integration.shipday.com/log/orders/30063817



## Questions:
priority -> New column in the order_info table?
Restaurant name -> from company_info or admin???
email -> from admin
order_number -> order_info
customer name -> from customer table  join by customer ID???
delivery name = customer name
order placement time -> from order_info placement_time
pick up time -> from order_info pickedup_time
delivery time -> order_info delivery_time
status -> order_info order_status
tracking_link -> Where should I get the tracking link????????????? Third party tracking vs our own tracking link?????
delivery address -> from customer table???????????????
tip -> order_info which one: predefined_tip or cash_tip??????????????
provider -> order_info provider
third party ID -> WHERE?????????
order log -> check admin portal
API key -> ??????
Notes -> ???????? A new table???? OR add another column for the order_info table???

WHERE SHOULD THE BACKEND BE IMPLEMENTED???????

Show evrything based on order status
ORDER_ASSIGNED
ORDER_ACCEPTED_AND_STARTED
ORDER_ONTHEWAY
ORDER_PIKEDUP
ORDER_UNASSIGNED
