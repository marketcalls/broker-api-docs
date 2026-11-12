# Webhook

> Source: https://invest.motilaloswal.com/moAPI/APIDocumentation/Introduction

## Trade Webhook

Webhook Trade Status API will function in providing trade status updates through webhook URL and provide Trade responses. The Webhook functionality can be called using below url and input parameters.

| Method | GET |
| --- | --- |
| Production URL | https://openapi.motilaloswal.com/webhook |
| Test URL | https://openapi.motilaloswaluat.com/webhook |
| Request | JSON |
| Response | JSON |

## Sample Request (Body)

```json
{
"clientid":  "AA020",
"authtoken": "166d2344567848wfgreg2334esa222_M",
"apikey":    ""
}
```

## Sample JSON response

```json
{
"clientid": "AA020",
"exchange": "NSE",
"symboltoken": 11536,
"producttype": "NORMAL",
"symbol": "TCS EQ",
"instrumenttype": "",
"series": "EQ",
"strikeprice": 0,
"optiontype": "EQ",
"expirydate": "0",
"lotsize": 1,
"precision": 2,
"multiplier": 1,
"tradeprice": 3597.05,
"tradeqty": 1,
"tradevalue": 3597.05,
"buyorsell": "BUY",
"orderid": "1100000000160907",
"tradeno": "50160094",
"tradetime": "15-Mar-2022 18:44:54",
"uniqueorderid": "1500006T024312"
}
```

## Webhook Server Error Codes

| Sr. No | Error Code | Description |
| --- | --- | --- |
| 1 | MO1001 | Invalid User Id Or Auth Token |
| 2 | MO8000 | Technical Error |
| 3 | MO2012 | Invalid Action Request. |
