# Margin Summary

> Source: https://invest.motilaloswal.com/moAPI/APIDocumentation/Introduction
>
> Section: Limit/Margin

This API is used to get margin report summary

| Method | POST |
| --- | --- |
| Production URL | https://openapi.motilaloswal.com/rest/report/v3/getreportmarginsummary |
| Test URL | https://openapi.motilaloswaluat.com/rest/report/v3/getreportmarginsummary |
| Request | None or JSON (in case of Dealer) |
| Response | JSON |

## Request JSON

| Field | Type | Mandatory | Description |
| --- | --- | --- | --- |
| clientcode | String(15) | N | It's mandatory in case of Dealer |

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
"message": "REPORT MARGIN SUMMARY",
"errorcode": "",
"data": [
{
"srno": 102,
"particulars": "Total Available Margin for Cash",
"amount": 999998900000
},
{
"srno": 103,
"particulars": "Total Available Margin for FNO",
"amount": 999998900000
},
{
"srno": 104,
"particulars": "Total Available Margin for Curr",
"amount": 999998900000
},
{
"srno": 105,
"particulars": "Total Available Margin for Comm",
"amount": 999998900000
},
{
"srno": 106,
"particulars": "Total Available Margin for Other",
"amount": 0
},
{
"srno": 201,
"particulars": "Cash deposit",
"amount": 1000000000000
},
{
"srno": 220,
"particulars": "Non cash deposit",
"amount": 0
},
{
"srno": 301,
"particulars": "Margin Usage(B) Cash",
"amount": 0
},
{
"srno": 321,
"particulars": "Margin Usage(B) FO",
"amount": 560127.5
},
{
"srno": 340,
"particulars": "Margin Usage(B) Currency",
"amount": 0
},
{
"srno": 360,
"particulars": "Margin Usage(B) Commodity",
"amount": 547544
},
{
"srno": 381,
"particulars": "Margin Usage(B) Brokerage",
"amount": 0
},
{
"srno": 600,
"particulars": "Total Profit and Loss(MTM)",
"amount": 16050.07
},
{
"srno": 700,
"particulars": "Total Profit and Loss(BPL)",
"amount": 0
}
]
}
```
