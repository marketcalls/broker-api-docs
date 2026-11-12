# Watch Lists

> Source: https://shoonya.com/api-documentation (Watch Lists)

## Contents

- [Get WatchList Names](#get-watchlist-names)
- [Get WatchList](#get-watchlist)
- [Add Scrip to Watch List](#add-scrip-to-watch-list)
- [Delete Scrip to Watch List](#delete-scrip-to-watch-list)

---

## Get WatchList Names

> Request to be POSTed to URL : /NorenWClientAPI/MWList

### Request Details

| Parameter Name | Possible value | Description |
|---|---|---|
| jData* | - | Should send json object with fields in below list |

**Json Fields**

| Parameter Name | Possible value | Description |
|---|---|---|
| uid* | - | Logged in User Id |

### Response Details

| Parameter Name | Possible value | Description |
|---|---|---|
| stat | Ok or Not_Ok | MWList Success or Failure Indication |
| values | - | Watch List names as a json array of strings. |
| request_time | - | It will be present only in a successful response |
| emsg | - | This will be present only in case of errors or No WatchLists are set yet. |

### Calculation :

```
  1.Available Margin=total -marginused;
where total = cash +payin+payout+daycash+unclearedcash+brkcollamt+collateral+aux_brkcollamt;
2.Total Credits=cash +payin+payout+daycash+unclearedcash+brkcollamt+collateral+aux_brkcollamt;
3.Utilization = marginused;
```

**Sample Success Response:**

```json
{
"request_time": "12:34:52 21-05-2020",
"values": [
Parameter Name Possible value Description
jData* Should send json object with fields in below list
22
"default",
"WL"
],
"stat": "Ok"
}
```

**Sample Failure Response:**

```json
{
"stat": "Not_Ok",
"emsg": "Session Expired : Invalid Session Key"
}
```

## Get WatchList

> Request to be POSTed to URL : /NorenWClientAPI/MarketWatch

### Request Details

| Parameter Name | Possible value | Description |
|---|---|---|
| jData* | - | Should send json object with fields in below list |

**Json Fields**

| Parameter Name | Possible value | Description |
|---|---|---|
| uid* | - | Logged in User Id |
| wlname* | - | Name of the Watchlist, for which scrip list is required. |

### Response Details

| Parameter Name | Possible value | Description |
|---|---|---|
| stat | Ok or Not_Ok | Market watch success or failure indication. |
| values | - | Array of json objects. (object fields given in below table) |
| request_time | - | It will be present only in a successful response. |
| emsg | - | This will be present only in case of errors. That is : 1) Invalid Input : Invalid WatchList Name 2) Session Expired |

**Json Fields of object in values Array**

| Parameter Name | Possible value | Description |
|---|---|---|
| exch | NSE, BSE, NFO ... | Exchange |
| tsym | - | Trading Symbol of the Scrip (Contract) |
| token | - | Token of the Scrip (Contract) |
| pp | - | Price Precision |
| ti | - | Tick Size |
| ls | - | Lot Size |
| dname | - | Broker Specific Contract Display Name (Present Only if Applicable) |
| oi | - | Open Interest [ # ] |
| ltt | - | Last Trading Time [ # ] |
| ltq | - | Last Trade Quantity [ # ] |
| totbuyqty | - | Total Buy Quantity [ # ] |
| totsellqty | - | Total Sell Quantity [ # ] |
| wk52_h | - | Week52 High Price [ # ] |
| wk52_l | - | Week52 Low Price [ # ] |
| lp | - | LTP [ # ] |
| frzqty | - | Freeze Quantity [ # ] |
| uniq_key | - | Scrip Unique Key [ # ] |
| sp1 | - | Ask Price 1 [ # ] |
| bq1 | - | BID Quantity 1 [ # ] |
| h | - | Day High Price [ # ] |
| l | - | Day Low Price [ # ] |
| sq1 | - | Ask Quantity 1 [ # ] |
| c | - | Close Price [ # ] |
| bp1 | - | Bid Price 1 [ # ] |
| v | - | Volume [ # ] |
| o | - | Open Price [ # ] |
| change | - | LTP - Previous Close Price [ # ] |
| pc | - | LTP Percentage Change [ # ] |
| cname | - | Company Name |
| seg | - | Segment |

**Sample Success Response:**

```json
{
"request_time": "13:25:17 21-05-2020",
"values": [
{
"exch": "BSE",
"token": "972889",
"tsym": "915PTCIF27"
},
{
"exch": "NSE",
"token": "13",
"tsym": "ABB-EQ"
},
{
"exch": "NSE",
"token": "22",
"tsym": "ACC-EQ"
}
],
"stat": "Ok"
}
```

**Sample Failure Response:**

```json
{
"stat": "Not_Ok",
"emsg": "Session Expired : Invalid Session Key"
}
```

## Add Scrip to Watch List

> Request to be POSTed to URL : /NorenWClientAPI/AddMultiScripsToMW

### Request Details

| Parameter Name | Possible value | Description |
|---|---|---|
| jData* | - | Should send json object with fields in below list |

**Json Fields**

| Parameter Name | Possible value | Description |
|---|---|---|
| uid* | - | Logged in User Id |
| wlname* | - | Name of the Watchlist, for which scrip list is required. |
| scrips | - | List of scrips, example format NSE\|22#BSE\|506734 |

### Response Details

| Parameter Name | Possible value | Description |
|---|---|---|
| stat | Ok or Not_Ok | Watch list update success or failure indication. |
| request_time | - | It will be present only in a successful response. |
| emsg | - | This will be present only in case of errors. That is : 1) Invalid Input 2) Session Expired |

**Sample Success Response:**

```json
{
  "request_time": "13:50:40 21-05-2020",
  "stat": "Ok"
}
```

**Sample Failure Response:**

```json
{
  "stat": "Not_Ok",
  "emsg": "Session Expired : Invalid Session Key"
}
```

## Delete Scrip to Watch List

> Request to be POSTed to URL : /NorenWClientAPI/DeleteMultiMWScrips

### Request Details

| Parameter Name | Possible value | Description |
|---|---|---|
| jData* | - | Should send json object with fields in below list |

**Json Fields**

| Parameter Name | Possible value | Description |
|---|---|---|
| uid* | - | Logged in User Id |
| wlname* | - | Name of the Watchlist, for which scrip list is required. |
| scrips | - | List of scrips, example format NSE\|22#BSE\|506734 |

### Response Details

| Parameter Name | Possible value | Description |
|---|---|---|
| stat | Ok or Not_Ok | Watch list update success or failure indication. |
| request_time | - | It will be present only in a successful response. |
| emsg | - | This will be present only in case of errors. That is : 1) Invalid Input 2) Session Expired |

**Sample Success Response:**

```json
{
  "request_time": "13:50:40 21-05-2020",
  "stat": "Ok"
}
```

**Sample Failure Response:**

```json
{
  "stat": "Not_Ok",
  "emsg": "Invalid Input : Missing uid or wlname or scrips."
}
```
