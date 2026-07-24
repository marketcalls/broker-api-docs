# User Details

`POST /UserDetails`

```bash
curl --location 'https://BaseURL/UserDetails' \
--header 'Content-Type: application/json' \
--data 'jData={ "uid": "FZ00000" }&jKey=<token>'
```

## Request Fields

| Field | Description |
| --- | --- |
| `uid`* | Logged-in User ID |

## Response

```json
{
  "request_time": "20:20:04 19-05-2020",
  "prarr": [
    { "prd": "C", "s_prdt_ali": "Delivery", "exch": ["NSE", "BSE"] },
    { "prd": "I", "s_prdt_ali": "Intraday", "exch": ["NSE", "BSE", "NFO"] },
    { "prd": "H", "s_prdt_ali": "High Leverage", "exch": ["NSE", "BSE", "NFO"] },
    { "prd": "B", "s_prdt_ali": "Bracket Order", "exch": ["NSE", "BSE", "NFO"] }
  ],
  "exarr": ["NSE", "NFO"],
  "orarr": ["LMT", "SL-LMT", "DS", "2L", "3L", "4L"],
  "brkname": "VIDYA",
  "brnchid": "VIDDU",
  "email": "gururaj@gmail.com",
  "actid": "GURURAJ",
  "uprev": "INVESTOR",
  "stat": "Ok"
}
```

| Field | Description |
| --- | --- |
| `stat` | `Ok` or `Not_Ok` |
| `exarr` | Array of enabled exchange names |
| `orarr` | Array of enabled price types for the user |
| `prarr` | Array of enabled product objects — see [Product Obj Format](#product-obj-format) |
| `brkname` | Broker ID |
| `brnchid` | Branch ID |
| `email` | Registered email |
| `actid` | Account ID |
| `m_num` | Mobile number |
| `uprev` | Always `INVESTOR` — other user types cannot log in via this API |
| `access_type` | Access type |
| `request_time` | Present only on success |
| `emsg` | Present only on errors |

### PRODUCT OBJ Format

| Field | Description |
| --- | --- |
| `prd` | Product name |
| `s_prdt_ali` | Product display name |
| `exch` | Array of exchange names enabled for this product |

`exarr`, `orarr`, and `prarr` drive which exchange/price-type/product combinations to offer in your UI, and which `exch`/`prctyp`/`prd` values are valid to send when [placing an order](03-orders.md#place-order).
