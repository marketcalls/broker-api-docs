# Orders and Trades

- [Place Regular Order](#place-regular-order)
- [Modify Regular Order](#modify-regular-order)
- [Cancel Regular Order](#cancel-regular-order)
- [Convert Regular Order](#convert-regular-order)
- [Place Cover Order](#place-cover-order)
- [Modify Cover Order](#modify-cover-order)
- [Exit Cover Order](#exit-cover-order)
- [Place Bracket Order](#place-bracket-order)
- [Modify Bracket Order](#modify-bracket-order)
- [Exit Bracket Order](#exit-bracket-order)
- [Order Book API - Filter by API Key](#order-book-api---filter-by-api-key)
- [Order Book API - All Orders](#order-book-api---all-orders)
- [Trade Book API](#trade-book-api)
- [Charges](#charges)

## Place Regular Order

Source: https://developer.paytmmoney.com/docs/api/place-regular-order/

**Method:** `POST`  
**Endpoint:** `https://developer.paytmmoney.com/orders/v1/place/regular`  

### Description

> Using Place Regular Order API one can place **Buy/Sell orders** for instruments. Placing an order implies registering it with the OMS via the API.  
> This does not guarantee the order's receipt at the exchange. The final execution of an order is dependent on several factors including market hours, availability of funds, risk checks and so on.  
> After a Successful execution API returns the Success message and order number, otherwise an Error code will be generated, this is for various reasons.

### Request Attributes

Content Type: JSON

#### Head

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `x-jwt-token` | string | optional | xxxxxx ( The one retrieved from Generate Access Token Steps ) . Can be accessed using: {access\_token} |

#### Body

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `source` | string | optional | Source from which the order is placed Website - W, mWeb - M, Android - N, iOS - I, Exe - R, OperatorWorkStation - O |
| `txn_type` | string | optional | The type of transaction that is being executed (Buy / Sell) |
| `exchange` | string | optional | The exchange which is involved for this specific transaction ( NSE/BSE ) |
| `segment` | string | optional | This describes, to which segment the transaction belongs. (E→ Equity Cash / D→ Equity Derivative) |
| `product` | string | optional | Type of product (C/I/B/V/M) C ((Cash and Carry / Delivery) Valid only for Segment='E'), I (Intraday (Valid for Segment= E/D)), M (Margin (Valid for Segment='D')) B (Bracket order (Valid for Segment= E/D)), V (Cover Order (Valid for Segment= E/D)), |
| `security_id` | string | optional | security\_id of scrip in NSE / BSE |
| `quantity` | string | optional | Quantity of stocks to be traded in NSE / BSE |
| `validity` | string | optional | Validity of the Order, Day/IOC/GTC/GTD DAY - valid for day only IOC - Immediate or cancel, GTC - good till cancel, GTD - good till date |
| `order_type` | string | optional | LMT - Limit order (order is to be traded at mentioned price). ~~MKT - Market order (order is to be traded at market price).~~ Market orders are not supported as an explicit order type. Use LIMIT orders (LMT). SL - Stop loss Limit (trigger which goes into trigger state when market reaches mentioned trigger price). SLM- Stop Loss Market. |
| `price` | string | optional | Price at which order is to be placed |
| `trigger_price` | string | optional | Price at which stop loss is to be triggered (mandatory if it is stop loss order) |
| `off_mkt_flag` | string | optional | Boolean Value, default is false Set False for Live Order Set True for AMO (After Market Order) |
| `order_ltp` | string | optional | The order\_ltp field should be populated with the last traded price of the security for which the order is being placed. This helps in selecting the appropriate market price protection. |

### Response Attributes

Content Type: JSON

#### Body

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `status` | string | optional | Describes whether the API request was Success/Failure |
| `message` | string | optional | Message to be displayed in the frontend |
| `order_no` | string | optional | PML specific order\_no. |
| `error_code` | string | optional | Internal exception specific codes |

### Code Samples

#### CURL

```bash
curl --location --request POST 'https://developer.paytmmoney.com/orders/v1/place/regular' \
--header 'x-jwt-token: {{JWT-TOKEN}}' \
--header 'Content-Type: application/json' \
--data-raw '{
    "txn_type": "B",
    "exchange": "BSE",
    "segment": "E",
    "product": "I",
    "security_id": "500570",
    "quantity": 2,
    "validity": "DAY",
    "order_type": "MKT",
    "price": 0,
    "source": "N",
    "off_mkt_flag": "false",
    "order_ltp": 0.0
}'
```

### Sample Responses

#### SUCCESS

```json
{
"status": "success",
"message": "Order submitted successfully. Your Order Ref No. 212106222471",
"data": [        
    {
"order_no": "212106222471"
    }
],
"error_code": "RS-0023"
}
```

### Possible Response Status

| Code | Status | Message |
| --- | --- | --- |
| PM-0001 | FAILURE | When requests are hitting some other url than PML API endpoint |
| PM-0002 | FAILURE | When PML system is down |
| PM-0003 | FAILURE | When network issues occur before hitting PML API |
| PM-0004 | FAILURE | If there is an error in Paytm MW service |
| PM-0005 | FAILURE | Internal Error PML API response is null |
| PM-0006 | FAILURE | When the wrong product is sent in order request payload |

### Notes

> Note: In case your order is rejected or if you receive an error code, please review your order book first and then try placing your order again.

---

## Modify Regular Order

Source: https://developer.paytmmoney.com/docs/api/modify-regular-order/

**Method:** `POST`  
**Endpoint:** `https://developer.paytmmoney.com/orders/v1/modify/regular`  

### Description

> As long as an order is **pending** in the system, certain attributes of it can be modified. Price, quantity, validity, product are some of the variables that can be modified by the user.  
>   
> You have to pass "order\_no", "serial\_no" "group\_id" as **compulsory** to modify the order.

### Request Attributes

Content Type: JSON

#### Head

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `x-jwt-token` | string | optional | xxxxxx ( The one retrieved from Generate Access Token Steps ) . Can be accessed using: {access\_token} |

#### Body

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `source` | string | optional | Source from which the order is placed Website - W, mWeb - M, Android - N, iOS - I, Exe - R, OperatorWorkStation - O |
| `txn_type` | string | optional | The type of transaction that is being executed (Buy / Sell) |
| `exchange` | string | optional | The exchange which is involved for this specific transaction ( NSE/BSE ) |
| `segment` | string | optional | This describes, to which segment the transaction belongs. (E→ Equity Cash / D→ Equity Derivative) |
| `product` | string | optional | Type of product (C/I/B/V/M) C ((Cash and Carry / Delivery) Valid only for Segment='E'), I (Intraday (Valid for Segment= E/D)), M (Margin (Valid for Segment='D')) B (Bracket order (Valid for Segment= E/D)), V (Cover Order (Valid for Segment= E/D)), |
| `security_id` | string | optional | security\_id of scrip in NSE / BSE |
| `quantity` | string | optional | Quantity of stocks to be traded in NSE / BSE |
| `validity` | string | optional | Validity of the Order, Day/IOC/GTC/GTD DAY - valid for day only IOC - Immediate or cancel, GTC - good till cancel, GTD - good till date |
| `order_type` | string | optional | LMT - Limit order (order is to be traded at mentioned price). ~~MKT - Market order (order is to be traded at market price).~~ Market orders are not supported as an explicit order type. Use LIMIT orders (LMT). SL - Stop loss Limit (trigger which goes into trigger state when market reaches mentioned trigger price). SLM- Stop Loss Market. |
| `price` | string | optional | Price at which order is to be placed |
| `trigger_price` | string | optional | Price at which stop loss is to be triggered (mandatory if it is stop loss order) |
| `off_mkt_flag` | string | optional | Boolean Value, default is false Set False for Live Order Set True for AMO (After Market Order) |
| `mkt_type` | string | optional | NL/OL/AU/SP/A1/A2 Default is NL- normal |
| `order_no` | string | optional | PML specific order\_no. |
| `serial_no` | string | optional | Serial number specific to PML. This is updated on every order updation |
| `group_id` | string | optional | Group\_id specific to PML |
| `order_ltp` | double | optional | The order\_ltp field should be populated with the last traded price of the security for which the order is being placed. This helps in selecting the appropriate market price protection. |
| `ext_info` | object | optional | The ext\_info field, available in the Order Book or Postback API response, must be passed back unchanged when canceling, exiting, or modifying orders. This JSON object ensures seamless execution and supports future enhancements. |

### Response Attributes

Content Type: JSON

#### Body

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `status` | string | optional | Describes whether the API request was Success/Failure |
| `message` | string | optional | Message to be displayed in the frontend |
| `oms_error_code` | string | optional | OMS specific error codes |
| `order_no` | string | optional | PML specific order\_no. |
| `error_code` | string | optional | Internal exception specific codes |

### Code Samples

#### CURL

```bash
curl --location --request POST 'https://developer.paytmmoney.com/orders/v1/modify/regular' \
--header 'x-jwt-token: {{JWT-TOKEN}}' \
--header 'Content-Type: application/json' \
--data-raw '{
  "source": "N",
  "txn_type": "B",
  "exchange": "NSE",
  "segment": "E",
  "product": "I",
  "security_id": "236”,
  "quantity": 10,
  "validity": "DAY",
  "order_type": "LMT",
  "price": 0,
  “trigger_price”: 380,
  "off_mkt_flag": "false",
  "mkt_type": "NL",
  "order_no": "212106222471",
  "serial_no": 1,
  "group_id": 1,
  "order_ltp": 0.0,
  "ext_info": {
    "total_qty": 10,
    "rem_qty": 10,
    "algo_order_no": "202503032025"
  }
}'
```

### Sample Responses

#### SUCCESS

```json
{
"status": "success",
"message": "Order Modification request submitted successfully. Your Order Ref No. 11906214401",
"data": [
{
"oms_error_code":"12345",
"order_no": "212106222471"
}
],
"error_code": "RS-0023"
}
```

### Possible Response Status

| Code | Status | Message |
| --- | --- | --- |
| PM-0001 | FAILURE | When requests are hitting some other url than PML API endpoin |
| PM-0002 | FAILURE | When PML system is down |
| PM-0003 | FAILURE | When network issues occur before hitting PML API |
| PM-0004 | FAILURE | If there is an error in Paytm MW service |
| PM-0005 | FAILURE | Internal Error PML API response is null |
| PM-0006 | FAILURE | When the wrong product is sent in order request payload |

### Notes

> Note: In case your order is rejected or if you receive an error code, please review your order book first and then try placing your order again.

---

## Cancel Regular Order

Source: https://developer.paytmmoney.com/docs/api/cancel-regular-order/

**Method:** `POST`  
**Endpoint:** `https://developer.paytmmoney.com/orders/v1/cancel/regular`  

### Description

> An user can cancel **only Pending orders** from the order book. User needs to fill in details before canceling the order. On successful completion of the request the user gets the confirmation.  
>   
> You have to pass "order\_no", "serial\_no" "group\_id" as **compulsory** to cancel the order.

### Request Attributes

Content Type: JSON

#### Head

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `x-jwt-token` | string | optional | xxxxxx ( The one retrieved from Generate Access Token Steps ) . Can be accessed using: {access\_token} |

#### Body

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `source` | string | optional | Source from which the order is placed Website - W, mWeb - M, Android - N, iOS - I, Exe - R, OperatorWorkStation - O |
| `txn_type` | string | optional | The type of transaction that is being executed (Buy / Sell) |
| `exchange` | string | optional | The exchange which is involved for this specific transaction ( NSE/BSE ) |
| `segment` | string | optional | This describes, to which segment the transaction belongs. (E→ Equity Cash / D→ Equity Derivative) |
| `product` | string | optional | Type of product (C/I/B/V/M) C ((Cash and Carry / Delivery) Valid only for Segment='E'), I (Intraday (Valid for Segment= E/D)), M (Margin (Valid for Segment='D')) B (Bracket order (Valid for Segment= E/D)), V (Cover Order (Valid for Segment= E/D)), |
| `security_id` | string | optional | security\_id of scrip in NSE / BSE |
| `quantity` | string | optional | Quantity of stocks to be traded in NSE / BSE |
| `validity` | string | optional | Validity of the Order, Day/IOC/GTC/GTD DAY - valid for day only IOC - Immediate or cancel, GTC - good till cancel, GTD - good till date |
| `order_type` | string | optional | LMT - Limit order (order is to be traded at mentioned price). ~~MKT - Market order (order is to be traded at market price).~~ Market orders are not supported as an explicit order type. Use LIMIT orders (LMT). SL - Stop loss Limit (trigger which goes into trigger state when market reaches mentioned trigger price). SLM- Stop Loss Market. |
| `price` | string | optional | Price at which order is to be placed |
| `off_mkt_flag` | string | optional | Boolean Value, default is false Set False for Live Order Set True for AMO (After Market Order) |
| `mkt_type` | string | optional | NL/OL/AU/SP/A1/A2 Default is NL- normal |
| `order_no` | string | optional | PML specific order\_no. |
| `serial_no` | string | optional | Serial number specific to PML. This is updated on every order updation |
| `group_id` | string | optional | Group\_id specific to PML |
| `trigger_price` | string | optional | Price at which stop loss is to be triggered (mandatory if it is stop loss order) |
| `ext_info` | object | optional | The ext\_info field, available in the Order Book or Postback API response, must be passed back unchanged when canceling, exiting, or modifying orders. This JSON object ensures seamless execution and supports future enhancements. |

### Response Attributes

Content Type: JSON

#### Body

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `status` | string | optional | Describes whether the API request was Success/Failure |
| `message` | string | optional | Message to be displayed in the frontend |
| `oms_error_code` | string | optional | OMS specific error codes |
| `order_no` | string | optional | PML specific order\_no. |
| `error_code` | string | optional | Internal exception specific codes |

### Code Samples

#### CURL

```bash
curl --location --request POST 'https://developer.paytmmoney.com/orders/v1/cancel/regular' \
--header 'x-jwt-token: {{JWT-TOKEN}}' \
--header 'Content-Type: application/json' \
--data-raw '{
  "source": "N",
  "txn_type": "B",
  "exchange": "BSE",
  "segment": "E",
  "product": "I",
  "security_id": "500003",
  "quantity": 2,
  "validity": "DAY",
  "order_type": "MKT",
  "price": 0,
  "off_mkt_flag": "false",
  "mkt_type": "NL",
  "order_no": "11906213771",
  "serial_no": 1,
  "group_id": "1",
  "ext_info": {
    "total_qty": 10,
    "rem_qty": 10,
    "algo_order_no": "202503032025"
  }
}'
```

### Sample Responses

#### SUCCESS

```json
{
"status": "success",
"message": "Order cancellation request submitted successfully. Your Order Ref No. 11906214401",
"data": [
{
"oms_error_code":"12345",
"order_no": "11905188861"
}
],
"error_code": "RS-0023"
}
```

### Possible Response Status

| Code | Status | Message |
| --- | --- | --- |
| PM-0001 | FAILURE | When requests are hitting some other url than PML API |
| PM-0002 | FAILURE | When PML system is down |
| PM-0003 | FAILURE | When network issues occur before hitting PML API |
| PM-0004 | FAILURE | If there is an error in Paytm MW service |
| PM-0005 | FAILURE | Internal Error PML API response is null |
| PM-0006 | FAILURE | When the wrong product is sent in order request payload |

### Notes

> Note: In case your order is rejected or if you receive an error code, please review your order book first and then try placing your order again.

---

## Convert Regular Order

Source: https://developer.paytmmoney.com/docs/api/convert-regular-order/

**Method:** `POST`  
**Endpoint:** `https://developer.paytmmoney.com/orders/v1/convert/regular`  

### Description

> One can **change the Product Type** from Intraday to Delivery/Overnight Carry Forward.  
>   
> For say you have placed order for Segment =D (Derivatives) and Product=I (Intraday). If you want to convert as a Overnight Carry Forward pass Product=M

### Request Attributes

Content Type: JSON

#### Head

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `x-jwt-token` | string | optional | xxxxxx ( The one retrieved from Generate Access Token Steps ) . Can be accessed using: {access\_token} |

#### Body

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `source` | string | optional | Source from which the order is placed Website - W, mWeb - M, Android - N, iOS - I, Exe - R, OperatorWorkStation - O |
| `txn_type` | string | optional | The type of transaction that is being executed (Buy / Sell) |
| `exchange` | string | optional | The exchange which is involved for this specific transaction ( NSE/BSE ) |
| `mkt_type` | string | optional | NL/OL/AU/SP/A1/A2 Default is NL- normal |
| `segment` | string | optional | This describes, to which segment the transaction belongs. (E→ Equity Cash / D→ Equity Derivative) |
| `product_from` | string | optional | Type of product (C/I/B/V/M) C ((Cash and Carry / Delivery) Valid only for Segment='E'), I (Intraday (Valid for Segment= E/D)), B (Bracket order (Valid for Segment= E/D)), V (Cover Order (Valid for Segment= E/D)), M (Margin (Valid for Segment='D')) |
| `product_to` | string | optional | Type of product (C/I/B/V/M) C ((Cash and Carry / Delivery) Valid only for Segment='E'), I (Intraday (Valid for Segment= E/D)), B (Bracket order (Valid for Segment= E/D)), V (Cover Order (Valid for Segment= E/D)), M (Margin (Valid for Segment='D')) |
| `security_id` | string | optional | security\_id of scrip in NSE / BSE |
| `quantity` | string | optional | Quantity of stocks to be traded in NSE / BSE |

### Response Attributes

Content Type: JSON

#### Body

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `status` | string | optional | Describes whether the API request was Success/Failure |
| `message` | string | optional | Message to be displayed in the frontend |
| `order_no` | string | optional | PML specific order\_no. |
| `error_code` | string | optional | Internal exception specific codes |

### Code Samples

#### CURL

```bash
curl --location --request POST 'https://developer.paytmmoney.com/orders/v1/convert/regular' \
--header 'x-jwt-token: {{JWT-TOKEN}}' \
--header 'Content-Type: application/json' \
--data-raw '{
    "source" : "M",
    "txn_type": "B",
    "exchange": "NSE",
    "mkt_type": "NL",
    "segment": "E",
    "product_from": "C",
    "product_to": "I",
    "quantity": 1,
    "security_id": "2885"
}'
```

### Sample Responses

#### SUCCESS

```json
{
  "status": "success",
  "message": "Order submitted successfully. Your Order Ref No. 11906043831",
  "data": [
    {
      "order_no": "11906043831"
    }
  ],
  "error_code": "RS-0023"
}
```

### Possible Response Status

| Code | Status | Message |
| --- | --- | --- |
| PM-0001 | FAILURE | When requests are hitting some other url than PML API endpoint |
| PM-0002 | FAILURE | When PML system is down |
| PM-0003 | FAILURE | When network issues occur before hitting PML API |
| PM-0004 | FAILURE | If there is an error in Paytm MW service |
| PM-0005 | FAILURE | Internal Error PML API response is null |
| PM-0006 | FAILURE | When the wrong product is sent in order request payload |

### Notes

> Note: In case your order is rejected or if you receive an error code, please review your order book first and then try placing your order again.

---

## Place Cover Order

Source: https://developer.paytmmoney.com/docs/api/place-cover-order/

**Method:** `POST`  
**Endpoint:** `https://developer.paytmmoney.com/orders/v1/place/cover`  

### Description

> Cover Order has 2 legs.  
> **Leg 1** will be Entry order (Buy or Sell) and **Leg 2** will be Stop Loss. Once the Entry order gets executed, the system places a Stop Loss order.  
>   
> These orders have **special properties**, where the first-leg order creates a position. The position is exited when the Leg 2 order is executed or canceled.  
>   
> Cover order can be used for intraday orders of Segment=E (Equity) only.

### Request Attributes

Content Type: JSON

#### Head

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `x-jwt-token` | string | optional | xxxxxx ( The one retrieved from Generate Access Token Steps ) . Can be accessed using: {access\_token} |

#### Body

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `source` | string | optional | Source from which the order is placed Website - W, mWeb - M, Android - N, iOS - I, Exe - R, OperatorWorkStation - O |
| `txn_type` | string | optional | The type of transaction that is being executed (Buy / Sell) |
| `exchange` | string | optional | The exchange which is involved for this specific transaction ( NSE/BSE ) |
| `segment` | string | optional | This describes, to which segment the transaction belongs. (E→ Equity Cash / D→ Equity Derivative) |
| `product` | string | optional | Type of product (C/I/B/V/M) C ((Cash and Carry / Delivery) Valid only for Segment='E'), I (Intraday (Valid for Segment= E/D)), M (Margin (Valid for Segment='D')) B (Bracket order (Valid for Segment= E/D)), V (Cover Order (Valid for Segment= E/D)), |
| `security_id` | string | optional | security\_id of scrip in NSE / BSE |
| `quantity` | string | optional | Quantity of stocks to be traded in NSE / BSE |
| `price` | string | optional | Price at which order is to be placed |
| `validity` | string | optional | Validity of the Order, Day/IOC/GTC/GTD DAY - valid for day only IOC - Immediate or cancel, GTC - good till cancel, GTD - good till date |
| `order_type` | string | optional | LMT - Limit order (order is to be traded at mentioned price). ~~MKT - Market order (order is to be traded at market price).~~ Market orders are not supported as an explicit order type. Use LIMIT orders (LMT). SL - Stop loss Limit (trigger which goes into trigger state when market reaches mentioned trigger price). SLM- Stop Loss Market. |
| `trigger_price` | string | optional | Price at which stop loss is to be triggered (mandatory if it is stop loss order) |
| `order_ltp` | string | optional | The order\_ltp field should be populated with the last traded price of the security for which the order is being placed. This helps in selecting the appropriate market price protection. |

### Response Attributes

Content Type: JSON

#### Body

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `status` | string | optional | Describes whether the API request was Success/Failure |
| `message` | string | optional | Message to be displayed in the frontend |
| `order_no` | string | optional | PML specific order\_no. |
| `error_code` | string | optional | Internal exception specific codes |

### Code Samples

#### CURL

```bash
curl --location --request POST 'https://developer.paytmmoney.com/orders/v1/place/cover' \
--header 'x-jwt-token: {{JWT-TOKEN}}' \
--header 'Content-Type: application/json' \
--data-raw '{
  "txn_type": "B",
  "exchange": "BSE",
  "segment": "E",
  "product": "V",
  "security_id": "500325",
  "quantity": 2,
  "price": 1500,
  "validity": "DAY",
  "order_type": "LMT",
  "trigger_price": 1490,
  "source": "N",
  "order_ltp": 0.0
}'
```

### Sample Responses

#### SUCCESS

```json
{
"status": "success",
"message": "Order submitted successfully. Your Order Ref No. 872104072451",
"data": [
{
"order_no": "872104072451"
}
],
"error_code": "RS-0023"
}
```

### Possible Response Status

| Code | Status | Message |
| --- | --- | --- |
| PM-0001 | FAILURE | When requests are hitting some other url than PML API endpoint |
| PM-0002 | FAILURE | When PML system is down |
| PM-0003 | FAILURE | When network issues occur before hitting PML API |
| PM-0004 | FAILURE | If there is an error in Paytm MW service |
| PM-0005 | FAILURE | Internal Error PML API response is null |
| PM-0006 | FAILURE | When the wrong product is sent in order request payload |

### Notes

> Note: In case your order is rejected or if you receive an error code, please review your order book first and then try placing your order again.

---

## Modify Cover Order

Source: https://developer.paytmmoney.com/docs/api/modify-cover-order/

**Method:** `POST`  
**Endpoint:** `https://developer.paytmmoney.com/orders/v1/modify/cover`  

### Description

> As long as an order **is pending** in the system, certain attributes of it **can be modified**.  
>   
> Price, quantity, validity, product etc are some of the variables that can be modified by the user.

### Request Attributes

Content Type: JSON

#### Head

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `x-jwt-token` | string | optional | xxxxxx ( The one retrieved from Generate Access Token Steps ) . Can be accessed using: {access\_token} |

#### Body

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `source` | string | optional | Source from which the order is placed Website - W, mWeb - M, Android - N, iOS - I, Exe - R, OperatorWorkStation - O |
| `txn_type` | string | optional | The type of transaction that is being executed (Buy / Sell) |
| `exchange` | string | optional | The exchange which is involved for this specific transaction ( NSE/BSE ) |
| `segment` | string | optional | This describes, to which segment the transaction belongs. (E→ Equity Cash / D→ Equity Derivative) |
| `product` | string | optional | Type of product (C/I/B/V/M) C ((Cash and Carry / Delivery) Valid only for Segment='E'), I (Intraday (Valid for Segment= E/D)), M (Margin (Valid for Segment='D')) B (Bracket order (Valid for Segment= E/D)), V (Cover Order (Valid for Segment= E/D)), |
| `security_id` | string | optional | security\_id of scrip in NSE / BSE |
| `quantity` | string | optional | Quantity of stocks to be traded in NSE / BSE |
| `validity` | string | optional | Validity of the Order, Day/IOC/GTC/GTD DAY - valid for day only IOC - Immediate or cancel, GTC - good till cancel, GTD - good till date |
| `order_type` | string | optional | LMT - Limit order (order is to be traded at mentioned price). ~~MKT - Market order (order is to be traded at market price).~~ Market orders are not supported as an explicit order type. Use LIMIT orders (LMT). SL - Stop loss Limit (trigger which goes into trigger state when market reaches mentioned trigger price). SLM- Stop Loss Market. |
| `price` | string | optional | Price at which order is to be placed |
| `mkt_type` | string | optional | NL/OL/AU/SP/A1/A2 Default is NL- normal |
| `order_no` | string | optional | PML specific order\_no. |
| `serial_no` | string | optional | Serial number specific to PML. This is updated on every order updation |
| `group_id` | string | optional | Group\_id specific to PML |
| `leg_no` | string | optional | Leg number for multi leg orders like BO, CO |
| `order_ltp` | double | optional | The order\_ltp field should be populated with the last traded price of the security for which the order is being placed. This helps in selecting the appropriate market price protection. |
| `ext_info` | object | optional | The ext\_info field, available in the Order Book or Postback API response, must be passed back unchanged when canceling, exiting, or modifying orders. This JSON object ensures seamless execution and supports future enhancements. |

### Response Attributes

Content Type: JSON

#### Body

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `status` | string | optional | Describes whether the API request was Success/Failure |
| `message` | string | optional | Message to be displayed in the frontend |
| `order_no` | string | optional | PML specific order\_no. |
| `oms_error_code` | string | optional | OMS specific error codes |
| `error_code` | string | optional | Internal exception specific codes |

### Code Samples

#### CURL

```bash
curl --location --request POST 'https://developer.paytmmoney.com/orders/v1/modify/cover' \
--header 'x-jwt-token: {{JWT-TOKEN}}' \
--header 'Content-Type: application/json' \
--data-raw '{
  "source": "N",
  "txn_type": "S",
  "exchange": "BSE",
  "segment": "E",
  "product": "V",
  "security_id": "500325",
  "quantity": 2,
  "price": 1510,
  "validity": "DAY",
  "order_type": "LMT",
  "mkt_type": "NL",
  "order_no": "212001032025",
  "serial_no": 3,
  "group_id": 2,
  "leg_no": "2",
  "order_ltp": 0.0,
  "ext_info": {
    "total_qty": 10,
    "rem_qty": 10,
    "algo_order_no": "202503032025"
  }
}'
```

### Sample Responses

#### SUCCESS

```json
{
"status": "success",
"message": "Order Modification request submitted successfully. Your Order Ref No. 11906214401",
"data": [
{
"oms_error_code":"12345",
"order_no": "11905188861"
}
],
"error_code": "RS-0023"
}
```

### Possible Response Status

| Code | Status | Message |
| --- | --- | --- |
| PM-0001 | FAILURE | When requests are hitting some other url than PML API endpoint |
| PM-0002 | FAILURE | When PML system is down |
| PM-0003 | FAILURE | When network issues occur before hitting PML API |
| PM-0004 | FAILURE | If there is an error in Paytm MW service |
| PM-0005 | FAILURE | Internal Error PML API response is null |
| PM-0006 | FAILURE | When the wrong product is sent in order request payload |

### Notes

> Note: In case your order is rejected or if you receive an error code, please review your order book first and then try placing your order again.

---

## Exit Cover Order

Source: https://developer.paytmmoney.com/docs/api/exit-cover-order/

**Method:** `POST`  
**Endpoint:** `https://developer.paytmmoney.com/orders/v1/exit/cover`  

### Description

> One can Exit the cover order **by exiting Leg 2 order**.  
> The position is exited when the Leg 2 order is executed or canceled.

### Request Attributes

Content Type: JSON

#### Head

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `x-jwt-token` | string | optional | xxxxxx ( The one retrieved from Generate Access Token Steps ) . Can be accessed using: {access\_token} |

#### Body

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `source` | string | optional | Source from which the order is placed Website - W, mWeb - M, Android - N, iOS - I, Exe - R, OperatorWorkStation - O |
| `txn_type` | string | optional | The type of transaction that is being executed (Buy / Sell) |
| `exchange` | string | optional | The exchange which is involved for this specific transaction ( NSE/BSE ) |
| `segment` | string | optional | This describes, to which segment the transaction belongs. (E→ Equity Cash / D→ Equity Derivative) |
| `product` | string | optional | Type of product (C/I/B/V/M) C ((Cash and Carry / Delivery) Valid only for Segment='E'), I (Intraday (Valid for Segment= E/D)), M (Margin (Valid for Segment='D')) B (Bracket order (Valid for Segment= E/D)), V (Cover Order (Valid for Segment= E/D)), |
| `security` | string | optional | security\_id of scrip in NSE / BSE |
| `quantity` | string | optional | Quantity of stocks to be traded in NSE / BSE |
| `price` | string | optional | Price at which order is to be placed |
| `validity` | string | optional | Validity of the Order, Day/IOC/GTC/GTD DAY - valid for day only IOC - Immediate or cancel, GTC - good till cancel, GTD - good till date |
| `order_type` | string | optional | LMT - Limit order (order is to be traded at mentioned price). ~~MKT - Market order (order is to be traded at market price).~~ Market orders are not supported as an explicit order type. Use LIMIT orders (LMT). SL - Stop loss Limit (trigger which goes into trigger state when market reaches mentioned trigger price). SLM- Stop Loss Market. |
| `trigger_price` | string | optional | Price at which stop loss is to be triggered (mandatory if it is stop loss order) |
| `mkt_type` | string | optional | NL/OL/AU/SP/A1/A2 Default is NL- normal |
| `order_no` | string | optional | PML specific order\_no. |
| `serial_no` | string | optional | Serial number specific to PML. This is updated on every order updation |
| `group_id` | string | optional | Group\_id specific to PML |
| `leg_no` | string | optional | Leg number for multi leg orders like BO, CO |
| `ext_info` | object | optional | The ext\_info field, available in the Order Book or Postback API response, must be passed back unchanged when canceling, exiting, or modifying orders. This JSON object ensures seamless execution and supports future enhancements. |

### Response Attributes

Content Type: JSON

#### Body

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `status` | string | optional | Describes whether the API request was Success/Failure |
| `message` | string | optional | Message to be displayed in the frontend |
| `order_no` | string | optional | PML specific order\_no. |
| `oms_error_code` | string | optional | OMS specific error codes |
| `error_code` | string | optional | Internal exception specific codes |

### Code Samples

#### CURL

```bash
curl --location --request POST 'https://developer.paytmmoney.com/orders/v1/exit/cover' \
--header 'x-jwt-token: {{JWT-TOKEN}}' \
--header 'Content-Type: application/json' \
--data-raw '{
  "txn_type": "B",
  "exchange": "BSE",
  "segment": "E",
  "product": "V",
  "security_id": "500010",
  "quantity": "5",
  "price": 2159.3,
  "trigger_price": "0",
  "validity": "DAY",
  "order_type": "LMT",
  "mkt_type": "NL",
  "order_no": "1119101711114",
  "serial_no": "1",
  "group_id": "1",
  "leg_no": "1",
  "source": "N",
  "ext_info": {
    "total_qty": 10,
    "rem_qty": 10,
    "algo_order_no": "202503032025"
  }
}'
```

### Sample Responses

#### SUCCESS

```json
{
"status": "success",
"message": "Order cancellation request submitted successfully. Your Order Ref No. 11906214401",
"data": [
{
"oms_error_code":"12345",
"order_no": "11905188861"
}
],
"error_code": "RS-0023"
}
```

### Possible Response Status

| Code | Status | Message |
| --- | --- | --- |
| PM-0001 | FAILURE | When requests are hitting some other url than PML API endpoint |
| PM-0002 | FAILURE | When PML system is down |
| PM-0003 | FAILURE | When network issues occur before hitting PML API |
| PM-0004 | FAILURE | If there is an error in Paytm MW service |
| PM-0005 | FAILURE | Internal Error PML API response is null |
| PM-0006 | FAILURE | When the wrong product is sent in order request payload |

### Notes

> Note: In case your order is rejected or if you receive an error code, please review your order book first and then try placing your order again.

---

## Place Bracket Order

Source: https://developer.paytmmoney.com/docs/api/place-bracket-order/

**Method:** `POST`  
**Endpoint:** `https://developer.paytmmoney.com/orders/v1/place/bracket`  

### Description

> Bracket Order has 3 legs.  
> **Leg 1** will be Entry order (Buy or Sell), **Leg 2** will be Stop Loss and **Leg 3** will be Target or Profit Order. Once the Entry order gets executed, the system places Stop Loss & Target orders.  
>   
> These orders have **special properties**, where the first-leg order creates a position. The position is exited when the Leg 2 or Leg 3 order gets executed or canceled.  
>   
> Bracket order can be used for intraday orders of **Segment=E (Equity) only**.

### Request Attributes

Content Type: JSON

#### Head

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `x-jwt-token` | string | optional | xxxxxx ( The one retrieved from Generate Access Token Steps ) . Can be accessed using: {access\_token} |

#### Body

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `source` | string | optional | Source from which the order is placed Website - W, mWeb - M, Android - N, iOS - I, Exe - R, OperatorWorkStation - O |
| `txn_type` | string | optional | The type of transaction that is being executed (Buy / Sell) |
| `exchange` | string | optional | The exchange which is involved for this specific transaction ( NSE/BSE ) |
| `segment` | string | optional | This describes, to which segment the transaction belongs. (E→ Equity Cash / D→ Equity Derivative) |
| `product` | string | optional | Type of product (C/I/B/V/M) C ((Cash and Carry / Delivery) Valid only for Segment='E'), I (Intraday (Valid for Segment= E/D)), M (Margin (Valid for Segment='D')) B (Bracket order (Valid for Segment= E/D)), V (Cover Order (Valid for Segment= E/D)), |
| `security_id` | string | optional | security\_id of scrip in NSE / BSE |
| `quantity` | string | optional | Quantity of stocks to be traded in NSE / BSE |
| `validity` | string | optional | Validity of the Order, Day/IOC/GTC/GTD DAY - valid for day only IOC - Immediate or cancel, GTC - good till cancel, GTD - good till date |
| `order_type` | string | optional | LMT - Limit order (order is to be traded at mentioned price). ~~MKT - Market order (order is to be traded at market price).~~ Market orders are not supported as an explicit order type. Use LIMIT orders (LMT). SL - Stop loss Limit (trigger which goes into trigger state when market reaches mentioned trigger price). SLM- Stop Loss Market. |
| `price` | string | optional | Price at which order is to be placed |
| `trigger_price` | string | optional | Price at which stop loss is to be triggered (mandatory if it is stop loss order) |
| `profit_value` | string | optional | Target order price value for Bracket order |
| `stoploss_value` | string | optional | Stop loss order price value for Bracket order |
| `order_ltp` | string | optional | The order\_ltp field should be populated with the last traded price of the security for which the order is being placed. This helps in selecting the appropriate market price protection. |

### Response Attributes

Content Type: JSON

#### Body

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `status` | string | optional | Describes whether the API request was Success/Failure |
| `message` | string | optional | Message to be displayed in the frontend |
| `order_no` | string | optional | PML specific order\_no. |
| `erroe_code` | string | optional | Internal exception specific codes |

### Code Samples

#### CURL

```bash
curl --location --request POST 'https://developer.paytmmoney.com/orders/v1/place/bracket' \
--header 'x-jwt-token: {{JWT-TOKEN}}' \
--header 'Content-Type: application/json' \
--data-raw '{
  "source": "N",
  "txn_type": "B",
  "exchange": "BSE",
  "segment": "E",
  "product": "B",
  "security_id": "500003",
  "quantity": 2,
  "validity": "DAY",
  "order_type": "LMT",
  "price": 163,
  "profit_value": 4,
  "stoploss_value": 2,
  "order_ltp": 0.0
}'
```

### Sample Responses

#### SUCCESS

```json
{
"status": "success",
"message": "Order submitted successfully. Your Order Ref No. 872104072451",
"data": [
{
"order_no": "872104072451"
}
],
"error_code": "RS-0023"
}
```

### Possible Response Status

| Code | Status | Message |
| --- | --- | --- |
| PM-0001 | FAILURE | When requests are hitting some other url than PML API endpoint |
| PM-0002 | FAILURE | When PML system is down |
| PM-0003 | FAILURE | When network issues occur before hitting PML API |
| PM-0004 | FAILURE | If there is an error in Paytm MW service |
| PM-0005 | FAILURE | Internal Error PML API response is null |
| PM-0006 | FAILURE | When the wrong product is sent in order request payload |

### Notes

> Note: In case your order is rejected or if you receive an error code, please review your order book first and then try placing your order again.

---

## Modify Bracket Order

Source: https://developer.paytmmoney.com/docs/api/modify-bracket-order/

**Method:** `POST`  
**Endpoint:** `https://developer.paytmmoney.com/orders/v1/modify/bracket`  

### Description

> As long as an order **is open or pending** in the system, certain attributes of it **can be modified**.  
> Price, quantity, validity, product etc are some of the variables that can be modified by the user.  
> Bracket Order has 3 Legs and the Leg 2 & Leg 3 orders will have a Parent Order ID field indicating the "algo\_order\_no" of its parent order, that is, the Leg 1 order. This field may be required while modifying or canceling an open Leg 2 or Leg 3 order.

### Request Attributes

Content Type: JSON

#### Head

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `x-jwt-token` | string | optional | xxxxxx ( The one retrieved from Generate Access Token Steps ) . Can be accessed using: {access\_token} |

#### Body

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `source` | string | optional | Source from which the order is placed Website - W, mWeb - M, Android - N, iOS - I, Exe - R, OperatorWorkStation - O |
| `txn_type` | string | optional | The type of transaction that is being executed (Buy / Sell) |
| `exchange` | string | optional | The exchange which is involved for this specific transaction ( NSE/BSE ) |
| `segment` | string | optional | This describes, to which segment the transaction belongs. (E→ Equity Cash / D→ Equity Derivative) |
| `product` | string | optional | Type of product (C/I/B/V/M) C ((Cash and Carry / Delivery) Valid only for Segment='E'), I (Intraday (Valid for Segment= E/D)), M (Margin (Valid for Segment='D')) B (Bracket order (Valid for Segment= E/D)), V (Cover Order (Valid for Segment= E/D)), |
| `security_id` | string | optional | security\_id of scrip in NSE / BSE |
| `quantity` | string | optional | Quantity of stocks to be traded in NSE / BSE |
| `validity` | string | optional | Validity of the Order, Day/IOC/GTC/GTD DAY - valid for day only IOC - Immediate or cancel, GTC - good till cancel, GTD - good till date |
| `order_type` | string | optional | LMT - Limit order (order is to be traded at mentioned price). ~~MKT - Market order (order is to be traded at market price).~~ Market orders are not supported as an explicit order type. Use LIMIT orders (LMT). SL - Stop loss Limit (trigger which goes into trigger state when market reaches mentioned trigger price). SLM- Stop Loss Market. |
| `price` | string | optional | Price at which order is to be placed |
| `trigger_price` | string | optional | Price at which stop loss is to be triggered (mandatory if it is stop loss order) |
| `off_mkt_flag` | string | optional | Boolean Value, default is false Set False for Live Order Set True for AMO (After Market Order) |
| `mkt_type` | string | optional | NL/OL/AU/SP/A1/A2 Default is NL- normal |
| `order_no` | string | optional | PML specific order\_no. |
| `serial_no` | string | optional | Serial number specific to PML. This is updated on every order updation |
| `group_id` | string | optional | Group\_id specific to PML |
| `leg_no` | string | optional | Leg number for multi leg orders like BO, CO |
| `algo_order_no` | string | optional | Order No. of Bracket Order 1st Leg in case of 2nd/3rd leg of BO. "-1" in case Bracket Order 1st Leg. 0 is default |
| `order_ltp` | double | optional | The order\_ltp field should be populated with the last traded price of the security for which the order is being placed. This helps in selecting the appropriate market price protection. |
| `ext_info` | object | optional | The ext\_info field, available in the Order Book or Postback API response, must be passed back unchanged when canceling, exiting, or modifying orders. This JSON object ensures seamless execution and supports future enhancements. |

### Response Attributes

Content Type: JSON

#### Body

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `status` | string | optional | Describes whether the API request was Success/Failure |
| `message` | string | optional | Message to be displayed in the frontend |
| `oms_error_code` | string | optional | OMS specific error codes |
| `order_no` | string | optional | PML specific order\_no. |
| `error_code` | string | optional | Internal exception specific codes |

### Code Samples

#### CURL

```bash
curl --location --request POST 'https://developer.paytmmoney.com/orders/v1/modify/bracket' \
--header 'x-jwt-token: {{JWT-TOKEN}}' \
--header 'Content-Type: application/json' \
--data-raw '{
  "source": "N",
  "txn_type": "S",
  "exchange": "NSE",
  "segment": "E",
  "product": "B",
  "security_id": "2885",
  "quantity": 5,
  "price": 0,
  "trigger_price": 1515,
  "validity": "DAY",
  "order_type": "SLM",
  "off_mkt_flag": "false",
  "mkt_type": "NL",
  "order_no": "212001022501",
  "serial_no": "1",
  "group_id": "2",
  "leg_no": "2",
  "algo_order_no": "212001022135",
  "order_ltp": 0.0,
  "ext_info": {
    "total_qty": 10,
    "rem_qty": 10,
    "algo_order_no": "202503032025"
  }
}'
```

### Sample Responses

#### SUCCESS

```json
{
"status": "success",
"message": "Order Modification request submitted successfully. Your Order Ref No. 11906214401",
"data": [
{
"oms_error_code":"12345",
"order_no": "11905188861"
}
],
"error_code": "RS-0023"
}
```

### Possible Response Status

| Code | Status | Message |
| --- | --- | --- |
| PM-0001 | FAILURE | When requests are hitting some other url than PML API endpoint |
| PM-0002 | FAILURE | When PML system is down |
| PM-0003 | FAILURE | When network issues occur before hitting PML API |
| PM-0004 | FAILURE | If there is an error in Paytm MW service |
| PM-0005 | FAILURE | Internal Error PML API response is null |
| PM-0006 | FAILURE | When the wrong product is sent in order request payload |

### Notes

> Note: In case your order is rejected or if you receive an error code, please review your order book first and then try placing your order again.

---

## Exit Bracket Order

Source: https://developer.paytmmoney.com/docs/api/exit-bracket-order/

**Method:** `POST`  
**Endpoint:** `https://developer.paytmmoney.com/orders/v1/exit/bracket`  

### Description

> One can Exit the Bracket order by exiting any of **Leg 2 & Leg 3** order.  
> The position is exited when the Leg 2 or Leg 3 order is executed or canceled.

### Request Attributes

Content Type: JSON

#### Head

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `x-jwt-token` | string | optional | xxxxxx ( The one retrieved from Generate Access Token Steps ) . Can be accessed using: {access\_token} |

#### Body

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `source` | string | optional | Source from which the order is placed Website - W, mWeb - M, Android - N, iOS - I, Exe - R, OperatorWorkStation - O |
| `txn_type` | string | optional | The type of transaction that is being executed (Buy / Sell) |
| `exchange` | string | optional | The exchange which is involved for this specific transaction ( NSE/BSE ) |
| `segment` | string | optional | This describes, to which segment the transaction belongs. (E→ Equity Cash / D→ Equity Derivative) |
| `product` | string | optional | Type of product (C/I/B/V/M) C ((Cash and Carry / Delivery) Valid only for Segment='E'), I (Intraday (Valid for Segment= E/D)), M (Margin (Valid for Segment='D')) B (Bracket order (Valid for Segment= E/D)), V (Cover Order (Valid for Segment= E/D)), |
| `security_id` | string | optional | security\_id of scrip in NSE / BSE |
| `quantity` | string | optional | Quantity of stocks to be traded in NSE / BSE |
| `validity` | string | optional | Validity of the Order, Day/IOC/GTC/GTD DAY - valid for day only IOC - Immediate or cancel, GTC - good till cancel, GTD - good till date |
| `order_type` | string | optional | LMT - Limit order (order is to be traded at mentioned price). ~~MKT - Market order (order is to be traded at market price).~~ Market orders are not supported as an explicit order type. Use LIMIT orders (LMT). SL - Stop loss Limit (trigger which goes into trigger state when market reaches mentioned trigger price). SLM- Stop Loss Market. |
| `price` | string | optional | Price at which order is to be placed |
| `trigger_price` | string | optional | Price at which stop loss is to be triggered (mandatory if it is stop loss order) |
| `off_mkt_flag` | string | optional | Boolean Value, default is false Set False for Live Order Set True for AMO (After Market Order) |
| `mkt_type` | string | optional | NL/OL/AU/SP/A1/A2 Default is NL- normal |
| `order_no` | string | optional | PML specific order\_no. |
| `serial_no` | string | optional | Serial number specific to PML. This is updated on every order updation |
| `group_id` | string | optional | Group\_id specific to PML |
| `leg_no` | string | optional | Leg number for multi leg orders like BO, CO |
| `algo_order_no` | string | optional | Order No. of Bracket Order 1st Leg in case of 2nd/3rd leg of BO. "-1" in case Bracket Order 1st Leg. 0 is default |
| `ext_info` | object | optional | The ext\_info field, available in the Order Book or Postback API response, must be passed back unchanged when canceling, exiting, or modifying orders. This JSON object ensures seamless execution and supports future enhancements. |

### Response Attributes

Content Type: JSON

#### Body

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `status` | string | optional | Describes whether the API request was Success/Failure |
| `message` | string | optional | Message to be displayed in the frontend |
| `oms_error_code` | string | optional | OMS specific error codes |
| `order_no` | string | optional | PML specific order\_no. |
| `error_code` | string | optional | Internal exception specific codes |

### Code Samples

#### CURL

```bash
curl --location --request POST 'https://developer.paytmmoney.com/orders/v1/exit/bracket' \
--header 'x-jwt-token: {{JWT-TOKEN}}' \
--header 'Content-Type: application/json' \
--data-raw '{
  "source": "N",
  "txn_type": "S",
  "exchange": "BSE",
  "segment": "E",
  "product": "B",
  "security_id": "500325",
  "quantity": 5,
  "price": 1575,
  "validity": "DAY",
  "order_type": "LMT",
  "off_mkt_flag": "false",
  "mkt_type": "NL",
  "order_no": "112001032241",
  "serial_no": "1",
  "group_id": "1",
  "leg_no": "3",
  "algo_order_no": "1120010311912",
  "ext_info": {
    "total_qty": 10,
    "rem_qty": 10,
    "algo_order_no": "202503032025"
  }
}'
```

### Possible Response Status

| Code | Status | Message |
| --- | --- | --- |
| PM-0001 | FAILURE | When requests are hitting some other url than PML API endpoint |
| PM-0002 | FAILURE | When PML system is down |
| PM-0003 | FAILURE | When network issues occur before hitting PML API |
| PM-0004 | FAILURE | If there is an error in Paytm MW service |
| PM-0005 | FAILURE | Internal Error PML API response is null |
| PM-0006 | FAILURE | When the wrong product is sent in order request payload |

### Notes

> Note: In case your order is rejected or if you receive an error code, please review your order book first and then try placing your order again.

---

## Order Book API - Filter by API Key

Source: https://developer.paytmmoney.com/docs/api/order-book-api-filter-by-api-key/

**Method:** `GET`  
**Endpoint:** `https://developer.paytmmoney.com/orders/v1/order-book`  

### Description

> Order Book API (Filter by API Key) lets users **retrieve all orders** requested in a day with their last updated status.  
> This API will give the logged in users orders for the **specific merchant (platform ) only**.  
>   
> For example, Order 1 & 2 are placed from Paytm Mobile App and Order 3 & 4 are placed from your custom application. In this case you will get order details for order 3 and 4 only.

### Request Attributes

Content Type: JSON

#### Head

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `x-jwt-token` | string | mandatory | xxxxxx ( The one retrieved from Generate Access Token Steps ) . Can be accessed using: {access\_token} or {read\_access\_token} . |

### Response Attributes

Content Type: JSON

#### Body

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `client_id` | string | optional | Unique customer identification number by PML |
| `txn_type` | string | optional | The type of transaction that is being executed (Buy / Sell) |
| `exchange` | string | optional | The exchange which is involved for this specific transaction ( NSE/BSE ) |
| `segment` | string | optional | This describes, to which segment the transaction belongs. (E→ Equity Cash / D→ Equity Derivative) |
| `product` | string | optional | Type of product (C/I/B/V/M) C ((Cash and Carry / Delivery) Valid only for Segment='E'), I (Intraday (Valid for Segment= E/D)), M (Margin (Valid for Segment='D')) B (Bracket order (Valid for Segment= E/D)), V (Cover Order (Valid for Segment= E/D)), |
| `security_id` | string | optional | security\_id of scrip in NSE / BSE |
| `quantity` | string | optional | Quantity of stocks to be traded in NSE / BSE |
| `validity` | string | optional | Validity of the Order, Day/IOC/GTC/GTD DAY - valid for day only IOC - Immediate or cancel, GTC - good till cancel, GTD - good till date |
| `order_type` | string | optional | LMT - Limit order (order is to be traded at mentioned price). ~~MKT - Market order (order is to be traded at market price).~~ Market orders are not supported as an explicit order type. Use LIMIT orders (LMT). SL - Stop loss Limit (trigger which goes into trigger state when market reaches mentioned trigger price). SLM- Stop Loss Market. |
| `price` | string | optional | Price at which order is to be placed |
| `off_mkt_flag` | string | optional | Boolean Value, default is false Set False for Live Order Set True for AMO (After Market Order) |
| `mkt_type` | string | optional | NL/OL/AU/SP/A1/A2 Default is NL- normal |
| `order_no` | string | optional | PML specific order\_no. |
| `serial_no` | string | optional | Serial number specific to PML. This is updated on every order updation |
| `group_id` | string | optional | Group\_id specific to PML |
| `leg_no` | string | optional | Leg number for multi leg orders like BO, CO |
| `algo_order_no` | string | optional | Order No. of Bracket Order 1st Leg in case of 2nd/3rd leg of BO. "-1" in case Bracket Order 1st Leg. 0 is default |
| `trigger_price` | string | optional | Price at which stop loss is to be triggered (mandatory if it is stop loss order) |
| `status` | string | optional | Describes whether the API request was Success/Failure |
| `exch_order_no` | string | optional | Exchange Order Number |
| `exch_order_time` | string | optional | Exchange Order Time |
| `traded_qty` | string | optional | Quantity of stocks traded in NSE / BSE |
| `remaining_quantity` | string | optional | Quantities yet to be traded out of the ordered quantities |
| `avg_traded_price` | string | optional | Average price at which security got traded |
| `reason_description` | string | optional | Reason behind the current status of the order |
| `pr_abstick_value` | string | optional | Profit Price |
| `sl_abstick_value` | string | optional | Stop Loss Price |
| `isin` | string | optional | The International Securities Identification Number is a code that uniquely identifies a specific security |
| `display_name` | string | optional | Custom Symbol Name |
| `order_date_time` | string | optional | Date and time at which order is placed |
| `last_updated_time` | string | optional | Recent date and time at which order got updated |
| `child_leg_unq_id` | string | optional | Unique ID of the Child Leg |
| `ref_ltp` | string | optional | Reference LTP |
| `display_status` | string | optional | Current status of the order by PML |
| `display_product` | string | optional | Full name of the product |
| `display_order_type` | string | optional | Full name of the product type |
| `display_validity` | string | optional | Fill name of the validity type |
| `error_code` | string | optional | Internal exception specific codes |
| `tick_size` | string | optional | Minimum price change between different bid and offer prices of an asset traded on an exchange platform |
| `strategy_id` | string | optional | Unique Id linked to particular strategy |
| `placed_by` | string | optional | Displays the Order is Placed By whom? |
| `lot_size` | string | optional | The no of contracts in a derivative security |
| `strike_price` | string | optional | Strike Price of option at which it is to be bought/sold |
| `expiry_date` | string | optional | The expiry date of an option is the date at which option expires |
| `opt_type` | string | optional | Option Type: Call/Put |
| `instrument` | string | optional | EQUITY(Cash)/FUTSTK/OPTSTK |
| `channel` | string | optional | MER\_226 is the merchant id (ex- Algomatrix) |
| `Platform` | string | optional | Placed via Open api |
| `instrument_type` | string | optional | Script Type like ES= Equity Stock ETF= Exchange Traded Fund FUTIDX= Future Index FUTSTK= Future Stock OPTIDX= Option Index OPTSTK= Option Stock |
| `ext_info` | object | optional | The ext\_info field, available in the Order Book or Postback API response, must be passed back unchanged when canceling, exiting, or modifying orders. This JSON object ensures seamless execution and supports future enhancements. |

### Code Samples

#### CURL

```bash
curl --location --request GET 'https://developer.paytmmoney.com/orders/v1/order-book' \
--header 'x-jwt-token: {{JWT-TOKEN}}'
```

### Sample Responses

#### SUCCESS

```json
{
   "status": "success",
   "message": "",
   "data": [
       {
           "client_id": "22820439",
           "txn_type": "B",
           "exchange": "NSE",
           "segment": "E",
           "product": "B",
           "security_id": "371",
           "quantity": 100,
           "validity": "DAY",
           "order_type": "MKT",
           "price": 0.0,
           "off_mkt_flag": "false",
           "mkt_type": "NL",
           "order_no": "812201052041",
           "serial_no": 3,
           "group_id": 8,
           "leg_no": "1",
           "algo_ord_no": "-1",
           "trigger_price": 0.0,
           "status": "Cancelled",
           "exch_order_no": "1000000000002830",
           "exch_order_time": "2022-01-05 11:35:21",
           "traded_qty": 0,
           "remaining_quantity": 0,
           "avg_traded_price": 0.0,
           "reason_description": "CONFIRMED",
           "pr_abstick_value": "0.0000",
           "sl_abstick_value": "0.0000",
           "isin": "INE176A01028",
           "display_name": "Bata",
           "order_date_time": "2022-01-05 11:35:21",
           "last_updated_time": "2022-01-05 11:35:21",
           "child_leg_unq_id": 0,
           "ref_ltp": 1812.9,
           "display_status": "Cancelled",
           "display_product": "Bracket Order",
           "display_order_type": "Market",
           "display_validity": "Day",
           "error_code": "0",
           "tick_size": 5.00000,
           "strategy_id": "NA",
           "placed_by": "CUSTOMER",
           "lot_size": 1,
           "strike_price": 0.0,
           "expiry_date": "0001-01-01",
           "opt_type": "XX",
           "instrument": "EQUITY",
           "platform": "Open-api",
           "channel": "MER_226",
           “instrument_type”: “ES”,
            "ext_info": {
              "total_qty": 10,
              "rem_qty": 10,
              "algo_order_no": "202503032025"
            }
       }
   ]
}
```

---

## Order Book API - All Orders

Source: https://developer.paytmmoney.com/docs/api/order-book-all-orders/

**Method:** `GET`  
**Endpoint:** `https://developer.paytmmoney.com/orders/v1/user/orders`  

### Description

> Order Book API (All Orders) lets users **retrieve all the orders** requested in a day by a specific user across all the-platforms with their last updated status.  
>   
> For example, Order 1 & 2 are placed from Paytm Mobile App and Order 3 & 4 are placed from your custom application. Whenever you try to retrieve orders from your custom application, you get the update for all the 4 orders placed across all the platforms.

### Request Attributes

Content Type: JSON

#### Head

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `x-jwt-token` | string | mandatory | xxxxxx ( The one retrieved from Generate Access Token Steps ) . Can be accessed using: {access\_token} or {read\_access\_token} . |

### Response Attributes

Content Type: JSON

#### Body

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `client_id` | string | optional | Unique customer identification number by PML |
| `txn_type` | string | optional | The type of transaction that is being executed (Buy / Sell) |
| `exchange` | string | optional | The exchange which is involved for this specific transaction ( NSE/BSE ) |
| `segment` | string | optional | This describes, to which segment the transaction belongs. (E→ Equity Cash / D→ Equity Derivative) |
| `product` | string | optional | Type of product (C/I/B/V/M) C ((Cash and Carry / Delivery) Valid only for Segment='E'), I (Intraday (Valid for Segment= E/D)), M (Margin (Valid for Segment='D')) B (Bracket order (Valid for Segment= E/D)), V (Cover Order (Valid for Segment= E/D)), |
| `security_id` | string | optional | security\_id of scrip in NSE / BSE |
| `quantity` | string | optional | Quantity of stocks to be traded in NSE / BSE |
| `validity` | string | optional | Validity of the Order, Day/IOC/GTC/GTD DAY - valid for day only IOC - Immediate or cancel, GTC - good till cancel, GTD - good till date |
| `order_type` | string | optional | LMT - Limit order (order is to be traded at mentioned price). ~~MKT - Market order (order is to be traded at market price).~~ Market orders are not supported as an explicit order type. Use LIMIT orders (LMT). SL - Stop loss Limit (trigger which goes into trigger state when market reaches mentioned trigger price). SLM- Stop Loss Market. |
| `price` | string | optional | Price at which order is to be placed |
| `off_mkt_flag` | string | optional | Boolean Value, default is false Set False for Live Order Set True for AMO (After Market Order) |
| `mkt_type` | string | optional | NL/OL/AU/SP/A1/A2 Default is NL- normal |
| `order_no` | string | optional | PML specific order\_no. |
| `serial_no` | string | optional | Serial number specific to PML. This is updated on every order updation |
| `group_id` | string | optional | Group\_id specific to PML |
| `leg_no` | string | optional | Leg number for multi leg orders like BO, CO |
| `algo_order_no` | string | optional | Order No. of Bracket Order 1st Leg in case of 2nd/3rd leg of BO. "-1" in case Bracket Order 1st Leg. 0 is default |
| `trigger_price` | string | optional | Price at which stop loss is to be triggered (mandatory if it is stop loss order) |
| `status` | string | optional | Describes whether the API request was Success/Failure |
| `exch_order_no` | string | optional | Exchange Order Number |
| `exch_order_time` | string | optional | Exchange Order Time |
| `traded_qty` | string | optional | Quantity of stocks traded in NSE / BSE |
| `remaining_quantity` | string | optional | Quantities yet to be traded out of the ordered quantities |
| `avg_traded_price` | string | optional | Average price at which security got traded |
| `reason_description` | string | optional | Reason behind the current status of the order |
| `pr_abstick_value` | string | optional | Profit Price |
| `sl_abstick_value` | string | optional | Stop Loss Price |
| `isin` | string | optional | The International Securities Identification Number is a code that uniquely identifies a specific security |
| `display_name` | string | optional | Custom Symbol Name |
| `order_date_time` | string | optional | Date and time at which order is placed |
| `last_updated_time` | string | optional | Recent date and time at which order got updated |
| `child_leg_unq_id` | string | optional | Unique ID of the Child Leg |
| `ref_ltp` | string | optional | Reference LTP |
| `display_status` | string | optional | Current status of the order by PML |
| `display_product` | string | optional | Full name of the product |
| `display_order_type` | string | optional | Full name of the product type |
| `display_validity` | string | optional | Fill name of the validity type |
| `error_code` | string | optional | Internal exception specific codes |
| `tick_size` | string | optional | Minimum price change between different bid and offer prices of an asset traded on an exchange platform |
| `strategy_id` | string | optional | Unique Id linked to particular strategy |
| `placed_by` | string | optional | Displays the Order is Placed By whom? |
| `lot_size` | string | optional | The no of contracts in a derivative security |
| `strike_price` | string | optional | Strike Price of option at which it is to be bought/sold |
| `expiry_date` | string | optional | The expiry date of an option is the date at which option expires |
| `opt_type` | string | optional | Option Type: Call/Put |
| `instrument` | string | optional | EQUITY(Cash)/FUTSTK/OPTSTK |
| `channel` | string | optional | MER\_226 is the merchant id (ex- Algomatrix) |
| `Platform` | string | optional | Placed via Open api |
| `instrument_type` | string | optional | Script Type like ES= Equity Stock ETF= Exchange Traded Fund FUTIDX= Future Index FUTSTK= Future Stock OPTIDX= Option Index OPTSTK= Option Stock |
| `ext_info` | object | optional | The ext\_info field, available in the Order Book or Postback API response, must be passed back unchanged when canceling, exiting, or modifying orders. This JSON object ensures seamless execution and supports future enhancements. |

### Code Samples

#### CURL

```bash
curl --location --request GET 'https://developer.paytmmoney.com/orders/v1/user/orders' \
--header 'x-jwt-token: {{JWT-TOKEN}}'
```

### Sample Responses

#### SUCCESS

```json
{
    "status": "success",
    "message": "",
    "data": [
        {
            "client_id": "22820439",
            "txn_type": "B",
            "exchange": "NSE",
            "segment": "D",
            "product": "M",
            "security_id": "42348",
            "quantity": 50,
            "validity": "DAY",
            "order_type": "MKT",
            "price": 0.0,
            "off_mkt_flag": "true",
            "mkt_type": "NL",
            "order_no": "152301319082",
            "serial_no": 1,
            "group_id": 1,
            "leg_no": "1",
            "algo_ord_no": "0",
            "trigger_price": 0.0,
            "status": "O-Pending",
            "exch_order_no": "0",
            "exch_order_time": "0001-01-01 00:00:00",
            "traded_qty": 0,
            "remaining_quantity": 50,
            "avg_traded_price": 0.0,
            "reason_description": "",
            "pr_abstick_value": "0.0000",
            "sl_abstick_value": "0.0000",
            "isin": "NA",
            "display_name": "NIFTY 02 FEB 17650 PUT",
            "order_date_time": "2023-01-31 18:17:25",
            "last_updated_time": "2023-01-31 18:17:25",
            "child_leg_unq_id": 0,
            "ref_ltp": 115.7,
            "display_status": "Pending",
            "display_product": "Overnight",
            "display_order_type": "Market",
            "display_validity": "Day",
            "error_code": "0",
            "tick_size": 5.00000,
            "strategy_id": "NA",
            "placed_by": "CUSTOMER",
            "lot_size": 50,
            "strike_price": 17650.0,
            "expiry_date": "2023-02-02",
            "opt_type": "PE",
            "instrument": "OPTIDX",
            "platform": "web",
            "channel": null,
            "instrument_type": "OPTIDX",
            "tag_type": "BA",
            "algo_module": null,
            "tag_id": "2035",
            "ext_info": {
              "total_qty": 10,
              "rem_qty": 10,
              "algo_order_no": "202503032025"
            }
        }
   ]
}
```

---

## Trade Book API

Source: https://developer.paytmmoney.com/docs/api/trade-book-api/

**Method:** `GET`  
**Endpoint:** `https://developer.paytmmoney.com/orders/v1/trade-details?order_no=122010213024&leg_no=1&segment=D`  

### Description

> Trade Book API helps to **fetch details** of all trades that are executed in a day.

### Request Attributes

Content Type: JSON

#### Head

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `x-jwt-token` | string | mandatory | xxxxxx ( The one retrieved from Generate Access Token Steps ) . Can be accessed using: {access\_token} or {read\_access\_token} . |

#### Body

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `order_no` | string | optional | PML specific order\_no. |
| `segment` | string | optional | This describes, to which segment the transaction belongs. (E→ Equity Cash / D→ Equity Derivative) |
| `leg_no` | string | optional | Leg number for multi leg orders like BO, CO |

### Response Attributes

Content Type: JSON

#### Body

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `client_id` | string | optional | Unique customer identification number by PML |
| `trade_no` | string | optional | Trade Number |
| `quantity` | string | optional | Quantity of stocks to be traded in NSE / BSE |
| `traded_price` | string | optional | Trade Price |
| `exch_trade_time` | string | optional | Exchange Trade Time |
| `exch_order_no` | string | optional | Exchange Order Number |
| `exch_order_time` | string | optional | Exchange Order Time |

### Code Samples

#### CURL

```bash
curl --location --request GET 'https://developer.paytmmoney.com/orders/v1/trade-details?order_no=122010213024&leg_no=1&segment=D' \
--header 'x-jwt-token: {{JWT-TOKEN}}'
```

### Sample Responses

#### SUCCESS

```json
{
"status": "success",
"message": "",
{
"status": "success",
"message": "",
"data": [
{
"client_id": "1194654",
"trade_no": "123800",
"quantity": 50,
"traded_price": 141.95,
"exch_trade_time": "31-07-2019 14:55:00",
"exch_order_no": "1564550760487001000",
"exch_order_time": "31-07-2019 14:55:00"
}
]
}
```

### Notes

### Query Parameters

| Attribute | Description |
| --- | --- |
| order\_no  string  mandatory | Order number specific to PML |
| segment  string  mandatory | This describes, to which segment the transaction belongs. (E→ Equity Cash / D→ Equity Derivative) |
| leg\_no  string  mandatory | Leg number for multi leg orders like BO, CO. |

---

## Charges

Source: https://developer.paytmmoney.com/docs/api/charges/

**Method:** `POST`  
**Endpoint:** `https://developer.paytmmoney.com/accounts/v1/charges/info`  

### Description

> Brokerage, Statutory & Regulatory charges to be levied for each order

### Request Attributes

Content Type: JSON

#### Head

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `x-jwt-token` | string | mandatory | xxxxxx ( The one retrieved from Generate Access Token Steps ) . Can be accessed using: {access\_token} |

#### Body

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `brokerage_profile_code` | string | mandatory | Customer subscription plan ("D00-I10-F10" / "D15-I15-F15") |
| `transaction_type` | string | mandatory | The type of transaction that is being executed (Buy / Sell) |
| `instrument_type` | string | optional | Script Type like ES= Equity Stock ETF= Exchange Traded Fund FUTIDX= Future Index FUTSTK= Future Stock OPTIDX= Option Index OPTSTK= Option Stock |
| `product_type` | string | optional | Type of product are C/M C=Cash and Carry / Delivery. This is Valid only for Segment='E' (Equity), M=Margin or Overnight Carry Forward. This is Valid only for Segment='D' (Derivatives), |
| `exchange` | string | mandatory | The exchange which is involved for this specific transaction ( NSE/BSE ) |
| `qty` | string | mandatory | Quantity of stocks to be traded in NSE / BSE |
| `price` | string | mandatory | Price at which order is to be placed |

### Response Attributes

Content Type: JSON

#### Body

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `PaytmMoney Brokerage` | string | mandatory | Rs 10 per executed order (Based on the subscription plan) |
| `Exchange Turnover Charges` | string | mandatory | qty \* price = Total \* 0.0000345 (Based on the tariff API response) |
| `SEBI Turnover Fees` | string | mandatory | qty \* price = Total \* 0.0010% (Based on the tariff API response) |
| `Stamp Duty` | string | mandatory | qty \* price = Total \* 0.015% (Based on the tariff API response) |
| `DP charges` | string | mandatory | Rs 10 per executed order (Based on the API response) |
| `Security Transaction Charges (STT)	` | string | mandatory | qty \* price = Total \* 0.001% (Based on the tariff API response) |
| `GST` | string | mandatory | 18% on (Brokerage + Exchange Turnover charges) (Based on the tariff API response) |
| `Total` | string | mandatory | PaytmMoney Brokerage+Exchange Turnover Charges+SEBI Turnover Fees+Stamp Duty+DP charges Security Transaction Charges (STT)+GST |

### Code Samples

#### CURL

```bash
curl --location 'https://developer.paytmmoney.com/accounts/v1/charges/info' \
--header 'x-jwt-token: {{JWT-TOKEN}}' \
--header 'Content-Type: application/json' \
--data '{
    "brokerage_profile_code": "D00-I10-F10",
    "transaction_type": "B", 
    "product_type": "C",
    "instrument_type": "ETF",
    "exchange": "NSE",
    "qty": 2,
    "price": 100
}'
```

### Sample Responses

#### SUCCESS

```json
{
  "data": {
    "sections": [
      {
        "title": "Paytm Money Brokerage",
        "total": 0.01,
        "items": null
      },      
      {
        "title": "Other Charges",
        "total": 0.14,
        "items": [
            {
              "header": "Exchange Turnover Charges",
              "formula": "0.00345% of turnover",
              "value":  0.17
            },
            {
              "header": "SEBI Turnover Fees",
              "formula": "0.0001% of turnover",
              "value": 0.01
            },
            {
              "header": "Stamp Duty",
              "formula": "0.015% of turnover",
              "value": 0.75
            },
            {
              "header": "DP charges",
              "formula": "Rs 10 per executed order",
              "value": 10
            }
          ]
      },
      {
        "title": "Taxes",
        "total": 5.03,
        "items": [
          {
            "header": "GST",
            "formula": "18% on Brokerage, SEBI and Exchange Turnover Charges",
            "value": 0.03
          },
          {
            "header": "Security Transaction Tax (STT)",
            "formula": "0.1% of turnover ",
            "value": 5.00
          }
        ]
      }
    ],
    "auto_sq_off": 0.03,
    "total": 0.99
  },
  "meta": {
    "code": "",
    "message": "",
    "displayMessage": ""
  }
}
```
