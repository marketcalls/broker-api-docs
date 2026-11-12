# Margin Detail

> Source: https://invest.motilaloswal.com/moAPI/APIDocumentation/Introduction
>
> Section: Limit/Margin

This API is used to get margin report summary in Detail

| Method | POST |
| --- | --- |
| Production URL | https://openapi.motilaloswal.com/rest/report/v3/getreportmargindetail |
| Test URL | https://openapi.motilaloswaluat.com/rest/report/v3/getreportmargindetail |
| Request | None or JSON(In case of Dealer) |
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
"message": "REPORT MARGIN DETAIL",
"errorcode": "",
"data": [
{
"srno": 100,
"particulars": "Total Available Margin(A-B-C-D)",
"amount": 49833896
},
{
"srno": 101,
"particulars": "Credit Limit",
"amount": 0
},
{
"srno": 102,
"particulars": "Available for Cash / SLBM Segment",
"amount": 49833896
},
{
"srno": 103,
"particulars": "Available for FO Segment",
"amount": 49833896
},
{
"srno": 104,
"particulars": "Available for Currency Segment",
"amount": 49833896
},
{
"srno": 105,
"particulars": "Available for Commodity Segment",
"amount": 49833896
},
{
"srno": 106,
"particulars": "Available for IPO/MF/FD/BOND / Option Buy",
"amount": 0
},
{
"srno": 200,
"particulars": "Total Margin (A)",
"amount": 50474920
},
{
"srno": 201,
"particulars": "Cash Balance(Cash Margin)",
"amount": 50000000
},
{
"srno": 202,
"particulars": "Cash Balance(Ledger Balance)",
"amount": 50000000
},
{
"srno": 203,
"particulars": "Add: Normal Fund Transfer",
"amount": 0
},
{
"srno": 204,
"particulars": "Add: MTF Loss",
"amount": 0
},
{
"srno": 205,
"particulars": "Add: Credit from stock sold from DMAT",
"amount": 0
},
{
"srno": 507,
"particulars": "Add: Scrip Capital Cash",
"amount": 0
},
{
"srno": 206,
"particulars": "Add: Option Premium Received",
"amount": 0
},
{
"srno": 207,
"particulars": "Add : Max Realize Cheque Amunt",
"amount": 0
},
{
"srno": 220,
"particulars": "Non-Cash Balance(Non-Cash Margin)",
"amount": 474919.06
},
{
"srno": 221,
"particulars": "Demat Stock Margin after Haircut",
"amount": 474919.06
},
{
"srno": 222,
"particulars": "Stock Margin after Haircut Segment - Intra",
"amount": 0
},
{
"srno": 223,
"particulars": "Stock Margin after Haircut Segment - Delivery",
"amount": 0
},
{
"srno": 224,
"particulars": "Stock Margin after Haircut Segment - FO",
"amount": 0
},
{
"srno": 225,
"particulars": "Stock Margin after Haircut Segment - Currency",
"amount": 0
},
{
"srno": 226,
"particulars": "Stock Margin after Haircut Segment - Commodity",
"amount": 0
},
{
"srno": 507,
"particulars": "Stock Capital Cash",
"amount": 0
},
{
"srno": 508,
"particulars": "Stock Capital Approved",
"amount": 474919.06
},
{
"srno": 250,
"particulars": "Add: Additional  Limit",
"amount": 0
},
{
"srno": 251,
"particulars": "Additional Cash Limit  - Cash",
"amount": 0
},
{
"srno": 252,
"particulars": "Additional Cash Limit  - FO",
"amount": 0
},
{
"srno": 253,
"particulars": "Additional Cash Limit  - Currency",
"amount": 0
},
{
"srno": 254,
"particulars": "Additional Cash Limit  - Commodity",
"amount": 0
},
{
"srno": 255,
"particulars": "Add: MutualFund/NCD/BOND/FD",
"amount": 0
},
{
"srno": 509,
"particulars": "Add: Mutual Fund Cash",
"amount": 0
},
{
"srno": 510,
"particulars": "Add: Mutual Fund  Approved",
"amount": 0
},
{
"srno": 300,
"particulars": "Margin Usage Details (B)",
"amount": 622432.4
},
{
"srno": 301,
"particulars": "Equities",
"amount": 674.75
},
{
"srno": 302,
"particulars": "Margin on orders/Trades",
"amount": 674.75
},
{
"srno": 303,
"particulars": "Mutual Fund / IPO / BOND",
"amount": 0
},
{
"srno": 304,
"particulars": "MTF Margin",
"amount": 0
},
{
"srno": 321,
"particulars": "FO",
"amount": 362139.88
},
{
"srno": 322,
"particulars": "Add: FO Span Margin on Order/Trade and Premium Paid",
"amount": 303062.5
},
{
"srno": 323,
"particulars": "Add: FO exposure margin on order/trade",
"amount": 59077.38
},
{
"srno": 324,
"particulars": "Add: FO Special margin on order/trade",
"amount": 0
},
{
"srno": 325,
"particulars": "Add: FO Additional margin on order/trade",
"amount": 0
},
{
"srno": 340,
"particulars": "Currency",
"amount": 1854.91
},
{
"srno": 341,
"particulars": "Add: Currency Span Margin on Order/Trade and Premium Paid",
"amount": 1465.27
},
{
"srno": 342,
"particulars": "Add: Currency exposure margin on order/trade",
"amount": 389.64
},
{
"srno": 343,
"particulars": "Add: Currency Special margin on order/trade",
"amount": 0
},
{
"srno": 344,
"particulars": "Add: Currency Additional margin on order/trade",
"amount": 0
},
{
"srno": 360,
"particulars": "Commodity",
"amount": 257500
},
{
"srno": 361,
"particulars": "Add: Commodity Span Margin on Order/Trade and Premium Paid",
"amount": 257500
},
{
"srno": 362,
"particulars": "Add: Commodity exposure margin on order/trade",
"amount": 0
},
{
"srno": 363,
"particulars": "Add: Commodity Special margin on order/trade",
"amount": 0
},
{
"srno": 364,
"particulars": "Add: Commodity Additional margin on order/trade",
"amount": 0
},
{
"srno": 380,
"particulars": "SLBM",
"amount": 262.84
},
{
"srno": 381,
"particulars": "Brokerage",
"amount": 0
},
{
"srno": 400,
"particulars": "Profit / Loss (MTM) Details C",
"amount": -18590
},
{
"srno": 401,
"particulars": "Equities",
"amount": 0
},
{
"srno": 402,
"particulars": "Add: Unrealised (Net)",
"amount": 0
},
{
"srno": 403,
"particulars": "Add: Realised P/L (Net)",
"amount": 0
},
{
"srno": 421,
"particulars": "FO",
"amount": -18590
},
{
"srno": 422,
"particulars": "Add: Unrealised (Net)",
"amount": -18590
},
{
"srno": 423,
"particulars": "Add: Realised P/L (Net)",
"amount": 0
},
{
"srno": 441,
"particulars": "Currency",
"amount": 0
},
{
"srno": 442,
"particulars": "Add: Unrealised (Net)",
"amount": 0
},
{
"srno": 443,
"particulars": "Add: Realised P/L (Net)",
"amount": 0
},
{
"srno": 461,
"particulars": "Commodity",
"amount": 0
},
{
"srno": 462,
"particulars": "Add: Unrealised (Net)",
"amount": 0
},
{
"srno": 463,
"particulars": "Add: Realised P/L (Net)",
"amount": 0
},
{
"srno": 481,
"particulars": "SLBM ",
"amount": 0
},
{
"srno": 482,
"particulars": "Add: Unrealised (Net)",
"amount": 0
},
{
"srno": 483,
"particulars": "Add: Realised P/L (Net)",
"amount": 0
},
{
"srno": 500,
"particulars": "Others(D)",
"amount": 0
},
{
"srno": 501,
"particulars": "Fund withdrawal Request (Transfer to Bank)",
"amount": 0
},
{
"srno": 502,
"particulars": "Max Fund Withdrawal for the day",
"amount": 0
},
{
"srno": 503,
"particulars": "Unrealize Cheque Amount",
"amount": 0
},
{
"srno": 504,
"particulars": "Option Obligation(F & O)",
"amount": 0
},
{
"srno": 505,
"particulars": "Option Obligation(Currency)",
"amount": 0
},
{
"srno": 506,
"particulars": "Option Obligation(Commodity)",
"amount": 0
},
{
"srno": 600,
"particulars": "Total Profit and Loss(MTM)",
"amount": -18590
},
{
"srno": 700,
"particulars": "Total Profit and Loss(BPL)",
"amount": 0
}
]
}
```
