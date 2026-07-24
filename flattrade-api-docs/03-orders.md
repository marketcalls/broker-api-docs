# Orders and Trades

All endpoints below are `POST` calls to `https://piconnect.flattrade.in/PiConnectAPI/<Endpoint>` with a form-encoded body of two fields:

| Parameter | Description |
| --- | --- |
| `jData` | JSON object with the fields listed under each endpoint |
| `jKey` | Access token obtained on login (see [Authentication](02-authentication.md)) |

```
curl --location 'https://BaseURL/<Endpoint>' \
--header 'Content-Type: application/json' \
--data 'jData={ ... }&jKey=<token>'
```

Fields marked `*` are mandatory.

---

## Place Order

`POST /PlaceOrder`

```bash
curl --location 'https://BaseURL/PlaceOrder' \
--header 'Content-Type: application/json' \
--data 'jData={
"uid": "FZ00000",
"actid": "FZ00000",
"exch": "NSE",
"tsym": "ACC-EQ",
"qty": "50",
"prc": "1400",
"prd": "H",
"trantype": "B",
"prctyp": "LMT",
"ret": "DAY"
}&jKey=<token>'
```

### Request Fields

| Field | Possible Value | Description |
| --- | --- | --- |
| `uid`* | | Logged-in User ID |
| `actid`* | | Login user's account ID |
| `exch`* | NSE / NFO / BSE / MCX | Exchange (select from `exarr` array in [User Details](10-user-details.md)) |
| `tsym`* | | Unique contract identifier. URL-encode symbols containing special characters (e.g. `M&M`) |
| `qty`* | | Order quantity (numeric) |
| `prc`* | | Order price (numeric, cannot be zero) |
| `trgprc` | | Trigger price — only for SL / SL-M orders |
| `dscqty`* | | Disclosed quantity (max 10% for NSE, 50% for MCX) |
| `prd`* | C - CNC / M - NRML / H - CO / B - BO / I - MIS / F - MTF | Product (select from `prarr` array in [User Details](10-user-details.md); must be allowed for the exchange) |
| `trantype`* | B / S | B = Buy, S = Sell |
| `prctyp`* | LMT / SL-LMT | Price type |
| `ret`* | DAY / EOS / IOC | Retention type |
| `remarks` | | User tag for the order |
| `ordersource` | API | Used to populate exchange info fields |
| `bpprc` | | Book Profit price — only if `prd` is `B` (Bracket order) |
| `blprc` | | Book Loss price — only if `prd` is `H` or `B` (High Leverage / Bracket order) |
| `trailprc` | | Trailing price — only if `prd` is `H` or `B` |
| `amo`* | Yes | Required for After Market Orders. Omit entirely if not an AMO — sending anything other than `Yes` returns "Invalid AMO" |
| `tsym2` / `trantype2` / `qty2` / `prc2` | | Second leg fields — mandatory for price type `2L` and `3L` |
| `tsym3` / `trantype3` / `qty3` / `prc3` | | Third leg fields — mandatory for price type `3L` |

### Response

```json
{
  "request_time": "10:48:03 20-05-2020",
  "stat": "Ok",
  "norenordno": "20052000000017"
}
```

| Field | Description |
| --- | --- |
| `stat` | `Ok` or `Not_Ok` |
| `norenordno` | Present only on successful placement |
| `emsg` | Present only on failure |

---

## Modify Order

`POST /ModifyOrder`

```bash
curl --location 'https://BaseURL/ModifyOrder' \
--header 'Content-Type: application/json' \
--data 'jData={
"uid": "FZ00000",
"actid": "FZ00000",
"exch": "NSE",
"tsym": "ACC-EQ",
"qty": "50",
"prc": "1400",
"prctyp": "LMT",
"ret": "DAY",
"norenordno": "123456789"
}&jKey=<token>'
```

### Request Fields

| Field | Possible Value | Description |
| --- | --- | --- |
| `exch`* | | Exchange |
| `norenordno`* | | Noren order number to modify |
| `prctyp` | LMT / SL-LMT | New price type |
| `prc`* | | New price (cannot be zero) |
| `qty`* | | New total quantity to fill (open/pending + already filled — do not send only the pending qty) |
| `tsym`* | | Contract identifier — cannot be changed, must match the original order |
| `ret`* | DAY / EOS / IOC | Retention type |
| `trgprc` | | New trigger price for SL-LMT |
| `uid`* | | User ID of the logged-in user |
| `bpprc` / `blprc` / `trailprc` | | Same semantics as in Place Order |

### Response

```json
{ "request_time": "14:14:08 26-05-2020", "stat": "Ok", "result": "20052600000103" }
```

| Field | Description |
| --- | --- |
| `stat` | `Ok` or `Not_Ok` |
| `result` | Noren order number modified |
| `emsg` | Present only on failure |

---

## Cancel Order

`POST /CancelOrder`

```bash
curl --location 'https://BaseURL/CancelOrder' \
--header 'Content-Type: application/json' \
--data 'jData={
"uid": "FZ00000",
"norenordno": "123456789"
}&jKey=<token>'
```

### Request Fields

| Field | Description |
| --- | --- |
| `norenordno`* | Noren order number to cancel |
| `uid`* | User ID of the logged-in user |

### Response

```json
{ "request_time": "14:14:10 26-05-2020", "stat": "Ok", "result": "20052600000103" }
```

`result` holds the Noren order number of the cancelled order; `emsg` is present only on failure.

---

## Exit SNO Order

Exits a Sequence Number Order (child order of a Cover or Bracket order).

`POST /ExitSNOOrder`

```bash
curl --location 'https://BaseURL/ExitSNOOrder' \
--header 'Content-Type: application/json' \
--data 'jData={
"uid": "FZ00000",
"prd": "H",
"norenordno": "123456789"
}&jKey=<token>'
```

### Request Fields

| Field | Possible Value | Description |
| --- | --- | --- |
| `norenordno`* | | Noren order number to exit |
| `prd`* | H / B | Only Cover (H) and Bracket (B) products are allowed |
| `uid`* | | User ID of the logged-in user |

### Response

| Field | Description |
| --- | --- |
| `stat` | `Ok` or `Not_Ok` |
| `dmsg` | Display message — present only on success |
| `emsg` | Present only on failure |

---

## Order Margin

`POST /GetOrderMargin`

```bash
curl --location 'https://BaseURL/GetOrderMargin' \
--header 'Content-Type: application/json' \
--data 'jData={
"uid": "FZ00000",
"actid": "FZ00000",
"exch": "NSE",
"tsym": "ACC-EQ",
"qty": "50",
"prc": "1400",
"prd": "H",
"trantype": "B",
"prctyp": "LMT",
"norenordno": "123456789"
}&jKey=<token>'
```

### Request Fields

Same order fields as [Place Order](#place-order) (`uid`, `actid`, `exch`, `tsym`, `qty`, `prc`, `trgprc`, `prd`, `trantype`, `prctyp`, `blprc`), plus modify-only helper fields:

| Field | Description |
| --- | --- |
| `rorgqty` | Optional — open order quantity (modify only) |
| `fillshares` | Optional — quantity already filled (modify only) |
| `rorgprc` | Optional — open order price (modify only) |
| `orgtrgprc` | Optional — open order trigger price (modify only) |
| `norenordno` | Optional — for H/B order modification |
| `snonum` | Optional — for H/B order modification |

### Response

| Field | Description |
| --- | --- |
| `stat` | `Ok` or `Not_Ok` |
| `remarks` | Present only on success |
| `cash` | Total credits available for the order |
| `marginused` | Total margin used |
| `emsg` | Present only on failure |

---

## Basket Margin

`POST /GetBasketMargin`

```bash
curl --location 'https://BaseURL/GetBasketMargin' \
--header 'Content-Type: application/json' \
--data 'jData={
"uid": "FZ00000",
"actid": "FZ00000",
"exch": "NSE",
"tsym": "ACC-EQ",
"qty": "50",
"prc": "1400",
"prd": "H",
"trantype": "B",
"prctyp": "LMT",
"norenordno": "123456789"
}&jKey=<token>'
```

### Request Fields

Same base fields as [Order Margin](#order-margin), plus:

| Field | Description |
| --- | --- |
| `basketlists` | Optional array of order objects, each with `exch`*, `tsym`*, `qty`*, `prc`*, `trgprc`, `prd`*, `trantype`*, `prctyp`*, `introp_key`, `introp_exch` (same semantics as the single-order fields above) |

### Response

| Field | Description |
| --- | --- |
| `stat` | `Ok` or `Not_Ok` |
| `remarks` | Rejection reason, if any |
| `marginused` | Total margin used |
| `marginusedtrade` | Margin used after the trade |
| `emsg` | Present only on failure |

---

## Order Book

`POST /OrderBook`

```bash
curl --location 'https://BaseURL/OrderBook' \
--header 'Content-Type: application/json' \
--data 'jData={ "uid": "FZ00000" }&jKey=<token>'
```

### Request Fields

| Field | Possible Value | Description |
| --- | --- | --- |
| `uid`* | | Logged-in User ID |
| `prd` | H / M / ... | Optional product filter |

### Response

Array of order objects. Key fields:

| Field | Description |
| --- | --- |
| `stat` | `Ok` or `Not_Ok` |
| `exch` | Exchange segment |
| `tsym` | Trading symbol / contract |
| `norenordno` | Noren order number |
| `prc` / `qty` | Order price / quantity |
| `prd` | Display product alias (from `prarr`) |
| `status` | Order status |
| `trantype` | `B` / `S` |
| `prctyp` | Price type |
| `fillshares` | Total traded quantity |
| `avgprc` | Average traded price |
| `rejreason` | Rejection reason, if rejected |
| `exchordid` | Exchange order number |
| `cancelqty` | Cancelled quantity (when status is cancelled) |
| `remarks` | Order entry tag |
| `dscqty` / `trgprc` / `ret` / `amo` | Same semantics as Place Order |
| `pp` / `ti` / `ls` | Price precision / tick size / lot size |
| `token` | Contract token |
| `orddttm` / `ordenttm` / `extm` | Order timestamps |
| `snoordt` | `0` for profit leg, `1` for stoploss leg |
| `snonum` | Present for H/B products when it's a profit/SL child order |
| `dname` | Broker-specific display name |
| `rorgqty` / `rorgprc` / `orgtrgprc` / `orgblprc` | Used when re-fetching margin from the modify window |
| `algo_name` | Algo name, if applicable |
| `C` | `CUST_FIRM_C` |

On failure: `{ "stat": "Not_Ok", "request_time": "...", "emsg": "..." }`

---

## Multi Leg Order Book

`POST /MultiLegOrderBook`

```bash
curl --location 'https://BaseURL/MultiLegOrderBook' \
--header 'Content-Type: application/json' \
--data 'jData={ "uid": "FZ00000" }&jKey=<token>'
```

### Request Fields

Same as [Order Book](#order-book): `uid`*, optional `prd`.

### Response

Same fields as [Order Book](#order-book), plus the multi-leg fields:

| Field | Description |
| --- | --- |
| `tsym2` / `trantype2` / `qty2` / `prc2` | Second leg |
| `tsym3` / `trantype3` / `qty3` / `prc3` | Third leg |
| `fillshares2` / `avgprc2` | Fill quantity / average price for leg 2 |
| `fillshares3` / `avgprc3` | Fill quantity / average price for leg 3 |

---

## Single Order History

`POST /SingleOrdHist`

```bash
curl --location 'https://BaseURL/SingleOrdHist' \
--header 'Content-Type: application/json' \
--data 'jData={"uid":"FZ00000", "norenordno":"20121300065716"}&jKey=<token>'
```

### Request Fields

| Field | Description |
| --- | --- |
| `uid`* | Logged-in User ID |
| `norenordno`* | Noren order number |

### Response

Array of order lifecycle events (New → PendingNew → Open → Fill), each with the same fields as [Order Book](#order-book) plus:

| Field | Description |
| --- | --- |
| `rpt` | Report type (`Fill`, `New`, `PendingNew`, `NewAck`, etc.) |
| `norentm` | Noren timestamp |
| `exch_tm` | Exchange update time |

Example:

```json
[
  {
    "stat": "Ok", "norenordno": "20121300065716", "uid": "DEMO1", "actid": "DEMO1",
    "exch": "NSE", "tsym": "ACCELYA-EQ", "qty": "180", "trantype": "B",
    "prctyp": "LMT", "ret": "DAY", "token": "7053", "pp": "2", "ls": "1", "ti": "0.05",
    "prc": "800.00", "avgprc": "800.00", "dscqty": "0", "prd": "M", "status": "COMPLETE",
    "rpt": "Fill", "fillshares": "180", "norentm": "19:59:32 13-12-2020",
    "exch_tm": "00:00:00 01-01-1980", "remarks": "WC TEST Order", "exchordid": "6858"
  }
]
```

---

## Trade Book

`POST /TradeBook`

```bash
curl --location 'https://BaseURL/TradeBook' \
--header 'Content-Type: application/json' \
--data 'jData={
"uid": "FZ00000",
"actid": "FZ00000"
}&jKey=<token>'
```

### Request Fields

| Field | Description |
| --- | --- |
| `uid`* | Logged-in User ID |
| `actid`* | Account ID of the logged-in user |

### Response

Array of trade (fill) objects:

| Field | Description |
| --- | --- |
| `stat` / `exch` / `tsym` / `norenordno` / `qty` / `prd` / `trantype` / `prctyp` / `fillshares` / `avgprc` / `exchordid` / `remarks` / `ret` / `uid` / `actid` / `pp` / `ti` / `ls` / `token` | Same semantics as Order Book |
| `cstFrm` | Custom Firm |
| `fltm` | Fill time |
| `flid` | Fill ID |
| `flqty` | Fill quantity |
| `flprc` | Fill price |
| `ordersource` | Order source |

On failure: `{ "stat": "Not_Ok", "request_time": "...", "emsg": "..." }`

---

## Position Book

`POST /PositionBook`

```bash
curl --location 'https://BaseURL/PositionBook' \
--header 'Content-Type: application/json' \
--data 'jData={
"uid": "FZ00000",
"actid": "FZ00000"
}&jKey=<token>'
```

### Request Fields

| Field | Description |
| --- | --- |
| `uid`* | Logged-in User ID |
| `actid`* | Account ID of the logged-in user |

### Response

Array of position objects. Key fields:

| Field | Description |
| --- | --- |
| `exch` / `tsym` / `token` / `uid` / `actid` / `prd` | Identity fields |
| `netqty` / `netavgprc` | Net position quantity / average price |
| `daybuyqty` / `daysellqty` / `daybuyavgprc` / `daysellavgprc` / `daybuyamt` / `daysellamt` | Day buy/sell stats |
| `cfbuyqty` / `cfsellqty` / `cfbuyavgprc` / `cfsellavgprc` / `cfbuyamt` / `cfsellamt` / `cforgavgprc` | Carry-forward buy/sell stats |
| `openbuyqty` / `opensellqty` / `openbuyamt` / `opensellamt` / `openbuyavgprc` / `opensellavgprc` | Open order stats |
| `totsellavgprc` | Total sell average price |
| `lp` | LTP |
| `rpnl` | Realized PNL |
| `urmtom` | Unrealized MTOM — recompute on LTP update as `netqty * (lp - netavgprc) * prcftr` |
| `bep` | Break-even price |
| `mult` / `pp` / `ti` / `ls` | Multiplier / price precision / tick size / lot size |
| `prcftr` | `gn*pn/(gd*pd)` |
| `instname` | Instrument name |

Example:

```json
[
  {
    "stat":"Ok","uid":"POORNA","actid":"POORNA","exch":"NSE","tsym":"ACC-EQ","prarr":"C",
    "pp":"2","ls":"1","ti":"5.00","mult":"1","prcftr":"1.000000",
    "daybuyqty":"2","daysellqty":"2","daybuyamt":"2610.00","daybuyavgprc":"1305.00",
    "daysellamt":"2610.00","daysellavgprc":"1305.00","netqty":"0","netavgprc":"0.00",
    "lp":"0.00","urmtom":"0.00","rpnl":"0.00"
  }
]
```

On failure: `{ "stat": "Not_Ok", "request_time": "...", "emsg": "Error Occurred : 5 \"no data\"" }`

---

## Product Conversion

`POST /ProductConversion`

```bash
curl --location 'https://BaseURL/ProductConversion' \
--header 'Content-Type: application/json' \
--data 'jData={
"uid": "FZ00000",
"actid": "FZ00000",
"exch": "NSE",
"tsym": "ACC-EQ",
"qty": "50",
"prc": "1400",
"prd": "H",
"trantype": "B",
"prctyp": "LMT",
"prevprd": "C",
"postype": "Day"
}&jKey=<token>'
```

### Request Fields

| Field | Possible Value | Description |
| --- | --- | --- |
| `exch`* | | Exchange |
| `tsym`* | | Contract identifier — must match the original order |
| `qty`* | | Quantity to convert |
| `uid`* | | User ID of the logged-in user |
| `actid`* | | Account ID |
| `prd`* | | Product to convert the position to |
| `prevprd`* | | Original product of the position |
| `trantype`* | B / S | Buy / Sell |
| `postype`* | Day / CF | Converting a Day or Carry Forward position |
| `ordersource` | API | For logging |

### Response

```json
{ "request_time": "10:52:12 02-06-2020", "stat": "Ok" }
```

`emsg` present only on failure.
