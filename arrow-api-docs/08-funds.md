> Source: https://docs.arrow.trade/rest-api/funds/

# Funds API

Access comprehensive margin and fund availability information for portfolio management and trade planning across all market segments.

## Overview

The Funds API provides detailed insights into available cash, margin utilization, collateral positions, and trading limits, enabling effective risk management and position sizing decisions.

## Endpoint Reference

### Get User Limits

Retrieve complete margin and fund details for the authenticated user account.

Endpoint Details

**Method:** `GET`
**URL:** `/user/limits`
**Header:** Required (`appID` \+ `token`)

#### Request Headers

Header | Type | Required | Description
---|---|---|---
`appID` | string | ✓ | Your application identifier
`token` | string | ✓ | User authentication token

#### Request Example

```bash
curl --location 'https://edge.arrow.trade/user/limits' \
--header 'appID: <YOUR_APP_ID>' \
--header 'token: <YOUR_TOKEN>'
```

## Response Schema

### Success Response

The API returns comprehensive fund and margin information across all trading segments.

```json
{
    "data": {
        "allocations": [
            {
                "cashCurrent": "0",
                "cashEqCurrent": "0",
                "cashEqOpening": "0",
                "cashOpening": "0",
                "nonCashCurrent": "0",
                "nonCashOpening": "0",
                "segment": "CM"
            },
            {
                "cashCurrent": "226462.37",
                "cashEqCurrent": "0",
                "cashEqOpening": "0",
                "cashOpening": "226462.37",
                "nonCashCurrent": "0",
                "nonCashOpening": "0",
                "segment": "FO"
            },
            {
                "cashCurrent": "0",
                "cashEqCurrent": "0",
                "cashEqOpening": "0",
                "cashOpening": "0",
                "nonCashCurrent": "0",
                "nonCashOpening": "0",
                "segment": "MCX"
            }
        ],
        "margin": {
            "allocated": "226462.37",
            "utilized": "-3641.75",
            "brokerage": "0",
            "buyOptionPremium": "12506.25",
            "cashUsed": "-3641.75",
            "exposureMargin": "0",
            "intradayCashMargin": "0",
            "otherMargin": "0",
            "realizedPnl": "0",
            "sellOptionPremium": "16148",
            "spanMargin": "0",
            "totalMargin": "0",
            "unrealizedPnl": "1180.75"
        }
    },
    "status": "success"
}
```

## Integration Guidelines

Best Practices

  * **Pre-trade validation:** Check available margin before order placement
  * **Real-time monitoring:** Track margin utilization continuously
  * **Risk management:** Set appropriate exposure limits
  * **Settlement tracking:** Monitor payIn/payOut cycles

Optimization Tips

  * Cache fund data for 30-60 seconds to reduce API calls
  * Implement margin alerts at 80% utilization
  * Use segment-wise breakdown for detailed analysis
  * Monitor MTM percentage for portfolio risk assessment
