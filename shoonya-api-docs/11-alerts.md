# Alerts

> Source: https://shoonya.com/api-documentation (Alerts)

## Contents

- [Set Alert](#set-alert)
- [Cancel Alert](#cancel-alert)
- [Modify Alert](#modify-alert)
- [Get Pending Alert → Get Pending GTT Order](#get-pending-gtt-order)
- [Get Enabled Alert Types → Get Enabled GTTs](#get-enabled-gtts)

---

## Set Alert

> Request to be POSTed to uri : /NorenWClientAPI/SetAlert

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
| validity* | DAY or GTT | Validity |
| d | - | Data to be compared with LTP |
| remarks* | - | Any message Entered during order entry. |

### Response Details

| Parameter Name | Possible value | Description |
|---|---|---|
| stat | - | alert success or failure indication. |
| request_time | - | This will be present only in a successful response. |
| al_id | - | Alert Id |
| emsg | - | This will be present only in case of errors. That is : 1) Invalid Input 2) Session Expired |

**Sample Success Output:**

```json
{
  "request_time":"11:22:26 08-04-2021",
  "stat":"OI created",
  "al_id":"210408000000004"
}
```

**Sample Failure Output:**

```json
{
  "stat":"Not_Ok",
  "emsg":"Session Expired : Invalid Session Key"
}
```

## Cancel Alert

> Request to be POSTed to uri : /NorenWClientAPI/CancelAlert

### Request Details

| Parameter Name | Possible value | Description |
|---|---|---|
| jData* | - | Should send json object with fields in below list |

**Json Fields**

| Parameter Name | Possible value | Description |
|---|---|---|
| uid* | - | User id of the logged in user. |
| ai_t* | - | Alert ID |

### Response Details

| Parameter Name | Possible value | Description |
|---|---|---|
| stat | - | alert success or failure indication. |
| request_time | - | This will be present only in a successful response. |
| al_id | - | Alert Id |
| emsg | - | This will be present only in case of errors. That is : 1) Invalid Input 2) Session Expired |

**Sample Success Output:**

```json
{
  "request_time":"15:03:33 08-04-2021",
  "stat":"O! delete success",
  "al_id":"210408000000008"
}
```

**Sample Failure Output:**

```json
{
  "stat":"Not_Ok",
  "emsg":"Session Expired : Invalid Session Key"
}
```

## Modify Alert

> Request to be POSTed to uri : /NorenWClientAPI/ModifyAlert

### Request Details

| Parameter Name | Possible value | Description |
|---|---|---|
| jData* | - | Should send json object with fields in below list |

**Json Fields**

| Parameter Name | Possible value | Description |
|---|---|---|
| uid* | - | User id of the logged in user. |
| ai_t* | - | Alert ID |

### Response Details

| Parameter Name | Possible value | Description |
|---|---|---|
| uid* | - | User id of the logged in user. |
| tsym* | - | Trading symbol |
| exch* | - | Exchange Segment |
| ai_t* | - | Alert Type, should be original alert type, can’t be modified. |
| al_id | - | Alert ID |
| validity* | DAY or GTT | Validity |
| d | - | Data to be compared with LTP |
| remarks* | - | Any message Entered during order entry. |

| Parameter Name | Possible value | Description |
|---|---|---|
| stat | - | alert success or failure indication. |
| request_time | - | This will be present only in a successful response. |
| al_id | - | Alert Id |
| emsg | - | This will be present only in case of errors. That is : 1) Invalid Input 2) Session Expired |

**Sample Success Output:**

```json
{
  "request_time":"16:36:42 08-04-2021",
  "stat":"Oi Replaced",
  "al_id":"210408000000013"
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

> **Note (conversion):** the sidebar entry **Get Pending Alert** on the live site renders this **Get Pending GTT Order** page — the two nav items share the same component. Reproduced as published; there is no separate Get Pending Alert page.

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

> **Note (conversion):** the sidebar entry **Get Enabled Alert Types** on the live site renders this **Get Enabled GTTs** page — the two nav items share the same component. Reproduced as published; there is no separate Get Enabled Alert Types page.

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
