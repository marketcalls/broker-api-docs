# GTT & OCO Orders

**GTT** = Good Till Triggered. **OCO** = One Cancels Other.

All APIs require the request header:

```
Authorization: <api_session_key>
```

| Method | Relative URL | Description |
| --- | --- | --- |
| GET | `/gttorders` | Get GTT/OCO order book |
| POST | `/gttplaceorder` | Place a GTT order |
| POST | `/gttmodify` | Modify a GTT order |
| GET | `/gttcancel/{alert_id}` | Cancel a GTT order |
| POST | `/ocoplaceorder` | Place an OCO order |
| POST | `/ocomodify` | Modify an OCO order |
| GET | `/ococancel/{alert_id}` | Cancel an OCO order |

---

## GTT Order Book

| Particular | Details |
| --- | --- |
| API Name | Get GTT Order book |
| Relative URL | `/gttorders` |
| Method | GET |
| Content-Type | NA |
| Produces | application/json |

### Description

This API returns order book data which represents all the open GTT orders.

### GTT Order Book Response

| Field | Possible values | Description |
| --- | --- | --- |
| `alert_id` | | Alert ID |
| `tradingsymbol` | | Trading symbol as per master file |
| `exchange` | | Specifies the Exchange for your trading symbol |
| `token` | | Unique token ID for each symbol |
| `remarks` | | Any tag by user to mark order |
| `order_time` | | Order Time |
| `order_type` | BUY / SELL | Order type BUY/SELL |
| `price_type` | LIMIT / MARKET / SL-LIMIT / SL-MARKET | Price type for order |
| `product_type` | CNC / INTRADAY / NORMAL | Product type |
| `lotsize` | | For Derivatives symbols, specifies its lot size |
| `trigger_price` | | Price at which the order should be triggered |
| `quantity` | | Order quantity (in multiples of lots for derivatives) |
| `condition` | | Condition for the placed GTT / OCO order |

> For OCO entries the item also includes: `stoploss_quantity`, `target_quantity`, `stoploss_price`, `target_price`, `stoploss_trigger`, `target_trigger`, and `condition` of `LMT_OCO`.

### Response Message Format

```json
{
  "status": "SUCCESS",
  "pendingGTTOrderBook": [
    {
      "alert_id": "1234001",
      "tradingsymbol": "TCS-EQ",
      "exchange": "NSE",
      "token": "11536",
      "remarks": "",
      "order_time": "16:23:36 27-03-2023",
      "order_type": "BUY",
      "price_type": "LIMIT",
      "product_type": "CNC",
      "lotsize": "1",
      "trigger_price": "3385.00",
      "price": "3390.00",
      "quantity": "3",
      "condition": "LTP_ABOVE"
    },
    {
      "alert_id": "1234002",
      "tradingsymbol": "RELIANCE-EQ",
      "exchange": "NSE",
      "token": "2885",
      "remarks": "",
      "order_time": "16:24:44 27-03-2023",
      "order_type": "BUY",
      "price_type": "LIMIT",
      "product_type": "CNC",
      "lotsize": "1",
      "trigger_price": "2195.00",
      "price": "2200.00",
      "quantity": "1",
      "condition": "LTP_BELOW"
    },
    {
      "alert_id": "1234003",
      "tradingsymbol": "NIFTY29MAR23F",
      "exchange": "NFO",
      "token": "37834",
      "remarks": "admin",
      "order_time": "16:31:10 27-03-2023",
      "order_type": "SELL",
      "price_type": "LIMIT",
      "product_type": "NORMAL",
      "lotsize": "50",
      "stoploss_quantity": "50",
      "target_quantity": "50",
      "stoploss_price": "17700.00",
      "target_price": "17400.00",
      "stoploss_trigger": "17700.00",
      "target_trigger": "17400.00",
      "condition": "LMT_OCO"
    }
  ]
}
```

---

## Place GTT Order

| Particular | Details |
| --- | --- |
| API Name | Place GTT order |
| Relative URL | `/gttplaceorder` |
| Method | POST |
| Content-Type | application/json |
| Produces | application/json |

### Description

This API places GTT (Good Till Triggered) BUY/SELL orders.

### Request Parameters

| Field | Possible values | Description |
| --- | --- | --- |
| `exchange` | | Specifies the Exchange for your trading symbol |
| `tradingsymbol` | | Trading symbol as per master file |
| `condition` | LTP_ABOVE / LTP_BELOW | Condition for the placed GTT / OCO order |
| `alert_price` | | Order Price |
| `order_type` | BUY / SELL | Order type BUY/SELL |
| `price` | | Order Price |
| `quantity` | | Order quantity (in multiples of lots for derivatives) |
| `product_type` | CNC / INTRADAY / NORMAL | (Optional) Product type, default Normal for Derivatives and CNC for Equity |

### Response Parameters

| Field | Description |
| --- | --- |
| `status` | Shows the status for the request |
| `alert_id` | Alert ID |
| `message` | Shows the status message |
| `request_time` | Request time |

### Request Message Format

```json
{
  "exchange": "NSE",
  "tradingsymbol": "TCS-EQ",
  "condition": "LTP_BELOW",
  "alert_price": "3100",
  "order_type": "BUY",
  "quantity": "1",
  "price": "3100"
}
```

### Response Message Format

```json
{
  "status": "SUCCESS",
  "alert_id": "1234001",
  "message": "Order Submitted Successfully",
  "request_time": "11:31:32 27-03-2023"
}
```

---

## Modify GTT Order

| Particular | Details |
| --- | --- |
| API Name | Modify GTT order |
| Relative URL | `/gttmodify` |
| Method | POST |
| Content-Type | application/json |
| Produces | application/json |

### Description

This API modifies an existing GTT order, if it is OPEN.

### Request Parameters

| Field | Possible values | Description |
| --- | --- | --- |
| `exchange` | | Specifies the Exchange for your trading symbol |
| `alert_id` | | Alert ID |
| `tradingsymbol` | | Trading symbol as per master file |
| `condition` | | Condition for the placed GTT / OCO order |
| `alert_price` | | Order Price |
| `order_type` | BUY / SELL | Order type BUY/SELL |
| `price` | | Order Price |
| `quantity` | | Order quantity (in multiples of lots for derivatives) |
| `product_type` | CNC / INTRADAY / NORMAL | (Optional) Product type, default Normal for Derivatives and CNC for Equity. Mandatory for Intraday Orders |

### Response Parameters

| Field | Description |
| --- | --- |
| `status` | Shows the status for the request |
| `alert_id` | Alert ID |
| `message` | Shows the status message |
| `request_time` | Request time |

### Request Message Format

```json
{
  "exchange": "NSE",
  "alert_id": "1234001",
  "tradingsymbol": "TCS-EQ",
  "condition": "LTP_ABOVE",
  "alert_price": "3390",
  "order_type": "BUY",
  "quantity": "3",
  "price": "3390"
}
```

### Response Message Format

```json
{
  "status": "SUCCESS",
  "alert_id": "1234001",
  "message": "Order Modified Successfully",
  "request_time": "12:51:10 27-03-2023"
}
```

---

## Cancel GTT Order

| Particular | Details |
| --- | --- |
| API Name | Cancel GTT order |
| Relative URL | `/gttcancel/{alert_id}` |
| Method | GET |
| Content-Type | NA |
| Produces | application/json |

### Description

This API cancels an existing GTT order if it is OPEN.

### Request message format

This is a GET request and the alert id needs to be put in the request URL.

```
e.g. /gttcancel/1234001
```

### Response Parameters

| Field | Description |
| --- | --- |
| `status` | Shows the status for the request |
| `alert_id` | Alert ID |
| `message` | Shows the status message |
| `request_time` | Request time |

### Response Message Format

```json
{
  "status": "SUCCESS",
  "request_time": "12:52:00 27-03-2023",
  "alert_id": "1234001",
  "message": "Order cancelled Successfully"
}
```

---

## Place OCO Order

| Particular | Details |
| --- | --- |
| API Name | Place OCO order |
| Relative URL | `/ocoplaceorder` |
| Method | POST |
| Content-Type | application/json |
| Produces | application/json |

### Description

This API places an OCO (One Cancels Other) order.

### Request Parameters

| Field | Possible values | Description |
| --- | --- | --- |
| `remarks` | | Any tag by user to mark order |
| `tradingsymbol` | | Trading symbol as per master file |
| `exchange` | | Specifies the Exchange for your trading symbol |
| `order_type` | BUY / SELL | Order type BUY/SELL |
| `target_quantity` | | Target Quantity |
| `stoploss_quantity` | | Stoploss Quantity |
| `target_price` | | Target Price |
| `stoploss_price` | | Stoploss Price |
| `product_type` | CNC / INTRADAY / NORMAL | (Optional) Product type, default Normal for Derivatives and CNC for Equity |

### Response Parameters

| Field | Description |
| --- | --- |
| `status` | Shows the status for the request |
| `alert_id` | Alert ID |
| `message` | Shows the status message |
| `request_time` | Request time |

### Request Message Format

```json
{
  "remarks": "admin",
  "tradingsymbol": "NIFTY29MAR23F",
  "exchange": "NFO",
  "order_type": "SELL",
  "target_quantity": "50",
  "stoploss_quantity": "50",
  "target_price": "17000",
  "stoploss_price": "17300"
}
```

### Response Message Format

```json
{
  "status": "SUCCESS",
  "request_time": "12:53:08 27-03-2023",
  "alert_id": "1234002",
  "message": "Order Submitted Successfully"
}
```

---

## Modify OCO Order

| Particular | Details |
| --- | --- |
| API Name | Modify OCO order |
| Relative URL | `/ocomodify` |
| Method | POST |
| Content-Type | application/json |
| Produces | application/json |

### Description

This API modifies an existing OCO order, if it is OPEN.

### Request Parameters

| Field | Possible values | Description |
| --- | --- | --- |
| `remarks` | | Any tag by user to mark order |
| `tradingsymbol` | | Trading symbol as per master file |
| `exchange` | | Specifies the Exchange for your trading symbol |
| `order_type` | BUY / SELL | Order type BUY/SELL |
| `target_quantity` | | Target Quantity |
| `stoploss_quantity` | | Stoploss Quantity |
| `target_price` | | Target Price |
| `stoploss_price` | | Stoploss Price |
| `alert_id` | | Alert ID |
| `product_type` | CNC / INTRADAY / NORMAL | (Optional) Product type, default Normal for Derivatives and CNC for Equity. Mandatory for Intraday Orders |

### Response Parameters

| Field | Description |
| --- | --- |
| `status` | Shows the status for the request |
| `alert_id` | Alert ID |
| `message` | Shows the status message |
| `request_time` | Request time |

### Request Message Format

```json
{
  "remarks": "admin",
  "tradingsymbol": "NIFTY29MAR23F",
  "exchange": "NFO",
  "order_type": "SELL",
  "target_quantity": "100",
  "stoploss_quantity": "100",
  "target_price": "17050",
  "stoploss_price": "17250",
  "alert_id": "1234002"
}
```

### Response Message Format

```json
{
  "status": "SUCCESS",
  "request_time": "12:54:06 27-03-2023",
  "alert_id": "1234002",
  "message": "Order Modified Successfully"
}
```

---

## Cancel OCO Order

| Particular | Details |
| --- | --- |
| API Name | Cancel OCO order |
| Relative URL | `/ococancel/{alert_id}` |
| Method | GET |
| Content-Type | NA |
| Produces | application/json |

### Description

This API cancels an existing OCO order if it is OPEN.

### Request message format

This is a GET request and the alert id needs to be put in the request URL.

```
e.g. /ococancel/1234002
```

### Response Parameters

| Field | Description |
| --- | --- |
| `status` | Shows the status for the request |
| `alert_id` | Alert ID |
| `message` | Shows the status message |
| `request_time` | Request time |

### Response Message Format

```json
{
  "status": "SUCCESS",
  "request_time": "12:54:41 27-03-2023",
  "alert_id": "1234002",
  "message": "Order cancelled Successfully"
}
```
