# Margin calculator

- [Scripts Margin Calculator](#scripts-margin-calculator)
- [Order Margin Calculator](#order-margin-calculator)

## Scripts Margin Calculator

Source: https://developer.paytmmoney.com/docs/api/scripts-margin-calculator/

**Method:** `POST`  
**Endpoint:** `https://developer.paytmmoney.com/margin/v1/scrips/calculator`  

### Description

> Margin Calculator API lets you **calculate required margin** for multiple orders/scripts.  
> This gives you SPAN, EXPOSURE MARGIN, OPTION PREMIUM, TOTAL MARGIN and MARGIN BENEFIT values for multiple orders/Scripts.

### Request Attributes

Content Type: JSON

#### Head

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `x-jwt-token` | string | optional | xxxxxx ( The one retrieved from Generate Access Token Steps ) . Can be accessed using: {access\_token} or {read\_access\_token} . |

### Response Attributes

Content Type: JSON

#### Body

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `source` | string | optional | Source from which the order is placed Website - W, mWeb - M, Android - N, iOS - I, Exe - R, OperatorWorkStation - O |
| `exchange` | string | optional | The exchange which is involved for this specific transaction ( NSE/BSE ) |
| `segment` | string | optional | This describes, to which segment the transaction belongs. (E→ Equity Cash / D→ Equity Derivative) |
| `security_id` | string | optional | security\_id of scrip in NSE / BSE |
| `txn_type` | string | optional | The type of transaction that is being executed (Buy / Sell) |
| `quantity` | string | optional | Quantity of stocks to be traded in NSE / BSE |
| `strike_price` | string | optional | Strike Price of option at which it is to be bought/sold |
| `trigger_price` | string | optional | Price at which stop loss is to be triggered (mandatory if it is stop loss order) |
| `instrument` | string | optional | EQUITY(Cash)/FUTSTK/OPTSTK |

### Code Samples

#### CURL

```bash
curl --location --request POST 'https://developer.paytmmoney.com/margin/v1/scrips/calculator' \
--header 'x-jwt-token: {{JWT-TOKEN}}' \
--header 'Content-Type: application/json' \
--data-raw '{
   "source":"N",
   "margin_list":[
      {
         "exchange":"NSE",
         "segment":"D",
         "security_id":"46840",
         "txn_type":"B",
         "quantity":"250",
         "strike_price":"0",
         "trigger_price":"0",
         "instrument":"FUTSTK"
      },
      {
         "exchange":"NSE",
         "segment":"D",
         "security_id":"46834",
         "txn_type":"B",
         "quantity":"250",
         "strike_price":"0",
         "trigger_price":"0",
         "instrument":"FUTSTK"
      },
      {
         "exchange":"NSE",
         "segment":"E",
         "security_id":"27466",
         "txn_type":"B",
         "quantity":"25",
         "strike_price":"0",
         "trigger_price":"0",
         "instrument":"EQUITY"
      }
   ]
}'
```

### Sample Responses

#### SUCCESS

```json
{
  "source": "N",
  "margin_list": [
    {
      "exchange": "NSE",
      "segment": "D",
      "security_id": "46840",
      "txn_type": "B",
      "quantity": "250",
      "strike_price": "0",
      "trigger_price": "0",
      "instrument": "FUTSTK"
    },
    {
      "exchange": "NSE",
      "segment": "D",
      "security_id": "46834",
      "txn_type": "B",
      "quantity": "250",
      "strike_price": "0",
      "trigger_price": "0",
      "instrument": "FUTSTK"
    },
    {
      "exchange": "NSE",
      "segment": "E",
      "security_id": "27466",
      "txn_type": "B",
      "quantity": "25",
      "strike_price": "0",
      "trigger_price": "0",
      "instrument": "EQUITY"
    }
  ]
}
```

---

## Order Margin Calculator

Source: https://developer.paytmmoney.com/docs/api/order-margin-calculator/

**Method:** `GET`  
**Endpoint:** `https://developer.paytmmoney.com/margin/v1/order/calculator?source=N&exchange=NSE&segment=E&security_id=2885&txn_type=B&quantity=2700&price=0&product=I&trigger_price=0`  

### Description

> Margin Calculator API lets you **calculate required margin** for multiple orders/scripts.  
> This gives you SPAN, EXPOSURE MARGIN, OPTION PREMIUM, TOTAL MARGIN and MARGIN BENEFIT values for multiple orders/Scripts.  
> Calculates margins for each order considering the existing positions and open orders Prev of order before placing.

### Request Attributes

Content Type: JSON

#### Head

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `x-jwt-token` | string | optional | xxxxxx ( The one retrieved from Generate Access Token Steps ) . Can be accessed using: {access\_token} or {read\_access\_token} . |

#### Body

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `source` | string | optional | Source from which the order is placed Website - W, mWeb - M, Android - N, iOS - I, Exe - R, OperatorWorkStation - O |
| `exchange` | string | optional | The exchange which is involved for this specific transaction ( NSE/BSE ) |
| `segment` | string | optional | This describes, to which segment the transaction belongs. (E→ Equity Cash / D→ Equity Derivative) |
| `security_id` | string | optional | security\_id of scrip in NSE / BSE |
| `txn_type` | string | optional | The type of transaction that is being executed (Buy / Sell) |
| `quantity` | string | optional | Quantity of stocks to be traded in NSE / BSE |
| `price` | string | optional | Price at which order is to be placed |
| `product` | string | optional | Type of product (C/I/B/V/M) C ((Cash and Carry / Delivery) Valid only for Segment='E'), I (Intraday (Valid for Segment= E/D)), M (Margin (Valid for Segment='D')) B (Bracket order (Valid for Segment= E/D)), V (Cover Order (Valid for Segment= E/D)), |
| `trigger_price` | string | optional | Price at which stop loss is to be triggered (mandatory if it is stop loss order) |

### Response Attributes

Content Type: JSON

#### Body

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `t_total_margin` | string | optional | Total Margin Block |
| `t_span_margin` | string | optional | SPAN Margin |
| `t_exposure_margin` | string | optional | Exposure Margin |
| `available_bal` | string | optional | Available Balance in the Account |
| `t_var_margin` | string | optional | VAR Margin |
| `insufficient_bal` | string | optional | Due Insufficient Balance |
| `brokerage` | string | optional | Brokerage Amount |
| `displayMessage` | string | optional | Message to be displayed |

### Code Samples

#### CURL

```bash
curl --location --request GET 'https://developer.paytmmoney.com/margin/v1/order/calculator?source=N&exchange=NSE&segment=E&security_id=2885&txn_type=B&quantity=2700&price=0&product=I&trigger_price=0' \
--header 'x-jwt-token: {{JWT-TOKEN}}'
```

### Sample Responses

#### SUCCESS

```json
{
    "data": {
        "t_total_margin": 1013437.66,
        "t_span_margin": 0.0,
        "t_exposure_margin": 0.0,
        "available_bal": 1.0E9,
        "t_var_margin": 1010407.04,
        "insufficient_bal": 0.0,
        "brokerage": 3030.62
    },
    "meta": {
        "displayMessage": "Order Margin response success"
    }
}
```

### Notes

### Query Parameters

| Attribute | Description |
| --- | --- |
| source  string  mandatory | Source from which the order is placed Website - W, mWeb - M, Android - N, iOS - I, Exe - R, OperatorWorkStation - O |
| segment  string  mandatory | This describes, to which segment the transaction belongs.(E→ Equity Cash / D→ Equity Derivative) |
| exchange  string  mandatory | The exchange which is involved for this specific transaction (National Stock Exchange / Bombay Stock Exchange) |
| security\_id  string  mandatory | security\_id of scrip in NSE / BSE |
| txn\_type  string  mandatory | The type of transaction that is being executed (Buy / Sell) |
| quantity  string  mandatory | Quantity of stocks to be traded in NSE / BSE |
| price  string  mandatory | Price at which order is to be placed |
| product  string  mandatory | TType of product (C/I/B/V/M) C ((Cash and Carry / Delivery) Valid only for Segment='E'), I (Intraday (Valid for Segment= E/D)), B (Bracket order (Valid for Segment= E/D)), V (CoverOrder (Valid for Segment= E/D)), M (Margin (Valid for Segment='D')) |
| trigger\_price  string  mandatory | Price at which stop loss is to be triggered (mandatory if it is stop loss order) |
