# Changelog

> Source: https://docs.delta.exchange/#changelog

## 03.06.26
1. Updated `Update MMP config` and `MMP Trigger` descriptions by removing the note about reaching out to support for MMP access.

## 20.05.26
1. Added a **Description** column to all "Enumerated Values" tables in the REST API docs, so each value now has a clear explanation of what it means. Covers values like `side`, `order_type`, `state`, `transaction_type`, `mmp`, `time_in_force`, `resolution`, and more. Updated across Products, Orders, Positions, TradeHistory, Trades, Wallet, Heartbeat Management, Historical OHLC Candles/Sparklines, and the Schemas section. This is a documentation update only — no API behaviour has changed.

## 17.04.26
1. The following WebSocket channels have been migrated to the **new public WebSocket endpoint** (`wss://public-socket.india.delta.exchange`). The new channels provide the same data with a more compact response format. The old channels on the **legacy private endpoint** (`wss://socket.india.delta.exchange`) will continue to work but are planned to be deprecated and removed on **31st July 2026** — please update your integrations before that date.
The new channels are: [`mark_price`](31-websocket-public-channels.md#mark_price), [`candlesticks`](31-websocket-public-channels.md#candlesticks), [`spot_price`](31-websocket-public-channels.md#spot_price), [`funding_rate`](31-websocket-public-channels.md#funding_rate), [`system_status`](31-websocket-public-channels.md#system_status).

2. The following legacy WebSocket channels have been migrated to the **new public WebSocket endpoint** (`wss://public-socket.india.delta.exchange`). The old channels on the **legacy private endpoint** (`wss://socket.india.delta.exchange`) will continue to work but are planned to be deprecated and removed on **31st July 2026** — please update your integrations before that date.

| Removed Channel | New Channel |
|---|---|
| `l1_orderbook` | [`ob_l1`](31-websocket-public-channels.md#ob_l1) |
| `l2_orderbook` | [`ob_l2`](31-websocket-public-channels.md#ob_l2) |
| `l2_updates` | [`ob_updates`](31-websocket-public-channels.md#ob_updates) |
| `v2/ticker` | [`ticker`](31-websocket-public-channels.md#ticker) |
| `all_trades` | [`trades`](31-websocket-public-channels.md#trades) |
| `v2/spot_price` | [`spot_price`](31-websocket-public-channels.md#spot_price) |

## 15.04.26
1. Introduced validation changes for `limit_price` parameter:
   - Any value ≤ 0 will now be rejected
   - If `limit_price` is not required, remove field from payload or send it as `null`

Please update your integrations accordingly to avoid request failures.

## 13.01.26
1. Order History `GET /v2/orders/history` and Fills `GET /v2/fills` history APIs will no longer include the total field in pagination meta, these changes are now live. We are planning to change max page_size allowed for these API endpoints to be 50, higher values than 50 will return only 50 items. These changes will go live on 28th January 2026 (tentative).
2. Updated parameter descriptions for product_ids and ticker symbol to clarify comma-separated format with maximum 10 Product_ids/symbols. Affected APIs endpoints are `GET /v2/tickers/{symbol}`, `GET /v2/orders`, `GET/v2/positions/margined`, `GET /v2/orders/history`, and `GET /v2/fills`. These changes will go live on 28th January 2026 (tentative). Passing more than 10 product_ids/symbols will return HTTP 4xx error. By default, if the product_ids parameter is not provided, these APIs returns data for all products.

## 11.12.25
1. Added a new WebSocket system_status channel which includes maintenance events such as maintenance_scheduled, maintenance_started, maintenance_finished, and maintenance_cancelled, along with real-time system status updates (live, api_fallback, degraded_mode) and an initial snapshot event providing the current system state.
2. We will be deprecating the announcements channel on 28 February 2026. All maintenance-related updates will be migrated to and provided through the system_status channel.

## 08.10.25
1. Added new websocket authentication method, {"type":"key-auth"}, which includes new formats of request and responses.  
2. Previous websocket authentication method, {"type":"auth"}, is now marked as deprecated. This method will stop working after 31st December 2025, users are requested to migrate to the newer websocket authentication.
3. We will be deprecating support for historical candlestick OHLC resolution 7d, 2w and 30d from 18th October 2025. The REST API `/history/candles` and websocket public channel `candlesticks` will stop supporting these resolutions. These resolutions have been removed from the documentation.
4. 'client_order_id' parameter in all Orders API is now restricted to max 32 length. e.g. REST API `POST /orders` parameter 'client_order_id' can be max 32 length string.

## 01.06.25
1. Added reason:"liquidation" for v2/user_trades websocket channel. Updated documentation for the v2/user_trades channel.
2. Added Connection rate limit for websocket URL endpoint of 150 connections per IP address per 5 minutes. Updated this info under 'Websocket Info' tab.

## 21.03.25
1. Better documentation for Websocket public channel 'candlesticks', now clearly states even Mark Price candles can be fetched.
2. /positions REST API fixed documentation for query parameters.
3. Better documentation for Websocket public channel 'announcements'.

## 20.02.25
1. Removed Websocket RPC section. Use REST API endpoints with normal HTTP requests (RPC requests still work, it is recommended not to use them).
2. Fixed documentation: "User-Agent" header is necessary for authenticated HTTP requests.
3. Fixed documentation: Better examples and documentation under 'General Information', 'Authentication', etc tabs.
4. Created separate documentation site for Indian and Global site for easier understanding and better examples for both.

## 18.10.2024
1. Added clickable links to the corresponding API response json schemas under some API "Responses" table. Updated some schemas to match the response. (This is a documentation fix, no changes in API)
2. Added "Testnet-India" REST and Websocket host endpoints.
3. Changed "Rate Limits" description and added an example.

## 01.05.2024
1. Added "po" positions key in /v2/user_trades websocket private channel.
2. Removed "fok" type for orders, as they are no longer supported.

## V2 Rest Api
Our v2 Api is significantly faster than the v1 api. Our focus while rebuilding v2 Apis was on the following

1. Remove Api gateway overheads as much as possible.
2. Remove overheads due to deep nesting in response payload.
3. Better Api structure to query only required data.

> New Response Format

```json
// The new format supports sending meta data alongside response body. 
// Success format
{
  success: true,
  result: {}         // response body
  meta: {
    after: "...",       // cursor for pagination, is returned in meta
    before: null,
  },
}

// Error Format
{
  success: false,
  error: {
    code: :insufficient_margin,             // error code
    context: {                              // error context
      additional_margin_required: "0.121"
    }
  }
}
```

### Key Api changes
- We have completely removed nested product/asset payloads from live orders and live positions. This ensures the payload is light.
- Rate limiting now works on a fixed window instead of a rolling window.
- Ticker Api - now includes turnover in USD, mark price, spot price.
- Orderbook and trades are now returned in separate Apis.
- For supporting trading strategies which require latest positions, Now we have two different Apis to query position. 
  
  /v2/positions - returns only size and entry price. This should be used when you want to get the latest position, but dont need the margin dependent fields like liquidation price, bankruptcy price etc

  /v2/positions/margined - returns all fields including margin dependent fields. When the position is updated due to a fill, changes might take some time to reflect in this Api.

- All Apis that support pagination now use cursor based pagination, instead of fixed page size pagination. Check more details in our [python rest client docs](https://github.com/delta-exchange/python-rest-client)

## New Socket Channels
- Socket Api interface hasn't changed much in terms of connection management and authentication. 
- We have deprecated old channels and created new channels which make integration easier. 
- To support easy management of live data, all private data channels now support initial snapshots and sequence numbers.

### List of new public channels
- v2/ticker - now includes turnover in USD, mark price, spot price
- candlesticks - subscribe to ohlc candle updates for different resolutions
- all_trades - subscribe to all public trades for a symbol

### List of new private channels
- orders - subscribe to lifecycle of live orders
- user_trades - subscribe to live user trades/fills feed
- positions - subscribe to position updates
- margins - get margin/wallet updates
