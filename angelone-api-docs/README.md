# AngelOne SmartAPI Documentation (Markdown)

A clean, offline, Markdown copy of the AngelOne SmartAPI developer documentation,
split into one file per section. Handy for reading offline, grepping, diffing across
versions, or feeding into AI tools and code assistants.

Source: https://smartapi.angelone.in/docs

## Contents

1. [Introduction](./01-introduction.md)
2. [Response structure](./02-response-structure.md)
3. [Error Codes](./03-error-codes.md)
4. [User (login, token, profile, funds, logout)](./04-user.md)
5. [Orders (place, modify, cancel, order/trade book, LTP)](./05-orders.md)
6. [Brokerage Calculator](./06-brokerage-calculator.md)
7. [Portfolio (holdings, positions, convert)](./07-portfolio.md)
8. [EDIS APIs](./08-edis-apis.md)
9. [Postback / Webhook](./09-postback-webhook.md)
10. [WebSocket Streaming 2.0](./10-websocket-streaming-2-0.md)
11. [WebSocket Order Status](./11-websocket-order-status.md)
12. [Instruments](./12-instruments.md)
13. [GTT](./13-gtt.md)
14. [Live Market Data API](./14-live-market-data-api.md)
15. [Historical API](./15-historical-api.md)
16. [Option Greeks](./16-option-greeks.md)
17. [Top Gainers / Losers, PCR and OI Buildup](./17-top-gainers-losers-pcr-and-oi-buildup.md)
18. [Margin Calculator](./18-margin-calculator.md)
19. [Rate Limit](./19-rate-limit.md)

## Quick reference

- Base REST endpoint: `https://apiconnect.angelone.in`
- Market data quote (`/market/v1/quote`): up to 50 tokens per request, 10 requests/second.
  Supports LTP, OHLC and FULL modes (open interest is only returned in FULL mode).
- Historical candles (`/historical/v1/getCandleData`): 3 requests/second. Max days per
  request depends on interval (1m = 30 days, 5m = 100, 1h = 400, 1D = 2000).
- Historical OI (`/historical/v1/getOIData`) is a separate call from candles.
- Order APIs (place, modify, cancel) share a cumulative limit of 9 requests/second.
- Historical data is available for NSE, NFO, BSE, BFO and MCX. CDS (currency) historical
  data is not served by the candle API.

See [19-rate-limit.md](./19-rate-limit.md) for the full per-endpoint limit table.

Each file keeps the original tables, request/response JSON, and code samples in all five
languages (Python, NodeJs, Java, R, Go).

## Disclaimer

This is an unofficial, community-maintained mirror provided for convenience and may lag
behind the official site. Always confirm details against the official documentation at
https://smartapi.angelone.in/docs. All documentation content and trademarks belong to
AngelOne. This repository is not affiliated with or endorsed by AngelOne.
