# IIFL Capital (Markets' APIs) Documentation

> **Unofficial Markdown conversion** of the IIFL Markets' API documentation, sourced from the official developer portal:
> <https://developers.iiflcapital.com/apidocs/introduction>

IIFL Markets' APIs provide REST-like trading solutions for retail traders and fintech platforms — order execution/modification/cancellation, portfolio management, live market data (REST and binary WebSocket streaming), and brokerage/charges calculation.

## Base URLs

| Purpose | Base URL |
| --- | --- |
| REST API | `https://api.iiflcapital.com/v1` |
| Market Data / Order & Trade Update Stream (Bridge Package) | `bridge.iiflcapital.com:8883` |
| Brokerage & Charges — Cash/F&O | `https://brkschemeapp.azurewebsites.net/api/brokerageScheme` |
| Brokerage & Charges — Commodity | `https://brkschemeapp-points.azurewebsites.net/api/brokerageScheme` |
| Login | `https://markets.iiflcapital.com/?v=1&appkey=<appKey>&redirecturl=<url>` |
| Token Exchange | `https://api.iiflcapital.com/v1/getusersession` |

## Table of Contents

| # | Document | Description |
| --- | --- | --- |
| 01 | [Introduction](01-introduction.md) | Overview, base URL, video tutorials, instrument master files, Postman/SDKs |
| 02 | [Request and Response Structure](02-request-response-structure.md) | Request/response conventions used across all endpoints |
| 03 | [User](03-user.md) | Login flow, session generation, profile, limits, logout |
| 04 | [Margin](04-margin.md) | Pre-order margin and SPAN/exposure margin calculators |
| 05 | [Order Management](05-orders.md) | Place/modify/cancel orders, order book, order history, trade book |
| 06 | [Order and Trade Updates](06-order-and-trade-updates.md) | Real-time order/trade push events via the Bridge Package |
| 07 | [Portfolio](07-portfolio.md) | Holdings and positions |
| 08 | [Market Data Stream](08-market-data-stream.md) | Binary WebSocket-style events: feed, OI, market status, circuits, LPP, 52-week high/low |
| 09 | [Market Data APIs](09-market-data-apis.md) | Historical candles, market quotes, market depth, open interest |
| 10 | [Brokerage and Charges APIs](10-brokerage-and-charges.md) | Cash, F&O, and commodity charge calculators |
| 11 | [Binary Decoding Guide](11-binary-decoding-guide.md) | Converting a raw Market Data Stream payload to decimal values |
| 12 | [Error Codes](12-error-codes.md) | Trading API error codes (`EC0xx`–`EC9xx`) |
| 13 | [Python SDK Codes](13-python-sdk-codes.md) | Bridge Package status, result, and packet-type codes |
| 14 | [RMS Order Rejections](14-rms-rejections.md) | Risk Management System rejection message formats |
| 15 | [Rate Limits](15-rate-limits.md) | Per-session order-per-second limits by endpoint |
| 16 | [FAQs](16-faq.md) | Frequently asked questions |

## Notes

- Authenticate every request (except `GET`-able instrument JSON files) with `Authorization: Bearer <userSession>`.
- `GET`/`DELETE` requests take query parameters; `POST`/`PUT` requests take a raw JSON body.
- A fresh login (and `userSession` token) is required every trading day.
