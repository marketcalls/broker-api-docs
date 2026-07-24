# Market Info

## Get Index List

`POST /GetIndexList`

```bash
curl --location 'https://BaseURL/GetIndexList' \
--header 'Content-Type: application/json' \
--data 'jData={
"uid": "FZ00000",
"exch": "NSE"
}&jKey=<token>'
```

### Request Fields

| Field | Description |
| --- | --- |
| `uid`* | Logged-in User ID |
| `exch`* | Exchange |

### Response

```json
{
  "request_time": "20:12:29 13-12-2020",
  "values": [
    { "idxname": "Nifty 50", "token": "26000" },
    { "idxname": "Nifty Bank", "token": "26009" },
    { "idxname": "India VIX", "token": "26017" }
  ]
}
```

| Field | Description |
| --- | --- |
| `stat` | `Ok` or `Not_Ok` |
| `values` | Array of `{ idxname, token }` objects — `token` is used to subscribe |
| `emsg` | Present only on errors |

---

## Get Top List Names

`POST /TopListName`

```bash
curl --location 'https://BaseURL/TopListName' \
--header 'Content-Type: application/json' \
--data 'jData={
"uid": "FZ00000",
"exch": "NSE"
}&jKey=<token>'
```

### Request Fields

| Field | Description |
| --- | --- |
| `uid`* | Logged-in User ID |
| `exch`* | Exchange |

### Response

```json
{
  "request_time": "13:08:22 03-06-2020",
  "values": [
    { "bskt": "NSEBL", "crt": "VOLUME" },
    { "bskt": "NSEBL", "crt": "LTP" },
    { "bskt": "NSEEQ", "crt": "VALUE" }
  ]
}
```

`values` is an array of `{ bskt (basket name), crt (criteria) }` pairs used as input to [Get Top List](#get-top-list).

---

## Get Top List

`POST /TopList`

```bash
curl --location 'https://BaseURL/TopList' \
--header 'Content-Type: application/json' \
--data 'jData={
"uid": "FZ00000",
"exch": "NSE",
"tb": "T",
"bskt": "NSEALL",
"crt": "LTP"
}&jKey=<token>'
```

### Request Fields

| Field | Possible Value | Description |
| --- | --- | --- |
| `uid`* | | Logged-in User ID |
| `exch`* | | Exchange |
| `tb`* | T / B | Top or Bottom |
| `bskt`* | | Basket, from [Get Top List Names](#get-top-list-names) |
| `crt`* | | Criteria, from [Get Top List Names](#get-top-list-names) |

### Response

```json
[
  {
    "stat": "Ok",
    "request_time": "15:44:45 03-06-2020",
    "values": [
      { "tsym": "AIRAN-EQ", "lp": "950.00", "c": "915.00", "v": "42705", "value": "40185405.00", "oi": "0", "pc": "3.83" }
    ]
  }
]
```

`values` is an array of contract objects: `tsym`, `lp` (LTP), `c` (previous close), `v` (volume), `value` (traded value), `oi` (open interest), `pc` (LTP % change).

---

## Get Time Price Data (Chart Data)

`POST /TPSeries`

```bash
curl --location 'https://BaseURL/TPSeries' \
--header 'Content-Type: application/json' \
--data 'jData={
"uid": "FZ00000",
"exch": "NSE",
"token": "23456",
"st": "12315",
"et": "4874564",
"intrv": "1"
}&jKey=<token>'
```

### Request Fields

| Field | Possible Value | Description |
| --- | --- | --- |
| `uid`* | | Logged-in User ID |
| `exch`* | | Exchange |
| `token`* | | Contract token |
| `st` | | Start time (seconds since epoch) |
| `et` | | End time (seconds since epoch) |
| `intrv` | 1 / 3 / 5 / 10 / 15 / 30 / 60 / 120 | Chart interval (minutes) |

### Response

```json
[
  {
    "stat": "Ok", "time": "02-06-2020 15:46:23",
    "into": "0.00", "inth": "0.00", "intl": "0.00", "intc": "0.00",
    "intvwap": "0.00", "intv": "0", "intoi": "0", "v": "980515", "oi": "128702"
  }
]
```

| Field | Description |
| --- | --- |
| `time` | `DD/MM/CCYY hh:mm:ss` |
| `into` / `inth` / `intl` / `intc` | Interval open / high / low / close |
| `intvwap` | Interval VWAP |
| `intv` | Interval volume |
| `v` | Cumulative volume |
| `intoi` | Interval OI change |
| `oi` | Open interest |

On failure: `{ "stat": "Not_Ok", "emsg": "..." }`

---

## Get EOD Chart Data

`POST /EODChartData`

```bash
curl --location 'https://BaseURL/EODChartData' \
--header 'Content-Type: application/json' \
--data 'jData={
"sym": "NSE:RELIANCE-EQ",
"from": "1624838400",
"to": "1663718400"
}&jKey=<token>'
```

### Request Fields

| Field | Description |
| --- | --- |
| `sym`* | Symbol, `EXCH:TSYM` format |
| `from`* | From date (epoch seconds) |
| `to`* | To date (epoch seconds) |

### Response

```json
[
  { "time": "21-SEP-2022", "into": "2496.75", "inth": "2533.00", "intl": "2495.00", "intc": "2509.75", "ssboe": "1663718400", "intv": "4249172.00" }
]
```

| Field | Description |
| --- | --- |
| `time` | `DD-MMM-YYYY` |
| `into` / `inth` / `intl` / `intc` | Day open / high / low / close |
| `ssboe` | Date, seconds-since-epoch format |
| `intv` | Day volume |

---

## Get Option Chain

`POST /GetOptionChain`

```bash
curl --location 'https://BaseURL/GetOptionChain' \
--header 'Content-Type: application/json' \
--data 'jData={
"uid": "FZ00000",
"exch": "NSE",
"tsym": "ACC-EQ",
"strprc": "2567",
"cnt": "5"
}&jKey=<token>'
```

### Request Fields

| Field | Description |
| --- | --- |
| `uid`* | Logged-in User ID |
| `tsym`* | Trading symbol of any option or future for the underlying (URL-encode special characters) |
| `exch`* | Exchange — must support options (NFO / CDS / MCX / etc.) |
| `strprc`* | Mid price used to center the option chain |
| `cnt`* | Number of strikes on each side of the mid price, per option type (e.g. `cnt=4` returns 16 contracts total; `cnt=5` returns 20) |

### Response

```json
{ "stat": "Ok", "values": [ { "exch": "NFO", "tsym": "ACC24AUG2600CE", "token": "...", "optt": "CE", "strprc": "2600", "pp": "2", "ti": "0.05", "ls": "500" } ] }
```

`values` is an array of `{ exch, tsym, token, optt, strprc, pp, ti, ls }` contract objects. `emsg` is present only on errors (invalid input / session expired).

---

## Get Option Greek

`POST /GetOptionGreek`

```bash
curl --location 'https://BaseURL/GetOptionGreek' \
--header 'Content-Type: application/json' \
--data 'jData={
"exd": "2021-07-28",
"strprc": "2567",
"sptprc": "2668",
"int_rate": "0.05",
"volatility": "0.2",
"optt": "C"
}&jKey=<token>'
```

### Request Fields

| Field | Description |
| --- | --- |
| `exd` | Expiry date |
| `strprc` | Strike price |
| `sptprc` | Spot price |
| `int_rate` | Interest rate |
| `volatility` | Volatility |
| `optt` | Option type |

### Response

```json
{
  "request_time": "17:22:58 28-07-2021", "stat": "OK",
  "cal_price": "1441", "put_price": "0.417071",
  "cal_delta": "0.997304", "put_delta": "-0.002696",
  "cal_gamma": "0.000001", "put_gamma": "0.000001",
  "cal_theta": "-31.535015", "put_theta": "-31.401346",
  "cal_rho": "0.000119", "put_rho": "-0.016590",
  "cal_vego": "0.006307", "put_vego": "0.006307"
}
```

Returns call (`cal_*`) and put (`put_*`) price, delta, gamma, theta, rho, and vega (`vego`).

---

## Exch Msg

`POST /ExchMsg`

```bash
curl --location 'https://BaseURL/ExchMsg' \
--header 'Content-Type: application/json' \
--data 'jData={"uid":"FZ00000","exch":"NSE"}&jKey=<token>'
```

### Request Fields

| Field | Description |
| --- | --- |
| `uid`* | Logged-in User ID |
| `exch` | Exchange (select from `exarr` in [User Details](10-user-details.md)) |

### Response

| Field | Description |
| --- | --- |
| `stat` | `Ok` on success |
| `exchmsg` | Present only on success |
| `exchtm` | Exchange time |

On failure: `{ "stat": "Not_Ok", "request_time": "...", "emsg": "..." }`

---

## Get Broker Msg

`POST /GetBrokerMsg`

```bash
curl --location 'https://BaseURL/GetBrokerMsg' \
--header 'Content-Type: application/json' \
--data 'jData={ "uid": "FZ00000" }&jKey=<token>'
```

### Request Fields

| Field | Description |
| --- | --- |
| `uid`* | Logged-in User ID |

### Response

```json
[
  { "stat": "Ok", "norentm": "02-05-1975 08:48:52", "msgtyp": "Admin Message", "dmsg": "Test Msg All Message Recovery2" }
]
```

| Field | Description |
| --- | --- |
| `dmsg` | Present only on success (e.g. days-to-expiry notices) |
| `norentm` | Noren timestamp |

---

## Span Calculator

`POST /SpanCalc`

```bash
curl --location 'https://BaseURL/SpanCalc' \
--header 'Content-Type: application/json' \
--data 'jData={
"actid": "FZ00000",
"pos": [
  {
    "exch": "NFO",
    "instname": "OPTSTK",
    "symname": "ACC",
    "expd": "2020-10-29",
    "optt": "CE",
    "strprc": "11900.00",
    "buyqty": "0",
    "sellqty": "0",
    "netqty": "100"
  }
]
}&jKey=<token>'
```

### Request Fields

| Field | Description |
| --- | --- |
| `actid`* | Account ID (preferably the real account ID if called from a post-login screen) |
| `pos`* | Array of position objects — see below |

#### Position Object

| Field | Possible Value | Description |
| --- | --- | --- |
| `exch` | NFO, CDS, MCX ... | Exchange |
| `instname` | FUTSTK, FUTIDX, OPTSTK, FUTCUR ... | Instrument name |
| `symname` | USDINR, ACC, ABB, NIFTY ... | Symbol name |
| `expd` | `YYYY-MM-DD` | Expiry date |
| `optt` | CE, PE | Option type |
| `strprc` | e.g. 11900.00 | Strike price |
| `buyqty` | | Buy open quantity |
| `sellqty` | | Sell open quantity |
| `netqty` | | Net traded quantity |

### Response

| Field | Description |
| --- | --- |
| `stat` | `Ok` or `Not_Ok` |
| `span` | Span value |
| `expo` | Exposure margin |
| `span_trade` | Span value ignoring `buyqty`/`sellqty` |
| `expo_trade` | Exposure margin ignoring `buyqty`/`sellqty` |
