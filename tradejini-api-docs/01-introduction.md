# Introduction

The Tradejini REST API is a set of HTTP APIs that provide everything needed to build a trading platform — order management, market data, account information, and real-time streaming. The APIs are language-agnostic and work with any HTTP client.

**Base URL:** `https://api.tradejini.com/v2`

## Getting Started

Follow these steps to make your first API call:

1. **Create a Tradejini trading account** — An active retail trading account is required before API access can be enabled.
2. **Register an app** in the [Apps](https://developer.tradejini.com/developer-portal) to obtain your `api_key` and `api_secret`. See [App Creation](https://developer.tradejini.com/docs/app-creation/individual-apps) for step-by-step instructions.
3. **Authenticate** using the appropriate flow for your app type. See [Authorization Flow](https://developer.tradejini.com/docs/authorization-flow/individual-apps) for a walkthrough.
4. **Make authenticated API calls** by passing `Authorization: Bearer <api_key>:<access_token>` in every request. See [API Basics](https://developer.tradejini.com/docs/api-basics) for the full request/response reference.

## Documentation Map

| Section | What you'll find |
| --- | --- |
| [API Basics](https://developer.tradejini.com/docs/api-basics) | Base URL, authentication header format, request/response conventions, field codes |
| [App Creation](https://developer.tradejini.com/docs/app-creation/individual-apps) | How to register an app and obtain API credentials |
| [Authorization Flow](https://developer.tradejini.com/docs/authorization-flow/individual-apps) | Step-by-step auth walkthroughs for Individual and Third-Party apps |
| [Authorization](https://developer.tradejini.com/docs/authorization/updatedIndividualToken) | Auth API endpoint reference |
| [Account](https://developer.tradejini.com/docs/account/getUserDetails) | User profile and session management |
| [Symbol Details](https://developer.tradejini.com/docs/symbol-details/getSymbolDetails) | Look up instrument IDs (`symId`) required for order placement |
| [Funds](https://developer.tradejini.com/docs/funds/retrieveFundsLimits) | Available margin and cash balances |
| [Orders](https://developer.tradejini.com/docs/orders/getOrders) | Place, modify, cancel, and track orders |
| [Advance Orders](https://developer.tradejini.com/docs/advance-orders/placeBracketOrder) | Bracket, Cover, GTT, and OCO order types |
| [Chart Data](https://developer.tradejini.com/docs/chart-data/getIntervalChartData) | Historical OHLCV candle data |
| [WebSocket SDKs](https://developer.tradejini.com/docs/websocket-sdks) | Real-time market data and order update streaming |
| [Rate Limits](https://developer.tradejini.com/docs/rate-limits) | Request limits per endpoint type |
| [Common Errors](https://developer.tradejini.com/docs/common-errors) | All error codes with causes and resolutions |
| [Market Hours](https://developer.tradejini.com/docs/market-hours) | Trading hours and session timings for supported exchanges and segments |
