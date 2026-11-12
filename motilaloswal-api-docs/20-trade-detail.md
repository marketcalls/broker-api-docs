# Trade Detail

> Source: https://invest.motilaloswal.com/moAPI/APIDocumentation/Introduction
>
> Section: Orders

This API allows to fetch the complete information of the Trades of the Users based on uniqueorderid

| Method | POST |
| --- | --- |
| Production URL | https://openapi.motilaloswal.com/rest/book/v4/gettradedetailbyuniqueorderid |
| Test URL | https://openapi.motilaloswaluat.com/rest/book/v4/gettradedetailbyuniqueorderid |
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
"clientcode":"AA017", // In case of dealer else not required
"uniqueorderid":"2700002AA020"
}
```

## Sample Response

```json
{
"status": "SUCCESS",
"message": "Trade Data",
"errorcode": "",
"data": [
{
"clientid": "AA020",
"exchange": "NCDEX",
"symboltoken": "48725",
"producttype": "NORMAL",
"symbol": "COCUDAKL",
"instrumenttype": "FUTCOM",
"series": "XX",
"strikeprice": -1,
"optiontype": "XX",
"expirydate": "20/01/2022",
"lotsize": 10,
"precision": 2,
"multiplier": 10,
"tradeprice": 278400,
"tradeqty": 20,
"tradevalue": 5568000,
"buyorsell": "Sell",
"orderid": "112000321",
"tradeno": "12343",
"tradetime": "10/01/2022",
"uniqueorderid": "2700002AA020",
},
{...}...
]
}
```
