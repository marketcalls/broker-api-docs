# WebSocket API

Connect to:

```
wss://piconnect.flattrade.in/PiConnectWSAPI/
```

> The WebSocket endpoint was changed from `PiConnectWSTp` to `PiConnectWSAPI`, and the connect payload's `t` field and token field were renamed. See [Change Log](15-changelog.md).

## General Guidelines

1. As soon as the connection is established, send a connect request with the User ID and login session ID.
2. All input and output messages are in JSON format.

## Connect

Every session must open with a connect message before any subscription.

```json
{
  "t": "a",
  "uid": "FZ00000",
  "actid": "FZ00000",
  "source": "API",
  "accesstoken": "<token>"
}
```

### Request

| Field | Possible Value | Description |
| --- | --- | --- |
| `t` | `a` | Represents the connect task |
| `uid` | | User ID |
| `actid` | | Account ID |
| `source` | API | Must match the login request's source |
| `accesstoken` | | User session token (the `jKey`/token from login) |

### Response

| Field | Possible Value | Description |
| --- | --- | --- |
| `t` | `ak` | Connect acknowledgement |
| `uid` | | User ID |
| `s` | Ok / Not_Ok | `Not_Ok` on invalid user ID or session ID |

---

## Subscribe Touchline

```json
{ "t": "t", "k": "NSE|22#BSE|508123#NSE|10#BSE|2879" }
```

### Request

| Field | Possible Value | Description |
| --- | --- | --- |
| `t` | `t` | Touchline subscription task |
| `k` | | One or more `Exchange\|Token` pairs joined with `#`, e.g. `NSE\|22#BSE\|508123#NSE\|NIFTY` |

### Subscription Acknowledgement

One acknowledgement is sent per scrip in `k`.

| Field | Description |
| --- | --- |
| `t` | `tk` — touchline acknowledgement |
| `e` | Exchange (NSE, BSE, NFO, ...) |
| `tk` | Scrip token |
| `pp` | Price precision (2 for NSE/BSE, 4 for CDS USDINR) |
| `ts` | Trading symbol |
| `ti` | Tick size |
| `ls` | Lot size |
| `lp` | LTP |
| `pc` | Percentage change |
| `v` | Volume |
| `o` / `h` / `l` / `c` | Open / High / Low / Close |
| `ap` | Average trade price |
| `oi` | Open interest |
| `poi` | Previous day closing open interest |
| `toi` | Total open interest for the underlying |
| `bq1` / `bp1` | Best buy quantity / price (level 1) |
| `sq1` / `sp1` | Best sell quantity / price (level 1) |
| `ft` | Feed time |
| `ord_msg` | Order message |

### Touchline Feed Updates

Sent as prices move. Always includes `t`, `e`, `tk`; other fields present only when changed.

| Field | Description |
| --- | --- |
| `t` | `tf` — touchline feed |
| `e` / `tk` | Exchange / token |
| `lp` / `pc` / `v` / `o` / `h` / `l` / `c` / `ap` / `oi` / `poi` / `toi` / `bq1` / `bp1` / `sq1` / `sp1` / `ft` | Same as the acknowledgement fields above |

---

## Unsubscribe Touchline

```json
{ "t": "uk", "k": "NSE|22#BSE|508123#NSE|10#BSE|2879" }
```

| Field | Description |
| --- | --- |
| `t` (request) | `u` — unsubscribe touchline |
| `t` (response) | `uk` — unsubscribe touchline acknowledgement |
| `k` | Same `Exchange\|Token` list format as subscribe |

---

## Subscribe Depth

```json
{ "t": "d", "k": "NSE|22#BSE|508123#NSE|10#BSE|2879" }
```

### Request

| Field | Description |
| --- | --- |
| `t` | `d` — depth subscription |
| `k` | One or more `Exchange\|Token` pairs joined with `#` |

### Subscription Acknowledgement

One acknowledgement per scrip in `k`.

| Field | Description |
| --- | --- |
| `t` | `dk` — depth acknowledgement |
| `e` / `tk` | Exchange / token |
| `lp` / `pc` / `v` / `o` / `h` / `l` | LTP / % change / volume / open / high / low |
| `c` | Previous close price |
| `cp` | Close price |
| `ap` | Average trade price |
| `ltt` / `ltq` | Last trade time / quantity |
| `tbq` / `tsq` | Total buy / sell quantity |
| `bq1..bq5` / `bp1..bp5` / `bo1..bo5` | Best buy quantity / price / orders, levels 1-5 |
| `sq1..sq5` / `sp1..sp5` / `so1..so5` | Best sell quantity / price / orders, levels 1-5 |
| `lc` / `uc` | Lower / upper circuit limit |
| `52h` / `52l` | 52-week high/low (life-time high/low on MCX) |
| `oi` / `poi` / `toi` | Open interest / previous day OI / total OI for underlying |
| `ft` | Feed time |

### Sample Message

```json
{
  "t": "df", "e": "NSE", "tk": "22",
  "o": "1166.00", "h": "1179.00", "l": "1145.35", "c": "1152.65", "ap": "1159.74", "v": "819881",
  "tbq": "120952", "tsq": "131730",
  "bp1": "1156.00", "sp1": "1156.50", "bq1": "4", "sq1": "10"
}
```

### Depth Feed Updates

| Field | Description |
| --- | --- |
| `t` | `df` — depth feed |
| all other fields | Same as the [Subscription Acknowledgement](#subscribe-depth) above, plus `ue` (LPP exchange high range) and `le` (LPP exchange low range) |

---

## Unsubscribe Depth

```json
{ "t": "ud", "k": "NSE|22#BSE|508123#NSE|10#BSE|2879" }
```

| Field | Description |
| --- | --- |
| `t` (request) | `ud` — unsubscribe depth |
| `t` (response) | `udk` — unsubscribe depth acknowledgement |
| `k` | Same `Exchange\|Token` list format as subscribe |

---

## Subscribe Order Update

```json
{ "t": "o", "actid": "FZ00000" }
```

| Field | Description |
| --- | --- |
| `t` | `o` — order update subscription task |
| `actid` | Account ID to receive order updates for |

> There is no subscription acknowledgement for order update subscription.

### Order Update Feed

| Field | Description |
| --- | --- |
| `t` | `om` — order update message |
| `norenordno` | Noren order number |
| `uid` / `actid` | User ID / Account ID |
| `exch` / `tsym` | Exchange / trading symbol |
| `qty` / `prc` | Order quantity / price |
| `pcode` | Product |
| `status` | Order status (New, Replaced, Complete, Rejected, ...) |
| `reporttype` | Order event that triggered this message (Fill, Rejected, Canceled) |
| `trantype` | Buy or sell |
| `prctyp` | Order price type (LMT, SL-LMT) |
| `ret` | Retention type (DAY / EOS / IOC) |
| `fillshares` / `avgprc` | Total filled shares / average fill price |
| `fltm` / `flid` / `flqty` / `flprc` | Fill time / ID / quantity / price — present only when `reporttype` is `Fill` |
| `rejreason` | Rejection reason, if rejected |
| `exchordid` | Exchange order ID |
| `cancelqty` | Cancelled quantity |
| `remarks` | User tag from order entry |
| `dscqty` | Disclosed quantity |
| `trgprc` | Trigger price for SL orders |
| `snonum` | Present for cover/bracket child orders — send during exit |
| `snoordt` | Indicates whether a cover/bracket child order is the profit or stoploss leg |
| `blprc` | Cover/bracket parent — differential stop-loss trigger price |
| `bpprc` | Bracket parent — differential profit price |
| `trailprc` | Cover/bracket parent — required if trailing ticks enabled |
| `exch_tm` | Exchange update time (`dd-mm-YYYY hh:MM:ss`) |
| `amo` | `Yes` if the order is an After Market Order |
| `tm` / `ntm` | Timestamp / nano timestamp |
| `kidid` | Kid ID |
| `sno_fillid` | BO sequence ID |
| `rejby` | Rejection source, if rejected |
| `dname` | Broker-specific display name, if applicable |
| `handlinst` | `DMA` / `TOUCH` / `WO` |
| `ordentm` | Order entry time |
| `uidc` | UI device code |
| `os` | Order source |
| `ai` | Algo ID |

---

## Unsubscribe Order Update

```json
{ "t": "uo" }
```

| Field | Description |
| --- | --- |
| `t` (request) | `uo` — unsubscribe order update |
| `t` (response) | `uok` — unsubscribe order update acknowledgement |

---

## Subscribe Position Update

```json
{ "t": "p", "actid": "FZ00000" }
```

| Field | Description |
| --- | --- |
| `t` (request) | `p` — position subscription |
| `uid` | User ID |
| `t` (response) | `pk` — position subscription acknowledgement |

On successful connection, position updates are received if made available at startup (`-position_update`).

### Position Update Feed

| Field | Description |
| --- | --- |
| `t` | `pm` — position update |
| `exch` / `token` | Exchange segment / contract token |
| `uid` / `actid` | User ID / Account ID |
| `prd` | Product name |
| `daybuyqty` / `daysellqty` / `daybuyamt` / `daysellamt` | Day buy/sell quantity and amount |
| `cfbuyqty` / `cfsellqty` / `cfbuyamt` / `cfsellamt` | Carry-forward buy/sell quantity and amount |
| `openbuyqty` / `opensellqty` / `openbuyamt` / `opensellamt` | Open buy/sell quantity and amount |
| `instname` | Instrument name |
| `upload_prc` | Upload price |
| `buyavgprc` | `(daybuyamt + cfbuyamt) / (daybuyqty + cfbuyqty)` |
| `sellavgprc` | `(daysellamt + cfsellamt) / (daysellqty + cfsellqty)` |
| `rpnl` | Realized PNL |
| `netqty` | `daybuyqty + cfbuyqty - daysellqty - cfsellqty` |
| `totbuyamt` / `totsellamt` | Total buy / sell amount |
| `totbuyavgprc` / `totsellavgprc` | Total buy / sell average price |
| `child_orders` | Array of child-order objects — see below |

#### CHILD_ORDERS Format

| Field | Description |
| --- | --- |
| `exch` / `token` / `tsym` | Contract identity |
| `daybuyqty` / `daysellqty` / `daybuyamt` / `daysellamt` | Day buy/sell quantity and amount |
| `cfbuyqty` / `cfsellqty` / `cfbuyamt` / `cfsellamt` | Carry-forward buy/sell quantity and amount |
| `openbuyqty` / `opensellqty` / `openbuyamt` / `opensellamt` | Open buy/sell quantity and amount |
| `rpnl` | Realized PNL |
| `netqty` | `daybuyqty + cfbuyqty - daysellqty - cfsellqty` |
| `upload_prc` | Upload price |
| `totbuyamt` / `totsellamt` / `totbuyavgprc` | Total buy/sell amount and average price |

---

## Heartbeat

To keep the connection alive, send a heartbeat message every 30 seconds.

```json
{ "t": "h" }
```

| Field | Description |
| --- | --- |
| `t` (request) | `h` — heartbeat task |
| `t` (response) | `hk` — heartbeat acknowledgement |
| `hk` (response) | Timestamp in seconds |
