# Index Data API

> Source: https://invest.motilaloswal.com/moAPI/APIDocumentation/Introduction
>
> Section: Index Data

This API is used to get index data for BSE,NSE in json format

| Method | POST |
| --- | --- |
| Production URL | https://openapi.motilaloswal.com/rest/report/v3/getindexdatabyexchangename |
| Test URL | https://openapi.motilaloswaluat.com/rest/report/v3/getindexdatabyexchangename |
| Request | JSON |
| Response | JSON |

## Request JSON

| Field | Type | Mandatory | Description |
| --- | --- | --- | --- |
| clientcode | String | N | It's mandatory in case of Dealer only |
| exchangename | String | Y | NSE,BSE |

## Sample Request (Body)

```json
{
"clientcode":"AA020", // In case of dealer else not required
"exchangename":"NSE"
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
"indexcode": 26009,
"indexname": "Nifty Bank",
},
{
"exchange": "NSE",
"indexcode": 26012,
"indexname": "Nifty 100",
},
{
"exchange": "NSE",
"indexcode": 26065,
"indexname": "Nifty 200",
},{..},{..},....

}
```
