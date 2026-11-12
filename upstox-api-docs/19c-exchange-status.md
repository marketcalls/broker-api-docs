# Exchange Status API

## Endpoint

**GET** `https://api.upstox.com/v2/market/status/{exchange}`

## Response

```json
{
  "status": "success",
  "data": {
    "exchange": "NSE",
    "status": "NORMAL_OPEN",
    "last_updated": 1705549500000
  }
}
```

## Error Codes

| Code | Description |
|------|-------------|
| UDAPI1089 | Invalid exchange |

## Closing Auction Session (CAS)

Effective 3 August 2026, the response carries an optional `cas_eligible_status` object for CAS-eligible segments (for example `NSE_EQ`). It is omitted for segments where CAS does not exist (for example `NSE_FO`).

| Field | Type | Description |
|-------|------|-------------|
| cas_eligible_status.status | string | Current closing auction phase |
| cas_eligible_status.last_updated | number | Timestamp of the last status change (ms) |

### CAS Status Values

| Time (IST) | Status | Meaning for order flow |
|------------|--------|------------------------|
| ~3:15 PM | `CTS_CLOSE` | Continuous trading closes for CAS-eligible securities |
| ~3:20 PM | `CAS_LM_START` | Closing auction opens; limit and market orders accepted |
| ~3:25 PM | `CAS_M_STOP` | Market-order entry restricted; limit orders continue |
| 3:28-3:30 PM | `CAS_STOP` | Order-entry window ends (randomised) |
| 3:30 PM | `NORMAL_CLOSE` | Market closes |

### Order Restrictions During CAS

- Stop-loss (`SL`, `SL-M`) orders are rejected at every phase of the auction.
- Immediate-or-Cancel (IOC) orders are not allowed.
- Order slicing is prohibited.
- GTT triggers for CAS stocks operate only until 3:15 PM.
- Unexecuted limit orders from the continuous session carry forward with price-time priority retained.
- Orders must fall within **±3% of the reference price**, including futures on CAS-eligible underlyings.

Rely on the `cas_eligible_status` value rather than parsing rejection message text.
