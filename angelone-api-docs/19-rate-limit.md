<!-- Source: https://smartapi.angelone.in/docs -->
<!-- Section: Rate Limit -->

# Rate Limit

Rate limiting defines limits on how many API calls can be made within a second.

The limit-exceeding requests will fail and returns 403 Access denied because of exceeding rate limit.

The rate limit for order APIs is enforced cumulatively across place order, modify order, and cancel order requests. The combined request count must not exceed **9 requests per second**.

| Sr. No | API Name | Throttling Limit Rate (Request/Second) | Throttling Limit Rate (Request/Minute) | Throttling Limit Rate (Request/Hour) |
| --- | --- | --- | --- | --- |
| 1 | /rest/auth/angelbroking/user/v1/loginByPassword | 1 | NA | NA |
| 2 | /rest/auth/angelbroking/jwt/v1//generateTokens | 1 | NA | 1000 |
| 3 | /rest/secure/angelbroking/user/v1/getProfile | 3 | NA | 1000 |
| 4 | /rest/secure/angelbroking/user/v1/logout | 1 | NA | NA |
| 5 | /rest/secure/angelbroking/user/v1/getRMS | 2 | NA | NA |
| 6 | /rest/secure/angelbroking/order/v1/placeOrder | 9 | 500 | 1000 |
| 7 | /rest/secure/angelbroking/order/v1/modifyOrder | 9 | 500 | 1000 |
| 8 | /rest/secure/angelbroking/order/v1/cancelOrder | 9 | 500 | 1000 |
| 9 | /rest/secure/angelbroking/order/v1/getOrderBook | 1 | NA | NA |
| 10 | /rest/secure/angelbroking/order/v1/getLtpData | 10 | 500 | 5000 |
| 11 | /rest/secure/angelbroking/order/v1/getPosition | 1 | NA | NA |
| 12 | /rest/secure/angelbroking/order/v1/getTradeBook | 1 | NA | NA |
| 13 | /rest/secure/angelbroking/order/v1/convertPosition | 10 | 500 | 5000 |
| 14 | /rest/secure/angelbroking/order/v1/searchScrip | 1 | NA | NA |
| 15 | /rest/secure/angelbroking/order/v1//details/{GuiOrderID} | 10 | 500 | 5000 |
| 16 | /rest/secure/angelbroking/portfolio/v1/getHolding | 1 | NA | NA |
| 17 | /rest/secure/angelbroking/portfolio/v1/getAllHolding | 1 | NA | NA |
| 18 | /rest/secure/angelbroking/market/v1/quote | 10 | 500 | 5000 |
| 19 | /rest/secure/angelbroking/margin/v1/batch | 10 | 500 | 5000 |
| 20 | /rest/secure/angelbroking/gtt/v1/createRule | 9 | 500 | 5000 |
| 21 | /rest/secure/angelbroking/gtt/v1/modifyRule | 9 | 500 | 5000 |
| 22 | /rest/secure/angelbroking/gtt/v1/cancelRule | 9 | 500 | 5000 |
| 23 | /rest/secure/angelbroking/gtt/v1/ruleDetails | 10 | 500 | 5000 |
| 24 | /rest/secure/angelbroking/gtt/v1/ruleList | 10 | 500 | 5000 |
| 25 | /rest/secure/angelbroking/historical/v1/getCandleData | 3 | 180 | 5000 |
| 25 | /rest/secure/angelbroking/marketData/v1/optionGreek | 1 | NA | NA |

**NOTE:**The Rate limit is calculated on the basis of client code.
