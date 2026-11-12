# INDEX LTP DATA API

> Source: https://invest.motilaloswal.com/moAPI/APIDocumentation/Introduction
>
> Section: Index Data

This API is used to get Open,High,Low,Close,LTP for different indexes of BSE and NSE in json format

| Method | POST |
| --- | --- |
| Production URL | https://openapi.motilaloswal.com/rest/report/v3/getindexltpdata |
| Test URL | https://openapi.motilaloswaluat.com/rest/report/v3/getindexltpdata |
| Request | JSON |
| Response | JSON |

## Request JSON

| Field | Type | Mandatory | Description |
| --- | --- | --- | --- |
| clientcode | String | N | Client ID Mandatory in case of Dealer |
| exchangename | String | Y | NSE,BSE |
| scripcode | String | Y | Index Code from Index data |

## Sample Request (Body)

```json
{
"clientcode":"AA020", // In case of dealer else not required
"exchange":"NSE",
"scripcode":"26000"
}
```

## Sample Response

```json
{
"status": "SUCCESS",
"message": "INDEX LTP DATA",
"errorcode": "",
"data": [
{
"exchange": "NSECASH",
"scripcode": 26000,
"open": 17451.25,
"high": 17579,
"low": 17427.7,
"close": 17321.9,
"ltp": 17566.6
}
]
}
```
