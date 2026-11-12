# Place Order

> Source: https://invest.motilaloswal.com/moAPI/APIDocumentation/Introduction
>
> Section: Orders

The status of the order is not known at the moment of placing order.

| Method | POST |
| --- | --- |
| Production URL | https://openapi.motilaloswal.com/rest/trans/v2/placeorder |
| Test URL | https://openapi.motilaloswaluat.com/rest/trans/v2/placeorder |
| Request | None or JSON (in case of Dealer) |
| Response | JSON |

## Request JSON

| Field | Type | Mandatory | Description |
| --- | --- | --- | --- |
| clientcode | String(15) | N | Client ID Mandatory in case of Dealer |
| exchange | String(15) | Y | Name of the Exchange |
| symboltoken | Number | Y | Exchange Scrip code or Symbol Token is unique identifier |
| buyorsell | String(10) | Y | Transaction Type (BUY, SELL) |
| ordertype | String(10) | N | Order Type(LIMIT, MARKET, STOPLOSS) |
| producttype | String(15) | Y | Product type (NORMAL, DELIVERY, SELLFROMDP, VALUEPLUS, BTST,MTF) |
| orderduration | String(10) | Y | Order duration (DAY,GTC,GTD,IOC) |
| price | Decimal(15,4) | Y | Price in Rupees. Up to 4 decimal places. |
| triggerprice | Decimal(15,4) | N | Price in Rupees. Up to 4 decimal places. |
| quantityinlot | Number | Y | Quantity to transact. In terms of Lots |
| disclosedquantity | Number | N | Quantity to disclose (for equity) |
| amoorder | String(1) | Y | AMO-Order (Y or N) |
| goodtilldate | String(11) | N | DD-MMM-YYYY |
| algoid | String(10) | N | Algo Id or Blank for Non-Algo Orders |
| tag | String(10) | N | Echo back to identify order. |
| participantcode | String(20) | N | Participant Code |

## Sample Request (Body)

```json
{
"clientcode":"", // Client code required only in case of Dealer
"exchange":"NSE",
"symboltoken":1660,
"buyorsell":"BUY",
"ordertype":"LIMIT",
"producttype":"Normal",
"orderduration":"DAY",
"price":235.5,
"triggerprice":0,
"quantityinlot":2,
"disclosedquantity":0,
"amoorder":"N",
"algoid":"",
"goodtilldate":"30-Jan-2022",
"tag":" ",   // max 10 characters
"participantcode": "218450147IH"
}
```

## Sample Response (Success)

```json
{
"status": "SUCCESS",
"message": "Order Placed Successfully",
"errorcode": "",
"uniqueorderid": "2400155AA020"
}
```

## Sample Response (Failure)

```json
{
"status": "ERROR",
"message": "Invalid Product Type Parameter",
"errorcode": "MO1057"
}
```

| Field | Type | Description |
| --- | --- | --- |
| uniqueorderid | String(50) | Unique Order ID as received in Order place |
