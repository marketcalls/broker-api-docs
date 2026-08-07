# Smart Orders (GTT)

> Source: https://api-docs.indstocks.com/smart_orders/

Smart Orders let you attach **stop-loss** and **target** legs (GTT / OCO) to an entry order.
They operate as linked **parent–child** pairs: the parent order executes first on the
exchange, then activates the child GTT order that holds the stop-loss and target legs.

**Order ID prefixes:** `EQ-` (equity parent), `DRV-` (derivative parent), `GTT-` (child).

## Endpoints Overview

| Method | Endpoint | Purpose |
|--------|----------|---------|
| POST | `/smart/order` | Create a multi-leg smart order |
| POST | `/smart/order/modify` | Modify a pending smart order |
| POST | `/smart/order/cancel` | Cancel a pending smart order |

---

## Place Smart Order

**Endpoint:** `POST /smart/order`

### Required Parameters

| Parameter | Type | Details |
|-----------|------|---------|
| `txn_type` | string | `"BUY"` or `"SELL"` |
| `exchange` | string | `"NSE"` |
| `segment` | string | `"EQUITY"` or `"DERIVATIVE"` |
| `product` | string | Equity: `"CNC"` / `"INTRADAY"`; Derivative: `"MARGIN"` / `"INTRADAY"` |
| `order_type` | string | `"LIMIT"`, `"MARKET"`, or `"TRIGGER"` |
| `validity` | string | `"DAY"` |
| `security_id` | string | Instrument identifier |
| `qty` | integer | Trade quantity |
| `algo_id` | string | `"99999"` for NSE |

### Conditional / Optional Parameters

| Parameter | Type | Details |
|-----------|------|---------|
| `limit_price` | number | Required for `LIMIT` orders |
| `trigger_price` | number | Required for `TRIGGER` orders; must be above (BUY) / below (SELL) CMP |
| `trigger_limit_price` | number | Optional trigger-limit price |
| `sl_trigger_price` | number | Stop-loss trigger; requires `sl_limit_price` |
| `sl_limit_price` | number | Stop-loss execution price |
| `tgt_trigger_price` | number | Target trigger; requires `tgt_limit_price` |
| `tgt_limit_price` | number | Target execution price |

### Response

Placement returns both the parent and its child order in a unified response:

```json
{
  "status": "success",
  "data": {
    "order_data": [
      {
        "order_id": "DRV-28131451",
        "order_status": "CREATED",
        "child_order_details": {
          "order_id": "GTT-2914581",
          "order_status": "CREATED"
        }
      }
    ]
  }
}
```

---

## Modify Smart Order

**Endpoint:** `POST /smart/order/modify`

### Required Parameters

| Parameter | Type | Details |
|-----------|------|---------|
| `order_id` | string | Order identifier |
| `segment` | string | `"EQUITY"` or `"DERIVATIVE"` |
| `algo_id` | string | `"99999"` |

### Optional Parameters

`order_type`, `qty`, `limit_price`, `trigger_price`, `trigger_limit_price`,
`sl_trigger_price`, `sl_limit_price`, `tgt_trigger_price`, `tgt_limit_price`

> ⚠️ The `order_type` in a modification request must match the existing order type, otherwise
> the request is rejected.

---

## Cancel Smart Order

**Endpoint:** `POST /smart/order/cancel`

### Required Parameters

| Parameter | Type | Details |
|-----------|------|---------|
| `order_id` | string | Order identifier |
| `segment` | string | `"EQUITY"` or `"DERIVATIVE"` |

> Parent and child orders must be cancelled **separately** using their respective order IDs.

---

## Behaviour & Constraints

- **MARKET** orders auto-convert to **LIMIT** at the live price.
- Omitting `trigger_limit_price` defaults it to equal `trigger_price`, so the order executes
  as a trigger-limit.
- Both the stop-loss and target legs require their corresponding `*_limit_price`.
- Child (GTT) orders activate **only after** the parent order executes. If the parent is
  cancelled or rejected, the child never activates.
- Parent and child orders are managed independently — modify or cancel each with its own
  order ID.

### Validation Rules

- Quantity must be above zero, within the freeze limit, and a multiple of the lot size.
- Trigger prices must be multiples of the instrument's **tick size**.
- **BUY** triggers must be **above** the current market price; **SELL** triggers must be
  **below** it.
- The stop-loss trigger must be **less than** the stop-loss limit price.
- The target trigger must be **greater than** the entry limit price.

> Smart orders remain active for up to **365 days**, or until the trigger fires, you cancel
> them, or the instrument expires.
