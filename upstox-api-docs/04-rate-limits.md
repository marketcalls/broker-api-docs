# Rate Limits

Upstox implements rate limiting to maintain service reliability and ensure fair access. These constraints apply on a per-API, per-user basis, as established per NSE circular from May 5, 2025.

## Order Placement APIs Rate Limits

Rate limits apply to Place, Modify, Cancel, Multi Order, and GTT Order endpoints.

### Regular Algos (No Registration Required)

| Time Duration | Request Limit |
|---|---|
| Per second | 10 requests |
| Per minute | 500 requests |
| Per 30 minutes | 2000 requests |

### SEBI-Registered Algos (Registration Required)

| Time Duration | Request Limit |
|---|---|
| Per second | 50 requests |
| Per minute | 500 requests |
| Per 30 minutes | 2000 requests |

## Standard APIs Rate Limits

These limits apply to holdings, positions, funds, historical candles, and similar endpoints.

| Time Duration | Request Limit |
|---|---|
| Per second | 50 requests |
| Per minute | 500 requests |
| Per 30 minutes | 2000 requests |

## Important Notice

Please adhere to these limits to avoid potential disruptions in service. Exceeding these limits might result in temporary suspension of access.

The framework distinguishes between retail investor algo types, with SEBI-registered algorithms receiving higher per-second allowances while maintaining consistent minute and 30-minute thresholds.
