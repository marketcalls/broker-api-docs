# Portfolio

> Source: https://shoonya.com/api-documentation (Portfolio)

## Contents

- [Holdings](#holdings)
- [Limits → Get WatchList Names](#get-watchlist-names)

---

## Holdings

> Request to be POSTed to URL : /NorenWClientAPI/Holdings

### Request Details

| Parameter Name | Possible value | Description |
|---|---|---|
| jData* | - | Should send json object with fields in below list |

**Json Fields**

| Parameter Name | Possible value | Description |
|---|---|---|
| uid* | - | Logged in User Id |
| actid* | - | Account id of the logged in user. |
| prd* | - | Product name |

### Response Details

| Parameter Name | Possible value | Description |
|---|---|---|
| stat | Ok or Not_Ok | Holding request success or failure indication. |
| exch_tsym | - | Array of objects exch_tsym objects as defined below. |
| holdqty | - | Holding quantity |
| dpqty | - | DP Holding quantity |
| npoaqty | - | Non Poa display quantity |
| colqty | - | Collateral quantity |
| benqty | - | Beneficiary quantity |
| unplgdqty | - | Unpledged quantity |
| brkcolqty | - | Broker Collateral |
| btstqty | - | BTST quantity |
| btstcolqty | - | BTST Collateral quantity |
| usedqty | - | Holding used today |
| upldprc | - | Average price uploaded along with holdings |
| hair_cut | - | Hair Cut |
| prd | - | Product |
| s_prdt_ali | - | Product display name |
| trdqty | - | Trade Quantity |
| sell_amt | - | Sell Amount |
| npoadt1qty | - | nonpoa display t1 qty |
| brk_hair_cut | - | Broker HairCut |
| epi_done_qty | - | EPI done Quantity |
| combrkcollqty | - | Com Broker Collateral Quantiry |
| eqtbrkcollqty | - | Eqt Broker Collateral Quantity |
| derbrkcollqty | - | Derivative Broker Collateral Quantity |
| fxbrkcollqty | - | Fx Broker Collateral Quantity |

**Notes**

| Parameter Name | Possible value | Description |
|---|---|---|
| Valuation |   | btstqty + holdqty + brkcolqty + unplgdqty + benqty + Max(npoaqty, dpqty) - usedqty |
| Salable |   | btstqty + holdqty + unplgdqty + benqty + dpqty - usedqty |

**Json Fields of object in values Array**

| Parameter Name | Possible value | Description |
|---|---|---|
| exch | NSE, BSE, NFO ... | Exchange |
| tsym | - | Trading symbol of the scrip (contract) |
| token | - | Token of the scrip (contract) |
| pp | - | Price precision |
| ti | - | Tick size |
| ls | - | Lot size |
| lp | - | LTP [#] |
| cname | - | Company Name |
| dname | - | Display Name |

**Response data will be in json format with below fields in case of failure:**

| Parameter Name | Possible value | Description |
|---|---|---|
| stat | Not_Ok | Position book request failure indication. |
| request_time | - | Response received time. |
| emsg | - | Error message |

**Sample Success Output:**

```json
[{
"stat":"Ok",
"exch_tsym":[
{
"exch":"NSE",
"token":"13",
"tsym":"ABB-EQ"
}
],
"holdqty":"2000000",
"colqty":"200",
"btstqty":"0",
"btstcolqty":"0",
"usedqty":"0",
"upldprc" : "1800.00"
},
{
"stat":"Ok",
"exch_tsym":[
{
}
],
"exch":"NSE",
"token":"22",
"tsym":"ACC-EQ"
"holdqty":"2000000",
"colqty":"200",
"btstqty":"0",
"btstcolqty":"0",
"usedqty":"0",
"upldprc" : "1400.00"
}]
```

**Sample Failure Output:**

```json
{
  "stat":"Not_Ok",
  "emsg":"Invalid Input : Missing uid or actid or prd."
}
```

## Get WatchList Names

> **Note (conversion):** the sidebar entry **Limits** on the live site renders this **Get WatchList Names** page — the two nav items share the same component. Reproduced as published; there is no separate Limits page.

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
