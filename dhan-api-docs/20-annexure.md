<!-- Annexure - DhanHQ Ver 2.0 / API Document -->
# Source: https://dhanhq.co/docs/v2/annexure/

# Annexure

## Exchange Segment

| Attribute | Exchange | Segment | enum |
| --- | --- | --- | --- |
| IDX\_I | Index | Index Value | `0` |
| NSE\_EQ | NSE | Equity Cash | `1` |
| NSE\_FNO | NSE | Futures & Options | `2` |
| NSE\_CURRENCY | NSE | Currency | `3` |
| BSE\_EQ | BSE | Equity Cash | `4` |
| MCX\_COMM | MCX | Commodity | `5` |
| BSE\_CURRENCY | BSE | Currency | `7` |
| BSE\_FNO | BSE | Futures & Options | `8` |

## Product Type

| Attribute | Detail |
| --- | --- |
| CNC | Cash & Carry for equity deliveries |
| INTRADAY | Intraday for Equity, Futures & Options |
| MARGIN | Carry Forward in Futures & Options |

## Order Status

| Attribute | Detail |
| --- | --- |
| TRANSIT | Did not reach the exchange server |
| PENDING | Awaiting execution |
| CLOSED | Used for Super Order, once both the entry and exit orders are placed |
| TRIGGERED | Used for Super Order, if Target or Stop Loss leg is triggered |
| REJECTED | Rejected by broker/exchange |
| CANCELLED | Cancelled by user |
| PART\_TRADED | Partial Quantity traded successfully |
| TRADED | Executed successfully |

## After Market Order time

| Attribute | Detail |
| --- | --- |
| PRE\_OPEN | AMO pumped at pre-market session |
| OPEN | AMO pumped at market open |
| OPEN\_30 | AMO pumped 30 minutes after market open |
| OPEN\_60 | AMO pumped 60 minutes after market open |

## Expiry Code

| Attribute | Detail |
| --- | --- |
| 0 | Current Expiry/Near Expiry |
| 1 | Next Expiry |
| 2 | Far Expiry |

## Instrument

| Attribute | Detail |
| --- | --- |
| INDEX | Index |
| FUTIDX | Futures of Index |
| OPTIDX | Options of Index |
| EQUITY | Equity |
| FUTSTK | Futures of Stock |
| OPTSTK | Options of Stock |
| FUTCOM | Futures of Commodity |
| OPTFUT | Options of Commodity Futures |
| FUTCUR | Futures of Currency |
| OPTCUR | Options of Currency |

## Feed Request Code

| Attribute | Detail |
| --- | --- |
| `11` | Connect Feed |
| `12` | Disconnect Feed |
| `15` | Subscribe - Ticker Packet |
| `16` | Unsubscribe - Ticker Packet |
| `17` | Subscribe - Quote Packet |
| `18` | Unsubscribe - Quote Packet |
| `21` | Subscribe - Full Packet |
| `22` | Unsubscribe - Full Packet |
| `23` | Subscribe - Full Market Depth |
| `25` | Unsubscribe - Full Market Depth |

## Feed Response Code

| Attribute | Detail |
| --- | --- |
| `1` | Index Packet |
| `2` | Ticker Packet |
| `4` | Quote Packet |
| `5` | OI Packet |
| `6` | Prev Close Packet |
| `7` | Market Status Packet |
| `8` | Full Packet |
| `50` | Feed Disconnect |

## Trading API Error

| Type | Code | Message |
| --- | --- | --- |
| Invalid Authentication | `DH-901` | Client ID or user generated access token is invalid or expired. |
| Invalid Access | `DH-902` | User has not subscribed to Data APIs or does not have access to Trading APIs. Kindly subscribe to Data APIs to be able to fetch Data. |
| User Account | `DH-903` | Errors related to User's Account. Check if the required segments are activated or other requirements are met. |
| Rate Limit | `DH-904` | Too many requests on server from single user breaching rate limits. Try throttling API calls. |
| Input Exception | `DH-905` | Missing required fields, bad values for parameters etc. |
| Order Error | `DH-906` | Incorrect request for order and cannot be processed. |
| Data Error | `DH-907` | System is unable to fetch data due to incorrect parameters or no data present. |
| Internal Server Error | `DH-908` | Server was not able to process API request. This will only occur rarely. |
| Network Error | `DH-909` | Network error where the API was unable to communicate with the backend system. |
| Others | `DH-910` | Error originating from other reasons. |
| Invalid IP | `DH-911` | Invalid IP address |

## Data API Error

| Code | Description |
| --- | --- |
| `800` | Internal Server Error |
| `804` | Requested number of instruments exceeds limit |
| `805` | Too many requests or connections. Further requests may result in the user being blocked. |
| `806` | Data APIs not subscribed |
| `807` | Access token is expired |
| `808` | Authentication Failed - Client ID or Access Token invalid |
| `809` | Access token is invalid |
| `810` | Client ID is invalid |
| `811` | Invalid Expiry Date |
| `812` | Invalid Date Format |
| `813` | Invalid SecurityId |
| `814` | Invalid Request |

## Conditional Triggers

### Comparison Type

| Type | Description | Mandatory fields |
| --- | --- | --- |
| TECHNICAL\_WITH\_VALUE | Compare technical indicator against a fixed numeric value | `indicatorName` `operator` `timeFrame` `comparingValue` |
| TECHNICAL\_WITH\_INDICATOR | Compare technical indicator against another indicator | `indicatorName` `operator` `timeFrame` `comparingIndicatorName` |
| TECHNICAL\_WITH\_CLOSE | Compare a technical indicator with closing price | `indicatorName` `operator` `timeFrame` |
| PRICE\_WITH\_VALUE | Compare market price against fixed value | `operator` `comparingValue` |

### Indicator Name

| Indicator | Description |
| --- | --- |
| SMA\_5 | Simple Moving Average (5 periods) |
| SMA\_10 | Simple Moving Average (10 periods) |
| SMA\_20 | Simple Moving Average (20 periods) |
| SMA\_50 | Simple Moving Average (50 periods) |
| SMA\_100 | Simple Moving Average (100 periods) |
| SMA\_200 | Simple Moving Average (200 periods) |
| EMA\_5 | Exponential Moving Average (5 periods) |
| EMA\_10 | Exponential Moving Average (10 periods) |
| EMA\_20 | Exponential Moving Average (20 periods) |
| EMA\_50 | Exponential Moving Average (50 periods) |
| EMA\_100 | Exponential Moving Average (100 periods) |
| EMA\_200 | Exponential Moving Average (200 periods) |
| BB\_UPPER | Upper Bollinger Band |
| BB\_LOWER | Lower Bollinger Band |
| RSI\_14 | Relative Strength Index |
| ATR\_14 | Average True Range |
| STOCHASTIC | Stochastic Oscillator |
| STOCHRSI\_14 | Stochastic RSI |
| MACD\_26 | MACD long-term component |
| MACD\_12 | MACD short-term component |
| MACD\_HIST | MACD histogram |

### Operator

| Operator | Description |
| --- | --- |
| CROSSING\_UP | Crosses above |
| CROSSING\_DOWN | Crosses below |
| CROSSING\_ANY\_SIDE | Crosses either side |
| GREATER\_THAN | Greater than |
| LESS\_THAN | Less than |
| GREATER\_THAN\_EQUAL | Greater than or equal |
| LESS\_THAN\_EQUAL | Less than or equal |
| EQUAL | Equal |
| NOT\_EQUAL | Not equal |

### Status

| Status | Description |
| --- | --- |
| ACTIVE | Alert is currently active |
| TRIGGERED | Alert condition met |
| EXPIRED | Alert expired |
| CANCELLED | Alert cancelled |
