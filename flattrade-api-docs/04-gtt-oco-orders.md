# GTT & OCO Orders

Good Till Triggered (GTT) and One Cancels Other (OCO) conditional orders. All endpoints are `POST` calls to `https://piconnect.flattrade.in/PiConnectAPI/<Endpoint>` with `jData` + `jKey` form fields, same as [Orders](03-orders.md).

---

## Place GTT Order

`POST /PlaceGTTOrder`

```bash
curl --location 'https://BaseURL/PlaceGTTOrder' \
--header 'Content-Type: application/json' \
--data 'jData={
"uid": "FZ00000",
"exch": "NSE",
"tsym": "ACC-EQ",
"validity": "DAY",
"qty": "50",
"prc": "1400",
"prd": "H",
"trantype": "B",
"prctyp": "LMT",
"prevprd": "C",
"ret": "DAY",
"dscqty": "10"
}&jKey=<token>'
```

### Request Fields

| Field | Possible Value | Description |
| --- | --- | --- |
| `uid`* | | User ID of the logged-in user |
| `tsym`* | | Trading symbol |
| `exch`* | | Exchange segment |
| `ai_t`* | | Alert type |
| `validity`* | DAY / GTT | Validity |
| `d` | | Data to compare with LTP |
| `remarks`* | | Order entry tag |
| `trantype`* | B / S | Buy / Sell |
| `prctyp`* | LMT / SL-LMT / DS / 2L / 3L | Price type |
| `prd`* | C / M / H | Product |
| `ret`* | DAY / EOS / IOC | Retention type |
| `actid`* | | Login user's account ID |
| `qty`* | | Order quantity |
| `prc`* | | Order price (cannot be zero) |
| `dscqty`* | | Disclosed quantity (max 10% NSE, 50% MCX) |

### Response

```json
[{ "request_time": "10:02:06 15-04-2021", "stat": "Oi created", "Al_id": "21041500000010" }]
```

| Field | Description |
| --- | --- |
| `stat` | Success/failure indication (`Oi created` on success) |
| `al_id` | Alert ID |
| `emsg` | Present only on errors (invalid input / session expired) |

---

## Modify GTT Order

`POST /ModifyGTTOrder`

```bash
curl --location 'https://BaseURL/ModifyGTTOrder' \
--header 'Content-Type: application/json' \
--data 'jData={
"uid": "FZ00000",
"actid": "FZ00000",
"exch": "NSE",
"tsym": "ACC-EQ",
"validity": "DAY",
"qty": "50",
"prc": "1400",
"prd": "H",
"trantype": "B",
"prctyp": "LMT",
"prevprd": "C",
"ret": "DAY",
"dscqty": "10"
}&jKey=<token>'
```

### Request Fields

Same as [Place GTT Order](#place-gtt-order), plus:

| Field | Description |
| --- | --- |
| `ai_t`* | Original alert type — cannot be modified |
| `al_id` | Alert ID to modify |

### Response

```json
[{ "request_time": "12:15:18 15-04-2021", "stat": "Oi Replacedt", "Al_id": "21041500000008" }]
```

---

## Cancel GTT Order

`POST /CancelGTTOrder`

```bash
curl --location 'https://BaseURL/CancelGTTOrder' \
--header 'Content-Type: application/json' \
--data 'jData={
"uid": "FZ00000",
"al_id": "21041500000013"
}&jKey=<token>'
```

### Request Fields

| Field | Description |
| --- | --- |
| `uid` | User ID of the logged-in user |
| `al_id` | Alert ID to cancel |

### Response

```json
[{ "request_time": "12:20:01 15-04-2021", "stat": "Oi delete success", "Al_id": "21041500000013" }]
```

---

## Get Pending GTT Order

`POST /GetPendingGTTOrder`

```bash
curl --location 'https://BaseURL/GetPendingGTTOrder' \
--header 'Content-Type: application/json' \
--data 'jData={ "uid": "FZ00000" }&jKey=<token>'
```

### Request Fields

| Field | Description |
| --- | --- |
| `uid`* | User ID of the logged-in user |

### Response

```json
[
  {
    "stat":"Ok","ai_t":"LTP_A","Al_id":"21041500000002","tsym":"ACC-EQ","exch":"NSE",
    "Token":"22","Remarks":"test","validity":"DAY","actid":"MOHINI","trantype":"B",
    "prctyp":"LMT","Qty":1,"Prc":"1305.00","C":"C","prd":"C","ordersource":"API",
    "d":"1900.00","oivariable":[{"var_name":"x","d":"5645"}]
  }
]
```

Fields mirror [Place GTT Order](#place-gtt-order) (`ai_t`, `al_id`, `tsym`, `exch`, `token`, `remarks`, `validity`, `d`, `trantype`, `prctyp`, `prd`, `ret`, `actid`, `qty`, `prc`), with `emsg` present only on errors.

---

## Get Enabled GTTs

`POST /GetEnabledGTTs`

```bash
curl --location 'https://BaseURL/GetEnabledGTTs' \
--header 'Content-Type: application/json' \
--data 'jData={ "uid": "FZ00000" }&jKey=<token>'
```

### Request Fields

| Field | Description |
| --- | --- |
| `uid`* | User ID of the logged-in user |

### Response

```json
{
  "stat":"Ok",
  "request_time":"04062021121503",
  "ai_ts": [{"ai_t":"ATP"}, {"ai_t":"LTP"}]
}
```

`ai_ts` is an array of enabled alert types.

---

## Place OCO Order

`POST /PlaceOCOOrder`

An OCO order places two linked orders (`place_order_params` and `place_order_params_leg2`) where the trigger of one alert type cancels the other.

```bash
curl --location 'https://BaseURL/PlaceOCOOrder' \
--header 'Content-Type: application/json' \
--data 'jData={
"uid": "FZ00000",
"ai_t": "LMT_BOS_O",
"remarks": "admn",
"validity": "GTT",
"tsym": "ACC-EQ",
"exch": "NSE",
"oivariable": [
  {"d": "20000", "var_name": "x"},
  {"d": "30000", "var_name": "y"}
],
"place_order_params": {
  "tsym": "ACC-EQ", "exch": "NSE", "trantype": "B", "prctyp": "LMT",
  "prd": "C", "ret": "DAY", "actid": "FZ00000", "uid": "FZ00000",
  "ordersource": "WEB", "qty": "1", "prc": "200"
},
"place_order_params_leg2": {
  "tsym": "ACC-EQ", "exch": "NSE", "trantype": "S", "prctyp": "LMT",
  "prd": "C", "ret": "DAY", "actid": "FZ00000", "uid": "FZ00000",
  "ordersource": "WEB", "qty": "1", "prc": "200"
}
}&jKey=<token>'
```

### Request Fields

| Field | Description |
| --- | --- |
| `uid`* | User ID of the logged-in user |
| `tsym`* | Contract identifier (URL-encode special characters) |
| `exch`* | Exchange |
| `validity`* | DAY or GTT |
| `ai_t`* | Alert type |
| `exchsym` | Exchange symbol |
| `remarks`* | Order entry tag |
| `oivariable` | Array of `{ d*, var_name* }` — see [OIVARIABLE Format](#oivariable-format) |
| `place_order_params` | Order object for leg 1 — see [PLACE_ORDER_PARAMS Format](#place_order_params-format) |
| `place_order_params_leg2` | Order object for leg 2 — same format as `place_order_params` |

#### OIVARIABLE Format

| Field | Description |
| --- | --- |
| `d`* | Data to compare with LTP |
| `var_name`* | `x` or `y` |

#### PLACE_ORDER_PARAMS Format

| Field | Possible Value | Description |
| --- | --- | --- |
| `tsym`* | | Trading symbol |
| `exch`* | | Exchange |
| `trantype`* | B / S | Buy / Sell |
| `prctyp`* | | Price type |
| `prd`* | | Product |
| `ret`* | DAY / EOS / IOC | Retention type |
| `actid`* | | Account ID |
| `uid`* | | User ID |
| `ordersource` | MOB / WEB / TT | Used to generate exchange info fields |
| `remarks` | | Order tag |
| `qty`* | | Order quantity |
| `prc`* | | Order price (cannot be zero) |
| `trgprc` | | New trigger price for SL-LMT |

### Response

```json
{ "request_time": "18:56:26 08-10-2021", "stat": "OI created", "al_id": "21100800000009" }
```

---

## Modify OCO Order

`POST /ModifyOCOOrder`

```bash
curl --location 'https://BaseURL/ModifyOCOOrder' \
--header 'Content-Type: application/json' \
--data 'jData={
"uid": "FZ00000",
"exch": "NSE",
"tsym": "ACC-EQ",
"validity": "DAY"
}&jKey=<token>'
```

### Request Fields

| Field | Description |
| --- | --- |
| `uid`* | User ID of the logged-in user |
| `tsym`* | Contract identifier |
| `exch`* | Exchange |
| `validity`* | DAY or GTT |
| `ai_t`* | Alert type |
| `al_id`* | Alert ID |
| `exchsym` | Exchange symbol |
| `oivariable` | Array — see [OIVARIABLE Format](#oivariable-format) |
| `place_order_params` | Order object — see [PLACE_ORDER_PARAMS Format](#place_order_params-format) |

### Response

```json
{ "request_time": "11:14:52 11-10-2021", "stat": "OI replaced", "al_id": "21101100000001" }
```

`stat` is `"OI replaced"` on success or `"Invalid Oi"` on failure; `emsg` present only on errors.

---

## Cancel OCO Order

`POST /CancelOCOOrder`

```bash
curl --location 'https://BaseURL/CancelOCOOrder' \
--header 'Content-Type: application/json' \
--data 'jData={
"uid": "FZ00000",
"al_id": "21083000000040"
}&jKey=<token>'
```

### Request Fields

| Field | Description |
| --- | --- |
| `uid` | User ID of the logged-in user |
| `al_id`* | Alert ID to cancel |

### Response

```json
{ "request_time": "17:41:02 30-08-2021", "stat": "Oi delete success", "al_id": "21083000000040" }
```
