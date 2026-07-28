# Broker API Docs

A growing collection of Indian stockbroker API documentation, converted to clean Markdown for offline reading, grepping, diffing across versions, and feeding into AI coding tools (Claude Code, Cursor, GitHub Copilot, etc.) as context.

Each broker's docs live in their own folder, one Markdown file per section/page, generally sourced from the broker's official developer documentation portal.

## Brokers

| Broker | Folder | Source |
| --- | --- | --- |
| Aliceblue (ANT API) | [`aliceblue-api-docs/`](aliceblue-api-docs/) | https://ant.aliceblueonline.com/productdocumentation/ |
| AngelOne (SmartAPI) | [`angelone-api-docs/`](angelone-api-docs/) | https://smartapi.angelone.in/docs |
| Arrow Trade (REST API + Python SDK) | [`arrow-api-docs/`](arrow-api-docs/) | https://docs.arrow.trade/ |
| Definedge Securities (INTEGRATE) | [`definedge-api-docs/`](definedge-api-docs/) | https://www.definedgesecurities.com/api-documentation/ |
| Dhan (DhanHQ v2) | [`dhan-api-docs/`](dhan-api-docs/) | https://dhanhq.co/docs/v2/ |
| Flattrade (Pi) | [`flattrade-api-docs/`](flattrade-api-docs/) | https://pi.flattrade.in/docs |
| Fyers (API v3) | [`fyers-api-docs/`](fyers-api-docs/) | https://myapi.fyers.in/docsv3 |
| HDFC Sky (Open API) | [`hdfcsky-api-docs/`](hdfcsky-api-docs/) | https://developer.hdfcsky.com/sky-docs/docs/intro |
| IIFL Capital (Markets' APIs) | [`iiflcapital-api-docs/`](iiflcapital-api-docs/) | https://developers.iiflcapital.com/apidocs/introduction |
| INDstocks | [`indstocks-api-docs/`](indstocks-api-docs/) | https://api-docs.indstocks.com/ |
| Kotak Securities (Neo Trade API v2) | [`kotak-api-docs/`](kotak-api-docs/) | https://app.notion.com/p/Client-documentation-236da70d37e280b3a979fc7be7b003bc |
| Nubra | [`nubra/`](nubra/) | https://uatapi.nubra.io |
| Upstox | [`upstox-api-docs/`](upstox-api-docs/) | https://upstox.com/developer/api-documentation |
| Zerodha (Kite Connect v3) | [`zerodha-api-docs/`](zerodha-api-docs/) | https://kite.trade/docs/connect/v3/ |

More brokers will be added over time.

## Why

Broker API docs are scattered across HTML portals, PDFs, and inconsistent formats. This repo mirrors them as plain Markdown so they're easy to:

- Read and grep offline
- Diff across API versions
- Feed directly into LLM context windows for coding assistants

## Disclaimer

These are unofficial Markdown conversions maintained for personal/educational reference. Each broker's original documentation is the authoritative source — always verify against it. Trademarks and content belong to their respective brokers.
