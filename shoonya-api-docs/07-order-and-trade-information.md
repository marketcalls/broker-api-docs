# Order & Trade Information

> Source: https://shoonya.com/api-documentation (Order & Trade Information)

## Contents

- [Order Margin](#order-margin)
- [Basket Margin](#basket-margin)
- [Order Book](#order-book)
- [Single Order History](#single-order-history)
- [Single Order Status](#single-order-status)
- [Trade Book](#trade-book)
- [Positions Book](#positions-book)

---

## Order Margin

> Request to be POSTed to URL : /NorenWClientAPI/GetOrderMargin

### Request Details

| Parameter Name | Possible value | Description |
|---|---|---|
| jData* | - | Should send json object with fields in below list |

**Json Fields**

| Parameter Name | Possible value | Description |
|---|---|---|
| uid* | - | Logged in User Id |
| actid* | - | Login users account ID |
| exch* | NSE / NFO / BSE / MCX | Exchange (Select from ‘exarr’ Array provided in User Details response) |
| tsym* | - | Unique id of contract on which order to be placed. (use url encoding to avoid special char error for symbols like M&M) |
| qty* | - | Order Quantity |
| prc* | - | Order Price |
| trgprc | - | Only to be sent in case of SL / SL-M order. |
| prd* | C / M / H | Product name (Select from 'prarr' Array provided in User Details response, and if same is allowed for selected, exchange. Show product display name, for user to select, and send corresponding prd in API call) |
| trantype* | B / S | B -> BUY, S -> SELL |
| prctyp* | LMT / MKT / SL-LMT / SL-MKT | - |
| blprc | - | Book loss Price applicable only if product is selected as H and B (High Leverage and Bracket order ) |
| rorgqty | - | Optional field. Application only for modify order, open order quantity |
| fillshares | - | Optional field. Application only for modify order, quantity already filled. |
| rorgprc | - | Optional field. Application only for modify order, open order price |
| orgtrgprc | - | Optional field. Application only for modify order, open order trigger price |
| norenordno | - | Optional field. Application only for H or B order modification |
| snonum | - | Optional field. Application only for H or B order modification |
| rms_exch | - | Optional field. |
| rms_seg | - | Optional field. |
| rms_prd | - | Optional field. |

### Response Details

| Parameter Name | Possible value | Description |
|---|---|---|
| stat | Ok or Not_Ok | Place order success or failure indication. |
| request_time | - | Response received time. |
| remarks | - | This field will be available only on success. |
| cash | - | Total credits available for order |
| marginused | - | Meaning changes with remarks as explained below. |
| ordermargin | - | Margin required for this order. |
| marginusedprev | - | Margin used excluding this order. |
| emsg | - | This will be present only if Order placement fails. |

### calculation

```
The /Limits API must be called first in order to calculate the post-trade margin and basket
margin. Here, the marginused in the Limits API response will be [marginused(Limits)].
1.not ticked - include existing margin
post trade margin = marginusedtrade(GetBasketMargin) - marginused(Limits)
basket margin = marginused(GetBasketMargin) - marginused(Limits)
2.ticked - include existing margin
post trade margin = marginusedtrade(GetBasketMargin)
basket margin = marginused(GetBasketMargin)
```

## Basket Margin

> Request to be POSTed to URL : /NorenWClientAPI/GetBasketMargin

### Request Details

| Parameter Name | Possible value | Description |
|---|---|---|
| jData* | - | Should send json object with fields in below list |

**Json Fields**

| Parameter Name | Possible value | Description |
|---|---|---|
| uid* | - | Logged in User Id |
| actid* | - | Login users account ID |
| exch* | NSE / NFO / BSE / MCX | Exchange (Select from 'exarr' Array provided in User Details response) |
| tsym* | - | Unique id of contract on which order to be placed. (use url encoding to avoid special char error for symbols like M&M) |
| qty* | - | Order Quantity |
| prc* | - | Order Price |
| trgprc | - | Only to be sent in case of SL / SL-M order. |
| prd* | C / M / H | Product name (Select from 'prarr' Array provided in User Details response, and if same is allowed for selected, exchange. Show product display name, for user to select, and send corresponding prd in API call) |
| trantype* | B / S | B -> BUY, S -> SELL |
| prctyp* | LMT / MKT / SL-LMT / SL-MKT | Login |
| blprc | - | Book loss Price applicable only if product is selected as H and B (High Leverage and Bracket order ) |
| rorgqty | - | Optional field. Application only for modify order, open order quantity |
| fillshares | - | Optional field. Application only for modify order, quantity already filled. |
| rorgprc | - | Optional field. Application only for modify order, open order price |
| orgtrgprc* | - | Optional field. Application only for modify order, open order trigger price |
| norenordno | - | Optional field. Application only for H or B order modification |
| snonum | - | Optional field. Application only for H or B order modification |
| basketlists* | - | Optional field. Array of json objects. (object fields given in below table) |

**Json Fields of object in values Array**

| Parameter Name | Possible value | Description |
|---|---|---|
| exch* | NSE / NFO / BSE / MCX | Unique id of contract on which order to be placed. (use url encoding to avoid special char error for symbols like M&M) |
| tsym* | - | Unique id of contract on which order to be placed. (use url encoding to avoid special char error for symbols like MSM) |
| qty* | - | Order Quantity |
| prc* | - | Order Price |
| trgprc | - | Only to be sent in case of SL / SL-M order. |
| prd* | C / M / H | Product name (Select from 'prarr' Array provided in User Details response, and if same is allowed for selected, exchange. Show product display name, for user to select, and send corresponding prd in API call) |
| trantype* | B / S | B -> BUY, S -> SELL |
| prctyp* | LMT / MKT / SL-LMT / SL-MKT | - |

### Response Details

| Parameter Name | Possible value | Description |
|---|---|---|
| stat | Ok or Not_Ok | Place order success or failure indication. |
| request_time | - | Response received time. |
| remarks | - | This field will contain rejection reason. |
| marginused | - | Total margin used. |
| marginusedtrade | - | Margin used after trade. |
| emsg | - | This will be present only if Order placement fails. |

## Order Book

> Request to be POSTed to URL : /NorenWClientAPI/OrderBook

### Request Details

| Parameter Name | Possible value | Description |
|---|---|---|
| jData* | - | Should send json object with fields in below list |

**Json Fields**

| Parameter Name | Possible value | Description |
|---|---|---|
| uid* | - | Logged in User Id |
| prd | H / M / ... | Product name |

### Response Details

**Response Details (Success)**

| Parameter Name | Possible value | Description |
|---|---|---|
| stat | Ok or Not_Ok | Order book success or failure indication. |
| uid | - | Logged in User Id |
| actid | - | Login users account ID |
| exch | - | Exchange Segment |
| tsym | - | Trading symbol / contract on which order is placed. |
| norenordno | - | Noren Order Number |
| prc | - | Order Price |
| qty | - | Order Quantity |
| mkt_protection | - | Market Protection percentage |
| prd | - | Display product alias name, using prarr returned in user details. |
| s_prdt_ali | - | Product display name |
| status | - | Order status |
| trantype | B / S | Transaction type of the order |
| prctyp | LMT / MKT / SLMKT / SL-LMT | Price type |
| fillshares | - | Total Traded Quantity of this order (will not be present if no trades for this order) |
| avgprc | - | Average trade price of total traded quantity (will not be present if no trades for this order) |
| rejreason | - | If order is rejected, reason in text form |
| exchordid | - | Exchange Order Number |
| cancelqty | - | Canceled quantity for order which is in status cancelled. |
| remarks | - | Any message Entered during order entry. |
| dscqty | - | Order disclosed quantity. |
| trgprc | - | Order trigger price |
| ret | DAY / IOC / EOS | Order validity |
| bpprc | - | Book Profit Price applicable only if product is selected as B (Bracket order ) |
| blprc | - | Book loss Price applicable only if product is selected as H and B (High Leverage and Bracket order ) |
| trailprc | - | Trailing Price applicable only if product is selected as H and B (High Leverage and Bracket order ) |
| amo | - | Yes / No |
| pp | - | Price precision |
| ti | - | Tick size |
| ls | - | Lot size |
| token | - | Contract Token |
| norentm | - | - |
| ordenttm | - | - |
| exch_tm | - | - |
| snoordt | - | 0 for profit leg and 1 for stoploss leg |
| snonum | - | This field will be present for product H and B; and only if it is profit/sl order. |
| sno_fillid | - | SNO fill id |
| prcftr | - | Contract price factor (GN*PN)/(GD*PD), (used for order value calculation) |
| mult | - | Contract price multiplier, (used for order value calculation) |
| dname | - | Broker specific contract display name, present only if applicable |
| cname | - | Company Name |
| rqty | - | To be used in get margin from modify window |
| rprc | - | To be used in get margin from modify window. |
| rtrgprc | - | To be used in get margin from modify window, for H/B products only |
| rorgqty | - | To be used in get margin from modify window. |
| rorgprc | - | To be used in get margin from modify window. |
| orgtrgprc | - | To be used in get margin from modify window, for H/B products only |
| orgblprc | - | To be used in get margin from modify window, for H/B products only |
| algo_name | - | Algo Name |
| add_ord_id | - | The "added_ord_id" response in the order book for the ICEBURG order is "AQU_ID," and for the GTT order, it is "GTT Order id". |
| C | - | CUST_FIRM_C |
| brnchid | - | Region id |
| instname | - | Instrument Name |
| ordersource | - | Order Source |
| st_intrn | - | - |
| rejby | - | If an order is rejected, it will indicate from where it got rejected. |
| src_uid | - | Source User Id |

**Response Details (Failure)**

| Parameter Name | Possible value | Description |
|---|---|---|
| stat | Not_Ok | Order book failure indication. |
| request_time | - | Response received time. |
| emsg | - | Error message |

**Sample Success Response:**

```json
{
“stat” : “Ok”,
“exch” : “NSE” ,
“tsym” : “ACC-EQ” ,
“norenordno” : “20062500000001223”,
“prc” : “127230”,
“qty” : “100”,
“prd” : “C”,
“status”: “Open”,
“trantype” : “B”,
“prctyp” : ”LMT”,
“fillshares” : “0”,
“avgprc” : “0”,
“exchordid” : “250620000000343421”,
“uid” : “VIDYA”,
“actid” : “CLIENT1”,
“ret” : “DAY”,
“amo” : “Yes”
},
{
“stat” : “Ok”,
“exch” : “NSE” ,
“tsym” : “ABB-EQ” ,
“norenordno” : “20062500000002543”,
“prc” : “127830”,
“qty” : “50”,
“prd” : “C”,
“status”: “REJECT”,
“trantype” : “B”,
“prctyp” : ”LMT”,
“fillshares” : “0”,
“avgprc” : “0”,
“rejreason” : “Insufficient funds”
“uid” : “VIDYA”,
“actid” : “CLIENT1”,
“ret” : “DAY”,
“amo” : “No”
}
```

**Sample Failure Response:**

```json
{
  "stat":"Not_Ok",
  "emsg":"Session Expired : Invalid Session Key"
}
```

**Example:**

```bash
curl https://apitest.kambala.co.in/NorenWClientAPI/OrderBook -d "jData={"uid":"VIDYA"}“ \
```

## Single Order History

> Request to be POSTed to URL : /NorenWClientAPI/SingleOrdHist

### Request Details

| Parameter Name | Possible value | Description |
|---|---|---|
| jData* | - | Should send json object with fields in below list |

**Json Fields**

| Parameter Name | Possible value | Description |
|---|---|---|
| uid* | - | Logged in User Id |
| norenordno* |   | Noren Order Number |

### Response Details

| Parameter Name | Possible value | Description |
|---|---|---|
| stat | Ok or Not_Ok | Order book success or failure indication. |
| exch | - | Exchange Segment |
| tsym | - | Trading symbol / contract on which order is placed. |
| norenordno | - | Noren Order Number |
| prc | - | Order Price |
| qty | - | Order Quantity |
| prd | - | Display product alias name, using prarr returned in user details |
| s_prdt_ali | - | Product display name |
| status | - | Order status |
| rpt | - | Report Type (fill/complete etc) |
| trantype | B / S | Transaction type of the order |
| prctyp | LMT / MKT | Price type |
| fillshares | - | Total Traded Quantity of this order |
| avgprc | - | Average trade price of total traded quantity |
| rejreason | - | If order is rejected, reason in text form |
| exchordid | - | Exchange Order Number |
| cancelqty | - | Canceled quantity for order which is in status cancelled. |
| remarks | - | Any message Entered during order entry. |
| dscqty | - | Order disclosed quantity. |
| trgprc | - | Order trigger price |
| ret | DAY / IOC / EOS | Order validity |
| uid | - | - |
| actid | - | - |
| bpprc | - | Book Profit Price applicable only if product is selected as B (Bracket order ) |
| blprc | - | Book loss Price applicable only if product is selected as H and B (High Leverage and Bracket order ) |
| trailprc | - | Trailing Price applicable only if product is selected as H and B (High Leverage and Bracket order ) |
| amo | - | Yes / No |
| pp | - | Price precision |
| ti | - | Tick size |
| ls | - | Lot size |
| token | - | Contract Token |
| norentm | - | - |
| ordenttm | - | - |
| exch_tm | - | - |

**Failure Response**

| Parameter Name | Possible value | Description |
|---|---|---|
| stat | Not_Ok | Order book failure indication. |
| request_time | - | Response received time. |
| emsg | - | Error message |

**Sample Success Output:**

```json
{
"stat": "Ok",
"norenordno": "20121300065716",
"uid": "DEMO1",
"actid": "DEMO1",
"exch": "NSE",
"tsym": "ACCELYA-EQ",
"qty": "180",
"trantype": "B",
"prctyp": "LMT",
"ret": "DAY",
"token": "7053",
"pp": "2",
"ls": "1",
"ti": "0.05",
"prc": "800.00",
"avgprc": "800.00",
"dscqty": "0",
"prd": "M",
"status": "COMPLETE",
"rpt": "Fill",
"fillshares": "180",
"norentm": "19:59:32 13-12-2020",
"exch_tm": "01-01-1980 00:00:00",
"remarks": "WC TEST Order",
"exchordid": "6858"
},
{
"stat": "Ok",
"norenordno": "20121300065716",
"uid": "DEMO1",
"actid": "DEMO1",
"exch": "NSE",
"tsym": "ACCELYA-EQ",
"qty": "180",
"trantype": "B",
"prctyp": "LMT",
"ret": "DAY",
"token": "7053",
"pp": "2",
"ls": "1",
"ti": "0.05",
"prc": "800.00",
"dscqty": "0",
"prd": "M",
"status": "OPEN",
"rpt": "New",
"norentm": "19:59:32 13-12-2020",
"exch_tm": "01-01-1980 00:00:00",
"remarks": "WC TEST Order",
"exchordid": "6858"
},
{
"stat": "Ok",
"norenordno": "20121300065716",
"uid": "DEMO1",
"actid": "DEMO1",
"exch": "NSE",
"tsym": "ACCELYA-EQ",
"qty": "180",
"trantype": "B",
"prctyp": "LMT",
"ret": "DAY",
"token": "7053",
"pp": "2",
"ls": "1",
"ti": "0.05",
"prc": "800.00",
"dscqty": "0",
"prd": "M",
"status": "PENDING",
"rpt": "PendingNew",
"norentm": "19:59:32 13-12-2020",
"remarks": "WC TEST Order"
},
{
"stat": "Ok",
"norenordno": "20121300065716",
"uid": "DEMO1",
"actid": "DEMO1",
"exch": "NSE",
"tsym": "ACCELYA-EQ",
"qty": "180",
"trantype": "B",
"prctyp": "LMT",
"ret": "DAY",
"token": "7053",
"pp": "2",
"ls": "1",
"ti": "0.05",
"prc": "800.00",
"prd": "M",
"status": "PENDING",
"rpt": "NewAck",
"norentm": "19:59:32 13-12-2020",
"remarks": "WC TEST Order"
}
```

**Sample Failure Response:**

```json
{
  "stat": "Not_Ok",
  "emsg": "Session Expired : Invalid Session Key"
}
```

**Example:**

```bash
curl https://apitest.kambala.co.in/NorenWClientAPI/SingleOrdHist -d "jData={"uid":"VIDYA", "norenordno":"20121300065716" }“ \
```

## Single Order Status

> Request to be POSTed to URL : /NorenWClientAPI/SingleOrdStatus

### Request Details

| Parameter Name | Possible value | Description |
|---|---|---|
| jData* | - | Should send json object with fields in below list |

**Json Fields**

| Parameter Name | Possible value | Description |
|---|---|---|
| uid* | - | Logged in User Id |
| norenordno* | - | Noren Order Number |
| actid* | - | Account id for which order was placed. |
| exch* | - | Exchange on which order was placed. |

### Response Details

| Parameter Name | Possible value | Description |
|---|---|---|
| stat | Ok or Not_Ok | Order book success or failure indication. |
| exch | - | Exchange Segment |
| tsym | - | Trading symbol / contract on which order is placed. |
| norenordno | - | Noren Order Number |
| prc | - | Order Price |
| qty | - | Order Quantity |
| prd | - | Display product alias name, using prarr returned in user details. |
| s_prdt_ali | - | Product display name |
| status | - | Order status |
| rpt | - | Report Type (fill/complete etc) |
| trantype | B / S | Transaction type of the order |
| prctyp | LMT / MKT | Price type |
| fillshares | - | Total Traded Quantity of this order |
| avgprc | - | Average trade price of total traded quantity |
| rejreason | - | If order is rejected, reason in text form |
| exchordid | - | Exchange Order Number |
| cancelqty | - | Canceled quantity for order which is in status cancelled. |
| remarks | - | Any message Entered during order entry. |
| dscqty | - | Order disclosed quantity. |
| trgprc | - | Order trigger price |
| ret | DAY / IOC / EOS | Order validity |
| uid | - |   |
| actid | - |   |
| bpprc | - | Book Profit Price applicable only if product is selected as B (Bracket order ) |
| blprc | - | Book loss Price applicable only if product is selected as H and B (High Leverage and Bracket order ) |
| trailprc | - | Trailing Price applicable only if product is selected as H and B (High Leverage and Bracket order ) |
| amo | - | Yes / No |
| pp | - | Price precision |
| ti | - | Tick size |
| ls | - | Lot size |
| token | - | Contract Token |
| norentm | - |   |
| ordenttm | - |   |
| exch_tm | - | Format: dd-mm-YYYY hh:MM:SS |

**Failure Response Details**

| Parameter Name | Possible value | Description |
|---|---|---|
| stat | Not_Ok | Order book failure indication. |
| request_time | - | Response received time. |
| emsg | - | Error message |

**Example:**

```bash
curl https://apitest.kambala.co.in/NorenWClientAPI/SingleOrdStatus -d "jData={"uid":"VIDYA"}“ \
```

**Sample Success Output:**

```json
[
 {
"stat":"Ok",
"norenordno": "23072300000001",
"kidid":"1",
"uid":"TESTINV",
"src_uid":"",
"actid":"TESTINV",
"exch":"NSE",
"tsym": "ACC-EQ",
"qty":"250",
"trantype": "S",
"prctyp": "LMT",
"ret":"DAY",
rejby": "RED",
"pan": "AAAAA1234A",
"ordersource":"WEB",
"token": "22",
"pp": "2",
"ls": "1",
"ti":"0.05",
"prc":"2400.00",
"dscqty": "0",
"s_prdt_ali":"Regular",
"prd": "M",
"status": "REJECTED",
"st_intrn": "REJECTED",
"rpt": "Rejected",
"ordenttm":"1690107153",
"norentm":"15:42:33 23-07-2023",
"remarks":"WC TEST Order",
"rejreason":"RED:RULE:{Check circuit limit including square off order}Current:INR 2,400.00 LowerCircuit:INR
1,590.05 UpperCircuit:INR 1,943.35:NSE.ACC-EQ for C-TESTINV [DEFAULT]",
"introp_exch": "EQT"
}
]
```

## Trade Book

> Request to be POSTed to URL : /NorenWClientAPI/TradeBook

### Request Details

| Parameter Name | Possible value | Description |
|---|---|---|
| jData* | - | Should send json object with fields in below list |

**Json Fields**

| Parameter Name | Possible value | Description |
|---|---|---|
| uid* | - | Logged in User Id |
| actid* | - | Account Id of logged in user |

### Response Details

| Parameter Name | Possible value | Description |
|---|---|---|
| stat | Ok or Not_Ok | Order book success or failure indication. |
| exch | - | Exchange Segment |
| tsym | - | Trading symbol / contract on which order is placed. |
| norenordno | - | Noren Order Number |
| qty | - | Order Quantity |
| prd | - | Display product alias name, using prarr returned in user details. |
| s_prdt_ali | - | Product display name |
| trantype | B / S | Transaction type of the order |
| prctyp | LMT / MKT | Price type |
| fillshares | - | Total Traded Quantity of this order |
| avgprc | - | Average trade price of total traded quantity |
| exchordid | - | Exchange Order Number |
| remarks | - | Any message Entered during order entry. |
| ret | DAY / IOC / EOS | Order validity |
| uid | - | - |
| actid | - | - |
| pp | - | Price precision |
| ti | - | Tick size |
| ls | - | Lot size |
| cstFrm | - | Custom Firm |
| fltm | - | Fill Time |
| flid | - | Fill ID |
| flqty | - | Fill Qty |
| flprc | - | Fill Price |
| ordersource | - | Order Source |
| token | - | Token |
| norentm | - | Noren time stamp |
| exch_tm | - | Exchange update time Format: dd-mm-YYYY hh:MM:SS |
| snoordt | - | 0 for profit leg and 1 for stoploss leg |
| snonum | - | This field will be present for product H and B; and only if it is profit/sl order. |
| remarks | - | Any message Entered during order entry |
| prc | - | Order Price |
| mult | - | Multiplier |

**Response data will be in json format with below fields in case of failure:**

| Parameter Name | Possible value | Description |
|---|---|---|
| stat | Not_Ok | Order book failure indication. |
| request_time | - | Response received time. |
| emsg | - | Error message |

**Example:**

```bash
curl https://apitest.kambala.co.in/NorenWClientAPI/TradeBook -d "jData={"uid":"VIDYA", “actid”:”DEMO1”}“ \
```

**Sample Success Output:**

```json
[{
"stat": "Ok",
"norenordno": "20121300065715",
"uid": "GURURAJ",
"actid": "GURURAJ",
"exch": "NSE",
"prctyp": "LMT",
"ret": "DAY",
"prd": "M",
"flid": "102",
"fltm": "01-01-1980 00:00:00",
"trantype": "S",
"tsym": "ACCELYA-EQ",
"qty": "180",
"token": "7053",
"fillshares": "180",
"flqty": "180",
"pp": "2",
"ls": "1",
"ti": "0.05",
"prc": "800.00",
"flprc": "800.00",
"norentm": "19:59:32 13-12-2020",
"exch_tm": "01-01-1980 00:00:00",
"remarks": "WC TEST Order",
"exchordid": "6857"
},
{
"stat": "Ok",
"norenordno": "20121300065716",
"uid": "GURURAJ",
"actid": "GURURAJ",
"exch": "NSE",
"prctyp": "LMT",
"ret": "DAY",
"prd": "M",
"flid": "101",
"fltm": "01-01-1980 00:00:00",
"trantype": "B",
"tsym": "ACCELYA-EQ",
"qty": "180",
"token": "7053",
"fillshares": "180",
"flqty": "180",
"pp": "2",
"ls": "1",
"ti": "0.05",
"prc": "800.00",
"flprc": "800.00",
"norentm": "19:59:32 13-12-2020",
"exch_tm": "01-01-1980 00:00:00",
"remarks": "WC TEST Order",
"exchordid": "6858"
}]
```

## Positions Book

> Request to be POSTed to URL : /NorenWClientAPI/PositionBook

### Request Details

| Parameter Name | Possible value | Description |
|---|---|---|
| jData* | - | Should send json object with fields in below list |

**Json Fields**

| Parameter Name | Possible value | Description |
|---|---|---|
| uid* | - | Logged in User Id |
| actid* | - | Account Id of logged in user |

### Response Details

| Parameter Name | Possible value | Description |
|---|---|---|
| stat | Ok or Not_Ok | Order book success or failure indication. |
| exch | - | Exchange Segment |
| tsym | - | Trading symbol / contract on which order is placed. |
| token | - | Contract token |
| uid | - | td> |
| actid | - | Account Id |
| prd | - | Product name to be shown. |
| s_prdt_ali | - | Product display name |
| netqty | - | Net Position quantity |
| netavgprc | - | Net position average price |
| daybuyqty | - | Day Buy Quantity |
| daysellqty | - | Day Sell Quantity |
| daybuyavgprc | - | Day buy average price |
| daysellavgprc | - | Day sell average price |
| daybuyamt | - | Day Buy Amount |
| daysellamt | - | Day Sell Amount |
| cfbuyqty | - | Carry Forward Buy Quantity |
| cforgavprc | - | Original Avg Price |
| cfsellqty | - | Carry Forward Sell Quantity |
| cfbuyavgprc | - | Carry Forward Buy average price |
| cfsellavgprc | - | Carry Forward Sell average price |
| cfbuyamt | - | Carry Forward Buy Amount |
| cfsellamt | - | Carry Forward Sell Amount |
| totbuyamt | - | Total Buy Amount |
| totsellamt | - | Total Sell Amount |
| totbuyavgprc | - | Total Buy Avg Price |
| totsellavgprc | - | Total Sell Avg Price |
| lp | - | LTP |
| rpnl | - | RealizedPNL |
| urmtom | - | UnrealizedMTOM. (Can be recalculated in LTP update : = netqty * (lp from web socket - netavgprc) * prcftr) |
| bep | - | Break even price |
| openbuyqty | - | - |
| opensellqty | - | - |
| openbuyamt | - | - |
| opensellamt | - | - |
| openbuyavgprc | - | - |
| opensellavgprc | - | - |
| mult | - | - |
| pp | - | - |
| prcftr | gn*pn/(gd*pd). | - |
| ti | - | Tick size |
| ls | - | Lot size |
| instname | - | Instrument Name |
| upldprc | - | Upload price |
| netupldprc | - | Net Upload Price |
| request_time | - | This will be present only in a failure response. |
| dname | - | Broker specific contract display name, present only if applicable. |
| cname | - | Company Name. |

**Response data will be in json format with below fields in case of failure:**

| Parameter Name | Possible value | Description |
|---|---|---|
| stat | Not_Ok | Position book request failure indication. |
| request_time | - | Response received time. |
| emsg | - | Error message |

**Example:**

```bash
curl https://apitest.kambala.co.in/NorenWClientAPI/PositionBook -d "jData={"uid":"VIDYA", ”actid”:”ACCT_1”}“ \
```

**Sample Success Output:**

```json
[{
"stat":"Ok",
"uid":"POORNA",
"actid":"POORNA",
"exch":"NSE",
"tsym":"ACC-EQ",
"prarr":"C",
"pp":"2",
"ls":"1",
"ti":"5.00",
"mult":"1",
"prcftr":"1.000000",
"daybuyqty":"2",
"daysellqty":"2",
"daybuyamt":"2610.00",
"daybuyavgprc":"1305.00",
"daysellamt":"2610.00",
"daysellavgprc":"1305.00",
"cfbuyqty":"0",
"cfsellqty":"0",
"cfbuyamt":"0.00",
"cfbuyavgprc":"0.00",
"cfsellamt":"0.00",
"cfsellavgprc":"0.00",
"openbuyqty":"0",
"opensellqty":"23",
"openbuyamt":"0.00",
"openbuyavgprc":"0.00",
"opensellamt":"30015.00",
"opensellavgprc":"1305.00",
"netqty":"0",
"netavgprc":"0.00",
"lp":"0.00",
"urmtom":"0.00",
"rpnl":"0.00",
"cforgavgprc":"0.00"
}]
```

**Sample Failure Output:**

```json
{
  "stat":"Not_Ok",
  "request_time":"14:14:11 26-05-2020",
  "emsg":"Error Occurred : 5 {\"no data\"}"
}
```
