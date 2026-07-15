# WebSocket API

Real-time market data streaming (touchline and market depth).

## Connect

**WebSocket connection URL:**

```
wss://trade.definedgesecurities.com/NorenWSTRTP/
```

> **Note:** Only one connection can be made at a time, and **500 tokens per connection** are allowed.

### Connect Request

| Field | Possible value | Description |
| --- | --- | --- |
| `t` | c | `c` represents the connect task |
| `uid` | | User ID |
| `actid` | | Account id |
| `source` | TRTP | Source should be TRTP |
| `susertoken` | | User Session Token (from Login Step 2) |

### Connect Response

| Field | Possible value | Description |
| --- | --- | --- |
| `t` | ck | `ck` represents connect acknowledgement |
| `uid` | | User ID |
| `s` | | `Ok` or `Not_Ok` (in case of invalid user id or session id) |

---

## Heartbeat

A heartbeat message must be sent every **50 seconds** in order to keep the connection alive. It is a JSON object as shown below.

> **Note:** There will be no response for the sent heartbeat message.

```json
{
  "t": "h"
}
```

---

## Subscribe Touchline

### Request

| Field | Possible value | Description |
| --- | --- | --- |
| `t` | t | `t` represents the touchline task |
| `k` | | One or more scrips for subscription. Example: `NSE|22#BSE|508123#NSE|NIFTY` |

### Subscription Acknowledgement

The number of acknowledgements for a single subscription will be the same as the number of scrips mentioned in the key (`k`) field.

| Field | Possible value | Description |
| --- | --- | --- |
| `t` | tk | `tk` represents connect acknowledgement |
| `e` | NSE, BSE, NFO … | Exchange name |
| `tk` | 22 | Scrip Token |
| `pp` | 2 for NSE/BSE, 4 for CDS USDINR | Price precision |
| `ts` | | Trading Symbol |
| `ti` | | Tick size |
| `ls` | | Lot size |
| `lp` | | LTP |
| `pc` | | Percentage change |
| `v` | | Volume |
| `o` | | Open price |
| `h` | | High price |
| `l` | | Low price |
| `c` | | Close price |
| `ap` | | Average trade price |
| `oi` | | Open interest |
| `poi` | | Previous day closing Open Interest |
| `toi` | | Total open interest for underlying |
| `bq1` | | Best Buy Quantity 1 |
| `bp1` | | Best Buy Price 1 |
| `sq1` | | Best Sell Quantity 1 |
| `sp1` | | Best Sell Price 1 |

### Touchline Subscription Updates

Except for `t`, `e`, and `tk`, other fields may / may not be present.

| Field | Possible value | Description |
| --- | --- | --- |
| `t` | tf | `tf` represents touchline feed |
| `e` | NSE, BSE, NFO … | Exchange name |
| `tk` | 22 | Scrip Token |
| `ft` | | Feed time |
| `lp` | | LTP |
| `pc` | | Percentage change |
| `v` | | Volume |
| `o` | | Open price |
| `h` | | High price |
| `l` | | Low price |
| `c` | | Close price |
| `ap` | | Average trade price |
| `oi` | | Open interest |
| `poi` | | Previous day closing Open Interest |
| `toi` | | Total open interest for underlying |
| `bq1` | | Best Buy Quantity 1 |
| `bp1` | | Best Buy Price 1 |
| `sq1` | | Best Sell Quantity 1 |
| `sp1` | | Best Sell Price 1 |

---

## Unsubscribe Touchline

### Request

| Field | Possible value | Description |
| --- | --- | --- |
| `t` | u | `u` represents Unsubscribe Touchline |
| `k` | | One or more scrips for unsubscription. Example: `NSE|22#BSE|508123` |

### Response

| Field | Possible value | Description |
| --- | --- | --- |
| `t` | uk | `uk` represents Unsubscribe Touchline acknowledgement |
| `k` | | One or more scrips for unsubscription. Example: `NSE|22#BSE|508123` |

---

## Subscribe Depth

### Request

| Field | Possible value | Description |
| --- | --- | --- |
| `t` | d | `d` represents depth subscription |
| `k` | | One or more scrips for subscription. Example: `NSE|22#BSE|508123` |

### Subscription Depth Acknowledgement

The number of acknowledgements for a single subscription will be the same as the number of scrips mentioned in the key (`k`) field.

| Field | Possible value | Description |
| --- | --- | --- |
| `t` | dk | `dk` represents depth acknowledgement |
| `e` | NSE, BSE, NFO … | Exchange name |
| `tk` | 22 | Scrip Token |
| `lp` | | LTP |
| `pc` | | Percentage change |
| `v` | | Volume |
| `o` | | Open price |
| `h` | | High price |
| `l` | | Low price |
| `c` | | Close price |
| `ap` | | Average trade price |
| `ltt` | | Last trade time |
| `ltq` | | Last trade quantity |
| `tbq` | | Total Buy Quantity |
| `tsq` | | Total Sell Quantity |
| `bq1` … `bq5` | | Best Buy Quantity 1–5 |
| `bp1` … `bp5` | | Best Buy Price 1–5 |
| `bo1` … `bo5` | | Best Buy Orders 1–5 |
| `sq1` … `sq5` | | Best Sell Quantity 1–5 |
| `sp1` … `sp5` | | Best Sell Price 1–5 |
| `so1` … `so5` | | Best Sell Orders 1–5 |
| `lc` | | Lower Circuit Limit |
| `uc` | | Upper Circuit Limit |
| `52h` | | 52 week high in other exchanges, Life time high in MCX |
| `52l` | | 52 week low in other exchanges, Life time low in MCX |
| `oi` | | Open interest |
| `poi` | | Previous day closing Open Interest |
| `toi` | | Total open interest for underlying |

### Depth Subscription Updates

| Field | Possible value | Description |
| --- | --- | --- |
| `t` | df | `df` represents depth feed |
| `e` | NSE, BSE, NFO … | Exchange name |
| `tk` | 22 | Scrip Token |
| `lp` | | LTP |
| `pc` | | Percentage change |
| `v` | | Volume |
| `o` | | Open price |
| `h` | | High price |
| `l` | | Low price |
| `c` | | Close price |
| `ap` | | Average trade price |
| `ltt` | | Last trade time |
| `ltq` | | Last trade quantity |
| `tbq` | | Total Buy Quantity |
| `tsq` | | Total Sell Quantity |
| `bq1` … `bq5` | | Best Buy Quantity 1–5 |
| `bp1` … `bp5` | | Best Buy Price 1–5 |
| `bo1` … `bo5` | | Best Buy Orders 1–5 |
| `sq1` … `sq5` | | Best Sell Quantity 1–5 |
| `sp1` … `sp5` | | Best Sell Price 1–5 |
| `so1` … `so5` | | Best Sell Orders 1–5 |
| `lc` | | Lower Circuit Limit |
| `uc` | | Upper Circuit Limit |
| `52h` / `52l` | | 52 week high/low (Life time high/low in MCX) |
| `oi` / `poi` / `toi` | | Open interest / Previous day closing OI / Total OI for underlying |

### Sample Message

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

---

## Unsubscribe Depth

### Request

| Field | Possible value | Description |
| --- | --- | --- |
| `t` | ud | `ud` represents Unsubscribe depth |
| `k` | | One or more scrips for unsubscription. Example: `NSE|22#BSE|508123` |

### Response

| Field | Possible value | Description |
| --- | --- | --- |
| `t` | udk | `udk` represents unsubscribe depth acknowledgement |
| `k` | | One or more scrips for unsubscription. Example: `NSE|22#BSE|508123` |
