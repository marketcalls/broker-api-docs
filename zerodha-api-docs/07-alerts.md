# Alerts API

Maximum 500 active alerts per user.

## Endpoints

| Method | Endpoint | Purpose |
|--------|----------|---------|
| POST | `/alerts` | Create new alert |
| GET | `/alerts` | Retrieve all alerts |
| GET | `/alerts/{uuid}` | Get specific alert |
| PUT | `/alerts/{uuid}` | Modify alert |
| DELETE | `/alerts?uuid={uuid}` | Delete alert(s) |
| GET | `/alerts/{uuid}/history` | Alert trigger history |

## Alert Types

- **Simple:** Standard price notification
- **ATO:** Automatically executes an order when triggered

## Required Parameters

| Parameter | Description |
|-----------|-------------|
| `name` | Alert description |
| `type` | `simple` or `ato` |
| `lhs_exchange` | Exchange code (NSE, BSE, NFO, CDS, BCD, MCX, INDICES) |
| `lhs_tradingsymbol` | Instrument trading symbol |
| `lhs_attribute` | Monitored attribute (e.g., LastTradedPrice) |
| `operator` | `<=`, `>=`, `<`, `>`, `==` |
| `rhs_type` | `constant` or `instrument` |
| `rhs_constant` | Comparison value (for constant type) |
| `basket` | JSON config (ATO alerts only) |

## Alert States

- `enabled` - Active and being evaluated
- `disabled` - Not being evaluated
- `deleted` - Soft-deleted by user

## Pagination

Query params: `status`, `page`, `page_size`
