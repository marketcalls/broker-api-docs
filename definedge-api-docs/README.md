# Definedge Securities INTEGRATE API Documentation

> **Unofficial Markdown conversion** of the Definedge Securities **INTEGRATE** trading API documentation, sourced from the official documentation portal:
> <https://www.definedgesecurities.com/api-documentation/>

The INTEGRATE API lets you build trading and investment platforms, execute and modify orders in real time across equities, derivatives, currencies and commodities, manage portfolios, and access live market data.

> **Note:** Data from the Integrate API and Websocket is intended for **personal use only**. Distribution of this data is strictly prohibited.

## Base URLs

| Purpose | Base URL |
| --- | --- |
| Trading APIs (buy, sell, order book, trade book, etc.) | `https://integrate.definedgesecurities.com/dart/v1` |
| Login Step 1 / Step 2 | `https://signin.definedgesecurities.com/auth/realms/debroking/dsbpkc` |
| Historical Data | `https://data.definedgesecurities.com/sds/history` |
| Master Files | `https://app.definedgesecurities.com/public` |
| WebSocket (market data) | `wss://trade.definedgesecurities.com/NorenWSTRTP/` |

> All endpoint paths and JSON keys are **case-sensitive**. Use them exactly as shown.

## Table of Contents

| # | Document | Description |
| --- | --- | --- |
| 01 | [Introduction](01-introduction.md) | API overview, base URL, Python client library |
| 02 | [Authentication](02-authentication.md) | Two-step 2FA login and API session key |
| 03 | [Master File](03-master-file.md) | Daily symbol master file downloads |
| 04 | [Historical Data](04-historical-data.md) | Daily / intraday / tick historical data |
| 05 | [Orders](05-orders.md) | Place, modify, cancel, slice orders; order/trade book; product conversion |
| 06 | [Portfolio](06-portfolio.md) | Position book and holdings |
| 07 | [GTT & OCO Orders](07-gtt-oco-orders.md) | GTT and OCO order book, place, modify, cancel |
| 08 | [Funds & Margin](08-funds-margin.md) | Limits, order margin, span calculator |
| 09 | [Market Data](09-market-data.md) | Quotes and security information |
| 10 | [WebSocket API](10-websocket.md) | Touchline and market depth streaming |
| 11 | [Order Update WebSocket](11-order-update-websocket.md) | Real-time order status streaming |
| 12 | [Error Codes](12-error-codes.md) | HTTP and business error codes |
| 13 | [Appendix](13-appendix.md) | Reference constants and enumerations |

## Support

- Customer Support: 020-61923200, care@definedge.com
- Call and Trade: 020-61923220
