## Notes

Polling:

after 1 or 2 mins we call the order API. Some return only ID, we can then use that to call for more info. We need to map their info to our info.



2 tables: restaurant mapping and platform_token?? mapping. 


Webhook

They send the order event to us whenever the order happens. Payload will contain all the merchant information so that we know which account to map it to. 




3 or 4 integrations use polling. 

WEbhook is first choice.

onboarding process is initiated from us for polling. 

Odoo is one of the example.

Check out odoo integration.

When add store we will add mapping in to the DB

mapping table -> restaurant_mapping, platform_token, lightspeed_mapping

might have to create a new table if can't map it to platform_token or lightspeed_mapping 

Even for webhook we need mapping table, so when order comes in we know which account it is for. 

after polling -> publish event.

we need to worry about whether the token is revoked 

It depends on each platform where the connection is initiated. 
