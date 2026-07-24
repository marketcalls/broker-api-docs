# Alerts

Price alerts (distinct from [GTT orders](04-gtt-oco-orders.md), which place a real order on trigger).

## Set Alert

`POST /SetAlert`

```bash
curl --location 'https://BaseURL/SetAlert' \
--header 'Content-Type: application/json' \
--data 'jData={
"uid": "FZ00000",
"exch": "NSE",
"tsym": "ACC-EQ",
"ai_t": "",
"validity": "DAY",
"remarks": ""
}&jKey=<token>'
```

### Request Fields

| Field | Description |
| --- | --- |
| `uid`* | User ID of the logged-in user |
| `tsym`* | Trading symbol |
| `exch`* | Exchange segment |
| `ai_t`* | Alert type |
| `validity`* | DAY or GTT |
| `d` | Data to compare with LTP |
| `remarks`* | Order entry tag |

### Response

```json
[{ "request_time": "11:22:26 08-04-2021", "stat": "Oi created", "al_id": "21040800000004" }]
```

`emsg` is present only on errors (invalid input / session expired).

---

## Cancel Alert

`POST /CancelAlert`

```bash
curl --location 'https://BaseURL/CancelAlert' \
--header 'Content-Type: application/json' \
--data 'jData={
"uid": "FZ00000",
"actid": "FZ00000"
}&jKey=<token>'
```

### Request Fields

| Field | Description |
| --- | --- |
| `uid` | User ID of the logged-in user |
| `al_id`* | Alert ID |

### Response

```json
[{ "request_time": "15:03:33 08-04-2021", "stat": "Oi delete success", "al_id": "21040800000008" }]
```

---

## Modify Alert

`POST /ModifyAlert`

```bash
curl --location 'https://BaseURL/ModifyAlert' \
--header 'Content-Type: application/json' \
--data 'jData={
"uid": "FZ00000",
"actid": "FZ00000",
"exch": "NSE",
"tsym": "ACC-EQ",
"ai_t": "",
"validity": "DAY",
"remarks": ""
}&jKey=<token>'
```

### Request Fields

| Field | Description |
| --- | --- |
| `uid`* | User ID of the logged-in user |
| `tsym`* | Trading symbol |
| `exch`* | Exchange segment |
| `ai_t`* | Original alert type — cannot be modified |
| `al_id` | Alert ID |
| `validity`* | DAY or GTT |
| `d` | Data to compare with LTP |
| `remarks`* | Order entry tag |

### Response

```json
[{ "request_time": "16:36:42 08-04-2021", "stat": "Oi Replaced", "al_id": "21040800000013" }]
```

---

## Get Pending Alert

`POST /GetPendingAlert`

```bash
curl --location 'https://BaseURL/GetPendingAlert' \
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
    "stat": "Ok", "ai_t": "LTP_A", "al_id": "21040800000008",
    "tsym": "ACC-EQ", "exch": "NSE", "token": "22",
    "remarks": "test", "validity": "DAY", "d": "95000.00"
  }
]
```

---

## Get Enabled Alert Types

`POST /GetEnabledAlertTypes`

```bash
curl --location 'https://BaseURL/GetEnabledAlertTypes' \
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
  "stat": "Ok",
  "request_time": "04062021121503",
  "ai_ts": [{ "ai_t": "ATP" }, { "ai_t": "LTP" }, { "ai_t": "Perc. Change" }]
}
```

`ai_ts` is an array of alert types enabled for the account.
