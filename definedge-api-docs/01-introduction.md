# Introduction

The Definedge Securities trading API **INTEGRATE** allows you to build trading and investment services platforms, execute strategies, and much more.

You can execute & modify orders in real time in equities, derivatives, currencies and commodities. You can also manage user portfolios, access live market data and much more with a lightning fast API.

We offer resource-based URLs that accept JSON or form-encoded requests. The response is returned as JSON-encoded responses using standard HTTP response codes, verbs, and authentication.

Below is complete documentation of the Integrate trading API.

## Base URL

```
https://integrate.definedgesecurities.com/dart/v1
```

This is the base URL for all trading related APIs. For example: buy, sell, order book, trade book etc.

> **Note:** Data from Integrate API and Websocket is intended for personal use only. Distribution of this data is strictly prohibited.

## Integrate Python Library

A Python Client Library for the INTEGRATE API, along with working examples, is available.

- Search for the official **Integrate** Python client library published by Definedge Securities for the project description and documentation.

## Conventions used in this documentation

- Fields marked with an asterisk (`*`) in request tables are **required**.
- All endpoint paths and JSON keys are **case-sensitive**.
- Relative URLs are appended to the trading Base URL, e.g. relative URL `/placeorder` becomes
  `https://integrate.definedgesecurities.com/dart/v1/placeorder`.
- Most trading APIs require the header `Authorization: <api_session_key>` (see [Authentication](02-authentication.md)).
