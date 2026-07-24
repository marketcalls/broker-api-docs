# Funds

## Get Max Payout Amount

`POST /GetMaxPayoutAmount`

```bash
curl --location 'https://BaseURL/GetMaxPayoutAmount' \
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
| `actid` | Login user's account ID |

### Response

```json
{ "request_time": "15:52:26 10-05-2021", "stat": "Ok", "actid": "C-GURURAJ", "payout": "21200.20" }
```

| Field | Description |
| --- | --- |
| `stat` | Success or failure indication |
| `actid` | Account ID |
| `payout` | Maximum payout amount |

---

## Funds Payout Request

`POST /FundsPayOutReq`

```bash
curl --location 'https://BaseURL/FundsPayOutReq' \
--header 'Content-Type: application/json' \
--data 'jData={
"actid": "FZ00000",
"payout": ""
}&jKey=<token>'
```

### Request Fields

| Field | Description |
| --- | --- |
| `uid`* | User ID of the logged-in user |
| `actid`* | Login user's account ID |
| `payout`* | Payout amount |
| `remarks` | Order entry tag |

### Response

```json
{ "request_time": "15:52:27 10-05-2021", "trn_id": "20211300000030", "stat": "W" }
```

`stat` is the transaction status; `trn_id` is the transaction ID.

---

## Get Payin Report

`POST /GetPayinReport`

```bash
curl --location 'https://BaseURL/GetPayinReport' \
--header 'Content-Type: application/json' \
--data 'jData={
"actid": "FZ00000",
"from_date": "",
"to_date": ""
}&jKey=<token>'
```

### Request Fields

| Field | Description |
| --- | --- |
| `actid`* | Login user's account ID |
| `from_date`* | From date |
| `to_date`* | To date |

### Response

```json
[
  { "stat": "Ok", "actid": "GURURAJ", "trans_ref_num": "20211250000001", "tran_status": "Complete", "amt": "10000.00" }
]
```

| Field | Description |
| --- | --- |
| `trans_ref_num` | Transaction reference number |
| `tran_status` | `ADD_FUND_ST_COMPLETE_STR` — indicates transaction status |
| `amt` | Amount |

---

## Get Payout Report

`POST /GetPayoutReport`

```bash
curl --location 'https://BaseURL/GetPayoutReport' \
--header 'Content-Type: application/json' \
--data 'jData={
"actid": "FZ00000",
"from_date": "",
"to_date": ""
}&jKey=<token>'
```

### Request Fields

| Field | Description |
| --- | --- |
| `actid`* | Login user's account ID |
| `from_date`* | From date |
| `to_date`* | To date |

### Response

```json
[
  { "stat": "Ok", "actid": "GURURAJ", "trans_ref_num": "20211270000002", "tran_status": "Complete", "amt": "-1000.00" }
]
```

`tran_status` is `WITHDRAW_ST_COMPLETE_STR` — indicates transaction status.

---

## Cancel Payout

`POST /CancelPayout`

```bash
curl --location 'https://BaseURL/CancelPayout' \
--header 'Content-Type: application/json' \
--data 'jData={
"uid": "FZ00000",
"actid": "FZ00000",
"trans_ref_num": ""
}&jKey=<token>'
```

### Request Fields

| Field | Description |
| --- | --- |
| `actid`* | Login user's account ID |
| `uid`* | User ID of the logged-in user |
| `trans_ref_num`* | Transaction reference number |
| `brkname` | Broker name |

### Response

```json
{ "request_time": "18:59:25 12-05-2021", "stat": "Ok", "actid": "GURURAJ", "tran_status": "88" }
```

Failure example: `{ "stat": "Not_Ok", "request_time": "...", "emsg": "Error Occurred : -103 20211300000033 is Already Canceled" }`
