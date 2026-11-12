# Motilal Oswal (MOFSL) Trading API Documentation

Unofficial Markdown conversion of the official Motilal Oswal Financial Services (MOFSL) Trading API
documentation.

> Source: https://invest.motilaloswal.com/moAPI/APIDocumentation/Introduction

The MOFSL Trading API (also called MO API / OpenAPI) is a JSON REST API for MOFSL clients and empanelled
vendors. It covers login (portal redirect and direct API login with TOTP/OTP), access token generation,
order management (place, modify, cancel), order and trade books, portfolio (holdings, positions, position
conversion), limits and margins, brokerage, LTP and index data, master/scrip data and DPR data (JSON and
CSV downloads), plus real-time streaming through a broadcast WebSocket, a trade/order WebSocket and a
webhook.

## Contents

| # | Section | Group |
|---|---------|-------|
| 01 | [Introduction](01-introduction.md) | Getting started |
| 02 | [Libraries and SDKs](02-libraries-and-sdks.md) | Getting started |
| 03 | [Request Format](03-request-format.md) | Getting started |
| 04 | [Responses Format](04-response-format.md) | Getting started |
| 05 | [Header Parameters](05-header-parameters.md) | Getting started |
| 06 | [Login through Portal](06-login-through-portal.md) | Getting started |
| 07 | [TOTP Secret Key](07-totp-secret-key.md) | Getting started |
| 08 | [Login through API](08-login-through-api.md) | Authentication/Profile |
| 09 | [Generate Access Token](09-generate-access-token.md) | Authentication/Profile |
| 10 | [Resend OTP](10-resend-otp.md) | Authentication/Profile |
| 11 | [Verify OTP](11-verify-otp.md) | Authentication/Profile |
| 12 | [Get Profile](12-get-profile.md) | Authentication/Profile |
| 13 | [Logout](13-logout.md) | Authentication/Profile |
| 14 | [Place Order](14-place-order.md) | Orders |
| 15 | [Modify Order](15-modify-order.md) | Orders |
| 16 | [Cancel Order](16-cancel-order.md) | Orders |
| 17 | [OrderBook](17-orderbook.md) | Orders |
| 18 | [Trade Book](18-trade-book.md) | Orders |
| 19 | [Order Detail](19-order-detail.md) | Orders |
| 20 | [Trade Detail](20-trade-detail.md) | Orders |
| 21 | [Holding](21-holding.md) | Portfolio |
| 22 | [Position](22-position.md) | Portfolio |
| 23 | [Position Conversion](23-position-conversion.md) | Portfolio |
| 24 | [Margin Summary](24-margin-summary.md) | Limit/Margin |
| 25 | [Margin Detail](25-margin-detail.md) | Limit/Margin |
| 26 | [Price/LTP](26-price-ltp.md) | Limit/Margin |
| 27 | [Scrip/Instrument](27-scrip-instrument.md) | Master Data |
| 28 | [Scrip/Instrument (CSV Format)](28-scrip-instrument-csv.md) | Master Data |
| 29 | [DPR Data API](29-dpr.md) | DPR Data |
| 30 | [DPR (CSV Format)](30-dpr-csv.md) | DPR Data |
| 31 | [Error Codes And Description](31-error-codes.md) | Reference |
| 32 | [Parameters / Constants](32-parameters-constants.md) | Reference |
| 33 | [WebSocket Broadcast](33-websocket-broadcast.md) | Streaming |
| 34 | [Trade WebSocket](34-trade-websocket.md) | Streaming |
| 35 | [Webhook](35-webhook.md) | Streaming |
| 36 | [Participant Detail](36-participant-detail.md) | Reference |
| 37 | [Brokerage Detail](37-brokerage-detail.md) | Reference |
| 38 | [EOD Data API](38-eod-api.md) | EOD Data |
| 39 | [EOD (CSV Format)](39-eod-csv.md) | EOD Data |
| 40 | [Index Data API](40-index-data-api.md) | Index Data |
| 41 | [INDEX DATA (CSV Format)](41-index-data-csv.md) | Index Data |
| 42 | [INDEX LTP DATA API](42-index-ltp.md) | Index Data |
| 43 | [Contact Us](43-contact-us.md) | Reference |
| 44 | [FAQ](44-faq.md) | Reference ([source](https://invest.motilaloswal.com/moAPI/APIDocumentation/FAQ)) |

## Base URLs

| Purpose | URL |
|---------|-----|
| REST API (production) | `https://openapi.motilaloswal.com` |
| REST API (UAT / test) | `https://openapi.motilaloswaluat.com` |
| Login page (production) | `https://invest.motilaloswal.com/OpenAPI/Login.aspx?apikey={apikey}` |
| Login page (UAT) | `https://uattrade.motilaloswaluat.com/OpenAPI/Login.aspx?apikey={apikey}` |
| Trade/Order WebSocket (production, marked WIP in the docs) | `wss://openapi.motilaloswal.com/ws` |
| Trade/Order WebSocket (UAT) | `wss://uatopenapi.motilaloswal.com/ws` |
| Developer portal | `https://invest.motilaloswal.com/moAPI/APIDocumentation/Introduction` |

## Endpoints at a glance

All REST paths below are relative to the base URL. Every call except login requires the common header
parameters (see [Header Parameters](05-header-parameters.md)).

| Method | Path | Doc |
|--------|------|-----|
| POST | `/rest/login/v7/authdirectapi` | [Login through API](08-login-through-api.md) |
| POST | `/rest/login/v1/getaccesstoken` | [Generate Access Token](09-generate-access-token.md) |
| POST | `/rest/login/v5/resendotp` | [Resend OTP](10-resend-otp.md) |
| POST | `/rest/login/v5/verifyotp` | [Verify OTP](11-verify-otp.md) |
| POST | `/rest/login/v5/getprofile` | [Get Profile](12-get-profile.md) |
| POST | `/rest/login/v5/logout` | [Logout](13-logout.md) |
| POST | `/rest/trans/v2/placeorder` | [Place Order](14-place-order.md) |
| POST | `/rest/trans/v5/modifyorder` | [Modify Order](15-modify-order.md) |
| POST | `/rest/trans/v2/cancelorder` | [Cancel Order](16-cancel-order.md) |
| POST | `/rest/book/v5/getorderbook` | [OrderBook](17-orderbook.md) |
| POST | `/rest/book/v4/gettradebook` | [Trade Book](18-trade-book.md) |
| POST | `/rest/book/v5/getorderdetailbyuniqueorderid` | [Order Detail](19-order-detail.md) |
| POST | `/rest/book/v4/gettradedetailbyuniqueorderid` | [Trade Detail](20-trade-detail.md) |
| POST | `/rest/report/v3/getdpholding` | [Holding](21-holding.md) |
| POST | `/rest/book/v4/getposition` | [Position](22-position.md) |
| POST | `/rest/trans/v2/positionconversion` | [Position Conversion](23-position-conversion.md) |
| POST | `/rest/report/v3/getreportmarginsummary` | [Margin Summary](24-margin-summary.md) |
| POST | `/rest/report/v3/getreportmargindetail` | [Margin Detail](25-margin-detail.md) |
| POST | `/rest/report/v3/getltpdata` | [Price/LTP](26-price-ltp.md) |
| POST | `/rest/report/v3/getscripsbyexchangename` | [Scrip/Instrument](27-scrip-instrument.md) |
| GET | `/getscripmastercsv?name={exchange}` | [Scrip/Instrument (CSV)](28-scrip-instrument-csv.md) |
| POST | `/rest/report/v3/getdprvalues` | [DPR Data](29-dpr.md) |
| GET | `/getdprcsv?symbol={NIFTY\|BANKNIFTY}` | [DPR (CSV)](30-dpr-csv.md) |
| POST | `/rest/report/v3/getparticipantsdetail` | [Participant Detail](36-participant-detail.md) |
| POST | `/rest/report/v3/getbrokeragedetail` | [Brokerage Detail](37-brokerage-detail.md) |
| POST | `/rest/report/v3/geteoddatabyexchangename` | [EOD Data](38-eod-api.md) |
| GET | `/geteoddatacsv?name={exchange}` | [EOD (CSV)](39-eod-csv.md) |
| POST | `/rest/report/v3/getindexdatabyexchangename` | [Index Data](40-index-data-api.md) |
| GET | `/getindexdatacsv?name={NSE\|BSE}` | [INDEX DATA (CSV)](41-index-data-csv.md) |
| POST | `/rest/report/v3/getindexltpdata` | [INDEX LTP DATA](42-index-ltp.md) |
| GET | `/webhook` | [Webhook](35-webhook.md) |

## Notes

- All requests and responses are JSON. The API endpoints cannot be called directly from a browser.
- The authentication token expires every day at 6 a.m. due to exchange compliance, so a fresh login is
  required each trading day.
- Responses carry `status` (`SUCCESS`/`FAILURE`/`ERROR`), `message`, `errorcode` and `data`; the error
  codes are listed in [Error Codes And Description](31-error-codes.md).
- Official SDKs: [C#/.Net](https://github.com/motradingapi/DotNetSDK.git),
  [Python](https://github.com/motradingapi/PythonSDK.git),
  [NodeJS](https://github.com/motradingapi/NodeJSSDK.git),
  [Java](https://github.com/motradingapi/JavaSDK.git).

## Disclaimer

This is an unofficial Markdown conversion maintained for personal/educational reference. The official
Motilal Oswal documentation is the authoritative source — always verify against it. Trademarks and
content belong to Motilal Oswal Financial Services Ltd.
