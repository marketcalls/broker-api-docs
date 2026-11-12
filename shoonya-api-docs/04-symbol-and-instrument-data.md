# Symbol & Instrument Data

> Source: https://shoonya.com/api-documentation (Symbol & Instrument Data)

## Contents

- [Search Scrips](#search-scrips)
- [Get Security Info](#get-security-info)

---

## Search Scrips

> Request to be POSTed to URL : /NorenWClientAPI/SearchScrip

### Request Details

| Parameter Name | Possible value | Description |
|---|---|---|
| jData* | - | Should send json object with fields in below list |

**Json Fields**

| Parameter Name | Possible value | Description |
|---|---|---|
| uid* | - | Logged in User Id |
| stext* | - | Search Text |
| exch | - | Exchange (Select from 'exarr' Array provided in User Details response) |

### Response Details

| Parameter Name | Possible value | Description |
|---|---|---|
| stat | Ok or Not_Ok | Market watch success or failure indication. |
| values | - | Array of json objects. (object fields given in below table) |
| emsg | - | This will be present only in case of errors. That is : 1) Invalid Input 2) Session Expired |

**Json Fields of object in values Array**

| Parameter Name | Possible value | Description |
|---|---|---|
| exch | NSE, BSE, NFO ... | Exchange |
| tsym | - | Trading symbol of the scrip (contract) |
| token | - | Token of the scrip (contract) |
| pp | - | Price precision |
| ti | - | Tick size |
| ls | - | Lot size |
| weekly | - | Weekly Option, ‘W1’, ‘W2’, ‘W3’, ‘W4’ th week |
| nontrd | - | Non tradable instruments |
| dname | - | display name |
| cname | - | company name |
| optt | - | option type |
| instname | - | instrument name |
| symname | - | symbol name |
| seg | - | segment |
| exd | - | expiry date |

**Sample Success Response:**

```json
{
  "stat": "Ok",
  "values": [
    { "exch": "NSE", "token": "18069", "tsym": "REL100NAV-EQ" },
    { "exch": "NSE", "token": "24225", "tsym": "RELAXO-EQ" },
    { "exch": "NSE", "token": "4327", "tsym": "RELAXOFOOT-EQ" },
    { "exch": "NSE", "token": "18068", "tsym": "RELBANKNAV-EQ" },
    { "exch": "NSE", "token": "2882", "tsym": "RELCAPITAL-EQ" },
    { "exch": "NSE", "token": "18070", "tsym": "RELCONSNAV-EQ" },
    { "exch": "NSE", "token": "18071", "tsym": "RELDIVNAV-EQ" },
    { "exch": "NSE", "token": "18072", "tsym": "RELGOLDNAV-EQ" },
    { "exch": "NSE", "token": "2885", "tsym": "RELIANCE-EQ" },
    { "exch": "NSE", "token": "15068", "tsym": "RELIGARE-EQ" },
    { "exch": "NSE", "token": "553", "tsym": "RELINFRA-EQ" },
    { "exch": "NSE", "token": "18074", "tsym": "RELNV20NAV-EQ" }
  ]
}
```

**Sample Failure Response:**

```json
{
  "stat":"Not_Ok",
  "emsg":"No Data : "
}
```

## Get Security Info

> Request to be POSTed to uri : /NorenWClientAPI/GetSecurityInfo

### Request Details

| Parameter Name | Possible value | Description |
|---|---|---|
| jData* | - | Should send json object with fields in below list |

**Json Fields**

| Parameter Name | Possible value | Description |
|---|---|---|
| uid* | - | Logged in User Id |
| exch | - | Exchange |
| token | - | Contract Token |

### Response Details

| Parameter Name | Possible value | Description |
|---|---|---|
| request_time | - | It will be present only in a successful response. |
| stat | Ok or Not_Ok | Market watch success or failure indication. |
| exch | NSE, BSE, NFO ... | Exchange |
| tsym | - | Trading Symbol |
| cname | - | Company Name |
| symname | - | Symbol Name |
| seg | - | Segment |
| exd | - | Expiry Date |
| instname | - | Intrument Name |
| strprc | - | Strike Price |
| optt | - | Option Type |
| isin | - | ISIN |
| ti | - | Tick Size |
| ls | - | Lot Size |
| pp | - | Price precision |
| mult | - | Multiplier |
| gp_nd | - | gn/gd * pn/pd |
| prcunt | - | Price Units |
| prcqnty | - | Price Quote Qty |
| trdunt | - | Trade Units |
| delunt | - | Delivery Units |
| frzqty | - | Freeze Qty |
| gsmind | - | scripupdate Gsm Ind |
| elbmrg | - | Elm Buy Margin |
| elmsmrg | - | Elm Sell Margin |
| addbmrg | - | Additional Long Margin |
| addsrmrg | - | Additional Short Margin |
| splbmrg | - | Special Long Margin |
| splsmrg | - | Special Short Margin |
| delmrg | - | Delivery Margin |
| tenmrg | - | Tender Margin |
| tenstrd | - | Tender Start Date |
| tenendd | - | Tender End Eate |
| exestrd | - | Exercise Start Date |
| exeendd | - | Exercise End Date |
| mkt_t | - | Market type |
| issue_d | - | Issue date |
| listing_d | - | Listing date |
| last_trd_d | - | last trading date |
| elmmrg | - | Elm Margin |
| varmrg | - | Var Margin |
| expmrg | - | Exposure Margin |
| token | - | Contract Token |
| prcftr_d | - | ((GN / GD) * (PN/PD)) (actual value for calculations) |
| weekly | - | Weekly Option, ‘W1’, ‘W2’, ‘W3’, ‘W4’ th week |
| nontrd | - | Non tradable instruments |
| dname | - | Broker specific contract display name, present only if applicable |
| uc | - | Upper circuit limitlc |
| ord_msg | - | Order Message |
| exptime | - | Expiry Time |

**Sample Success Response:**

```json
{
  "request_time": "17:43:38 31-10-2020",
  "stat": "Ok",
  "exch": "NSE",
  "tsym": "ACC-EQ",
  "cname": "ACC LIMITED",
  "symname": "ACC",
  "seg": "EQT",
  "instname": "EQ",
  "isin": "INE012A01025",
  "pp": "2",
  "ls": "1",
  "ti": "0.05",
  "mult": "1",
  "prcftr_d": "(1 / 1) * (1 / 1)",
  "trdunt": "ACC,BO",
  "delunt": "ACC",
  "token": "22",
  "varmrg": "40.00"
}
```

**Sample Failure Response:**

```json
{
  "stat": "Not_Ok",
  "request_time": "10:50:54 10-12-2020",
  "emsg": "Error Occurred : 5 \"no data\""
}
```

**Example:**

```
jData={"uid":"{{USER_ID}}", "exch":"NSE", "token":"22"}
```
