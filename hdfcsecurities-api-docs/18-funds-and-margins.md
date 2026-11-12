# Funds and Margins

> Source: https://developer.hdfcsec.com/ir-docs/docs/funds_and_margins

## Description

The Funds and Margins API furnishes users with crucial details regarding their accessible funds and margin limits within the InvestRight platform. It grants insights into trading funds availability, margin usage, and the overall financial status of the user's account.

## EndPoint

```js
Method: GET 
`https://developer.hdfcsec.com/oapi/v1/user/margins?api_key=<api_key>`
```

## Headers

- **Authorization**: access_token
- **User-Agent**: User-Agent header is required indicating the client application making the request.

## Query Params

- `api_key`: The API key used for authentication.

## Glossary of constants

| Field | Description |
| --- | --- |
| total_available_limit | Total available equity limit, representing the maximum amount of equity funds available for trading. |
| total_utilised_limit | Total utilised equity limit, representing the amount of equity funds currently utilized for trading. |
| total_limit | Total equity limit, representing the overall equity limit, which is the sum of available and utilized limits. |
| totalAvailableLimitDetails | Detailed breakdown of the total available limits for various types of funds, such as cash, margin trading facility (MTF), intraday equity, etc. |
| totalUtilizationDetails | Detailed breakdown of the total utilized limits for various types of funds, indicating the amount of each type of fund currently being used. |
| totalLimitDetails | Detailed breakdown of the total limits for various types of funds, including bank hold, intraday sales proceeds, ledger balance, ad-hoc limit, and pledge limit. |

## Request Curl

```js
curl --location 'https://developer.hdfcsec.com/user/margins?api_key=api_key' \
--header 'Authorization: access_token'
```

> The curl sample omits the `/oapi/v1` prefix and the mandatory `User-Agent` header. Use
> `https://developer.hdfcsec.com/oapi/v1/user/margins` from the EndPoint block above.

## API Response

```js
{
    "status": "success",
    "data": {
        "equity": {
            "total_available_limit": 9.99,
            "total_utilised_limit": 184,
            "total_limit": 9.99,
            "totalAvailableLimitDetails": {
                "cash": 9.99,
                "mtf": 9.99,
                "equity_intraday": 9.99,
                "equity_margin": 9.99,
                "cover_order": 9.99,
                "derivative_future_shortOption": 9.99,
                "option_buy": 9.99,
                "mutual_fund": 9.99,
                "cdx_future_shortOption": 9.99,
                "cdx_option_buy": 9.99,
                "com_derivative_future_shortOption": 9.99,
                "com_derivative_option_buy": 9.99
            },
            "totalUtilizationDetails": {
                "cash": 1597,
                "mtf": 20,
                "equity_margin_intraday_cover": 240,
                "derivative_future_shortOption": 0.0,
                "option_buy": 0.0,
                "mutual_fund": 0.0,
                "cdxFutureShortOption": 0.0,
                "cdxOptionBuy": 0.0,
                "comDerivativeFutureShortOption": 0.0
            },
            "totalLimitDetails": {
                "bank_hold": 0.0,
                "intraday_sales_proceed": 0.0,
                "ledger_balance": 0.0,
                "adhoc_limit": 0.0,
                "pledge_limit": 0.0
            }
        }
    }
}
```

## Response field notes

- Everything is nested under `data.equity`; the sample shows no commodity or currency bucket.
- Key casing is mixed within a single response: the three top-level totals are `snake_case`, the
  three breakdown objects are `camelCase`, and inside `totalUtilizationDetails` some keys are
  `snake_case` (`cash`, `mtf`, `equity_margin_intraday_cover`) while others are `camelCase`
  (`cdxFutureShortOption`, `cdxOptionBuy`, `comDerivativeFutureShortOption`).
- `totalAvailableLimitDetails` and `totalUtilizationDetails` do not share a key set:
  `totalAvailableLimitDetails` has `equity_intraday`, `equity_margin` and `cover_order`, which
  `totalUtilizationDetails` collapses into `equity_margin_intraday_cover`.
- The sample values (`9.99`, `184`) are placeholders — `total_limit` does not equal
  `total_available_limit + total_utilised_limit` there.
