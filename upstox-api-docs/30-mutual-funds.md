# Mutual Funds

Read-only endpoints for mutual fund holdings, orders, and systematic investment plans held on the account.

---

## Get Mutual Fund Holdings

API to retrieve the list of mutual fund (MF) holdings for the user. The data reflects the user's current MF portfolio and can be used to track investment performance and portfolio allocation.

### Endpoint

**GET** `https://api.upstox.com/v2/mf/holdings`

### Response

```json
{
    "status": "success",
    "data": [
        {
            "instrument_key": "INF200K01T51",
            "folio": "3108290884",
            "fund": "SBI SMALL CAP FUND - DIRECT PLAN - GROWTH",
            "pnl": -703.68,
            "quantity": 110.0,
            "average_price": 181.80,
            "last_price": 175.43,
            "last_price_date": "2026-03-06",
            "pledged_quantity": 0
        },
        {
            "instrument_key": "INF179K01WM1",
            "folio": "310829013",
            "fund": "HDFC NIFTY 50 INDEX FUND - DIRECT PLAN - GROWTH",
            "pnl": -46.8,
            "quantity": 2.0,
            "average_price": 250.0,
            "last_price": 226.6,
            "last_price_date": "2026-03-06",
            "pledged_quantity": 0
        },
        {
            "instrument_key": "INF204K01K15",
            "folio": "3108290881",
            "fund": "NIPPON INDIA SMALL CAP FUND DIRECT PLAN GROWTH PLAN GROWTH",
            "pnl": 796.86,
            "quantity": 11.0,
            "average_price": 100.0,
            "last_price": 172.45,
            "last_price_date": "2026-03-06"
        }
    ]
}
```

| Name | Type | Description |
| --- | --- | --- |
| status | string | Outcome of the request. |
| data | array | Holding rows. |
| data[].instrument_key | string | Fund ISIN when available. |
| data[].folio | string | Folio number when available. |
| data[].average_price | number | Average cost per unit. |
| data[].last_price | number | Last available NAV. |
| data[].last_price_date | string | Date for which last NAV applies. |
| data[].pledged_quantity | number | Units pledged when applicable. |
| data[].fund | string | Fund display name. |
| data[].pnl | number | Unrealized profit or loss. |
| data[].quantity | number | Units held. |

### Error Codes

Errors follow the [standard API error format](https://upstox.com/developer/api-documentation/error-codes) . Ensure the request is authenticated and your account has access to mutual fund data.

---

## Get Mutual Fund Order Book

API to retrieve a paginated list of mutual fund orders for the user. The response can be filtered by order status and transaction type, with pagination managed through the `page_number` and `records` parameters.

### Endpoint

**GET** `https://api.upstox.com/v2/mf/orders`

### Query Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| status | Optional | string | Filter by order status: `ALL` , `ARCHIVED` , `NEW` , `PENDING` , `OPEN` , `INPROCESS` , `COMPLETED` , `PLACED` , `REJECTED` , `CREATED` , `PAYMENT_PENDING` , `FAILED` , `CANCELLED` , or `VERIFIED` . Default: `ALL` . |
| transaction_type | Optional | string | Filter by transaction type: `BUY` , `SELL` , or `ALL` . Default: `ALL` . |
| page_number | Optional | integer | Page number, starting from `1` . Default: `1` |
| records | Optional | integer | Records per page. Default: `10` , Max: `30` . |

### Response

```json
{
  "status": "success",
  "data": [
    {
        "instrument_key": "INF109K01Q49",
        "status": "INPROCESS",
        "status_message": "",
        "folio": "",
        "fund": "ICICI Prudential Liquid Fund Direct Plan Growth",
        "amount": 1000.0,
        "quantity": 0.0,
        "price": 0.0,
        "order_id": "ABC123-a9b52e90-3de6-4674-84b9-e3bcced7ec30",
        "exchange_order_id": "254657127",
        "order_timestamp": "2026-03-12 15:17:42",
        "exchange_timestamp": null,
        "transaction_type": "BUY",
        "last_price": 0.0,
        "average_price": 0.0,
        "settlement_id": "254657127",
        "variety": "REGULAR",
        "purchase_type": "FRESH",
        "last_price_date": "2026-03-06"
    },
    {
        "instrument_key": "INF277K01YE6",
        "status": "OPEN",
        "status_message": null,
        "folio": "",
        "fund": "Tata Liquid Fund Direct Plan Growth",
        "amount": 500.0,
        "quantity": 0.0,
        "price": 0.0,
        "order_id": "ABC123-1dcb96f2-e5d1-49c1-a03b-151c066365c2",
        "exchange_order_id": "254657127",
        "order_timestamp": "2026-03-12 00:00:00",
        "exchange_timestamp": null,
        "transaction_type": "BUY",
        "last_price": 0.0,
        "average_price": 0.0,
        "settlement_id": "254657127",
        "variety": "REGULAR",
        "purchase_type": "FRESH",
        "last_price_date": "2026-03-06"
    },
    {
        "instrument_key": "INF204K01K15",
        "status": "COMPLETED",
        "status_message": null,
        "folio": "131082908",
        "fund": "Nippon India Small Cap Fund - Direct Plan - Growth Plan",
        "amount": 1000.0,
        "quantity": 10.0,
        "price": 100.0,
        "order_id": "ABC123-5c17d81a-24b9-4ec0-8a71-77fc0572030c",
        "exchange_order_id": "254657127",
        "order_timestamp": "2026-03-06 13:28:26",
        "exchange_timestamp": null,
        "transaction_type": "BUY",
        "last_price": 100.0,
        "average_price": 100.0,
        "settlement_id": "254657127",
        "variety": "REGULAR",
        "purchase_type": "FRESH",
        "last_price_date": "2026-03-06"
    }
  ],
  "meta_data": {
    "page": {
      "page_number": 1,
      "total_pages": 1,
      "records": 10,
      "total_records": 3
    }
  }
}
```

| Name | Type | Description |
| --- | --- | --- |
| status | string | Outcome of the request. Typically `success` or `error` . |
| data | array | List of mutual fund order rows. |
| data[].order_id | string | Unique order identifier. |
| data[].exchange_order_id | string | Exchange order id when available. |
| data[].instrument_key | string | Fund ISIN when available. |
| data[].status | string | Current order status. |
| data[].status_message | string | Human-readable status or rejection reason. |
| data[].folio | string | Folio when allotted. |
| data[].fund | string | Fund or scheme display name. |
| data[].order_timestamp | string | When the order was registered in format: `YYYY-MM-DD HH:mm:ss` . |
| data[].exchange_timestamp | string | Exchange date when available in format: `YYYY-MM-DD HH:mm:ss` . |
| data[].settlement_id | string | Settlement id when available. |
| data[].transaction_type | string | `BUY` or `SELL` . |
| data[].amount | number | Order amount. |
| data[].variety | string | Order variety either `REGULAR` or `SIP` . |
| data[].purchase_type | string | `FRESH` or `ADDITIONAL` for buys when applicable. (null incase of SELL order) |
| data[].quantity | number | Units allotted or sold. |
| data[].price | number | Price or NAV used when available. |
| data[].last_price | number | Last known NAV. |
| data[].average_price | number | Allotted or sold NAV. |
| data[].last_price_date | string | Date for last NAV when available in format: `YYYY-MM-DD` . |
| meta_data | object | Pagination wrapper. |
| meta_data.page | object | Page metadata. |
| meta_data.page.page_number | integer | Current page. |
| meta_data.page.total_pages | integer | Total pages. |
| meta_data.page.records | integer | Page size used. |
| meta_data.page.total_records | integer | Total rows across pages. |

### Error Codes

| Error code | Description |
| --- | --- |
| UDAPI1173 | **Page records exceeds limit** — `records` must not exceed 30. |
| UDAPI1174 | **Page number must be greater than or equal to 1** — `page_number` must be at least 1. |
| UDAPI1196 | **Records must be greater than or equal to 1** — `records` must be at least 1. |
| UDAPI1197 | **Invalid mutual fund order status** — The provided `status` value is not a valid order status. |

---

## Get Mutual Fund Order Details

This API provides the status and full details for a specific mutual fund order. Call with a valid `order_id` for an order that belongs to the user account.

### Endpoint

**GET** `https://api.upstox.com/v2/mf/orders/{order_id}`

### Path Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| order_id | Required | string | Mutual fund order id. |

### Response

```json
{
    "status": "success",
    "data": {
        "instrument_key": "INF109K01Q49",
        "status": "INPROCESS",
        "status_message": null,
        "folio": "",
        "fund": "ICICI Prudential Liquid Fund Direct Plan Growth",
        "amount": 1000.0,
        "quantity": 0.0,
        "price": 0.0,
        "order_id": "ABC123-a9b52e90-3de6-4674-84b9-e3bcced7ec30",
        "exchange_order_id": "254657127",
        "order_timestamp": "2026-03-12 15:17:42",
        "exchange_timestamp": null,
        "transaction_type": "BUY",
        "last_price": 0.0,
        "average_price": 0.0,
        "settlement_id": "254657127",
        "variety": "REGULAR",
        "purchase_type": "FRESH",
        "last_price_date": "2026-03-06"
    }
}
```

| Name | Type | Description |
| --- | --- | --- |
| status | string | Outcome of the request. Typically `success` or `error` . |
| data | object | Single mutual fund order object. |
| data.order_id | string | Unique order identifier. |
| data.exchange_order_id | string | Exchange order id when available. |
| data.instrument_key | string | Fund ISIN when available. |
| data.status | string | Current order status. |
| data.status_message | string | Human-readable status or rejection reason. |
| data.folio | string | Folio when allotted. |
| data.fund | string | Fund or scheme display name. |
| data.order_timestamp | string | When the order was registered in format: `YYYY-MM-DD HH:mm:ss` . |
| data.exchange_timestamp | string | Exchange date when available in format: `YYYY-MM-DD HH:mm:ss` . |
| data.settlement_id | string | Settlement id when available. |
| data.transaction_type | string | `BUY` or `SELL` . |
| data.amount | number | Order amount. |
| data.variety | string | Order variety either `REGULAR` or `SIP` . |
| data.purchase_type | string | `FRESH` or `ADDITIONAL` when applicable. |
| data.quantity | number | Units allotted or sold. |
| data.price | number | Price or NAV when available. |
| data.last_price | number | Last known NAV. |
| data.average_price | number | Allotted or sold NAV. |
| data.last_price_date | string | Date for last NAV when available in format: `YYYY-MM-DD` . |

### Error Codes

Errors follow the [standard API error format](https://upstox.com/developer/api-documentation/error-codes) . Ensure the request is authenticated and your account has access to mutual fund data.

---

## Get Mutual Fund SIPs

This API provides the mutual fund SIP registrations for the user. Use `page_number` and `records` for pagination.

### Endpoint

**GET** `https://api.upstox.com/v2/mf/sips`

### Query Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| page_number | Optional | integer | Page number, starting from `1` . Default: `1` |
| records | Optional | integer | Records per page. Default: `10` , Max: `30` . |

### Response

```json
{
    "status": "success",
    "data": [
        {
            "instrument_key": "INF179KB15Q6",
            "fund": "HDFC Ultra S/T Fund Direct Growth",
            "dividend_type": "Growth",
            "status": "ACTIVE",
            "created": "2025-03-11 00:00:00.0",
            "frequency": "MONTHLY",
            "instalments": 999,
            "sip_id": "133321093",
            "transaction_type": "BUY",
            "next_instalment": "2025-04-11 00:00:00.0",
            "instalment_amount": 300.0,
            "last_instalment": "2025-03-11 00:00:00.0",
            "pending_instalments": 0,
            "instalment_day": 11,
            "trigger_price": 0.0,
            "sip_type": "Auto",
            "completed_instalments": 0
        },
        {
            "instrument_key": "INF174K01JI7",
            "fund": "Kotak Bond Short Term Plan Direct Growth",
            "dividend_type": "Growth",
            "status": "ACTIVE",
            "created": "2025-03-11 00:00:00.0",
            "frequency": "MONTHLY",
            "instalments": 999,
            "sip_id": "133321205",
            "transaction_type": "BUY",
            "next_instalment": "2025-04-11 00:00:00.0",
            "instalment_amount": 1000.0,
            "last_instalment": "2025-03-11 00:00:00.0",
            "pending_instalments": 0,
            "instalment_day": 30,
            "trigger_price": 0.0,
            "sip_type": "Auto",
            "completed_instalments": 1
        }
    ],
    "meta_data": {
        "page": {
            "page_number": 1,
            "total_pages": 1,
            "records": 10,
            "total_records": 2
        }
    }
}
```

| Name | Type | Description |
| --- | --- | --- |
| status | string | Outcome of the request. |
| data | array | SIP rows. |
| data[].sip_id | string | SIP identifier. |
| data[].instrument_key | string | Fund ISIN when available. |
| data[].fund | string | Scheme display name. |
| data[].dividend_type | string | Dividend option: `Dividend Payout` , `Dividend Reinvestment` , or `Growth` . |
| data[].transaction_type | string | Typically `BUY` or `SELL` . |
| data[].status | string | SIP status: `ACTIVE` , `ARCHIVED` , `CANCEL_REQUESTED` , `CANCELLED` , `CREATED` , `FAILED` , `NEW` , `PAUSE` , `PAUSED` , `PENDING` , `REGISTERED` , `REJECTED` , or `SUSPENDED` . |
| data[].created | string | When the SIP was registered in format: `YYYY-MM-DD HH:mm:ss` . |
| data[].frequency | string | Typically `MONTHLY` or `WEEKLY` . |
| data[].next_instalment | string | Next instalment date in format: `YYYY-MM-DD` . |
| data[].instalment_amount | number | Amount per instalment. |
| data[].instalments | integer | Total instalments, or `-1` when open-ended. |
| data[].last_instalment | string | Last triggered instalment time in format: `YYYY-MM-DD` . |
| data[].pending_instalments | integer | Pending count when applicable. |
| data[].instalment_day | integer | Day of month for monthly SIPs when applicable. |
| data[].completed_instalments | integer | Completed count when available. |
| data[].trigger_price | number | Trigger price when applicable. |
| data[].sip_type | string | SIP type: `Manual` or `Auto` . |
| meta_data | object | Pagination metadata (same shape as orders API). |
| meta_data.page | object | Page metadata. |
| meta_data.page.page_number | integer | Current page. |
| meta_data.page.total_pages | integer | Total pages. |
| meta_data.page.records | integer | Page size used. |
| meta_data.page.total_records | integer | Total rows across pages. |

### Error Codes

| Error code | Description |
| --- | --- |
| UDAPI1173 | **Page records exceeds limit** — `records` must not exceed 30. |
| UDAPI1174 | **Page number must be greater than or equal to 1** — `page_number` must be at least 1. |
| UDAPI1196 | **Records must be greater than or equal to 1** — `records` must be at least 1. |
