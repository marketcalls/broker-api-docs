# Order Detail

> Source: https://invest.motilaloswal.com/moAPI/APIDocumentation/Introduction
>
> Section: Orders

This API allows to fetch the complete information of the Orders based on uniqueorderid

| Method | POST |
| --- | --- |
| Production URL | https://openapi.motilaloswal.com/rest/book/v5/getorderdetailbyuniqueorderid |
| Test URL | https://openapi.motilaloswaluat.com/rest/book/v5/getorderdetailbyuniqueorderid |
| Request | None or JSON(In case of Dealer) |
| Response | JSON |

## Request JSON

| Field | Type | Mandatory | Description |
| --- | --- | --- | --- |
| clientcode | String(15) | N | Its mandatory in case of Dealer |
| uniqueorderid | String(50) | Y | Unique Order ID |

## Sample Request (Body)

```json
{
"clientcode":"", // In case of dealer else not required
"uniqueorderid":"1000001AA020"
}
```

## Sample Response

```json
{
"status": "SUCCESS",
"message": "Order Data",
"errorcode": "",
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
"ordertype": "C",
"booktype": "Market",
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
"stoploss": 0,
"squareoff": 0,
"trailingstoploss": 0,
"uniqueorderid": "1000001AA020",
"goodtilldate": "0",
"algoid": 0,
"algocategory": 0,
"averageprice": 394305,
"totalqtytraded": 1,
"lotsize": 1,
"recordinserttime": 14-Feb-2023 10:52:50,
"participantcode": "218450147IH"
},
{...}...
]
}
```
