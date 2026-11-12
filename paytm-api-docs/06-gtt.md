# GTT

- [Create GTT](#create-gtt)
- [Update GTT API](#update-gtt-api)
- [Get All GTT](#get-all-gtt)
- [Get GTT By Status and User](#get-gtt-by-status-and-user)
- [Get GTT](#get-gtt)
- [Get GTT Aggregate](#get-gtt-aggregate)
- [Get GTT Expiry Date](#get-gtt-expiry-date)
- [Get GTT Instruction](#get-gtt-instruction)
- [Delete GTT API](#delete-gtt-api)

## Create GTT

Source: https://developer.paytmmoney.com/docs/api/create-gtt/

**Method:** `POST`  
**Endpoint:** `https://developer.paytmmoney.com/gtt/v2/gtt`  

### Description

> Place Single or One Cancels Other(OCO) GTT orders

### Request Attributes

Content Type: JSON

#### Head

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `x-jwt-token` | string | mandatory | xxxxxx ( The one retrieved from Generate Access Token Steps ) . Can be accessed using: {access\_token} |

#### Body

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `segment` | string | mandatory | This describes, to which segment the transaction belongs. (E→ Equity Cash / D→ Equity Derivative) |
| `exchange` | string | mandatory | The exchange which is involved for this specific transaction (National Stock Exchange / Bombay Stock Exchange) |
| `security_id` | string | mandatory | security\_id of scrip in NSE / BSE |
| `product_type` | string | mandatory | Type of product are C/M C=Cash and Carry / Delivery. This is Valid only for Segment='E' (Equity), M=Margin or Overnight Carry Forward. This is Valid only for Segment='D' (Derivatives) |
| `set_price` | string | mandatory | LTP at the time of GTT order creation |
| `transaction_type` | string | mandatory | The type of transaction that is being executed (Buy / Sell) |
| `transaction_details` | string | mandatory | The type of transaction that is being executed (Buy / Sell) |
| `quantity` | string | mandatory | Quantity of stocks to be traded in NSE / BSE |
| `trigger_price` | string | mandatory | Price at which GTT is to be triggered |
| `limit_price` | string | mandatory | User entered limit price, mandatory when order type is LIMIT |
| `order_type` | string | mandatory | LMT - Limit order (order is to be traded at mentioned price), MKT - market order (order is to be traded at market price). |
| `trigger_type` | string | mandatory | SINGLE/OCO |
| `sub type` | string | conditional | Applicable for SELL transaction type only. STOPLOSS/TARGET |

### Response Attributes

Content Type: JSON

#### Body

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | mandatory | GTT Order Id |
| `instruction_id` | string | optional | GTT Instruction Id |
| `segment` | string | optional | This describes, to which segment the transaction belongs. (E→ Equity Cash / D→ Equity Derivative) |
| `exchange` | string | optional | The exchange which is involved for this specific transaction (National Stock Exchange / Bombay Stock Exchange) |
| `security_id` | string | optional | security\_id of scrip in NSE / BSE |
| `pml_id` | string | optional | PML id of the stock |
| `name` | string | optional | Symbol Name |
| `user_id` | string | optional | Unique customer identification number by PML |
| `status` | string | optional | Status of the gtt (optional , Default values: [ACTIVE,TRIGGERED]) . Other possible values for status param can be "CREATED, DELETED, NOTIFIED, EXPIRED" |
| `transaction_type` | string | optional | The type of transaction that is being executed (Buy / Sell) |
| `sub_type` | string | optional | Applicable for SELL transaction type only. STOPLOSS/TARGET |
| `quantity` | string | optional | Quantity of stocks to be traded in NSE / BSE |
| `trigger_price` | string | optional | Price at which GTT is to be triggered |
| `limit_price` | string | optional | User entered limit price, mandatory when order type is LIMIT |
| `notification_ref_id` | string | optional | price alert id |
| `execution_ref_id` | string | optional | id of placed order for triggered gtt instruction |
| `triggered_at` | string | optional | time at which order triggered gtt instruction |
| `triggered_at_price` | string | optional | Price at which GTT instruction got triggered |
| `triggered_at_type` | string | optional | this represents transaction sub type (STOPLOSS/TARGET) |
| `set_price` | string | optional | LTP at the time of GTT order creation |
| `order_type` | string | optional | LMT - Limit order (order is to be traded at mentioned price), MKT - market order (order is to be traded at market price). |
| `trigger_type` | string | optional | SINGLE/OCO |
| `product_type` | string | optional | Type of product are C/M C=Cash and Carry / Delivery. This is Valid only for Segment='E' (Equity), M=Margin or Overnight Carry Forward. This is Valid only for Segment='D' (Derivatives) |
| `cancellation_code` | string | optional | GTT\_USER\_DELETE GTT\_EXPIRY\_JOB GTT\_CA\_BONUS GTT\_SYSTEM\_DELETE GTT\_SYSTEM\_REJECTION |
| `cancellation_reason` | string | optional | GTT\_USER\_DELETE GTT\_EXPIRY\_JOB GTT\_CA\_BONUS GTT\_SYSTEM\_DELETE GTT\_SYSTEM\_REJECTION |
| `expiry_date` | string | optional | date till when the gtt should be valid |
| `created_at` | string | optional | Order Creation date time |
| `updated_at` | string | optional | Order Updation date time |
| `deleted_at` | string | optional | Order Deletion date time |
| `request_metadata` | string | optional | stores value of x-user-agent header sent in create gtt request |
| `status` | string | optional | Status of the gtt (optional , Default values: [ACTIVE,TRIGGERED]) . Other possible values for status param can be "CREATED, DELETED, NOTIFIED, EXPIRED" |
| `displayMessage` | string | optional | Message to be displayed in the frontend |

### Code Samples

#### CURL

```bash
curl --location 'https://developer.paytmmoney.com/gtt/v2/gtt' \
--header 'x-jwt-token: {{JWT-TOKEN}}' \
--header 'Content-Type: application/json' \
--data '{
    "segment": "E",
    "exchange": "NSE",
    "security_id": "1270",
    "product_type": "C",
    "set_price": "581.0",
    "transaction_type": "S",
    "transaction_details": [
        {
            "sub_type": "STOPLOSS",     
            "quantity": "100",
            "trigger_price": "575.5",
            "limit_price": "0",
            "order_type": "MKT"
        },
        {
            "sub_type": "TARGET",
            "quantity": "100",
            "trigger_price": "583.0",
            "limit_price": "590.00",
            "order_type": "LMT"
        }
    ],
    "trigger_type": "OCO"
}'
```

### Sample Responses

#### SUCCESS

```json
{
    "data": {
        "id": 303,
        "instruction_id": "7t0i7V6Z6H1N6J",
        "segment": "E",
        "exchange": "NSE",
        "security_id": "1270",
        "pml_id": "1000002680",
        "name": "Ambuja Cements",
        "user_id": "1020044179",
        "transaction_type": "S",
        "transaction_details": [
            {
                "id": 304, //blank for single gtt
                "sub_type": "STOPLOSS", //blank for single gtt
                "quantity": 100,
                "trigger_price": 575.5,
                "set_price": 581.0,
                "limit_price": 0.0,
                "notification_ref_id": null,
                "execution_ref_id": null,
                "triggered_at": null,
                "triggered_at_price": null,
                "triggered_at_type": null,
                "order_type": "MKT",
                "status": "CREATED"
            },
            {
                "id": 305,
                "sub_type": "TARGET",
                "quantity": 100,
                "trigger_price": 583.0,
                "set_price": 581.0,
                "limit_price": 590.0,
                "notification_ref_id": null,
                "execution_ref_id": null,
                "triggered_at": null,
                "triggered_at_price": null,
                "triggered_at_type": null,
                "order_type": "LMT",
                "status": "CREATED"
            }
        ],
        "trigger_type": "OCO",
        "product_type": "C",
        "cancellation_code": null,
        "cancellation_reason": null,
        "expiry_date": "2023-09-27",
        "created_at": "2022-09-27 17:20:39",
        "updated_at": "2022-09-27 17:20:39",
        "deleted_at": null,
        "request_metadata": "{\"platform\":\"web\",\"app_version\":null,\"device_id\":null,\"model\":null,\"os_version\":\"5\",\"user_id\":\"1020044179\"}"
    },
    "meta": {
        "status": "OK",
        "displayMessage": "SUCCESS"
    }
}
```

---

## Update GTT API

Source: https://developer.paytmmoney.com/docs/api/update-gtt-api/

**Method:** `PUT`  
**Endpoint:** `https://developer.paytmmoney.com/gtt/v2/gtt/2528`  

### Request Attributes

Content Type: JSON

#### Head

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `x-jwt-token` | string | optional | xxxxxx ( The one retrieved from Generate Access Token Steps ) . Can be accessed using: {access\_token} |

#### Body

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `set_price` | string | optional | LTP at the time of GTT order creation |
| `transaction_type` | string | optional | The type of transaction that is being executed (Buy / Sell) |
| `quantity` | string | optional | Quantity of stocks to be traded in NSE / BSE |
| `trigger_price` | string | optional | Price at which GTT is to be triggered |
| `limit_price` | string | optional | User entered limit price, mandatory when order type is LIMIT |
| `order_type` | string | optional | LMT - Limit order (order is to be traded at mentioned price), MKT - market order (order is to be traded at market price). |
| `trigger_type` | string | optional | SINGLE/OCO |
| `transaction_details` | string | mandatory | The type of transaction that is being executed (Buy / Sell) |
| `id` | string | mandatory | GTT Order Id |
| `sub_type` | string | mandatory | Applicable for SELL transaction type only. STOPLOSS/TARGET |

### Response Attributes

Content Type: JSON

#### Body

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | optional | GTT Order Id |
| `instruction_id` | string | optional | GTT Instruction Id |
| `segment` | string | optional | This describes, to which segment the transaction belongs. (E→ Equity Cash / D→ Equity Derivative) |
| `exchange` | string | optional | The exchange which is involved for this specific transaction (National Stock Exchange / Bombay Stock Exchange) |
| `security_id` | string | optional | security\_id of scrip in NSE / BSE |
| `pml_id` | string | optional | PML id of the stock |
| `name` | string | optional | Symbol Name |
| `user_id` | string | optional | Unique customer identification number by PML |
| `status` | string | optional | Status of the gtt (optional , Default values: [ACTIVE,TRIGGERED]) . Other possible values for status param can be "CREATED, DELETED, NOTIFIED, EXPIRED" |
| `transaction_type` | string | optional | The type of transaction that is being executed (Buy / Sell) |
| `sub_type` | string | optional | Applicable for SELL transaction type only. STOPLOSS/TARGET |
| `quantity` | string | optional | Quantity of stocks to be traded in NSE / BSE |
| `trigger_price` | string | optional | Price at which GTT is to be triggered |
| `limit_price` | string | optional | User entered limit price, mandatory when order type is LIMIT |
| `notification_ref_id` | string | optional | price alert id |
| `execution_ref_id` | string | optional | id of placed order for triggered gtt instruction |
| `triggered_at` | string | optional | time at which order triggered gtt instruction |
| `triggered_at_price` | string | optional | Price at which GTT instruction got triggered |
| `triggered_at_type` | string | optional | this represents transaction sub type (STOPLOSS/TARGET) |
| `set_price` | string | optional | LTP at the time of GTT order creation |
| `order_type` | string | optional | LMT - Limit order (order is to be traded at mentioned price), MKT - market order (order is to be traded at market price). |
| `trigger_type` | string | optional | SINGLE/OCO |
| `product_type` | string | optional | Type of product are C/M C=Cash and Carry / Delivery. This is Valid only for Segment='E' (Equity), M=Margin or Overnight Carry Forward. This is Valid only for Segment='D' (Derivatives), |
| `cancellation_code` | string | optional | GTT\_USER\_DELETE GTT\_EXPIRY\_JOB GTT\_CA\_BONUS GTT\_SYSTEM\_DELETE GTT\_SYSTEM\_REJECTION |
| `cancellation_reason` | string | optional | GTT\_USER\_DELETE GTT\_EXPIRY\_JOB GTT\_CA\_BONUS GTT\_SYSTEM\_DELETE GTT\_SYSTEM\_REJECTION |
| `expiry_date` | string | optional | date till when the gtt should be valid |
| `created_at` | string | optional | Order Creation date time |
| `updated_at` | string | optional | Order Updation date time |
| `deleted_at` | string | optional | Order Deletion date time |
| `request_metadata` | string | optional | stores value of x-user-agent header sent in create gtt request |
| `status` | string | optional | Describes whether the API request was Success/Failure |
| `displayMessage` | string | optional | Message to be displayed in the frontend |

### Code Samples

#### CURL

```bash
curl --location --request PUT 'https://developer.paytmmoney.com/gtt/v2/gtt/2528' \
--header 'x-jwt-token: {{JWT-TOKEN}}' \
--header 'Content-Type: application/json' \
--data-raw '{
    "set_price": "8.40",
    "transaction_type": "S",
    "transaction_details": [
        {
            "id": 218,               
            "sub_type": "STOPLOSS",  
            "quantity": "2",
            "trigger_price": "9.0",
            "limit_price": "15.0",
            "order_type": "LMT"    
        },
        {
            "id": 219,                
            "sub_type": "TARGET",   
            "quantity": "2",
            "trigger_price": "15.0",
            "limit_price": "20",
            "order_type": "LMT"   
        }
    ],
    "trigger_type": "OCO"
}'
```

### Sample Responses

#### SUCCESS

```json
{
    "data": {
        "id": 294,
        "instruction_id": "7F166B1F3D4Y1K",
        "segment": "E",
        "exchange": "BSE",
        "security_id": "543578",
        "pml_id": "1100000684",
        "name": "Olatech Solutions Limited",
        "user_id": "1020044179",
        "transaction_type": "S",
        "transaction_details": [
            {
                "id": 295,
                "sub_type": "STOPLOSS",
                "quantity": 10,
                "trigger_price": 281.0,
                "set_price": 300.0,
                "limit_price": 0.0,
                "notification_ref_id": "59b45a48-7819-4e2f-9a6f-fa648efbb34b",
                "execution_ref_id": null,
                "triggered_at": null,
                "triggered_at_price": null,
                "triggered_at_type": null,
                "order_type": "MKT",
                "status": "ACTIVE"
            },
            {
                "id": 296,
                "sub_type": "TARGET",
                "quantity": 10,
                "trigger_price": 320.0,
                "set_price": 300.0,
                "limit_price": 321.0,
                "notification_ref_id": "1422e9d7-d4e9-426c-aac4-329ca32ce78d",
                "execution_ref_id": null,
                "triggered_at": null,
                "triggered_at_price": null,
                "triggered_at_type": null,
                "order_type": "LMT",
                "status": "ACTIVE"
            }
        ],
        "trigger_type": "OCO",
        "product_type": "C",
        "cancellation_code": null,
        "cancellation_reason": null,
        "expiry_date": "2023-09-27",
        "created_at": "2022-09-27 16:36:21",
        "updated_at": "2022-09-27 16:51:31",
        "deleted_at": null,
        "request_metadata": "{\"platform\":\"web\",\"app_version\":null,\"device_id\":null,\"model\":null,\"os_version\":\"5\",\"user_id\":\"1020044179\"}"
    },
    "meta": {
        "status": "OK",
        "displayMessage": "SUCCESS"
    }
}
```

### Notes

### Path Parameters

| Parameter | Description |
| --- | --- |
| id  string  mandatory | GTT Order ID |

---

## Get All GTT

Source: https://developer.paytmmoney.com/docs/api/get-all-gtt/

**Method:** `GET`  
**Endpoint:** `https://developer.paytmmoney.com/gtt/v2/gtt`  

### Description

> Get All GTT orders

### Request Attributes

Content Type: JSON

#### Head

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `x-jwt-token` | string | mandatory | xxxxxx ( The one retrieved from Generate Access Token Steps ) . Can be accessed using: {access\_token} |

### Response Attributes

Content Type: JSON

#### Body

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | optional | GTT Order Id |
| `instruction_id` | string | optional | GTT Instruction Id |
| `segment` | string | optional | This describes, to which segment the transaction belongs. (E→ Equity Cash / D→ Equity Derivative) |
| `exchange` | string | optional | The exchange which is involved for this specific transaction (National Stock Exchange / Bombay Stock Exchange) |
| `security_id` | string | optional | security\_id of scrip in NSE / BSE |
| `pml_id` | string | optional | PML id of the stock |
| `name` | string | optional | Symbol Name |
| `user_id` | string | optional | Unique customer identification number by PML |
| `status` | string | optional | Status of the gtt (optional , Default values: [ACTIVE,TRIGGERED]) . Other possible values for status param can be "CREATED, DELETED, NOTIFIED, EXPIRED" |
| `transaction_type` | string | optional | The type of transaction that is being executed (Buy / Sell) |
| `sub_type` | string | optional | Applicable for SELL transaction type only. STOPLOSS/TARGET |
| `quantity` | string | optional | Quantity of stocks to be traded in NSE / BSE |
| `trigger_price` | string | optional | Price at which GTT is to be triggered |
| `limit_price` | string | optional | User entered limit price, mandatory when order type is LIMIT |
| `notification_ref_id` | string | optional | price alert id |
| `execution_ref_id` | string | optional | id of placed order for triggered gtt instruction |
| `triggered_at_price` | string | optional | Price at which GTT instruction got triggered |
| `triggered_at_type` | string | optional | this represents transaction sub type (STOPLOSS/TARGET) |
| `set_price` | string | optional | LTP at the time of GTT order creation |
| `order_type` | string | optional | LMT - Limit order (order is to be traded at mentioned price), MKT - market order (order is to be traded at market price). |
| `trigger_type` | string | optional | SINGLE/OCO |
| `product_type` | string | optional | Type of product are C/M C=Cash and Carry / Delivery. This is Valid only for Segment='E' (Equity), M=Margin or Overnight Carry Forward. This is Valid only for Segment='D' (Derivatives), |
| `cancellation_code` | string | optional | GTT\_USER\_DELETE GTT\_EXPIRY\_JOB GTT\_CA\_BONUS GTT\_SYSTEM\_DELETE GTT\_SYSTEM\_REJECTION |
| `cancellation_reason` | string | optional | GTT\_USER\_DELETE GTT\_EXPIRY\_JOB GTT\_CA\_BONUS GTT\_SYSTEM\_DELETE GTT\_SYSTEM\_REJECTION |
| `expiry_date` | string | optional | date till when the gtt should be valid |
| `created_at` | string | optional | Order Creation date time |
| `updated_at` | string | optional | Order Updation date time |
| `deleted_at` | string | optional | Order Deletion date time |
| `request_metadata` | string | optional | stores value of x-user-agent header sent in create gtt request |
| `status` | string | optional | Status of the gtt (optional , Default values: [ACTIVE,TRIGGERED]) . Other possible values for status param can be "CREATED, DELETED, NOTIFIED, EXPIRED" |
| `displayMessage` | string | optional | Message to be displayed in the frontend |

### Code Samples

#### CURL

```bash
curl --location --request GET 'https://developer.paytmmoney.com/gtt/v2/gtt' \
--header 'x-jwt-token: {{JWT-TOKEN}}'
```

### Sample Responses

#### SUCCESS

```json
{
    "data": {
        "gtts": [
            {
                "id": 2892,
                "instruction_id": "3A5S4K4M6e7w6I",
                "segment": "E",
                "exchange": "NSE",
                "security_id": "3456",
                "pml_id": "1000000118",
                "name": "Tata Motors",
                "user_id": "1020044179",
                "transaction_type": "B",
                "transaction_details": [
                    {
                        "id": null,
                        "sub_type": null,
                        "quantity": 500,
                        "trigger_price": 437.5,
                        "set_price": 430.0,
                        "limit_price": 0.0,
                        "notification_ref_id": "3c1a4924-3745-4f7f-a3d1-2e96a858a494",
                        "execution_ref_id": "812209202005",
                        "triggered_at": "2022-09-20 13:19:01",
                        "triggered_at_price": 438.75,
                        "triggered_at_type": null,
                        "order_type": null,
                        "status": TRIGGERED
                     }
                ],
                "trigger_type": "SINGLE",
                "product_type": "C",
                "cancellation_code": null,
                "cancellation_reason": null,
                "expiry_date": "2023-09-20",
                "created_at": "2022-09-20 12:52:14",
                "updated_at": "2022-09-20 13:19:02",
                "deleted_at": null,
                "request_metadata": "{\"platform\":\"web\",\"app_version\":null,\"device_id\":null,\"model\":null,\"os_version\":\"5\",\"user_id\":\"1020044179\"}"
            },
            {
                "id": 2899,
                "instruction_id": "7h2F354j204l6V",
                "segment": "E",
                "exchange": "NSE",
                "security_id": "1270",
                "pml_id": "1000002680",
                "name": "Ambuja Cements",
                "user_id": "1020044179",
                "transaction_type": "S",
                "transaction_details": [
                    {
                        "id":2900,
                        "sub_type": "STOPLOSS",
                        "quantity": 100,
                        "trigger_price": 575.5,
                        "set_price": 581.0,
                        "limit_price": 0.0,
                        "notification_ref_id": "039274a6-87a0-4db6-8c19-ba644e7065ad",
                        "execution_ref_id": "112209202145",
                        "triggered_at": "2022-09-20 15:07:57",
                        "triggered_at_price": 575.45,
                        "triggered_at_type": null,
                        "order_type": "MKT",
                        "status": "TRIGGERED"
                    },
                    {
                        "id":2901,                         
                        "sub_type": "TARGET",
                        "quantity": 100,
                        "trigger_price": 583.0,
                        "set_price": 581.0,
                        "limit_price": 20000.0,
                        "notification_ref_id": "ea0ceb62-9c87-4c91-a802-7451f1c089a5",
                        "execution_ref_id": null,
                        "triggered_at": null,
                        "triggered_at_price": null,
                        "triggered_at_type": null,
                        "order_type": "LMT",
                        "status": "DELETED"
                    }
                ],
                "trigger_type": "OCO",
                "product_type": C,
                "cancellation_code": null,
                "cancellation_reason": null,
                "expiry_date": "2023-09-20",
                "created_at": "2022-09-20 14:48:39",
                "updated_at": "2022-09-20 15:07:58",
                "deleted_at": null,
                "request_metadata": "{\"platform\":\"web\",\"app_version\":null,\"device_id\":null,\"model\":null,\"os_version\":\"5\",\"user_id\":\"1020044179\"}"
            },
            "meta": {
                "status": "OK",
                "displayMessage": "SUCCESS"
            }
        }
```

---

## Get GTT By Status and User

Source: https://developer.paytmmoney.com/docs/api/get-gtt-by-status-and-user/

**Method:** `GET`  
**Endpoint:** `https://developer.paytmmoney.com/gtt/v1/gtt?status=TRIGGERED&pml-id=1000001488`  

### Request Attributes

Content Type: JSON

#### Head

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `x-jwt-token` | string | optional | xxxxxx ( The one retrieved from Generate Access Token Steps ) . Can be accessed using: {access\_token} |

### Response Attributes

Content Type: JSON

#### Body

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | optional | GTT Order Id |
| `instruction_id` | string | optional | GTT Instruction Id |
| `segment` | string | optional | This describes, to which segment the transaction belongs. (E→ Equity Cash / D→ Equity Derivative) |
| `exchange` | string | optional | The exchange which is involved for this specific transaction (National Stock Exchange / Bombay Stock Exchange) |
| `security_id` | string | optional | security\_id of scrip in NSE / BSE |
| `pml_id` | string | optional | PML id of the stock |
| `name` | string | optional | Symbol Name |
| `user_id` | string | optional | Unique customer identification number by PML |
| `status` | string | optional | Status of the gtt (optional , Default values: [ACTIVE,TRIGGERED]) . Other possible values for status param can be "CREATED, DELETED, NOTIFIED, EXPIRED" |
| `transaction_type` | string | optional | The type of transaction that is being executed (Buy / Sell) |
| `sub_type` | string | optional | Applicable for SELL transaction type only. STOPLOSS/TARGET |
| `quantity` | string | optional | Quantity of stocks to be traded in NSE / BSE |
| `trigger_price` | string | optional | Price at which GTT is to be triggered |
| `limit_price` | string | optional | User entered limit price, mandatory when order type is LIMIT |
| `notification_ref_id` | string | optional | price alert id |
| `execution_ref_id` | string | optional | id of placed order for triggered gtt instruction |
| `triggered_at` | string | optional | time at which order triggered gtt instruction |
| `triggered_at_price` | string | optional | Price at which GTT instruction got triggered |
| `triggered_at_type` | string | optional | this represents transaction sub type (STOPLOSS/TARGET) |
| `set_price` | string | optional | LTP at the time of GTT order creation |
| `order_type` | string | optional | LMT - Limit order (order is to be traded at mentioned price), MKT - market order (order is to be traded at market price). |
| `trigger_type` | string | optional | SINGLE/OCO |
| `product_type` | string | optional | Type of product are C/M C=Cash and Carry / Delivery. This is Valid only for Segment='E' (Equity), M=Margin or Overnight Carry Forward. This is Valid only for Segment='D' (Derivatives), |
| `cancellation_code` | string | optional | GTT\_USER\_DELETE GTT\_EXPIRY\_JOB GTT\_CA\_BONUS GTT\_SYSTEM\_DELETE GTT\_SYSTEM\_REJECTION |
| `cancellation_reason` | string | optional | GTT\_USER\_DELETE GTT\_EXPIRY\_JOB GTT\_CA\_BONUS GTT\_SYSTEM\_DELETE GTT\_SYSTEM\_REJECTION |
| `expiry_date` | string | optional | date till when the gtt should be valid |
| `created_at` | string | optional | Order Creation date time |
| `updated_at` | string | optional | Order Updation date time |
| `deleted_at` | string | optional | Order Deletion date time |
| `request_metadata` | string | optional | stores value of x-user-agent header sent in create gtt request |
| `status` | string | optional | Describes whether the API request was Success/Failure |
| `displayMessage` | string | optional | Message to be displayed in the frontend |

### Code Samples

#### CURL

```bash
curl --location --request GET 'https://developer.paytmmoney.com/gtt/v1/gtt?status=TRIGGERED&pml-id=1000001488' \
--header 'x-jwt-token: {{JWT-TOKEN}}'
```

### Sample Responses

#### SUCCESS

```json
{
    "data": {
        "gtts": [
            {
                "id": 2529,
                "instruction_id": "7f3K7w7g5i6Z6Y",
                "segment": "E",
                "exchange": "NSE",
                "security_id": "14366",
                "pml_id": "1000001488",
                "name": "Shalimar Wires Industries",
                "user_id": "794569",
                "status": "ACTIVE",
                "transaction_type": "S",
                "transaction_details": [
                    {
                        "sub_type": null,
                        "quantity": 1,
                        "trigger_price": 12.7,
                        "limit_price": 0.0,
                        "notification_ref_id": "62cf99f2-c9bb-4c49-8b98-843bc154bc84",
                        "execution_ref_id": null,
                        "triggered_at": null,
                        "triggered_at_price": null,
                        "triggered_at_type": null
                    }
                ],
                "set_price": 12.8,
                "order_type": "MKT",
                "trigger_type": "SINGLE",
                "product_type": "C",
                "cancellation_code": null,
                "cancellation_reason": null,
                "expiry_date": "2023-05-23",
                "created_at": "2022-05-23 13:50:24",
                "updated_at": "2022-05-23 13:50:27",
                "deleted_at": null,
                "request_metadata": "{\"platform\":\"Open-api\",\"app_version\":\"2.1.2602-development\",\"device_id\":\"296db049af616c4\",\"model\":\"motorola Moto G (5S)\",\"os_version\":\"25\",\"user_id\":\"794569\"}"
            }
        ]
    },
    "meta": {
        "status": "OK",
        "displayMessage": "SUCCESS"
    }
}
```

### Notes

### Query Parameters

| Attribute | Description |
| --- | --- |
| status  string  mandatory | Status of the gtt (optional , Default values: [ACTIVE,TRIGGERED]) . Other possible values for status param can be "CREATED, DELETED, NOTIFIED, EXPIRED" |
| pml-id  string  mandatory | PML id of the stock |

---

## Get GTT

Source: https://developer.paytmmoney.com/docs/api/get-gtt/

**Method:** `GET`  
**Endpoint:** `https://developer.paytmmoney.com/gtt/v2/gtt/2516`  

### Request Attributes

Content Type: JSON

#### Head

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `x-jwt-token` | string | optional | xxxxxx ( The one retrieved from Generate Access Token Steps ) . Can be accessed using: {access\_token} |

### Response Attributes

Content Type: JSON

#### Body

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | optional | GTT Order Id |
| `instruction_id` | string | optional | GTT Instruction Id |
| `segment` | string | optional | This describes, to which segment the transaction belongs. (E→ Equity Cash / D→ Equity Derivative) |
| `exchange` | string | optional | The exchange which is involved for this specific transaction (National Stock Exchange / Bombay Stock Exchange) |
| `security_id` | string | optional | security\_id of scrip in NSE / BSE |
| `pml_id` | string | optional | PML id of the stock |
| `name` | string | optional | Symbol Name |
| `user_id` | string | optional | Unique customer identification number by PML |
| `status` | string | optional | Status of the gtt (optional , Default values: [ACTIVE,TRIGGERED]) . Other possible values for status param can be "CREATED, DELETED, NOTIFIED, EXPIRED" |
| `transaction_type` | string | optional | The type of transaction that is being executed (Buy / Sell) |
| `sub_type` | string | optional | Applicable for SELL transaction type only. STOPLOSS/TARGET |
| `quantity` | string | optional | Quantity of stocks to be traded in NSE / BSE |
| `trigger_price` | string | optional | Price at which GTT is to be triggered |
| `limit_price` | string | optional | User entered limit price, mandatory when order type is LIMIT |
| `notification_ref_id` | string | optional | price alert id |
| `execution_ref_id` | string | optional | id of placed order for triggered gtt instruction |
| `triggered_at` | string | optional | time at which order triggered gtt instruction |
| `triggered_at_price` | string | optional | Price at which GTT instruction got triggered |
| `triggered_at_type` | string | optional | this represents transaction sub type (STOPLOSS/TARGET) |
| `set_price` | string | optional | LTP at the time of GTT order creation |
| `order_type` | string | optional | LMT - Limit order (order is to be traded at mentioned price), MKT - market order (order is to be traded at market price). |
| `trigger_type` | string | optional | SINGLE/OCO |
| `product_type` | string | optional | Type of product are C/M C=Cash and Carry / Delivery. This is Valid only for Segment='E' (Equity), M=Margin or Overnight Carry Forward. This is Valid only for Segment='D' (Derivatives), |
| `cancellation_code` | string | optional | GTT\_USER\_DELETE GTT\_EXPIRY\_JOB GTT\_CA\_BONUS GTT\_SYSTEM\_DELETE GTT\_SYSTEM\_REJECTION |
| `cancellation_reason` | string | optional | GTT\_USER\_DELETE GTT\_EXPIRY\_JOB GTT\_CA\_BONUS GTT\_SYSTEM\_DELETE GTT\_SYSTEM\_REJECTION |
| `expiry_date` | string | optional | date till when the gtt should be valid |
| `created_at` | string | optional | Order Creation date time |
| `updated_at` | string | optional | Order Updation date time |
| `deleted_at` | string | optional | Order Deletion date time |
| `request_metadata` | string | optional | stores value of x-user-agent header sent in create gtt request |
| `status` | string | optional | Describes whether the API request was Success/Failure |
| `displayMessage` | string | optional | Message to be displayed in the frontend |

### Code Samples

#### CURL

```bash
curl --location --request GET 'https://developer.paytmmoney.com/gtt/v2/gtt/2516' \
--header 'x-jwt-token: {{JWT-TOKEN}}'
```

### Sample Responses

#### SUCCESS

```json
{
    "data": {
        "id": 2529,
        "instruction_id": "7f3K7w7g5i6Z6Y",
        "segment": "E",
        "exchange": "NSE",
        "security_id": "14366",
        "pml_id": "1000001488",
        "name": "Shalimar Wires Industries",
        "user_id": "794569",
        "status": "ACTIVE",
        "transaction_type": "S",
        "transaction_details": [
            {
                "sub_type": null,
                "quantity": 1,
                "trigger_price": 12.7,
                "limit_price": 0.0,
                "notification_ref_id": "62cf99f2-c9bb-4c49-8b98-843bc154bc84",
                "execution_ref_id": null,
                "triggered_at": null,
                "triggered_at_price": null,
                "triggered_at_type": null
            }
        ],
        "set_price": 12.8,
        "order_type": "MKT",
        "trigger_type": "SINGLE",
        "product_type": "C",
        "cancellation_code": null,
        "cancellation_reason": null,
        "expiry_date": "2023-05-23",
        "created_at": "2022-05-23 13:50:24",
        "updated_at": "2022-05-23 13:50:27",
        "deleted_at": null,
        "request_metadata": "{\"platform\":\"Open-api\",\"app_version\":\"2.1.2602-development\",\"device_id\":\"296db049af616c4\",\"model\":\"motorola Moto G (5S)\",\"os_version\":\"25\",\"user_id\":\"794569\"}"
    },
    "meta": {
        "status": "OK",
        "displayMessage": "SUCCESS"
    }
}
```

### Notes

### Path Parameters

| Parameter | Description |
| --- | --- |
| id  string  mandatory | GTT Order ID |

---

## Get GTT Aggregate

Source: https://developer.paytmmoney.com/docs/api/get-gtt-aggregate/

**Method:** `GET`  
**Endpoint:** `https://developer.paytmmoney.com/gtt/v1/gtt/aggregate`  

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
| `name` | string | optional | Symbol Name |
| `pml_id` | string | optional | PML id of the stock |
| `security_id` | string | optional | security\_id of scrip in NSE / BSE |
| `exchange` | string | optional | The exchange which is involved for this specific transaction (National Stock Exchange / Bombay Stock Exchange) |
| `instrument_type` | string | optional | Script Type like ES= Equity Stock ETF= Exchange Traded Fund FUTIDX= Future Index FUTSTK= Future Stock OPTIDX= Option Index OPTSTK= Option Stock |
| `segment` | string | optional | This describes, to which segment the transaction belongs. (E→ Equity Cash / D→ Equity Derivative) |
| `lot_size` | string | optional | The no of contracts in a derivative security |
| `tick_size` | string | optional | Minimum price change between different bid and offer prices of an asset traded on an exchange platform |
| `status` | string | optional | Describes whether the API request was Success/Failure |
| `displayMessage` | string | optional | Message to be displayed in the frontend |

### Code Samples

#### CURL

```bash
curl --location --request GET 'https://developer.paytmmoney.com/gtt/v1/gtt/aggregate' \
--header 'x-jwt-token: {{JWT-TOKEN}}'
```

### Sample Responses

#### SUCCESS

```json
{
    "data": {
        "pending": [
            {
                "name": "Tata Consultancy Services",
                "pml_id": "1000000481",
                "count": 2,
                "security_id": "11536",
                "exchange": "NSE",
                "instrument_type": "ES",
                "segment": "E",
                "lot_size": "1",
                "tick_size": "5.0"
            }
        ],
        "triggered": [
            {
                "name": "Reliance Industries",
                "pml_id": "1000003043",
                "count": 2,
                "security_id": "2885",
                "exchange": "NSE",
                "instrument_type": "ES",
                "segment": "E",
                "lot_size": "1",
                "tick_size": "5.0"
            }
        ]
    },
    "meta": {
        "status": "OK",
        "displayMessage": "SUCCESS"
    }
}
```

---

## Get GTT Expiry Date

Source: https://developer.paytmmoney.com/docs/api/get-gtt-expiry-date/

**Method:** `GET`  
**Endpoint:** `https://developer.paytmmoney.com/gtt/v1/gtt/expiry-date?pml-id=1000001488`  

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
| `expiry_date` | string | optional | date till when the gtt should be valid |
| `displayMessage` | string | optional | Message to be displayed in the frontend |

### Code Samples

#### CURL

```bash
curl --location --request GET 'https://developer.paytmmoney.com/gtt/v1/gtt/expiry-date?pml-id=1000001488' \
--header 'x-jwt-token: {{JWT-TOKEN}}'
```

### Sample Responses

#### SUCCESS

```json
{
    "data": {
        "expiry_date": "2023-05-23"
    },
    "meta": {
        "status": "OK",
        "displayMessage": "SUCCESS"
    }
}
```

### Notes

### Query Parameters

| Parameter | Description |
| --- | --- |
| pml\_id  string  mandatory | Pml\_ID of Script |

---

## Get GTT Instruction

Source: https://developer.paytmmoney.com/docs/api/get-gtt-instruction/

**Method:** `POST`  
**Endpoint:** `https://developer.paytmmoney.com/gtt/v1/gtt/instructions/3s4U8L7i350b5T`  
**Staging endpoint:** `https://developer.paytmmoney.com/gtt/v2/gtt/instructions/3s4U8L7i350b5T`  

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
| `id` | string | optional | GTT Order Id |
| `instruction_id` | string | optional | GTT Instruction Id |
| `segment` | string | optional | This describes, to which segment the transaction belongs. (E→ Equity Cash / D→ Equity Derivative) |
| `exchange` | string | optional | The exchange which is involved for this specific transaction (National Stock Exchange / Bombay Stock Exchange) |
| `security_id` | string | optional | security\_id of scrip in NSE / BSE |
| `pml_id` | string | optional | PML id of the stock |
| `name` | string | optional | Symbol Name |
| `user_id` | string | optional | Unique customer identification number by PML |
| `status` | string | optional | Status of the gtt (optional , Default values: [ACTIVE,TRIGGERED]) . Other possible values for status param can be "CREATED, DELETED, NOTIFIED, EXPIRED" |
| `transaction_type` | string | optional | The type of transaction that is being executed (Buy / Sell) |
| `sub_type` | string | optional | Applicable for SELL transaction type only. STOPLOSS/TARGET |
| `quantity` | string | optional | Quantity of stocks to be traded in NSE / BSE |
| `trigger_price` | string | optional | Price at which GTT is to be triggered |
| `limit_price` | string | optional | User entered limit price, mandatory when order type is LIMIT |
| `notification_ref_id` | string | optional | price alert id |
| `execution_ref_id` | string | optional | id of placed order for triggered gtt instruction |
| `triggered_at` | string | optional | time at which order triggered gtt instruction |
| `triggered_at_price` | string | optional | Price at which GTT instruction got triggered |
| `triggered_at_type` | string | optional | this represents transaction sub type (STOPLOSS/TARGET) |
| `set_price` | string | optional | LTP at the time of GTT order creation |
| `order_type` | string | optional | LMT - Limit order (order is to be traded at mentioned price), MKT - market order (order is to be traded at market price). |
| `trigger_type` | string | optional | SINGLE/OCO |
| `product_type` | string | optional | Type of product are C/M C=Cash and Carry / Delivery. This is Valid only for Segment='E' (Equity), M=Margin or Overnight Carry Forward. This is Valid only for Segment='D' (Derivatives), |
| `cancellation_code` | string | optional | GTT\_USER\_DELETE GTT\_EXPIRY\_JOB GTT\_CA\_BONUS GTT\_SYSTEM\_DELETE GTT\_SYSTEM\_REJECTION |
| `cancellation_reason` | string | optional | GTT\_USER\_DELETE GTT\_EXPIRY\_JOB GTT\_CA\_BONUS GTT\_SYSTEM\_DELETE GTT\_SYSTEM\_REJECTION |
| `expiry_date` | string | optional | date till when the gtt should be valid |
| `created_at` | string | optional | Order Creation date time |
| `updated_at` | string | optional | Order Updation date time |
| `deleted_at` | string | optional | Order Deletion date time |
| `request_metadata` | string | optional | stores value of x-user-agent header sent in create gtt request |
| `status` | string | optional | Describes whether the API request was Success/Failure |
| `displayMessage` | string | optional | Message to be displayed in the frontend |

### Code Samples

#### CURL

```bash
curl --location --request GET 'https://developer.paytmmoney.com/gtt/v2/gtt/instructions/3s4U8L7i350b5T' \
--header 'x-jwt-token: {{JWT-TOKEN}}'
```

### Sample Responses

#### SUCCESS

```json
{
    "data": {
        "id": 2529,
        "instruction_id": "7f3K7w7g5i6Z6Y",
        "segment": "E",
        "exchange": "NSE",
        "security_id": "14366",
        "pml_id": "1000001488",
        "name": "Shalimar Wires Industries",
        "user_id": "794569",
        "status": "ACTIVE",
        "transaction_type": "S",
        "transaction_details": [
            {
                "sub_type": null,
                "quantity": 3,
                "trigger_price": 12.7,
                "limit_price": 0.0,
                "notification_ref_id": "62cf99f2-c9bb-4c49-8b98-843bc154bc84",
                "execution_ref_id": null,
                "triggered_at": null,
                "triggered_at_price": null,
                "triggered_at_type": null
            }
        ],
        "set_price": 12.8,
        "order_type": "MKT",
        "trigger_type": "SINGLE",
        "product_type": "C",
        "cancellation_code": null,
        "cancellation_reason": null,
        "expiry_date": "2023-05-23",
        "created_at": "2022-05-23 13:50:24",
        "updated_at": "2022-05-23 14:10:35",
        "deleted_at": null,
        "request_metadata": "{\"platform\":\"Open-api\",\"app_version\":\"2.1.2602-development\",\"device_id\":\"296db049af616c4\",\"model\":\"motorola Moto G (5S)\",\"os_version\":\"25\",\"user_id\":\"794569\"}"
    },
    "meta": {
        "status": "OK",
        "displayMessage": "SUCCESS"
    }
}
```

### Notes

### Path Parameters

| Parameter | Description |
| --- | --- |
| instruction id  string  mandatory | GTT Instruction ID |

---

## Delete GTT API

Source: https://developer.paytmmoney.com/docs/api/delete-gtt-api/

**Method:** `DELETE`  
**Endpoint:** `https://developer.paytmmoney.com/gtt/v1/gtt/2516`  

### Request Attributes

Content Type: JSON

#### Head

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `x-jwt-token` | string | optional | xxxxxx ( The one retrieved from Generate Access Token Steps ) . Can be accessed using: {access\_token} |

### Response Attributes

Content Type: JSON

#### Body

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `status` | string | optional | Describes whether the API request was Success/Failure |
| `displayMessage` | string | optional | Message to be displayed in the frontend |

### Code Samples

#### CURL

```bash
curl --location --request DELETE 'https://developer.paytmmoney.com/gtt/v1/gtt/2516' \
--header 'x-jwt-token: {{JWT-TOKEN}}'
```

### Sample Responses

#### SUCCESS

```json
{
    "data": null,
    "meta": {
        "status": "OK",
        "displayMessage": "SUCCESS"
    }
}
```

### Notes

### How to use it ?

1. Create a jwt token using the get access token API

   ```
   curl --location --request POST 'https://developer.paytmmoney.com/accounts/v1/gettoken?apiKey=xxxxx
   xxxxxxxxxxxxxxxxxxxxxxxxxxx&requestToken=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx' \
   --header 'Content-Type: application/json' \
   --data-raw '{
      "merchantSecret" : "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
   }'
   ```
2. To create a web socket connection with the Open Api broadcast service, send a web socket connection request to
   > wss://developer.paytmmoney.com/broadcast/client\_user?x\_jwt\_token={{VALID\_JWT\_TOKEN}}
3. Once successfully connected, you may send a preference to receive live market data.
4. For fetching the latest security ids please use the below API

### Preference structure

#### A single preference must contain the following fields:

##### **ActionType**

actionType key may have one of the following values

| ActionType | Description |
| --- | --- |
| ADD | To subscribe to a particular scripts |
| REMOVE | To unsubscribe to a particular scripts |

##### **ModeType**

ModeType key may have one of the following values

| ModeType | Description |
| --- | --- |
| LTP | The packet contains several fields including the last traded price |
| QUOTE | The packet contains several fields excluding the market depth |
| FULL | The packet contains several fields including the market depth |

##### **ScripType**

ScripType key may have one of the following values

| ScripType | Description |
| --- | --- |
| INDEX | for scrip ids belonging to the index script type |
| EQUITY | for scrip ids belonging to equity script type |
| ETF | for scrip ids belonging to ETF script type |
| FUTURE | for scrip ids belonging to future script type |
| OPTION | for scrip ids belonging to option script type |

##### **ExchangeType**

ExchangeType key may have one of the following values

| ExchangeType | Description |
| --- | --- |
| BSE | for scrip ids belonging to BSE Limited |
| NSE | for scrip ids belonging to the National Stock Exchange of India Limited |

##### **ScripId**

| ScripId | Description |
| --- | --- |
| xxx15 | The exchange scrip id of the stock you want to receive live market data for. |

```
    // Preference structure for subscribing a scrip 
    {
      "actionType": "ADD",
      "modeType": "FULL",
      "scripType": "INDEX",
      "exchangeType": "NSE",
      "scripId": "13"
    }
    // Preference structure for unsubscribing a scrip 
    {
      "actionType": "REMOVE",
      "modeType": "QUOTE",
      "scripType": "ETF",
      "exchangeType": "NSE",
      "scripId": "2328"
    }
```

### Api Info

> GET - wss://developer-ws.paytmmoney.com/broadcast/client\_user?x\_jwt\_token={{VALID\_JWT\_TOKEN}}

##### **Description**

GET Request to establish a web socket connection

| Key/Parameter | Type | Required? | Value | Description |
| --- | --- | --- | --- | --- |
| x\_jwt\_token | string | Yes | jwtToken | JWTToken |

##### **Response Fields**

| Attribute | Description |
| --- | --- |
| tradableid  Byte | 0 for false, 1 for true. True if stock is tradable else false |
| mode  Byte | Type of Packet LTP/QUOTE/FULL LTP=61; QUOTE=62; FULL=63; INDEX LTP=64; INDEX QUOTE=65; INDEX FULL=66 |
| security\_id  Integer | Security Id for which broadcast is received |
| last\_price  Float | Last traded market price |
| last\_traded\_quantity  Integer | Last traded quantity |
| average\_traded\_price  Float | Average traded market price |
| volume\_traded  Integer | Volume traded today |
| total\_buy\_quantity  Integer | Total quantity of buy orders pending at the exchange |
| total\_sell\_quantity  Integer | Total quantity of sell orders pending at the exchange |
| open  Float | Price when the market opened |
| high  Float | Highest price today |
| low  Float | Lowest price today |
| close  Float | Closing price of the instrument from the last trading day |
| change\_percent  Float | The absolute percentage price change of the security's price since the previous day's close |
| change\_absolute  Float | The absolute change in security's price since the previous day's close |
| 52\_week\_high  Float | The highest price at which a security has traded during the time period that equates to one year |
| 52\_week\_low  Float | The lowest price at which a security has traded during the time period that equates to one year |
| last\_traded\_time  String | Last trade timestamp |
| last\_update\_time  String | Last update timestamp |
| oi  Integer | Number of future and option contracts traded but not yet liquidated |
| change\_oi  Integer | The change in the number of future and option contracts traded but not yet liquidated |
| Buy Quantity  Integer | Net quantity from the pending orders |
| Buy Price  Float | Price at which the buy order depth stands |
| Buy Orders  Float | Price at which the buy order depth stands |
| Sell Quantity  Float | Net quantity from the pending orders |
| Sell Price  Float | Price at which the sell order depth stands |
| Sell Orders  Integer | Number of open sell orders at the price |

##### **Error Codes and Messages**

HTTP Error Codes

| Response Code | Response message | Description |
| --- | --- | --- |
| 400 | Bad Request | Bad Request |
| 401 | Unauthorized | Unauthorized jwt token or sso token |
| 500 | Internal Server Error | Internal Server Error |
| 509 | Bandwidth limit exceeded | The server has reached its maximum connection limit |

##### **Web socket Error Message**

| Error Message | Description |
| --- | --- |
| "You have sent preference packet in an invalid format" | preference structure is invalid |
| "You have reached the maximum subscription limit: 500" | connection's preference subscription limit of 500 reached |
