-   What is the deployment process
-   Walk through how to gather data for each columns for the  Churn Model???
-   Where to store the CSV file?
-   Server access for ml-service？
-   Can we enable the scheduler?
-   What is the deal with the carrier count?
-   We should probably get number of drivers logged in???
-   For the internal dashboard API, should I write on the current function or should I write ANOTHER one myself???
-   pkl file for Ensemble???
-   


Daily
Active Integration          -> platform(if not null -> True)&order_source(if not null -> True, need to figure our whether order source is a valid platform) in the order_info table
Payment Type                -> payment_source from monthly billing table (Stripe/Shopify)  (company&month are primary keys)
Plan Type                   -> company_info table
Orders Inserted             -> order_info table 
Orders Completed            -> order_info_historical
Logged In Web               -> daily usage track table
Logged In App               -> daily usage track table
Driver Log Ins              -> daily usage track table (probably should not be boolean???)
Reports Usage               -> daily usage track table
Notification click in App   -> daily usage track table
Read reviews                -> daily usage track table
Responded to review         -> get from chat DB, (Ask access)
Time active on web          -> TBD
Time active on app          -> TBD
Used Driver List            -> daily usage track table
In-house completed          -> order_info table, (ask Shaon)  third_party_assigned
Third Party Completed       -> order_info table  (ask Shaon)
Takeout Orders              -> pickup_order table
Reviews Received            -> 


analytics_service=> select * from daily_usage_track limit 1;
 id |    date    | companyid | loggedinweb | loggedinmobile | driverloggedin | reportsused | notificationsviewed | reviewsviewed | driversviewed 
----+------------+-----------+-------------+----------------+----------------+-------------+---------------------+---------------+---------------
 83 | 2025-02-10 |     56385 | t           |                |                |             |                     |               | 


mysql> desc monthly_billing;
+---------------------------+---------------+------+-----+---------+-------+
| Field                     | Type          | Null | Key | Default | Extra |
+---------------------------+---------------+------+-----+---------+-------+
| start_date                | date          | YES  | MUL | NULL    |       |
| admin_id                  | int           | NO   |     | NULL    |       |
| company_id                | int           | NO   |     | NULL    |       |
| is_paid                   | bit(1)        | NO   |     | NULL    |       |
| number_of_orders          | int           | YES  |     | NULL    |       |
| number_of_paid_orders     | int           | YES  |     | NULL    |       |
| billable_amount           | decimal(10,2) | YES  |     | NULL    |       |
| charge_id                 | varchar(100)  | YES  |     | NULL    |       |
| charged_at                | datetime      | YES  |     | NULL    |       |
| last_tried_at             | datetime      | YES  |     | NULL    |       |
| billing_subscription_plan | varchar(60)   | YES  |     | NULL    |       |
| upfront_payment_amount    | decimal(10,2) | YES  |     | 0.00    |       |
| discount_amount           | decimal(10,2) | NO   |     | 0.00    |       |
| wallet_amount             | decimal(10,2) | YES  |     | 0.00    |       |
| payment_source            | varchar(56)   | YES  |     | NULL    |       |
+---------------------------+---------------+------+-----+---------+-------+
15 rows in set (0.07 sec)



mysql> desc order_info;
+--------------------------------------+----------------------------------------------------------------------------+------+-----+---------------------+-------------------+
| Field                                | Type                                                                       | Null | Key | Default             | Extra             |
+--------------------------------------+----------------------------------------------------------------------------+------+-----+---------------------+-------------------+
| order_id                             | int                                                                        | NO   | PRI | NULL                | auto_increment    |
| order_number                         | varchar(250)                                                               | NO   |     | NULL                |                   |
| company_id                           | int                                                                        | NO   | MUL | NULL                |                   |
| area_id                              | int                                                                        | NO   |     | NULL                |                   |
| customer_id                          | int                                                                        | NO   | MUL | NULL                |                   |
| resturant_id                         | int                                                                        | NO   | MUL | NULL                |                   |
| placement_time                       | datetime                                                                   | NO   |     | CURRENT_TIMESTAMP   | DEFAULT_GENERATED |
| distance_between_pickup_delivery     | double                                                                     | YES  |     | NULL                |                   |
| driving_time_between_pickup_delivery | double                                                                     | YES  |     | NULL                |                   |
| expected_delivery_date               | date                                                                       | YES  |     | NULL                |                   |
| expected_pickup_time                 | time                                                                       | YES  |     | NULL                |                   |
| expected_delivery_time               | time                                                                       | YES  |     | NULL                |                   |
| order_item                           | longtext                                                                   | NO   |     | NULL                |                   |
| assigned_carrier_id                  | int                                                                        | YES  | MUL | NULL                |                   |
| accepted                             | tinyint(1)                                                                 | NO   |     | 1                   |                   |
| assigned_time                        | datetime                                                                   | YES  |     | NULL                |                   |
| start_time                           | datetime                                                                   | YES  |     | NULL                |                   |
| pickedup_time                        | datetime                                                                   | YES  |     | NULL                |                   |
| arrived_time                         | datetime                                                                   | YES  |     | NULL                |                   |
| delivery_time                        | datetime                                                                   | YES  |     | NULL                |                   |
| tag_number                           | int                                                                        | YES  |     | NULL                |                   |
| signature_path                       | longtext                                                                   | YES  |     | NULL                |                   |
| signature_location_latitude          | double                                                                     | YES  |     | NULL                |                   |
| signature_location_longitude         | double                                                                     | YES  |     | NULL                |                   |
| address_mark                         | int                                                                        | YES  |     | 1                   |                   |
| feedback                             | tinyint                                                                    | YES  |     | NULL                |                   |
| delivery_note                        | longtext                                                                   | YES  |     | NULL                |                   |
| total_cost                           | decimal(30,10)                                                             | NO   |     | NULL                |                   |
| delivery_fee                         | decimal(30,10)                                                             | NO   |     | NULL                |                   |
| predefined_tip                       | decimal(30,10)                                                             | NO   |     | NULL                |                   |
| cash_tip                             | decimal(30,10)                                                             | NO   |     | NULL                |                   |
| discount_amount                      | decimal(30,10)                                                             | NO   |     | NULL                |                   |
| tax                                  | decimal(30,10)                                                             | NO   |     | NULL                |                   |
| payment_method                       | enum('CASH','CREDIT_CARD','ONLINE','CARD','CARD_PHONE','CARD_ON_DELIVERY') | YES  |     | NULL                |                   |
| credit_card_type                     | enum('VISA','MASTER_CARD','AMEX','OTHER')                                  | YES  |     | NULL                |                   |
| credit_card_id                       | int                                                                        | YES  |     | NULL                |                   |
| delivery_instruction                 | longtext                                                                   | YES  |     | NULL                |                   |
| order_source                         | longtext                                                                   | NO   |     | NULL                |                   |
| second_leg_time                      | double                                                                     | YES  |     | NULL                |                   |
| auto_assignment_status               | enum('NOT_ASSIGNED','ASSIGNED','NO_AVAILABLE_CARRIER','NO_VALID_CARRIER')  | NO   |     | NOT_ASSIGNED        |                   |
| incomplete                           | tinyint                                                                    | NO   |     | 0                   |                   |
| parent_id                            | int                                                                        | NO   |     | -1                  |                   |
| dispatcher_note                      | longtext                                                                   | YES  |     | NULL                |                   |
| is_scheduled                         | tinyint                                                                    | NO   |     | 0                   |                   |
| force_completed                      | tinyint(1)                                                                 | NO   |     | 0                   |                   |
| order_image                          | mediumtext                                                                 | YES  |     | NULL                |                   |
| order_thumb_image                    | mediumtext                                                                 | YES  |     | NULL                |                   |
| order_seq_num                        | int                                                                        | NO   |     | 0                   |                   |
| eta_time                             | varchar(50)                                                                | YES  |     | NULL                |                   |
| failed_delivery_time                 | datetime                                                                   | YES  |     | NULL                |                   |
| provider                             | varchar(63)                                                                | YES  |     | NULL                |                   |
| driver_payment                       | double                                                                     | YES  |     | NULL                |                   |
| additional_id                        | varchar(255)                                                               | YES  |     | NULL                |                   |
| pickup_id                            | varchar(255)                                                               | YES  |     | NULL                |                   |
| feedback_details                     | varchar(512)                                                               | NO   |     |                     |                   |
| order_status                         | varchar(45)                                                                | YES  |     | NOT_ASSIGNED        |                   |
| order_status_admin                   | varchar(45)                                                                | YES  |     | NOT_READY_TO_PICKUP |                   |
| id_required                          | tinyint(1)                                                                 | YES  |     | 0                   |                   |
| gateway                              | varchar(255)                                                               | YES  |     | NULL                |                   |
| platform                             | varchar(255)                                                               | YES  |     | NULL                |                   |
| review_submitted                     | tinyint(1)                                                                 | YES  |     | 0                   |                   |
| review_notified                      | tinyint(1)                                                                 | YES  |     | 0                   |                   |
| is_replicated                        | tinyint                                                                    | YES  |     | 0                   |                   |
| third_party_assigned                 | tinyint                                                                    | YES  |     | 0                   |                   |
| pickup_instruction                   | text                                                                       | YES  |     | NULL                |                   |
| third_party_assigned_anytime         | tinyint                                                                    | YES  |     | 0                   |                   |
| arrived_dropoff_time                 | datetime                                                                   | YES  |     | NULL                |                   |
| arrived_pickup_time                  | bigint                                                                     | YES  |     | NULL                |                   |
| pickup_ready_time                    | bigint                                                                     | YES  |     | NULL                |                   |
| driver_rating                        | int                                                                        | YES  |     | NULL                |                   |
| left_pickup                          | bigint                                                                     | YES  |     | NULL                |                   |
| is_catering                          | tinyint(1)                                                                 | YES  |     | 0                   |                   |
| meta_data                            | json                                                                       | YES  |     | NULL                |                   |
| insert_time                          | datetime                                                                   | YES  |     | CURRENT_TIMESTAMP   | DEFAULT_GENERATED |
| insert_seq                           | int                                                                        | YES  |     | 0                   |                   |
| approaching_drop_off_notified        | tinyint(1)                                                                 | YES  |     | 0                   |                   |
+--------------------------------------+----------------------------------------------------------------------------+------+-----+---------------------+-------------------+
76 rows in set (0.08 sec)

mysql> 



-----------------------+--------------+------+-----+---------+----------------+
| Field                 | Type         | Null | Key | Default | Extra          |
+-----------------------+--------------+------+-----+---------+----------------+
| carrier_id            | int          | NO   | PRI | NULL    | auto_increment |
| name                  | longtext     | NO   |     | NULL    |                |
| code_name             | longtext     | NO   |     | NULL    |                |
| phone_number          | longtext     | NO   |     | NULL    |                |
| company_id            | int          | NO   | MUL | NULL    |                |
| status                | tinyint(1)   | NO   |     | NULL    |                |
| area_id               | int          | NO   |     | NULL    |                |
| vehicle_id            | int          | NO   | MUL | NULL    |                |
| email                 | longtext     | NO   |     | NULL    |                |
| password              | longtext     | NO   |     | NULL    |                |
| image_path            | longtext     | YES  |     | NULL    |                |
| is_logged_in          | tinyint(1)   | NO   |     | NULL    |                |
| attending_order_id    | int          | YES  |     | NULL    |                |
| plate_number          | text         | YES  |     | NULL    |                |
| vehicle_description   | text         | NO   |     | NULL    |                |
| thumbnail_image_path  | text         | YES  |     | NULL    |                |
| is_deleted            | tinyint(1)   | NO   |     | 0       |                |
| is_locked             | tinyint(1)   | YES  |     | 0       |                |
| deletion_time         | datetime     | YES  |     | NULL    |                |
| personal_id           | mediumtext   | YES  |     | NULL    |                |
| device                | varchar(255) | YES  |     | ""      |                |
| os_info               | varchar(255) | YES  |     | ""      |                |
| carrier_note          | longtext     | YES  |     | NULL    |                |
| login_time            | datetime     | YES  |     | NULL    |                |
| login_domain          | varchar(50)  | YES  |     | NULL    |                |
| app_version           | varchar(50)  | YES  |     |         |                |
| total_rated_orders    | bigint       | NO   |     | 0       |                |
| total_rating          | bigint       | NO   |     | 0       |                |
| aggregation_count     | int          | NO   |     | 0       |                |
| ai_summary_carrier    | mediumtext   | NO   |     | NULL    |                |
| ai_summary_dispatcher | mediumtext   | NO   |     | NULL    |                |
+-----------------------+--------------+------+-----+---------+----------------+
31 rows in set (0.07 sec)

mysql> 
