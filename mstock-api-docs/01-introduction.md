# Introduction

> Source: https://tradingapi.mstock.com/docs/v1/Introduction/
>
> Section: Getting started

mStock Trading API is a set of REST-like HTTP APIs that expose many capabilities required to build a complete stock market investment and trading platform. It lets you execute orders in real time (equities, derivatives), stream live market data over WebSockets, get order status through websockets & much more.

All inputs are form-encoded parameters and responses are JSON (apart from a couple exceptions). The responses may be Gzipped. Standard HTTP codes are used to indicate success and error states with accompanying JSON data. The API endpoints are not cross site request enabled, hence cannot be called directly from browser.

> **Note**
>
> If you don't have a mStock account, read more about it and sign up [here](https://www.mstock.com/open-demat-account). If you already have the mStock account you can generate the api key [here](https://www.mstock.com/trading-api).

### Libraries and SDKs

- Python
- NodeJS NEW
- Postman Collection NEW

### Version

The mstock trading API current version is 1.0 and All requests go by default to this version. Look for this space for any version related changes in future

> **Note**
>
> This version is a mstock trading API version and should not be confused with the specific library release version going forward

### Root End point

- Interactive URL : https://api.mstock.trade
- Broadcasting URL : wss://ws.mstock.trade

### Rate Limits

| Rate Limit | Order APIs | Data APIs | Quote APIs | Non Trading APIs |
| --- | --- | --- | --- | --- |
| per second | 30 | 1 | 20 | Another order |
| per minute | 250 | 1000 | Unlimited | Unlimited |
| per hour | 1000 | 5000 | Unlimited | Unlimited |
| per day | Unlimited | Unlimited | Unlimited | Unlimited |

### Api Key & Access token Validity

| Token Type | Validity | Note |
| --- | --- | --- |
| API Key | 1 year, 1 month, 1 day | Used for initial authentication. Store securely. |
| Access Token | Within 12 hours or on the same day, whichever occurs first | Required for all API requests. Renew daily. |

> **BOD and EOD Timings**
>
> Please note that BOD (Beginning of Day) operations occur between 07:00 AM and 08:30 AM, while EOD (End of Day) processes run from 07:00 PM to 09:00 PM. During these times, system performance may be affected. Plan accordingly.

### Request Headers to be passed in every API call

**X-Mirae-Version :** Specifies the version of the API being used. In this case, it is set to 1.

**Authorization :** A token-based authentication header. The format is token api_key:jwtToken.

**Content-Type :** A token-based authentication header. The format is token api_key:jwtToken.

**Content-Type :** For this request, it is set to application/json, which is used for submiting form data through body

**X-PrivateKey :** ay3xxxxxxxxxxYzkB/MAK@@

---
