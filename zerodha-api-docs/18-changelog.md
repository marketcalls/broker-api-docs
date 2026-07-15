# Changelog

## Kite Connect 3.1 Updates

- **Orders:** Added `exchange_update_timestamp` and `meta` fields
- **GTT Orders:** Added support for placing, updating, and deleting GTT orders
- **Quote:** Circuit limits added to market quote responses
- **Historical:** Open Interest (OI) data in candle responses

## Kite Connect 3.0 Major Changes

- **Authentication:** Shifted from query parameters to header-based: `Authorization: token api_key:access_token`
- **WebSocket:** Endpoint moved to `wss://ws.kite.trade`; capacity increased from 200 to 1,000 instruments; binary protocol enhanced with OI and timestamp fields
- **Quotes:** Three new endpoints (`/quote`, `/quote/ohlc`, `/quote/ltp`) replacing `/market/instruments`
- **Login:** URLs require `v=3` parameter

## Notable Milestones

- **June 2025:** Alerts API
- **January 2025:** MTF orders
- **March 2022:** Iceberg and TTL orders
- **August 2020:** Margin calculator APIs
