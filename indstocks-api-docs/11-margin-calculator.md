# Margin Calculator

> Source: https://api-docs.indstocks.com/margin_calculation/

Calculates the margin required and estimated charges for a prospective order before you place
it.

## Calculate Margin

**Endpoint:** `GET /margin`

**Full URL:** `https://api.indstocks.com/margin`

### Request Parameters

| Parameter | Type | Required | Details |
|-----------|------|----------|---------|
| `segment` | string | ✅ | `"DERIVATIVE"`, `"EQUITY"` |
| `exchange` | string | ✅ | `"NSE"`, `"BSE"` |
| `securityID` | string | ✅ | Instrument identifier |
| `txnType` | string | ✅ | `"BUY"`, `"SELL"` |
| `quantity` | string | ✅ | Trade quantity |
| `price` | string | ✅ | Per-unit price |
| `product` | string | ✅ | `"MARGIN"`, `"INTRADAY"`, `"CNC"` |

### Request

```bash
GET https://api.indstocks.com/margin
Authorization: YOUR_ACCESS_TOKEN
Content-Type: application/json

{
  "segment": "DERIVATIVE",
  "txnType": "BUY",
  "quantity": "75",
  "price": "10",
  "product": "MARGIN",
  "securityID": "40131",
  "exchange": "NSE"
}
```

### Response

```json
{
  "status": "success",
  "data": {
    "total_margin": 750,
    "span_margin": 0,
    "hedge_benefit": 0,
    "exposure_margin": 0,
    "available_balance": 0,
    "var_margin": 0,
    "insufficient_balance": 0,
    "delivery_margin": 0,
    "brokerage": 0,
    "charges": {
      "stt": 0,
      "exchange_charges": 0,
      "stamp_duty": 0,
      "sebi_turn_over_charges": 0,
      "brokerage": 5,
      "gst": 0.9,
      "IPFTCharges": 0,
      "total_charges": 5.9
    }
  }
}
```

### Response Fields

| Field | Description |
|-------|-------------|
| `total_margin` | Total margin required for the order |
| `span_margin` | SPAN margin (derivatives) |
| `exposure_margin` | Exposure margin (derivatives) |
| `hedge_benefit` | Margin benefit from hedged positions |
| `var_margin` | Value-at-Risk margin |
| `delivery_margin` | Delivery margin (equity CNC) |
| `available_balance` | Balance available to fund the order |
| `insufficient_balance` | Shortfall, if any |
| `brokerage` | Brokerage component |
| `charges` | Breakdown of statutory & platform charges (STT, exchange, stamp duty, SEBI turnover, brokerage, GST, IPFT, and total) |
