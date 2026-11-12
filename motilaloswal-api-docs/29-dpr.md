# DPR Data API

> Source: https://invest.motilaloswal.com/moAPI/APIDocumentation/Introduction
>
> Section: DPR Data

This API is used to get daily price range of BANKNIFTY OR NIFTY scripts in json format

| Method | POST |
| --- | --- |
| Production URL | https://openapi.motilaloswal.com/rest/report/v3/getdprvalues |
| Test URL | https://openapi.motilaloswaluat.com/rest/report/v3/getdprvalues |
| Request | JSON |
| Response | JSON |

## Request JSON

| Field | Type | Mandatory | Description |
| --- | --- | --- | --- |
| clientcode | String | N | It's mandatory in case of Dealer only |
| Symbol | String | Y | It's either BANKNIFTY or NIFTY |

## Sample Request (Body)

```json
{
"clientcode":"", // In case of dealer else not required
"symbol:"BANKNIFTY"
}
```

## Sample Response

```json
{
"status": "SUCCESS",
"message": "DPR Data",
"errorcode": "",
"data": [
{
"exchangename": "NSEFO",
"exchange": 2,
"scripcode": 60605,
"scripname": "BANKNIFTY 24-Nov-2022 PE 38300",
"scripshortname": "BANKNIFTY",
"strikeprice": 38300,
"optiontype": "PE",
"instrumentname": "OPTIDX",
"expirydate": 1353767400,
"lowercircuitprice": 218.7,
"uppercircuitprice": 1918
},{......}  ]
}
```
