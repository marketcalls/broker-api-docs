# GTT Orders

> Source: https://shoonya.com/api-documentation (GTT Orders)

## Contents

- [Place GTT Orders → Place GTT Order](#place-gtt-order)
- [Cancel GTT Orders → Cancel GTT Order](#cancel-gtt-order)
- [Get Pending GTT Orders → Get Pending GTT Order](#get-pending-gtt-order)
- [Get Enabled GTT Orders → Get Enabled GTTs](#get-enabled-gtts)
- [Get Unsettled Trading Date → Get UnSettled Trading date](#get-unsettled-trading-date)

---

## Place GTT Order

> Request to be POSTed to uri : /NorenWClientAPI/PlaceGTTOrder

### Request Details

| Parameter Name | Possible value | Description |
|---|---|---|
| jData* | - | Should send json object with fields in below list |

**Json Fields**

| Parameter Name | Possible value | Description |
|---|---|---|
| uid* | - | User id of the logged in user. |
| tsym* | - | Trading symbol |
| exch* | - | Exchange Segment |
| ai_t* | - | Alert type |
| validity* | DAY or GTT | validity |
| d | - | Data to be compared with LTP |
| remarks* | - | Any message Entered during order entry. |
| trantype* | B / S | B -> BUY, S -> SELL |
| prctyp* | LMT / MKT / SL-LMT / SL-MKT / DS / 2L / 3L | - |
| prd* | C / M / H | Product name |
| ret* | DAY / EOS / IOC | Retention type (Show options as per allowed exchanges) |
| actid* | - | Login users account ID |
| qty* | - | Order Quantity |
| prc* | - | Order Price |
| dscqty | - | Disclosed quantity (Max 10% for NSE, and 50% for MCX) |

### Response Details

| Parameter Name | Possible value | Description |
|---|---|---|
| stat | - | GTT order success or failure indication. |
| request_time | - | This will be present only in a successful response. |
| al_id | - | Alert Id |

| Parameter Name | Possible value | Description |
|---|---|---|
|   |   | This will be present only in case of errors. That is : 1) Invalid Input 2) Session Expired |

**Sample Success Output:**

```json
{
  "request_time":"10:02:06 15-04-2021",
  "stat":"Oi created",
  "al_id":"210415000000010"
}
```

**Sample Failure Output:**

```json
{
  "stat":"Not_Ok",
  "emsg":"Session Expired : Invalid Session Key"
}
```

## Cancel GTT Order

> Request to be POSTed to uri : /NorenWClientAPI/CancelGTTOrder

### Request Details

| Parameter Name | Possible value | Description |
|---|---|---|
| jData* | - | Should send json object with fields in below list |

**Json Fields**

| Parameter Name | Possible value | Description |
|---|---|---|
| uid* | - | User id of the logged in user. |
| al_id* | - | Alert Id |

### Response Details

| Parameter Name | Possible value | Description |
|---|---|---|
| stat | - | GTT order success or failure indication. |
| request_time | - | This will be present only in a successful response. |
| al_id | - | Alert Id |
| emsg | - | This will be present only in case of errors. That is: 1) Invalid Input 2) Session Expired |

**Sample Success Output:**

```json
{
  "request_time":"12:20:01 15-04-2021",
  "stat":"Oi delete success",
  "al_id":"210415000000013"
}
```

**Sample Failure Output:**

```json
{
  "stat":"Not_Ok",
  "emsg":"Session Expired : Invalid Session Key"
}
```

## Get Pending GTT Order

> Request to be POSTed to uri : /NorenWClientAPI/GetPendingGTTOrder

### Request Details

| Parameter Name | Possible value | Description |
|---|---|---|
| jData* | - | Should send json object with fields in below list |

**Json Fields**

| Parameter Name | Possible value | Description |
|---|---|---|
| uid* | - | User id of the logged in user. |

### Response Details

| Parameter Name | Possible value | Description |
|---|---|---|
| stat | - | alert success or failure indication. |
| ai_t | - | Alert type |
| al_id | - | Alert Id |
| tsym | - | Trading symbol |
| exch | - | Exchange Segment |
| token | - | Contract token |
| remarks* | - | Any message Entered during order entry. |
| validity | DAY or GTT | validity |
| d | - | Data to be compared with LTP |
| trantype | B / S | B -> BUY, S -> SELL |
| prctyp | LMT / MKT / SL-LMT / SL-MKT / DS / 2L / 3L | - |
| prd | C / M / H | Product name |
| ret | DAY / EOS / IOC | Retention type (Show options as per allowed exchanges) |
| actid | - | Login users account ID |
| qty | - | Order Quantity |
| prc | - | Order Price |
| emsg | - | This will be present only in case of errors. That is: 1) Invalid Input 2) Session Expired |

**Sample Success Output:**

```json
{
  "stat":"OK",
  "ai_t":"LTP_A",
  "al_id":"210415000000002",
  "tsym":"ACC-EQ",
  "exch":"NSE",
  "token":"22",
  "Remarks":"test",
  "validity":"DAY",
  "actid":"MDHINIT",
  "trantype":"B",
  "prctyp":"LMT",
  "qty":1,
  "prc":"1305.00",
  "C":"C",
  "prd":"C",
  "ordersource":"MOB",
  "d":"1900.00"
}
```

**Sample Failure Output:**

```json
{
  "stat":"Not_Ok",
  "emsg":"Session Expired : Invalid Session Key"
}
```

## Get Enabled GTTs

> Request to be POSTed to uri : /NorenWClientAPI/GetEnabledGTTs

### Request Details

| Parameter Name | Possible value | Description |
|---|---|---|
| jData* | - | Should send json object with fields in below list |

**Json Fields**

| Parameter Name | Possible value | Description |
|---|---|---|
| uid* | - | User id of the logged in user. |

### Response Details

| Parameter Name | Possible value | Description |
|---|---|---|
| stat | - | GTT order success or failure indication. |
| request_time | - | This will be present only in a successful response. |
| ai_ts | - | Array of alert types |
| emsg | - | This will be present only in case of errors. That is: 1) Invalid Input 2) Session Expired |

**Sample Success Output:**

```json
{
  "stat":"OK",
  "request_time":"04062021121503",
  "ai_ts":[
    {"ai_t":"ATP"},
    {"ai_t":"LTP"}
  ]
}
```

**Sample Failure Output:**

```json
{
  "stat":"Not_Ok",
  "emsg":"Session Expired : Invalid Session Key"
}
```

## Get UnSettled Trading date

> Request to be POSTed to uri : /NorenWClientAPI/GetUnSttledTradingDate

### Request Details

| Parameter Name | Possible value | Description |
|---|---|---|
| jData* | - | Should send json object with fields in below list |

**Json Fields**

| Parameter Name | Possible value | Description |
|---|---|---|
| uid* | - | User id of the logged in user. |

### Response Details

| Parameter Name | Possible value | Description |
|---|---|---|
| stat | - | success or failure indication. |
| request_time | - | This will be present only in a successful response. |
| trd_date | - | Array of objects (trade date as defined below) |

**Sample Success Response:**

```json
{
  "stat":"OK",
  "request_time":"10052021152900",
  "trd_date":[
    { "trd_date":"28-04-2021" },
    { "trd_date":"29-04-2021" },
    { "trd_date":"30-04-2021" }
  ]
}
```

**Sample Failure Response:**

```json
{
  "stat":"Not_Ok",
  "emsg":"Session Expired : Invalid Session Key"
}
```
