# Holding

> Source: https://invest.motilaloswal.com/moAPI/APIDocumentation/Introduction
>
> Section: Portfolio

This API allows to fetch the complete information of the DP Holding of the Users

| Method | POST |
| --- | --- |
| Production URL | https://openapi.motilaloswal.com/rest/report/v3/getdpholding |
| Test URL | https://openapi.motilaloswaluat.com/rest/report/v3/getdpholding |
| Request | None or JSON (in case of Dealer) |
| Response | JSON |

## Request JSON

| Field | Type | Mandatory | Description |
| --- | --- | --- | --- |
| clientcode | String(15) | N | Client ID Mandatory in case of Dealer |

## Sample Request (Body)

```json
{
"clientcode":"AA017", // In case of dealer else not required
}
```

## Sample Response

```json
{
"status": "SUCCESS",
"message": "DP Holding Data",
"errorcode": "",
"data": [
{
"clientcode": "AA020",
"scripisinno": "INE131B01039",
"dpquantity": 1119,
"blockedquantity": 0,
"scripname": "RELAXO EQ",
"buyavgprice": 813.66,
"poaquantity": 41,
"collateralquantity": 1078,
"outstandingquantity": 0,
"debitstockquantity": 0,
"nonpoaquantity": 0,
"rmssellingquantity": 0,
"btstquantity": 0,
"buybackquantity": 0,
"tpinquantity": 0,
"slbmquantity": 0,
"nbfcquantity": 0,
"bsescripcode":50001,
"nsesymboltoken":123
},
{....}..
]
}
```

| Field | Type | Description |
| --- | --- | --- |
| clientcode | String(20) | Client |
| scripisinno | String(20) | Unique Identifier of Scrip |
| dpquantity | Number | Total Quantity |
| blockedquantity | Number | Quantity Blocked against executed or pending orders |
| scripname | String(30) | Name of scrip |
| buyavgprice | Decimal(15,4) | Average price at which all shares were bought |
| poaquantity | Number | POA Quantity |
| collateralquantity | Number | Collateral Quantity |
| outstandingquantity | Number | Share purchased on T-2 Days |
| debitstockquantity | Number | CUSA Stock |
| nonpoaquantity | Number | Non POA Quantity |
| rmssellingquantity | Number | RMS Selling Quantity |
| btstquantity | Number | Share Purchased on T-1 Day |
| buybackquantity | Number | Quantity blocked against Buyback Orders |
| tpinquantity | Number | Quantity which required EDIS to sell |
| slbmquantity | Number | SLBM Quantity |
| nbfcquantity | Number | NBFC Quantity |
| bsescripcode | Number | BSE Scrip code i.e. unique identifier |
| nsesymboltoken | Number | NSE Symbol Token i.e. unique identifier |
