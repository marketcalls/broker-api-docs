# Upstox Developer API - Overview

Develop your app on the Upstox platform, utilizing a robust collection of REST APIs that deliver the necessary data for building a comprehensive investment and trading platform. With this API set, you can execute real-time orders, effectively manage user portfolios, stream live market data via Websockets, and more.

## Documentation Sections

| Section | Description |
|---------|-------------|
| Sandbox | Test your trading app in the Upstox API sandbox environment |
| Authentication | OAuth 2.0 authentication flow |
| API Structure | Request/response formats and error codes |
| Rate Limits | Per-second, per-minute, and per-user limits |
| SDK | Multi-language SDK support (Python, Java, Node.js, PHP, .NET) |
| MCP Integration | AI assistant integration via Model Context Protocol |
| Agent Integration | Agent quickstart, Agent Skills, Claude plugin marketplace |
| Instruments | Instrument files and search |
| Expired Instruments | Historical F&O contract data |
| Login | Authorization, token management, logout |
| User | Profile and fund/margin details (V2 and V3) |
| Kill Switch | Segment-level trading halt for risk management |
| Static IP Management | Register and update user-level static IPs |
| Payments | Payin history, payout requests and management |
| Charges | Brokerage calculation |
| Margins | Margin calculation for orders |
| Orders | Place, modify, cancel, track orders |
| GTT Orders | Good Till Triggered orders |
| Portfolio | Positions, holdings, conversions |
| IPO | IPO discovery and applications |
| Mutual Funds | Mutual fund holdings, orders and SIPs |
| Trade Profit And Loss | P&L reports and trade charges |
| Historical Data | OHLC candle data (historical and intraday) |
| Market Quote | Real-time quotes, LTP, OHLC, option Greeks |
| Market Information | Holidays, timings, exchange status, CAS phases |
| Market Analytics | OI, change in OI, PCR, max pain, FII/DII activity |
| Smartlist | Ranked futures, options and MTF lists |
| Fundamentals | Company financials, ratios, corporate actions |
| News | Instrument and category news |
| Backtesting | Backtesting guidance |
| Option Chain | Option contracts and put/call chain |
| Websocket | Real-time streaming (market data and portfolio) |
| Websocket Implementation | Implementation guide |
| Webhook | Order and GTT order update notifications |
| Appendix | Reference data, changelog, examples |

## Base URL

```
https://api.upstox.com/v2/
https://api.upstox.com/v3/
```

Orders may also be routed through the HFT host: `https://api-hft.upstox.com/v2/` or `/v3/`.

## Documentation Vintage

This snapshot tracks the Upstox documentation as of **8 September 2026**. See the Changelog appendix for the dated update history.

## API Documentation

Source: https://upstox.com/developer/api-documentation/open-api
