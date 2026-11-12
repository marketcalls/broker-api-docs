# Samco (Trade API v3.2) Documentation

> **Unofficial Markdown conversion** of the Samco Trade API documentation, sourced from the official developer portal:
> <https://docs-tradeapi.samco.in/>

Samco's Trade API is a REST + WebSocket trading API covering order placement (regular, bracket, cover, GTT/OCO, basket), portfolio and position management, market data (quotes, depth, option/future chains), intraday and historical candles, live streaming ticks, and trade analytics. Authentication is via a daily `x-session-token` JWT obtained either server-to-server or through an OAuth 2.1 authorization-code flow.

## Base URLs

| Purpose | Base URL |
| --- | --- |
| REST API | `https://tradeapi.samco.in` |
| WebSocket streaming (market depth & quotes) | `wss://stream.samco.in` |
| Web Dashboard (OAuth apps, static IPs) | `https://tradeapi.samco.in/app/login` |
| OAuth authorize page | `https://tradeapi.samco.in/app/oauth/authorize` |

Every authenticated request carries the session token in the `x-session-token` header.

## Table of Contents

| # | Document | Description |
| --- | --- | --- |
| 01 | [Introduction](01-introduction.md) | Setup flow, supported runtimes, token lifetime, deprecated-API migration table |
| 02 | [Release Notes](02-release-notes.md) | What changed in v3.2.0 |
| 03 | [Getting Started — Web Dashboard](03-dashboard.md) | Dashboard user manual, API keys / OAuth apps, static IP registration |
| 04 | [Authentication](04-authentication.md) | `POST /session/token`, OAuth 2.1 authorization-code flow, login code, logout |
| 05 | [IP Diagnostics](05-ip-diagnostics.md) | `GET /ip/whoami` — the public IP Samco sees for your requests |
| 06 | [Account and Limits](06-account-and-limits.md) | User limits / margin, personal index |
| 07 | [Market Data](07-market-data.md) | Market depth, contract analyser, symbol search, option & future chains, quotes |
| 08 | [Orders](08-orders.md) | Span margin, place/modify/cancel regular, BO and CO orders, order book, order status, trigger orders, bulk order |
| 09 | [GTT and OCO Orders](09-gtt-orders.md) | Add/modify/delete GTT and OCO, list GTT & OCO |
| 10 | [Basket Orders](10-basket-orders.md) | Create/modify/delete/list baskets and basket orders, rearrange, execute, span calculator |
| 11 | [Portfolio](11-portfolio.md) | Positions, position conversion, square-off, holdings, trade book |
| 12 | [Candle Data](12-candle-data.md) | Intraday and historical candles for scrips and indices |
| 13 | [Streaming Data](13-streaming-data.md) | WebSocket market depth and quote streams |
| 14 | [Trade View Analytics](14-analytics.md) | Analytics summary, analytics details, gain/loss |
| 15 | [Publisher](15-publisher.md) | Publisher app creation, offsite order execution, JS plugin, demo |
| 16 | [Deprecated APIs](16-deprecated-apis.md) | Legacy login / 2FA / static-IP endpoints, kept for reference |

## Endpoint Index

| Method | Endpoint | Section |
| --- | --- | --- |
| POST | `/session/token` | [Authentication](04-authentication.md#generate-session-token) |
| GET | `/webSecretCode` | [Authentication](04-authentication.md#login-code) |
| POST | `/webSecretCodeValidation` | [Authentication](04-authentication.md#login-code-validation) |
| GET | `/ip/whoami` | [IP Diagnostics](05-ip-diagnostics.md#who-am-i) |
| GET | `/limit/getLimits` | [Account and Limits](06-account-and-limits.md#user-limits) |
| GET | `/indexData` | [Account and Limits](06-account-and-limits.md#personal-index) |
| POST | `/marketDepth` | [Market Data](07-market-data.md#market-depth) |
| POST | `/contractsAnalyser` | [Market Data](07-market-data.md#contract-analyser) |
| GET | `/eqDervSearch/search` | [Market Data](07-market-data.md#search-equity-scrips) |
| GET | `/option/optionChain` | [Market Data](07-market-data.md#option-chain) |
| GET | `/future/futureChain` | [Market Data](07-market-data.md#future-chain) |
| GET | `/quote/indexQuote` | [Market Data](07-market-data.md#index-quote) |
| GET | `/quote/getQuote` | [Market Data](07-market-data.md#get-quote) |
| POST | `/quote/multiQuote` | [Market Data](07-market-data.md#multi-quote) |
| POST | `/spanMargin` | [Orders](08-orders.md#span-margin) |
| POST | `/order/placeOrder` | [Orders](08-orders.md#place-order) |
| POST | `/order/placeOrderBO` | [Orders](08-orders.md#place-bo-order) |
| POST | `/order/placeOrderCO` | [Orders](08-orders.md#place-co-order) |
| GET | `/order/getOrderStatus` | [Orders](08-orders.md#get-order-status) |
| GET | `/order/orderBook` | [Orders](08-orders.md#order-book) |
| GET | `/order/getTriggerOrders` | [Orders](08-orders.md#triggerorders) |
| PUT | `/order/modifyOrder/{orderNumber}` | [Orders](08-orders.md#modify-order) |
| DELETE | `/order/exitBO` | [Orders](08-orders.md#cancel-bo-order) |
| DELETE | `/order/exitCO` | [Orders](08-orders.md#cancel-co-order) |
| DELETE | `/order/cancelOrder` | [Orders](08-orders.md#cancel-order) |
| POST | `/order/bulkOrder` | [Orders](08-orders.md#bulk-order) |
| POST | `/gttoco/addGtt` | [GTT and OCO](09-gtt-orders.md#add-gtt) |
| PUT | `/gttoco/modifyGtt` | [GTT and OCO](09-gtt-orders.md#modify-gtt) |
| DELETE | `/gttoco/deleteGtt` | [GTT and OCO](09-gtt-orders.md#delete-gtt) |
| POST | `/gttoco/addOco` | [GTT and OCO](09-gtt-orders.md#add-oco) |
| PUT | `/gttoco/modifyOco` | [GTT and OCO](09-gtt-orders.md#modify-oco) |
| DELETE | `/gttoco/deleteOco` | [GTT and OCO](09-gtt-orders.md#delete-oco) |
| GET | `/gttoco/listGttOco` | [GTT and OCO](09-gtt-orders.md#list-gtt-oco) |
| POST | `/basket/createBasket` | [Basket Orders](10-basket-orders.md#create-basket) |
| PUT | `basket/modifyBasket` | [Basket Orders](10-basket-orders.md#modify-basket) |
| DELETE | `basket/deleteBasket` | [Basket Orders](10-basket-orders.md#delete-basket) |
| GET | `basket/listBasket` | [Basket Orders](10-basket-orders.md#list-basket) |
| POST | `basket/createOrder` | [Basket Orders](10-basket-orders.md#create-basket-order) |
| PUT | `basket/modifyBasketOrder` | [Basket Orders](10-basket-orders.md#modify-basket-order) |
| DELETE | `basket/deleteBasketOrder` | [Basket Orders](10-basket-orders.md#delete-basket-order) |
| POST | `basket/executeBasketOrder` | [Basket Orders](10-basket-orders.md#execute-basket-order) |
| GET | `basket/listBasketOrder` | [Basket Orders](10-basket-orders.md#list-basket-order) |
| POST | `basket/rearrangeBasketOrder` | [Basket Orders](10-basket-orders.md#rearrange-basket-order) |
| POST | `basket/spanCalculator` | [Basket Orders](10-basket-orders.md#basket-margin-calculator) |
| GET | `/position/getPositions` | [Portfolio](11-portfolio.md#user-positions) |
| POST | `/position/convertPosition` | [Portfolio](11-portfolio.md#position-conversion) |
| POST | `/position/squareOff` | [Portfolio](11-portfolio.md#position-square-off) |
| GET | `/holding/getHoldings` | [Portfolio](11-portfolio.md#user-holdings) |
| GET | `/trade/tradeBook` | [Portfolio](11-portfolio.md#trade-book) |
| GET | `/intraday/candleData` | [Candle Data](12-candle-data.md#intraday-candle-data) |
| GET | `/intraday/indexCandleData` | [Candle Data](12-candle-data.md#index-intraday-candle-data) |
| GET | `/history/candleData` | [Candle Data](12-candle-data.md#historical-candle-data) |
| GET | `/history/indexCandleData` | [Candle Data](12-candle-data.md#index-historical-candledata) |
| WSS | `wss://stream.samco.in` | [Streaming Data](13-streaming-data.md) |
| POST | `tradeview/analyticsSummary` | [Analytics](14-analytics.md#analytics-summary-api) |
| POST | `tradeview/analyticsDetails` | [Analytics](14-analytics.md#analytics-details) |
| POST | `tradeview/gainLoss` | [Analytics](14-analytics.md#gain-loss) |

Deprecated endpoints (`POST /login`, `/otp/generateOtp`, `/otp/secretKeyGenerator`, `/accessToken/token`, `/ip/ipRegistration`, `/ip/ipUpdate`) are documented in [16-deprecated-apis.md](16-deprecated-apis.md).

## Notes

- **Session tokens expire at 08:00 IST the next calendar day**, regardless of how they were obtained. Re-authenticate daily.
- **Static IP registration is mandatory** for order-related APIs — requests from unregistered IPs are rejected. SEBI mandates a 7-day cooldown on IP changes.
- The **API Secret is displayed only once** when an OAuth app is created in the Web Dashboard; regenerating it invalidates all active sessions for that app.
- Symbols come from `ScripMaster.csv` — pass `name` for equity cash symbols and `tradingSymbol` for all F&O contracts.
- Samco does **not** provide a sandbox. Every successful call affects live positions and balances.
- Screenshots referenced in [03-dashboard.md](03-dashboard.md) remain hot-linked to `https://docs-tradeapi.samco.in/assets/...`.
- [15-publisher.md](15-publisher.md) ends with a live interactive demo page; only its prose survives conversion, since the buttons are rendered by JavaScript.
