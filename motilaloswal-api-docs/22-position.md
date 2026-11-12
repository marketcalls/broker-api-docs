# Position

> Source: https://invest.motilaloswal.com/moAPI/APIDocumentation/Introduction
>
> Section: Portfolio

This API allows to fetch the complete information of the DP Holding of the Users

| Method | POST |
| --- | --- |
| Production URL | https://openapi.motilaloswal.com/rest/book/v4/getposition |
| Test URL | https://openapi.motilaloswaluat.com/rest/book/v4/getposition |
| Request | None or JSON(In case of Dealer) |
| Response | JSON |

## Request JSON

| Field | Type | Mandatory | Description |
| --- | --- | --- | --- |
| clientcode | String(15) | N | Client ID Mandatory in case of Dealer |

## Sample Request (Body)

```json
{
"clientcode":"AA017", //  in case of dealer else not required
}
```

## Sample Response

```json
{
"status": "SUCCESS",
"message": "Position Data",
"errorcode": "",
"data": [
{
"exchange": "NSE",
"clientcode": "AA020",
"productname": "NORMAL",
"symboltoken": 1660,
"symbol": "INFY",
"buyquantity": 0,
"buyamount": 0,
"sellquantity": 0,
"sellamount": 0,
"daybuyquantity": 0,
"daybuyamount": 0,
"daysellquantity": 0,
"daysellamount": 0,
"LTP": 0,
"marktomarket": 0,
"bookedprofitloss": 0,
"cfbuyquantity": 0,
"cfbuyamount": 0,
"cfsellquantity": 0,
"cfsellamount": 0,
"actualbookedprofitloss": 0,
"actualmarktomarket": 0,
"series": "EQ",
"expirydate": "0",
"strikeprice": 0,
"optiontype": "XX"
}
]
}
```

| Field | Type | Description |
| --- | --- | --- |
| exchange | String(50) | Name of the Exchange |
| clientcode | String(50) | Client ID |
| productname | String(20) | Name of product |
| symboltoken | Number | Exchange Scrip code or Symbol Token i.e.unique identifier |
| symbol | String(40) | Symbol |
| buyquantity | Number | Buy Order Quantity for transactaion i.e.carryforward + traded |
| buyamount | Decimal(15,4) | Buy Amount for transactaion i.e.carryforward (based on last day close) + traded |
| sellquantity | Number | Sell Order Quantity for transactaion i.e.carryforward + traded |
| sellamount | Decimal(15,4) | Sell Amount for transactaion i.e.carryforward (based on last day close) + traded |
| daybuyquantity | Number | Buy Order Quantity in a Day for transactaion i.e.todays traded |
| daybuyamount | Decimal(15,4) | Buy Amount in a day for transactaion i.e.today traded |
| daysellquantity | Number | Sell Order Quantity in a Day for transactaion i.e.today traded |
| daysellamount | Decimal(15,4) | Sell Amount in a day for transactaion i.e.today traded |
| LTP | Decimal(15,4) | Last Traded Price |
| marktomarket | Decimal(15,4) | Unrealized Loss / Profit |
| bookedprofitloss | Decimal(15,4) | Realized Loss / Profit |
| cfbuyquantity | Number | Buy Order Quantity in a Day for transactaion i.e. caryforward |
| cfbuyamount | Decimal(15,4) | Buy Amount in a day for transactaion i.e.caryforward (on actual buy amount) |
| cfsellquantity | Number | Sell Order Quantity in a Day for transactaion i.e.caryforward |
| cfsellamount | Decimal(15,4) | Sell Amount in a day for transactaion i.e.caryforward (on actual sell amount) |
| actualbookedprofitloss | Decimal(15,4) | Unrealized Loss / Profit based on Actual Avg Price |
| actualmarktomarket | Decimal(15,4) | Realized Loss / Profit based on Actual Avg Price |
| series | String(2) | Series |
| expirydate | String(40) | Expiry date of scrip |
| strikeprice | Decimal(15,4) | Price when order will excute |
| optiontype | String(2) | Option type |
