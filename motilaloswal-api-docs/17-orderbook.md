# OrderBook

> Source: https://invest.motilaloswal.com/moAPI/APIDocumentation/Introduction
>
> Section: Orders

This API allows to fetch the complete information of the Orders of the Users

| Method | POST |
| --- | --- |
| Production URL | https://openapi.motilaloswal.com/rest/book/v5/getorderbook |
| Test URL | https://openapi.motilaloswaluat.com/rest/book/v5/getorderbook |
| Request | None or JSON(In case of Dealer) |
| Response | JSON |

## Request JSON

| Field | Type | Mandatory | Description |
| --- | --- | --- | --- |
| clientcode | String(15) | N | Its Mandatory in case of Dealer |

## Sample Request (Body)

```json
{
"clientcode":"AA017" // in case of dealer else not required
}
```

## Sample Response

```json
{
"status": "SUCCESS",
"message": "Order Data",
"errorcode": ""
"data": [
{
"ordercategory": "NORMAL",
"clientid": "AA020",
"exchange": "BSE",
"symboltoken": 500116,
"symbol": "IDBI",
"series": "A",
"expirydate": "0",
"strikeprice": 0,
"optiontype": "XX ",
"orderid": "1120001",
"orderinitiatorid": "27120",
"ordertype": "Market",
"orderduration": "Day",
"producttype": "NORMAL",
"error": "Market/Close price not available.",
"orderstatus": "Error",
"buyorsell": "Buy",
"totalqtyremaining": 1,
"orderqty": 1,
"qtytradedtoday": 0,
"disclosedqty": 0,
"price": 0,
"triggerprice": 0,
"entrydatetime": "0",
"lastmodifiedtime": "0",
"vendor": "NewOrder",
"uniqueorderid": "1000001AA020",
"goodtilldate": "0",
"algoid": 0,
"algocategory": 0
"averageprice": 394305,
"totalqtytraded": 1,
"lotsize": 1,
"tag":" ",
"recordinserttime": 14-Feb-2023 10:52:50,
"participantcode": "218450147IH"
},
{...}...
]

}
```

## Response JSON

| Field | Type | Description |
| --- | --- | --- |
| Field | Type | Description |
| ordercategory | String(15) | Category of order by default NORMAL |
| clientid | String(50) | Client Id |
| exchange | String(50) | Name of the Exchange |
| symboltoken | Number | Exchange Scrip code or Symbol Token i.e. unique identifier |
| symbol | String(40) | Symbol |
| series | String(2) | Series |
| expirydate | String(20) | Expiry date of scrip |
| strikeprice | Number | Strike Price |
| optiontype | String(2) | Option Type |
| orderid | String(50) | Order ID |
| orderinitiatorid | String(50) | Contains logged in ID from which order is generated |
| ordertype | String(10) | Order Type(LIMIT, MARKET, STOPLOSS) |
| orderduration | String(50) | Order duration (DAY,GTC,GTD,IOC) |
| producttype | String(20) | Product type (Normal, Delivery etc.) |
| error | String(1000) | Error in case of order is not executed |
| orderstatus | String(50) | Current status of the order |
| buyorsell | String(10) | Order Transaction Type (BUY, SELL) |
| totalqtyremaining | Number | Total quantityremaining for the order |
| orderqty | Number | Order Quantity for transactaion |
| qtytradedtoday | Number | It contains quantity traded today for the order |
| disclosedqty | Number | Order Quantity to be disclosed (for equity) |
| price | Decimal(15,4) | Price in Rupees. Up to 4 decimal places. |
| triggerprice | Decimal(15,4) | the price at which an order will be triggered |
| entrydatetime | String(40) | Time when fresh order is executed |
| lastmodifiedtime | String(40) | Time which order last modified |
| vendor | String(50) | Name of the vendor |
| uniqueorderid | String(50) | Unique Order ID as received in Order |
| goodtilldate | String(40) | Date up to which order should be retained |
| algoid | Number | Algo Id or Blank for Non-Algo Orders |
| algocategory | Number | Algo category |
| averageprice | Decimal(15,4) | Average price at which the order was executed |
| totalqtytraded | Number | Quantity traded |
| lotsize | Number | Quantity of a single lot |
| tag | String(10) | Echo back to identify order |
| recordinserttime | String(20) | Record Insert Time |
| participantcode | String(20) | Participant Code |
