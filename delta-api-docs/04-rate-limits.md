# Rate Limits

> Source: https://docs.delta.exchange/#rate-limits

When a rate limit is exceeded, a HTTP response status 429 Too Many Requests will be returned.
'X-RATE-LIMIT-RESET' is returned in response header with time left in milliseconds after which next API request can be hit. 

We throttle unauthenticated api requests by IP address and authenticated requests by user ID. 

Default Quota is 10000 for a fixed 5 minute window. Rate Limit quota resets to full every 5 mins.

## API & product rate limits

### REST API 
Every REST endpoint has been assigned a weight. When you make an API call, the weight of that endpoint is deducted from your 5 min window quota. Exceeding the rate limit quota, results in 429 HTTP response status error. API endpoints related to reading public data are lighter in weight, whereas API endpoints related to writing private data (like placing an order) are heavier in weight. 

Here is the cost structure for various endpoints. Please note that any endpoint not mentioned here has a cost of 1 unit.

Weight Slab|API Endpoints
--|--
3| Get Products, Get Orderbook, Get Tickers, Get Open Orders, Get Open Postions, Get Balances, OHLC Candles
5| Place/Edit/Delete Order, Add Position Margin
10| Get Order History, Get Fills, Get Txn Logs
25| Batch Order Apis

e.g. Consider making all the below requests in a 5 minute window.  
100 Get Open Orders requests = 100 * 3 = 300 weight.  
50 Get Balances requests = 50 * 3 = 150 weight.  
200 Place order requests = 200 * 5 = 1000 weight.  
20 Batch Order requests = 20 * 25 = 500 weight.  
Total quota used: 300 + 150 + 1000 + 500 = 1950 quota used. If this is greater than quota assigned to you, rate limit error will occur.

### Product
We have also introduced rate limits to manage operations within the matching engine. The current rate limit is set at 500 operations per second for each product. For example, placing 50 orders in a batch counts as 50 operations, as each individual order will be processed by the matching engine.

This measure is in place to prevent excessive operations on the matching engine, which could slow down its performance.

Even if you have not exceeded the rate limit on the REST API level, your requests may still fail with a 429 error if you breach the product-level rate limit.

## Increasing your rate limits

If you are running up against our limits and believe that you have a legitimate need, please email us at [support@delta.exchange](mailto:support@delta.exchange) to discuss increasing your rate limits.
