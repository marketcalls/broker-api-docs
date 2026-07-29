# Web Socket API

> Source: https://shoonya.com/api-documentation (Web Socket API)

## Contents

- [Connect](#connect)
- [Subscribe Touchline](#subscribe-touchline)
- [Unsubscribe Touchline](#unsubscribe-touchline)
- [Subscribe Depth](#subscribe-depth)
- [Unsubscribe Depth](#unsubscribe-depth)
- [Subscribe Order Update](#subscribe-order-update)
- [Unsubscribe Order Update](#unsubscribe-order-update)

---

## Connect

> Request to be POSTed to uri: wss://api.shoonya.com/NorenWSAPI/

### Request Details

**Request**

| Parameter Name | Possible value | Description |
|---|---|---|
| t | a | 'a' represents connect task |
| uid | - | User ID |
| actid | - | Account id |
| source | WEB / MOB | Source should be same as login request. |
| usertoken | - | User Session Token |

### Response Details

**Response**

| Parameter Name | Possible value | Description |
|---|---|---|
| t | ak | 'ak' represents connect acknowledgement |
| uid | - | User ID |
| s | - | Ok or Not_Ok (in case of invalid user id or session id) |

## Subscribe Touchline

> Number of acknowledgements for a single subscription will be the same as the number of scrips mentioned in the key (k) field.

### Request Details

**Request**

| Parameter Name | Possible value | Description |
|---|---|---|
| t | t | 't' represents touchline task |
| k | - | One or more scriptlist for subscription. Example: NSE\|22\|PBSE\|508123\|NSE\|NIFTY |

### Response Details

**Subscription Acknowledgement**

| Parameter Name | Possible value | Description |
|---|---|---|
| t | tk | 'tk' represents connect acknowledgement |
| e | NSE, BSE, NFO, BFO ... | Exchange name |
| tk | 22 | Scrip Token |
| pp | 2 for NSE, BSE, 4 for CDS USDINR | Price precision |
| ts | - | Trading Symbol |
| ti | - | Tick size |
| ls | - | Lot size |
| lp | - | LTP |
| pc | - | Percentage change |
| v | - | volume |
| o | - | Open price |
| h | - | High price |
| l | - | Low price |
| c | - | Close price |
| ap | - | Average trade price |
| oi | - | Open interest |
| poi | - | Previous day closing Open Interest |
| toi | - | Total open interest for underlying |
| bq1 | - | Best Buy Quantity 1 |
| bp1 | - | Best Buy Price 1 |
| sq1 | - | Best Sell Quantity 1 |
| sp1 | - | Best Sell Price 1 |

**TouchLine subscription Updates**

| Parameter Name | Possible value | Description |
|---|---|---|
| t | tf | 'tf' represents touchline feed |
| e | NSE, BSE, NFO ... | Exchange name |
| tk | 22 | Scrip Token |
| lp | - | LTP |
| pc | - | Percentage change |
| v | - | volume |
| o | - | Open price |
| h | - | High price |
| l | - | Low price |
| c | - | Close price |
| ap | - | Average trade price |
| oi | - | Open interest |
| poi | - | Previous day closing Open Interest |
| toi | - | Total open interest for underlying |
| bq1 | - | Best Buy Quantity 1 |
| bp1 | - | Best Buy Price 1 |
| sq1 | - | Best Sell Quantity 1 |
| sp1 | - | Best Sell Price 1 |

## Unsubscribe Touchline

### Request Details

**Request**

| Parameter Name | Possible value | Description |
|---|---|---|
| t | u | 'u' represents Unsubscribe Touchline |
| k | - | One or more scriptlist for unsubscription. Example NSE\|22\|BSE\|508123 |

### Response Details

**Response**

| Parameter Name | Possible value | Description |
|---|---|---|
| t | uk | 'uk' represents Unsubscribe Touchline acknowledgement |
| k | - | One or more scriptlist for unsubscription. Example NSE\|22\|BSE\|508123 |

## Subscribe Depth

> Request to be POSTed to URL : <websocket>

### Request Details

**Request**

| Parameter Name | Possible value | Description |
|---|---|---|
| t | d | 'd' represents depth subscription |
| k | - | One or more scriplist for subscription. Example NSE\|22#BSE\|508123 |

### Response Details

**Subscription Depth Acknowledgement**

| Parameter Name | Possible value | Description |
|---|---|---|
| t | dk | 'dk' represents depth acknowledgement |
| e | NSE, BSE, NFO, BFO .. | Exchange name |
| tk | 22 | Scrip Token |
| lp | - | LTP |
| pc | - | Percentage change |
| v | - | volume |
| o | - | Open price |
| h | - | High price |
| l | - | Low price |
| c | - | Close price |
| ap | - | Average trade price |
| ltt | - | Last trade time |
| ltq | - | Last trade quantity |
| tbq | - | Total Buy Quantity |
| tsq | - | Total Sell Quantity |
| bq1 | - | Best Buy Quantity 1 |
| bq2 | - | Best Buy Quantity 2 |
| bq3 | - | Best Buy Quantity 3 |
| bq4 | - | Best Buy Quantity 4 |
| bq5 | - | Best Buy Quantity 5 |
| bp1 | - | Best Buy Price 1 |
| bp2 | - | Best Buy Price 2 |
| bp3 | - | Best Buy Price 3 |
| bp4 | - | Best Buy Price 4 |
| bp5 | - | Best Buy Price 5 |
| bo1 | - | Best Buy Orders 1 |
| bo2 | - | Best Buy Orders 2 |
| bo3 | - | Best Buy Orders 3 |
| bo4 | - | Best Buy Orders 4 |
| bo5 | - | Best Buy Orders 5 |
| sq1 | - | Best Sell Quantity 1 |
| sq2 | - | Best Sell Quantity 2 |
| sq3 | - | Best Sell Quantity 3 |
| sq4 | - | Best Sell Quantity 4 |
| sq5 | - | Best Sell Quantity 5 |
| sp1 | - | Best Sell Price 1 |
| sp2 | - | Best Sell Price 2 |
| sp3 | - | Best Sell Price 3 |
| sp4 | - | Best Sell Price 4 |
| sp5 | - | Best Sell Price 5 |
| so1 | - | Best Sell Orders 1 |
| so2 | - | Best Sell Orders 2 |
| so3 | - | Best Sell Orders 3 |
| so4 | - | Best Sell Orders 4 |
| so5 | - | Best Sell Orders 5 |
| lc | - | Lower Circuit Limit |
| uc | - | Upper Circuit Limit |
| 52h | - | 52 week high low in other exchanges, Life time high low in mcx |
| 52l | - | 52 week high low in other exchanges, Life time high low in mcx |
| oi | - | Open interest |
| poi | - | Previous day closing Open Interest |
| toi | - | Total open interest for underlying |

**Depth subscription Updates**

| Parameter Name | Possible value | Description |
|---|---|---|
| t | df | 'df' represents depth feed |
| e | NSE, BSE, NFO .. | Exchange name |
| tk | 22 | Scrip Token |
| lp | - | LTP |
| pc | - | Percentage change |
| v | - | volume |
| o | - | Open price |
| h | - | High price |
| l | - | Low price |
| c | - | Close price |
| ap | - | Average trade price |
| ltt | - | Last trade time |
| ltq | - | Last trade quantity |
| tbq | - | Total Buy Quantity |
| tsq | - | Total Sell Quantity |
| bq1 | - | Best Buy Quantity 1 |
| bq2 | - | Best Buy Quantity 2 |
| bq3 | - | Best Buy Quantity 3 |
| bq4 | - | Best Buy Quantity 4 |
| bq5 | - | Best Buy Quantity 5 |
| bp1 | - | Best Buy Price 1 |
| bp2 | - | Best Buy Price 2 |
| bp3 | - | Best Buy Price 3 |
| bp4 | - | Best Buy Price 4 |
| bp5 | - | Best Buy Price 5 |
| bo1 | - | Best Buy Orders 1 |
| bo2 | - | Best Buy Orders 2 |
| bo3 | - | Best Buy Orders 3 |
| bo4 | - | Best Buy Orders 4 |
| bo5 | - | Best Buy Orders 5 |
| sq1 | - | Best Sell Quantity 1 |
| sq2 | - | Best Sell Quantity 2 |
| sq3 | - | Best Sell Quantity 3 |
| sq4 | - | Best Sell Quantity 4 |
| sq5 | - | Best Sell Quantity 5 |
| sp1 | - | Best Sell Price 1 |
| sp2 | - | Best Sell Price 2 |
| sp3 | - | Best Sell Price 3 |
| sp4 | - | Best Sell Price 4 |
| sp5 | - | Best Sell Price 5 |
| so1 | - | Best Sell Orders 1 |
| so2 | - | Best Sell Orders 2 |
| so3 | - | Best Sell Orders 3 |
| so4 | - | Best Sell Orders 4 |
| so5 | - | Best Sell Orders 5 |
| lc | - | Lower Circuit Limit |
| uc | - | Upper Circuit Limit |
| 52h | - | 52 week high low in other exchanges, Life time high low in mcx |
| 52l | - | 52 week high low in other exchanges, Life time high low in mcx |
| oi | - | Open interest |
| poi | - | Previous day closing Open Interest |
| toi | - | Total open interest for underlying |

**Sample Message:**

```json
{
  "t":"df",
  "e":"NSE",
  "tk":"22",
  "o":"1166.00",
  "h":"1179.00",
  "l":"1145.35",
  "c":"1152.65",
  "ap":"1159.74",
  "v":"819881",
  "tbq":"120952",
  "tsq":"113700",
  "bp1":"1156.00",
  "sp1":"1156.80",
  "bp2":"1156.80",
  "bp3":"1155.70",
  "bp4":"1155.65",
  "bp5":"1155.65",
  "bq1":"42",
  "bq2":"67",
  "bq3":"83",
  "bq4":"139",
  "bq5":"393",
  "sq1":"17",
  "sq2":"63",
  "sq3":"53",
  "sq4":"33",
  "sq5":"94"
}
```

## Unsubscribe Depth

### Request Details

**Request**

| Parameter Name | Possible value | Description |
|---|---|---|
| t | ud | 'ud' represents Unsubscribe depth |
| k | - | One or more scriplist for unsubscription. Example NSE\|22#BSE\|508123 |

### Response Details

**Response**

| Parameter Name | Possible value | Description |
|---|---|---|
| t | udk | 'udk' represents unsubscribe depth acknowledgement |
| k | - | One or more scriplist for unsubscription. Example NSE\|22#BSE\|508123 |

## Subscribe Order Update

> Request to be POSTed to URL : /NorenWSTP

### Request Details

**Request**

| Parameter Name | Possible value | Description |
|---|---|---|
| t | o | 'o' represents order update subscription task |
| actid | - | Account id based on which order update to be sent. |

### Response Details

**Subscription Acknowledgement**

| Parameter Name | Possible value | Description |
|---|---|---|
| t | ok | 'ok' represents order update subscription acknowledgement |
| t | om | 'om' represents touchline feed |
| norenoordno | - | Noren Order Number |
| uid | - | User Id |
| actid | - | Account ID |
| exch | - | Exchange |
| tsym | - | Trading symbol |
| qty | - | Order quantity |
| prc | - | Order Price |
| prd | - | Product |
| status | - | Order status (New, Replaced, Complete, Rejected etc) |
| reporttype | - | Order event for which this message is sent out. (Fill, Rejected, Canceled) |
| trantype | - | Order transaction type, buy or sell |
| prctyp | - | Order price type (LMT, MKT, SL-LMT, SL-MKT) |
| ret | - | Order retention type (DAY, EOS, IOC,...) |
| fillshares | - | Total Filled shares for this order |
| avgprc | - | Average fill price |
| filltm | - | Fill Time(present only when reporttype is Fill) |
| flid | - | Fill ID (present only when reporttype is Fill) |
| flqty | - | Fill Qty(present only when reporttype is Fill) |
| flprc | - | Fill Price(present only when reporttype is Fill) |
| rejreason | - | Order rejection reason, if rejected |
| exchorderid | - | Exchange Order ID |
| cancelqty | - | Canceled quantity, in case of canceled order |
| remarks | - | User added tag, while placing order |
| dscqty | - | Disclosed quantity |
| trgprc | - | Trigger price for SL orders |
| snonum | - | Present for child orders in case of cover and bracket orders, if present needs to be sent during exit |
| snoordt | - | Present for child orders in case of cover and bracket orders, will indicate profit/stoploss |
| blprc | - | Present for cover and bracket parent order. Differential stop loss trigger price. |
| bpprc | - | Present for bracket parent order. Differential profit price. |
| trailprc | - | Present for cover and bracket parent order. For trailing ticks to be enabled. |
| exch_tm | - | Exchange update time |

## Unsubscribe Order Update

### Request Details

| Parameter Name | Possible value | Description |
|---|---|---|
| t | ud | 'ud' represents Unsubscribe Order update |

### Response Details

| Parameter Name | Possible value | Description |
|---|---|---|
| t | uok | 'uok' represents Unsubscribe Order update acknowledgement |
