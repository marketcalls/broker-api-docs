# Instant Withdrawal Eligibility

## Overview

IMPS (Instant) withdrawals are subject to real-time eligibility checks at the time of placing a [Payout Request](https://upstox.com/developer/api-documentation/payout-request) . All criteria must be met for an instant withdrawal to proceed. If any criterion is not met, the IMPS mode will be unavailable and only NEFT (Standard) withdrawal will be offered.

## Eligibility Criteria

| Criterion | Description |
| --- | --- |
| Markets are open | No active settlement holiday on the day of the request. |
| Request timing | Must be placed between 10:00 AM – 7:00 PM. |
| Daily withdrawal limit | Up to ₹5,00,000 per day. |
| Account status | Your trading account must be active. |
| Open F&O positions/orders | No open F&O positions or orders at the time of request. |

If any criterion is not met, IMPS is not available. All criteria must be satisfied for the instant withdrawal mode to be enabled for your account.
