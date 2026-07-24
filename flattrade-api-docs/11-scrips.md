# Scrips

## Search Scrips

`POST /SearchScrip`

```bash
curl --location 'https://BaseURL/SearchScrip' \
--header 'Content-Type: application/json' \
--data 'jData={
"uid": "FZ00000",
"stext": "NIFTY",
"exch": "NSE"
}&jKey=<token>'
```

### Request Fields

| Field | Description |
| --- | --- |
| `uid`* | Logged-in User ID |
| `stext`* | Search text |
| `exch` | Exchange (select from `exarr` in [User Details](10-user-details.md)) |

### Response

```json
{
  "stat": "Ok",
  "values": [
    { "exch": "NSE", "token": "2885", "tsym": "RELIANCE-EQ" },
    { "exch": "NSE", "token": "553", "tsym": "RELINFRA-EQ" }
  ]
}
```

| Field | Description |
| --- | --- |
| `stat` | `Ok` or `Not_Ok` |
| `values` | Array of `{ exch, tsym, token, pp, ti, ls }` matches |
| `emsg` | Present only on errors |

Failure example: `{ "stat": "Not_Ok", "emsg": "No Data : " }`

---

## Get Quotes

`POST /GetQuotes`

```bash
curl --location 'https://BaseURL/GetQuotes' \
--header 'Content-Type: application/json' \
--data 'jData={"uid":"FZ00000", "exch":"NSE", "token":"22"}&jKey=<token>'
```

### Request Fields

| Field | Description |
| --- | --- |
| `uid`* | Logged-in User ID |
| `exch` | Exchange |
| `token` | Contract token |

### Response

```json
{
  "request_time": "12:05:21 18-05-2021", "stat": "Ok",
  "exch": "NSE", "tsym": "ACC-EQ", "cname": "ACC LIMITED", "symname": "ACC",
  "seg": "EQT", "instname": "EQ", "isin": "INE012A01025",
  "pp": "2", "ls": "1", "ti": "0.05", "mult": "1",
  "uc": "2093.95", "lc": "1713.25", "prcftr_d": "(1 / 1 ) * (1 / 1)",
  "token": "22", "lp": "0.00", "h": "0.00", "l": "0.00", "v": "0",
  "ltq": "0", "ltt": "05:30:00",
  "bp1": "2000.00", "sp1": "0.00", "bq1": "2", "sq1": "0", "bo1": "2", "so1": "0"
}
```

| Field | Description |
| --- | --- |
| `stat` | `Ok` or `Not_Ok` |
| `request_time` | Present only on success |
| `exch` / `tsym` | Exchange / trading symbol |
| `cname` | Company name |
| `symname` | Symbol name |
| `seg` | Segment |
| `instname` | Instrument name |
| `isin` | ISIN |
| `pp` / `ls` / `ti` | Price precision / lot size / tick size |
| `mult` | Multiplier |
| `uc` / `lc` | Upper / lower circuit limit |
| `prcftr_d` | Price factor `((GN / GD) * (PN / PD))` |
| `token` | Contract token |
| `lp` | LTP |
| `h` / `l` | Day high / low |
| `v` | Volume |
| `ltq` / `ltt` | Last trade quantity / time |
| `ltd` | Last trade date (`dd-mm-yy`) |
| `bp1..bp5` / `sp1..sp5` | Best buy / sell price, levels 1-5 |
| `bq1..bq5` / `sq1..sq5` | Best buy / sell quantity, levels 1-5 |
| `bo1..bo5` / `so1..so5` | Best buy / sell order count, levels 1-5 |
| `und_exch` / `und_tk` | Underlying exchange segment / token |
| `ord_msg` | Order message |
| `sptprc` | Spot price |
| `issuecap` | Issue capital |
| `e_date` | End date |

Failure example: `{ "stat": "Not_Ok", "request_time": "...", "emsg": "Error Occurred : 5 \"no data\"" }`
