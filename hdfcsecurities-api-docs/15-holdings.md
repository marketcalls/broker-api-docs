# Holdings/Portfolio API

> Source: https://developer.hdfcsec.com/ir-docs/docs/holdings

## Description

The user's long-term equity delivery equities portfolio is stored in Holdings/Portfolio. Once included, an item remains in the holdings portfolio permanently until it is sold or modified by the exchanges. All these stocks are stored in the user's CDSL or NSDL DEMAT account.

The holding value API retrieves both the invested value and the current value of the holdings or portfolio.

## EndPoint

```js
Method: GET
`https://developer.hdfcsec.com/oapi/v1/portfolio/holdings?api_key=<api_key>`
```

## Headers

- **Authorization**: access_token
- **User-Agent**: User-Agent header is required indicating the client application making the request.

## Query Params

- `api_key`: The API key used for authentication.

## Glossary of constants

| Constant | Description |
| --- | --- |
| security_id | Unique identifier for the security. |
| exchange | The exchange where the security is listed. |
| company_name | Name of the company associated with the security. |
| sector_name | Name of the sector to which the company belongs. |
| isin | International Securities Identification Number. |
| quantity | The quantity of the security held. |
| average_price | The average price at which the security was bought or sold. |
| investment_value | Total investment value in the security. |
| close_price | The closing price of the security. |
| realised | Realized profit or loss from the holding. |
| sip_indicator | Indicator for Systematic Investment Plan (SIP). |
| mtf_indicator | Indicator for Mutual Fund Transfer (MTF). |
| ltcg_quantity | Quantity of the security eligible for Long Term Capital Gains (LTCG). |
| corporate_action_indicator | Indicator for any corporate actions affecting the holding. |
| corporate_action_message | Message related to any corporate actions affecting the holding. |

> `mtf_indicator` is glossed as "Mutual Fund Transfer"; in context it is the Margin Trading
> Facility flag, matching the `MTF` product in [Place Order](07-place-order.md).

## Request Curl

```js
curl --location 'https://developer.hdfcsec.com/oapi/v1/portfolio/holdings?api_key=api_key' \
--header 'Authorization: access_token' \
--header 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
```

## API Response

```js
{
  "status": "success",
  "data": [
    {
      "security_id": "",
      "exchange": "BSE",
      "company_name": "",
      "sector_name": "",
      "isin": "INF204KB17I5",
      "quantity": 2,
      "average_price": 40.67,
      "investment_value": "",
      "close_price": 42.28,
      "realised": "",    
      "sip_indicator": "N",
      "mtf_indicator": "N",
      "ltcg_quantity": 0,
      "corporate_action_indicator": "",
      "corporate_action_message": ""
    }
  ]
}
```

> In the official sample `security_id`, `company_name`, `sector_name`, `investment_value` and
> `realised` are all returned empty, so `isin` is the only reliable instrument identifier shown.
> `investment_value` and `realised` are typed as strings there, not numbers.
