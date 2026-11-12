# EOD Data API

> Source: https://invest.motilaloswal.com/moAPI/APIDocumentation/Introduction
>
> Section: EOD Data

This API is used to get end of day data (OHLC,Volume) for different exchanges in json format

| Method | POST |
| --- | --- |
| Production URL | https://openapi.motilaloswal.com/rest/report/v3/geteoddatabyexchangename |
| Test URL | https://openapi.motilaloswaluat.com/rest/report/v3/geteoddatabyexchangename |
| Request | JSON |
| Response | JSON |

## Request JSON

| Field | Type | Mandatory | Description |
| --- | --- | --- | --- |
| clientcode | String | N | It's mandatory in case of Dealer only |
| exchangename | String | Y | NSE,BSE,NSEFO,NSECD,NCDEX,MCX,NSECO,BSECO,BSECD |

## Sample Request (Body)

```json
{
"clientcode":"AA020", // In case of dealer else not required
"exchangename":"NSEFO"
}
```

## Sample Response

```json
{
"status": "SUCCESS",
"message": "EOD Data",
"errorcode": "",
"data": [
{
"exchange": "NSE",
"scripcode": 4934,
"open": 218.9,
"high": 223.95,
"low": 217.55,
"close": 222.45,
"volume": 99235,
"date": "09-02-2023",
"scripfullname": "INDIA PESTICIDES LIMITED-IPL EQ",
"scripshortname": "IPL",
"instrumentname": "      ",
"expirydate": "0",
"strikeprice": 0,
"optiontype": "  "
},
{….} ]
}
```
