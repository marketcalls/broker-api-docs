# Postback API

- [Postback](#postback)

## Postback

Source: https://developer.paytmmoney.com/docs/api/Postback/

### Description

> The Postback API initiates a POST request containing a JSON payload to the designated postback\_url of your application whenever there's a change in an order's status. This functionality ensures that you consistently receive updates regarding your orders, regardless of the timing (whether they're Executed, Canceled, Rejected, or Pending). An UPDATE postback specifically occurs when there's a modification to an open order or a partial fill, providing a means to monitor trades.

### Notes

To configure your postback URL, follow these steps:

1) Log in to your Paytm Money developer account.

      a) If you're setting up a new app: Click on the "Create New App" button to begin creating the app.

      b) If you're configuring an existing app: Click on the app for which you need to set up the postback URL.

2) Once you're in the app settings, locate the section for postback URL setup.

3) Enter the desired postback URL into the provided field. Ensure that it accurately reflects where you want to receive the postback notifications.

4) Fill in any other required fields or details as necessary.

5) After entering the necessary information, proceed with saving your settings by clicking on the appropriate button, typically labeled "Proceed" or "Save".

**Sample response on Postback URL**

{

  "exchange": "NSE",

  "segment": "E",

  "security\_id": "772",

  "client\_id": "2282\*\*\*\*",

  "exch\_order\_no": "1100000000117023",

  "order\_no": "8351240409121",

  "product": "C",

  "txn\_type": "B",

  "order\_type": "MKT",

  "display\_order\_type": "Market",

  "validity": "DAY",

  "display\_validity": "Day",

  "disc\_qty": 0,

  "disc\_qty\_rem": 0,

  "remaining\_quantity": 1,

  "quantity": 1,

  "traded\_qty": 0,

  "price": 0,

  "trigger\_price": 0,

  "serial\_no": 1,

  "trade\_price": 0,

  "avg\_traded\_price": 0,

  "algo\_ord\_no": "0.0",

  "strategy\_id": "NA",

  "off\_mkt\_flag": "false",

  "order\_date\_time": "2024-04-09 17:14:53",

  "exch\_order\_time": "2024-04-09 17:14:54",

  "last\_updated\_time": "2024-04-09 17:14:53",

  "remarks": "bhmpd171266309393400103",

  "mkt\_type": "NL",

  "reason\_description": "CONFIRMED",

  "leg\_no": "1",

  "mark\_pro\_flag": "N",

  "mark\_pro\_val": 0,

  "participant\_type": "B",

  "settlor": "90165",

  "gtc\_flag": "N",

  "encash\_flag": "N",

  "group\_id": 8,

  "instrument": "EQUITY",

  "symbol": "DABUR",

  "display\_product": "Delivery",

  "display\_status": "Pending",

  "status": "Pending",

  "lot\_size": 1,

  "sl\_trail": 0,

  "sl\_abstick\_value": "0.0",

  "pr\_abstick\_value": "0.0",

  "strike\_price": 0,

  "expiry\_date": "0001-01-01",

  "opt\_type": "XX",

  "display\_name": "Dabur India",

  "isin": "INE016A01026",

  "series": "EQ",

  "gtd\_date": "2024-04-09",

  "instrument\_type": "ES",

  "ref\_ltp": 503.15,

  "tick\_size": 5,

  "algo\_id": "0",

  "platform": "Open-api",

  "ext\_info": "{\"total\_qty\":10,\"rem\_qty\":10,\"algo\_order\_no\":\"202503032025\"}"

}
