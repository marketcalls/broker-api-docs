# Scrip/Instrument

> Source: https://invest.motilaloswal.com/moAPI/APIDocumentation/Introduction
>
> Section: Master Data

This API is used to get exchange data by name in json format

| Method | POST |
| --- | --- |
| Production URL | https://openapi.motilaloswal.com/rest/report/v3/getscripsbyexchangename |
| Test URL | https://openapi.motilaloswaluat.com/rest/report/v3/getscripsbyexchangename |
| Request | None or JSON (in case of Dealer) |
| Response | JSON |

## Request JSON

| Field | Type | Mandatory | Description |
| --- | --- | --- | --- |
| clientcode | String(15) | N | Client ID Mandatory in case of Dealer |
| exchangename | String(10) | Y | Name of the Exchange |

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
"message": "Scrips Data",
"errorcode": "",
"data": [
{
"exchange": 2,
"exchangename": "NSEFO",
"scripcode": 35020,
"scripname": "BANKNIFTY 03-Feb-2022 PE 32300",
"marketlot": 25,
"scripshortname": "BANKNIFTY",
"issuspended": "N",
"instrumentname": "OPTIDX",
"expirydate": 1328365800,
"strikeprice": 32300,
"optiontype": "PE",
"markettype": " ",
"foexposurepercent": 0,
"lowercircuitprice": 0.05,
"uppercircuitprice": 26.6,
"ticksize": 0.05,
"scripisinno": "",
"indicesidentifier": 0,
"isbanscrip": "N",
"scripfullname": "BANKNIFTY 03-Feb-2022 PE 32300",
"facevalue": 0,
"calevel": 0 },
{
….}
]
}
```
