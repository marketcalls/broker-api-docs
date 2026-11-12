# Rate Limits

Rate limits are enforced at the API gateway level. Exceeding any limit returns HTTP `429 Too Many Requests`. See [Common Errors](https://developer.tradejini.com/docs/common-errors) for how to handle 429 responses.

## REST API Limits

There are five independent rate-limit zones. A request may be subject to more than one zone simultaneously — all applicable limits must be satisfied.

| Zone | Applies to | Limit | Scope |
| --- | --- | --- | --- |
| OTP limit | Individual Token endpoint (`POST /api-gw/oauth/individual-token-v2`) | **3 req / second** | Per client IP address |
| API key limit | Unauthenticated endpoints that accept only an API key (e.g. OAuth token exchange) | **100 req / second** | Per `api_key` |
| Data fetch limit | Market data and account data endpoints | **100 req / second** | Per auth token |
| Place Order limit | Place Order (`POST /api/oms/place-order`) | **10 req / second** | Per auth token |
| General API limit | All other authenticated endpoints | **10 req / second** and **400 req / minute** | Per auth token |

### How multiple limits interact

The per-second and per-minute general limits apply together. You can burst at 10 req/sec, but you cannot sustain that rate for more than 40 seconds in a minute before the 400 req/min ceiling kicks in.

```
Sustainable throughput  = 400 req/min  ≈  6.7 req/sec average
Peak throughput (burst) = 10 req/sec   (short bursts only)
```

## WebSocket Limits

| Resource | Limit |
| --- | --- |
| Concurrent WebSocket connections | **5 per user** |
| Instrument subscriptions per connection | **3,000 instruments** |

## Session Limits

| Resource | Limit |
| --- | --- |
| Active login sessions | **10 per user** |

## Best Practices

- **Implement exponential backoff** when you receive a 429. Start with a 1-second delay and double on each retry (1s → 2s → 4s → 8s).
- **Respect the minute-level cap.** Even if individual calls are under 10 req/sec, sustained throughput above ~6.7 req/sec will eventually trigger the 400 req/min limit on general endpoints.
- **Separate OTP calls from other traffic.** The OTP limit is IP-based and stricter (3 req/sec) — unrelated API calls do not consume this quota, but your server's IP is the scope, so multiple users sharing an IP each count against it.
- **Cache symbol data.** The Scrip Master Data endpoint returns large payloads — download once per session start and cache locally rather than fetching repeatedly.
- **Batch order margin checks** using `POST /api/oms/basket-margin` instead of calling the single-order margin endpoint in a loop.
- **Use WebSocket streaming** for real-time quotes and order updates instead of polling REST market-data endpoints.

Visit our [FAQ](https://developer.tradejini.com/faq) page for more information and solutions.
