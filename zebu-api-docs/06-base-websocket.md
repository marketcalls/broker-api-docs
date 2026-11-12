# Web Socket

> Source: <https://zebumyntapi.web.app/Base/WebSocket/>

## General Guidelines

1. As soon as connection is done, a connection request should be sent with User id and login session id.
2. All input and output messages will be in json format.
3. ATO price is sent as “42949672.95”

## Connect

**Request**

| Json Fields | Possible value | Description |
| --- | --- | --- |
| t | c | ‘c’ represents connect task |
| actid* |  | Account id of the logged in user. |
| uid |  | User ID |
| actid |  | Account id |
| source | WEB / MOB | Source should be same as login request. |
| susertoken |  | User Session Token |

Response

| Json Fields | Possible value | Description |
| --- | --- | --- |
| t | c | ‘ck’ represents connect acknowledgement |
| uid |  | User ID |
| s |  | Ok or Not_Ok(in case of invalid user id or session id) |

### Subscribe Touchline

Request

| Json Fields | Possible value | Description |
| --- | --- | --- |
| t | t | ‘t’ represents touchline task |
| k |  | One or more scriplist for subscription. Example NSE\|22#BSE\|508123#NSE\|NIFTY |

Subscription Acknowledgement:

Number of Acknowledgements for a single subscription will be the same as the number of scrips mentioned in the key (k) field.

| Json Fields | Possible value | Description |
| --- | --- | --- |
| t | tk | ‘t’ represents touchline task |
| e | NSE, BSE, NFO .. | Exchange name |
| tk | 22 | Scrip Token |
| pp | 2 for NSE, BSE 4 for CDS USDINR | Price precision |
| ts |  | Trading Symbol |
| ti |  | Tick size |
| ls |  | Lot size |
| lp |  | LTP |
| pc |  | Percentage change |
| v |  | volume |
| o |  | Open price |
| h |  | High price |
| I |  | Low price |
| c |  | Close price |
| ap |  | Average trade price |
| oi |  | Open interest |
| poi |  | Previous day closing Open Interest |
| toi |  | Total open interest for underlying |
| bq1 |  | Best Buy Quantity 1 |
| bp1 |  | Best Buy Price 1 |
| sq1 |  | Best Sell Quantity 1 |
| sp1 |  | Best Sell Price 1 |
| ft |  | Feed time |

TouchLine subscription Updates

Accept for t, e, and tk other fields may / may not be present.

| Json Fields | Possible value | Description |
| --- | --- | --- |
| t | tf | ‘tf’ represents touchline feed |
| e | NSE, BSE, NFO .. | Exchange name |
| tk | 22 | Scrip Token |
| lp |  | LTP |
| pc |  | Percentage change |
| v |  | volume |
| o |  | Open price |
| h |  | High price |
| I |  | Low price |
| c |  | Close price |
| ap |  | Average trade price |
| oi |  | Open interest |
| poi |  | Previous day closing Open Interest |
| toi |  | Total open interest for underlying |
| bq1 |  | Best Buy Quantity 1 |
| bp1 |  | Best Buy Price 1 |
| sq1 |  | Best Sell Quantity 1 |
| sp1 |  | Best Sell Price 1 |
| ft |  | Feed time |

### Unsubscribe Touchline

Request

| Json Fields | Possible value | Description |
| --- | --- | --- |
| t | u | ‘u’ represents Unsubscribe Touchline |
| k |  | One or more scriplist for unsubscription. Example NSE\|22#BSE\|508123 |

Response

| Json Fields | Possible value | Description |
| --- | --- | --- |
| t | uk | ‘u’ represents Unsubscribe Touchline acknowledgement |
| k |  | One or more scriplist for unsubscription. Example NSE\|22#BSE\|508123 |

## Subscribe Depth

Request

| Json Fields | Possible value | Description |
| --- | --- | --- |
| t | d | ‘d’ represents depth subscription |
| k |  | One or more scriplist for unsubscription. Example NSE\|22#BSE\|508123 |

Subscription Depth Acknowledgement

Number of Acknowledgements for a single subscription will be the same as the number of scrips mentioned in the key (k) field.

| Json Fields | Possible value | Description |
| --- | --- | --- |
| t | dk | ‘dk’ represents depth acknowledgement |
| e | NSE, BSE, NFO .. | Exchange name |
| tk | 22 | Scrip Token |
| lp |  | LTP |
| cp |  | Percentage change |
| v |  | volume |
| o |  | Open price |
| h |  | High price |
| l |  | Low price |
| c |  | Close price |
| ap |  | Average trade price |
| ltt |  | Last trade time |
| ltq |  | Last trade quantity |
| tbq |  | Total Buy Quantity |
| tsq |  | Total Sell Quantity |
| bq1 |  | Best Buy Quantity 1 |
| bq2 |  | Best Buy Quantity 2 |
| bq3 |  | Best Buy Quantity 3 |
| bq4 |  | Best Buy Quantity 4 |
| bq5 |  | Best Buy Quantity 5 |
| bp1 |  | Best Buy Price 1 |
| bp2 |  | Best Buy Price 2 |
| bp3 |  | Best Buy Price 3 |
| bp4 |  | Best Buy Price 4 |
| bp5 |  | Best Buy Price 5 |
| bo1 |  | Best Buy Orders 1 |
| bo2 |  | Best Buy Orders 2 |
| bo3 |  | Best Buy Orders 3 |
| bo4 |  | Best Buy Orders 4 |
| bo5 |  | Best Buy Orders 5 |
| sq1 |  | Best Sell Quantity 1 |
| sq2 |  | Best Sell Quantity 2 |
| sq3 |  | Best Sell Quantity 3 |
| sq4 |  | Best Sell Quantity 4 |
| sq5 |  | Best Sell Quantity 5 |
| sp1 |  | Best Sell Price 1 |
| sp2 |  | Best Sell Price 2 |
| sp3 |  | Best Sell Price 3 |
| sp4 |  | Best Sell Price 4 |
| sp5 |  | Best Sell Price 5 |
| so1 |  | Best Sell Orders 1 |
| so2 |  | Best Sell Orders 2 |
| so3 |  | Best Sell Orders 3 |
| so4 |  | Best Sell Orders 4 |
| so5 |  | Best Sell Orders 5 |
| lc |  | Lower Circuit Limit |
| uc |  | Upper Circuit Limit |
| 52h |  | 52 week high low in other exchanges, Life time high low in mcx |
| 52l |  | 52 week high low in other exchanges, Life time high low in mcx |
| oi |  | Open interest |
| poi |  | Previous day closing Open Interest |
| toi |  | Total open interest for underlying |
| ft |  | Feed time |

Depth subscription Updates :

| Json Fields | Possible value | Description |
| --- | --- | --- |
| t | df | ‘df’ represents depth feed |
| e | NSE, BSE, NFO .. | Exchange name |
| tk | 22 | Scrip Token |
| lp |  | LTP |
| pc |  | Percentage change |
| v |  | volume |
| o |  | Open price |
| h |  | High price |
| l |  | Low price |
| c |  | Close price |
| ap |  | Average trade price |
| ltt |  | Last trade time |
| ltq |  | Last trade quantity |
| tbq |  | Total Buy Quantity |
| tsq |  | Total Sell Quantity |
| bq1 |  | Best Buy Quantity 1 |
| bq2 |  | Best Buy Quantity 2 |
| bq3 |  | Best Buy Quantity 3 |
| bq4 |  | Best Buy Quantity 4 |
| bq5 |  | Best Buy Quantity 5 |
| bp1 |  | Best Buy Price 1 |
| bp2 |  | Best Buy Price 2 |
| bp3 |  | Best Buy Price 3 |
| bp4 |  | Best Buy Price 4 |
| bp5 |  | Best Buy Price 5 |
| bo1 |  | Best Buy Orders 1 |
| bo2 |  | Best Buy Orders 2 |
| bo3 |  | Best Buy Orders 3 |
| bo4 |  | Best Buy Orders 4 |
| bo5 |  | Best Buy Orders 5 |
| sq1 |  | Best Sell Quantity 1 |
| sq2 |  | Best Sell Quantity 2 |
| sq3 |  | Best Sell Quantity 3 |
| sq4 |  | Best Sell Quantity 4 |
| sq5 |  | Best Sell Quantity 5 |
| sp1 |  | Best Sell Price 1 |
| sp2 |  | Best Sell Price 2 |
| sp3 |  | Best Sell Price 3 |
| sp4 |  | Best Sell Price 4 |
| sp5 |  | Best Sell Price 5 |
| so1 |  | Best Sell Orders 1 |
| so2 |  | Best Sell Orders 2 |
| so3 |  | Best Sell Orders 3 |
| so4 |  | Best Sell Orders 4 |
| so5 |  | Best Sell Orders 5 |
| lc |  | Lower Circuit Limit |
| uc |  | Upper Circuit Limit |
| 52h |  | 52 week high low in other exchanges, Life time high low in mcx |
| 52l |  | 52 week high low in other exchanges, Life time high low in mcx |
| oi |  | Open interest |
| poi |  | Previous day closing Open Interest |
| toi |  | Total open interest for underlying |
| ft |  | Feed time |
| ft |  | Feed time |

Depth subscription Updates :

| Json Fields | Possible value | Description |
| --- | --- | --- |
| t | df | ‘df’ represents depth feed |
| e | NSE, BSE, NFO .. | Exchange name |
| tk | 22 | Scrip Token |
| lp |  | LTP |
| pc |  | Percentage change |
| v |  | volume |
| o |  | Open price |
| h |  | High price |
| l |  | Low price |
| c |  | Close price |
| ap |  | Average trade price |
| ltt |  | Last trade time |
| ltq |  | Last trade quantity |
| tbq |  | Total Buy Quantity |
| tsq |  | Total Sell Quantity |
| bq1 |  | Best Buy Quantity 1 |
| bq2 |  | Best Buy Quantity 2 |
| bq3 |  | Best Buy Quantity 3 |
| bq4 |  | Best Buy Quantity 4 |
| bq5 |  | Best Buy Quantity 5 |
| bp1 |  | Best Buy Price 1 |
| bp2 |  | Best Buy Price 2 |
| bp3 |  | Best Buy Price 3 |
| bp4 |  | Best Buy Price 4 |
| bp5 |  | Best Buy Price 5 |
| bo1 |  | Best Buy Orders 1 |
| bo2 |  | Best Buy Orders 2 |
| bo3 |  | Best Buy Orders 3 |
| bo4 |  | Best Buy Orders 4 |
| bo5 |  | Best Buy Orders 5 |
| sq1 |  | Best Sell Quantity 1 |
| sq2 |  | Best Sell Quantity 2 |
| sq3 |  | Best Sell Quantity 3 |
| sq4 |  | Best Sell Quantity 4 |
| sq5 |  | Best Sell Quantity 5 |
| sp1 |  | Best Sell Price 1 |
| sp2 |  | Best Sell Price 2 |
| sp3 |  | Best Sell Price 3 |
| sp4 |  | Best Sell Price 4 |
| sp5 |  | Best Sell Price 5 |
| so1 |  | Best Sell Orders 1 |
| so2 |  | Best Sell Orders 2 |
| so3 |  | Best Sell Orders 3 |
| so4 |  | Best Sell Orders 4 |
| so5 |  | Best Sell Orders 5 |
| lc |  | Lower Circuit Limit |
| uc |  | Upper Circuit Limit |
| 52h |  | 52 week high low in other exchanges, Life time high low in mcx |
| 52l |  | 52 week high low in other exchanges, Life time high low in mcx |
| oi |  | Open interest |
| poi |  | Previous day closing Open Interest |
| toi |  | Total open interest for underlying |
| ft |  | Feed time |

Sample Message

```json
{
  "t": "df",
  "e": "NSE",
  "tk": "22",
  "o": "1166.00",
  "h": "1179.00",
  "l": "1145.35",
  "c": "1152.65",
  "ap": "1159.74",
  "v": "819881",
  "tbq": "120952",
  "tsq": "131730",
  "bp1": "1156.00",
  "sp1": "1156.50",
  "bp2": "1155.80",
  "sp2": "1156.55",
  "bp3": "1155.75",
  "sp3": "1156.65",
  "bp4": "1155.70",
  "sp4": "1156.70",
  "bp5": "1155.65",
  "sp5": "1156.75",
  "bq1": "4",
  "sq1": "10",
  "bq2": "67",
  "sq2": "63",
  "bq3": "83",
  "sq3": "1",
  "bq4": "139",
  "sq4": "53",
  "bq5": "393",
  "sq5": "94"
}
```

### Unsubscribe Depth

Request

| Json Fields | Possible value | Description |
| --- | --- | --- |
| t | ud | ‘ud’ represents Unsubscribe depth |
| k |  | One or more scriplist for unsubscription. Example NSE\|22#BSE\|508123 |

Response

| Json Fields | Possible value | Description |
| --- | --- | --- |
| t | udk | ‘udk’ represents unsubscribe depth acknowledgement |
| k |  | One or more scriplist for unsubscription. Example NSE\|22#BSE\|508123 |

### Subscribe Order Update

Request

| Json Fields | Possible value | Description |
| --- | --- | --- |
| t | o | ‘o’ represents order update subscription task |
| actid |  | Account id based on which order updated to be sent. |

Subscription Acknowledgement:

| Json Fields | Possible value | Description |
| --- | --- | --- |
| t | ok | ‘ok’ represents order update subscription acknowledgement |

Order Update subscription Updates :

| Json Fields | Possible value | Description |
| --- | --- | --- |
| t | om | ‘om’ represents touchline feed |
| norenordno |  | Noren Order Number |
| uid |  | User Id |
| actid |  | Account ID |
| exch |  | Exchange |
| tsym |  | Trading symbol |
| qty |  | Order quantity |
| prc |  | Order Price |
| prd |  | Product |
| status |  | Order status (New, Replaced, Complete, Rejected etc) |
| reporttype |  | Order event for which this message is sent out. (Fill, Rejected, Canceled) |
| trantype |  | Order transaction type, buy or sell |
| prctyp |  | Order price type (LMT, MKT, SL-LMT, SL-MKT) |
| ret |  | Order retention type (DAY, EOS, IOC,...) |
| fillshares |  | Total Filled shares for this order |
| avgprc |  | Average fill price |
| fltm |  | Fill Time(present only when reporttype is Fill) |
| flid |  | Fill ID (present only when reporttype is Fill) |
| flqty |  | Fill Qty(present only when reporttype is Fill) |
| flprc |  | Fill Price(present only when reporttype is Fill) |
| rejreason |  | Order rejection reason, if rejected |
| exchordid |  | Exchange Order ID |
| cancelqty |  | Canceled quantity, in case of canceled order |
| remarks |  | User added tag, while placing order |
| dscqty |  | Disclosed quantity |
| trgprc |  | Trigger price for SL orders |
| snonum |  | This will be present for child orders in case of cover and bracket orders, if present needs to be sent during exit |
| snoordt |  | This will be present for child orders in case of cover and bracket orders, it will indicate whether the order is profit or stoploss |
| blprc |  | This will be present for cover and bracket parent order. This is the differential stop loss trigger price to be entered. |
| bpprc |  | This will be present for bracket parent order. This is the differential profit price to be entered. |
| trailprc |  | This will be present for cover and bracket parent order. This is required if trailing ticks is to be enabled. |
| exch_tm |  | This will have the exchange update time Format: dd-mm-YYYY hh:MM:SS |

### Unsubscribe Order Update

Request:

| Json Fields | Possible value | Description |
| --- | --- | --- |
| t | uo | ‘uo’ represents Unsubscribe Order update |

Response :

| Json Fields | Possible value | Description |
| --- | --- | --- |
| t | uok | ‘uo’ represents Unsubscribe Order update acknowledgement |
