# Rate Limits

Per-session order-per-second (OPS) rate limits, differing by whether the session is registered for more than 10 orders/second (see [Introduction](01-introduction.md)).

| API | Non-Registered (< 10 OPS) | Registered (> 10 OPS) |
| --- | --- | --- |
| **User** | | |
| Logout | 2 | 2 |
| Get User Session | 3 | 3 |
| Profile | 3 | 3 |
| Limits | 10 | 20 |
| **Margin** | | |
| Pre-order Margin | 10 | 20 |
| SPAN Exposure | 10 | 20 |
| **Order Management** | | |
| Place Order | 10 (combined rate limit across place/modify/cancel) | 20 |
| Modify Order | — | 20 |
| Cancel Order | — | 20 |
| Cancel All Orders | 3 | 3 |
| Get Order Book | 3 | 3 |
| Get Order History | 10 | 10 |
| Trade Book | 3 | 3 |
| **Portfolio** | | |
| Positions | 3 | 3 |
| Holdings | 3 | 3 |
| **Market Data API** | | |
| Historical Data | 10 | 10 |
| Market Depth | 10 | 10 |
| Open Interest | 10 | 20 |
| Market Quotes | 10 | 10 |
| **Contract Master APIs** | | |
| NSEEQ / NSEFO / NSECOMM / MCXCOMM / INDICES / NSECURR / BSEEQ / BSEFO / BSECURR | 2 each | 2 each |
