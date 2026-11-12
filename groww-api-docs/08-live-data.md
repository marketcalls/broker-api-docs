# Source: https://groww.in/trade-api/docs/curl/live-data

# Live Data

Live data endpoints support up to 50 symbols per request where noted. Set `segment=CASH` for stocks and indices, and `segment=FNO` for derivatives. All quoted prices are in rupees.

## Get Quote

`GET https://api.groww.in/v1/live-data/quote`

Required query parameters: `exchange`, `segment`, `trading_symbol`. Returns a full snapshot including last price, OHLC, depth, volume, and related fields.

```bash
curl -G 'https://api.groww.in/v1/live-data/quote' \
  --data-urlencode 'exchange=NSE' --data-urlencode 'segment=CASH' \
  --data-urlencode 'trading_symbol=RELIANCE' \
  -H 'Accept: application/json' -H 'Authorization: Bearer {ACCESS_TOKEN}' \
  -H 'X-API-VERSION: 1.0'
```

Quote payload includes `average_price`, `bid_quantity`, `bid_price`, `day_change`, `day_change_perc`, circuit limits, `ohlc`, `depth.buy` and `depth.sell`, `high_trade_range`, `low_trade_range`, `implied_volatility`, last trade quantity/time, `last_price`, market cap, offer price/quantity, open interest values, total buy/sell quantity, volume, and 52-week high/low.

## Get LTP

`GET https://api.groww.in/v1/live-data/ltp`

Required: `segment` and `exchange_symbols` (comma-separated exchange_symbol identifiers). Supports up to 50 instruments.

```bash
curl -G 'https://api.groww.in/v1/live-data/ltp' \
  --data-urlencode 'segment=CASH' \
  --data-urlencode 'exchange_symbols=NSE_RELIANCE,BSE_SENSEX' \
  -H 'Accept: application/json' -H 'Authorization: Bearer {ACCESS_TOKEN}' \
  -H 'X-API-VERSION: 1.0'
```

The `payload` maps each supplied exchange symbol to its last traded price.

## Get OHLC Snapshot

`GET https://api.groww.in/v1/live-data/ohlc`

Required: `segment` and `exchange_symbols`. Supports up to 50 instruments. This returns the current real-time OHLC snapshot, not interval candles. Use historical candle data for interval-based OHLC.

```bash
curl -G 'https://api.groww.in/v1/live-data/ohlc' \
  --data-urlencode 'segment=CASH' \
  --data-urlencode 'exchange_symbols=NSE_RELIANCE,BSE_SENSEX' \
  -H 'Accept: application/json' -H 'Authorization: Bearer {ACCESS_TOKEN}' \
  -H 'X-API-VERSION: 1.0'
```

## Get Option Chain

`GET https://api.groww.in/v1/option-chain/exchange/{exchange}/underlying/{underlying}?expiry_date={expiry_date}`

Required path/query values: exchange (`NSE` or `BSE`), underlying symbol, expiry date (`YYYY-MM-DD`). The response includes underlying LTP and strike-keyed CE/PE entries with Greeks, trading symbol, LTP, open interest, and volume.

## Get Greeks

`GET https://api.groww.in/v1/live-data/greeks/exchange/{exchange}/underlying/{underlying}/trading_symbol/{trading_symbol}/expiry/{expiry}`

Returns Greeks for an FNO contract. Required values are exchange, underlying, trading symbol, and expiry (`YYYY-MM-DD`). The payload contains `delta`, `gamma`, `theta`, `vega`, `rho`, and `iv`.

All endpoints use `Accept: application/json`, `Authorization: Bearer {ACCESS_TOKEN}`, and `X-API-VERSION: 1.0` headers.
