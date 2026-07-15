<!-- Source: https://smartapi.angelone.in/docs -->
<!-- Section: Postback/Webhook -->

# Postback/Webhook

Postback URL provides real time order updates for the orders placed via APIs. The Postback URL can be specified while creating the API Key. Updates will be sent to the mapped url against the API key used to execute the orders.

#### Sample Response

```json
{
"variety": "NORMAL",
"ordertype": "MARKET",
"producttype": "DELIVERY",
"duration": "DAY",
"price": 0.0,
"triggerprice": 0.0,
"quantity": "1000",
"disclosedquantity": "0",
"squareoff": 0.0,
"stoploss": 0.0,
"trailingstoploss": 0.0,
"tradingsymbol": "SBIN-EQ",
"transactiontype": "BUY",
"exchange": "NSE",
"symboltoken": "3045",
"ordertag": "10007712",
"instrumenttype": "",
"strikeprice": -1.0,
"optiontype": "",
"expirydate": "",
"lotsize": "1",
"cancelsize": "0",
"averageprice": 584.7,
"filledshares": "74",
"unfilledshares": "926",
"orderid": "111111111111111",
"text": "",
"status": "open",
"orderstatus": "open",
"updatetime": "09-Oct-2023 18:22:02",
"exchtime": "09-Oct-2023 18:21:12",
"exchorderupdatetime": "09-Oct-2023 18:21:12",
"fillid": "",
"filltime": "",
"parentorderid": "",
"clientcode": "DUMMY123"
}
```

**NOTE:**Postback service only allows the updates on HTTPS port 443For AMO orders, postback notifications will not be sent immediately at the time of placing the order after market hours. These notifications will be sent at 9:00 AM when those orders are sent to the exchange for processing.We are providing order status such as open, pending, executed, cancelled, partially executed and so on the postback call for the orders placed during market hours.
