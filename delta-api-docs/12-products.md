# Products

> Source: https://docs.delta.exchange/#delta-exchange-api-v2-products

Get Product List

## Get list of products

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('https://api.india.delta.exchange/v2/products', params={

}, headers = headers)

print r.json()
```

```shell
# You can also use wget
curl -X GET https://api.india.delta.exchange/v2/products \
  -H 'Accept: application/json'
```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get 'https://api.india.delta.exchange/v2/products',
  params: {
  }, headers: headers

p JSON.parse(result)
```

`GET /products`

The endpoint provides details about all available trading products on the platform. Each product represents a financial instrument like perpetual futures, options, or contracts for specific asset pairs.

### Parameters

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|contract_types|query|string|false|Comma separated list of contract types e.g. perpetual_futures,call_options, put_options|
|states|query|string|false|Comma separated list of states e.g. upcoming,live,expired,settled to get expired contracts.|
|after|query|string|false|after cursor for paginated request|
|before|query|string|false|before cursor for paginated request|
|page_size|query|string|false|size of a single page for paginated request, default: 100|
|expiry|query|string|false|Expiry date in YYYY-MM-DD format to filter products by current & future expiry date.|

> Example responses
>
> 200 Response

```json
{
  "success": true,
  "result": [
    {
      "id": 27,
      "symbol": "BTCUSD",
      "description": "Bitcoin Perpetual futures, quoted, settled & margined in USD",
      "created_at": "2023-12-18T13:10:39Z",
      "updated_at": "2024-11-15T02:47:50Z",
      "settlement_time": null,
      "notional_type": "vanilla",
      "impact_size": 10000,
      "initial_margin": "0.5",
      "maintenance_margin": "0.25",
      "contract_value": "0.001",
      "contract_unit_currency": "BTC",
      "tick_size": "0.5",
      "product_specs": {
        "funding_clamp_value": 0.05,
        "only_reduce_only_orders_allowed": false,
        "expiry_interval": 28800,
        "isolated_liq_penalty_factor": 0.01,
        "rate_exchange_interval": 28800,
        "tags": [
          "layer_1"
        ]
      },
      "state": "live",
      "trading_status": "operational",
      "max_leverage_notional": "100000",
      "default_leverage": "200",
      "initial_margin_scaling_factor": "0.0000025",
      "maintenance_margin_scaling_factor": "0.00000125",
      "taker_commission_rate": "0.0005",
      "maker_commission_rate": "0.0002",
      "liquidation_penalty_factor": "0.5",
      "contract_type": "perpetual_futures",
      "position_size_limit": 229167,
      "basis_factor_max_limit": "10.95",
      "is_quanto": false,
      "funding_method": "mark_price",
      "annualized_funding": "10.95",
      "price_band": "2.5",
      "underlying_asset": {
        "id": 14,
        "symbol": "USD",
        "precision": 8,
        "deposit_status": "enabled",
        "withdrawal_status": "enabled",
        "base_withdrawal_fee": "0.000000000000000000",
        "min_withdrawal_amount": "0.000000000000000000"
      },
      "quoting_asset": {
        "id": 14,
        "symbol": "USD",
        "precision": 8,
        "deposit_status": "enabled",
        "withdrawal_status": "enabled",
        "base_withdrawal_fee": "0.000000000000000000",
        "min_withdrawal_amount": "0.000000000000000000"
      },
      "settling_asset": {
        "id": 14,
        "symbol": "USD",
        "precision": 8,
        "deposit_status": "enabled",
        "withdrawal_status": "enabled",
        "base_withdrawal_fee": "0.000000000000000000",
        "min_withdrawal_amount": "0.000000000000000000"
      },
      "spot_index": {
        "id": 14,
        "symbol": ".DEXBTUSD",
        "constituent_exchanges": [
          {
            "name": "ExchangeA",
            "weight": 0.25
          }
        ],
        "underlying_asset_id": 13,
        "quoting_asset_id": 14,
        "tick_size": "0.5",
        "index_type": "spot_pair"
      }
    }
  ]
}
```

### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|List of [Products](25-schemas.md#tocSproduct)|Inline|

### Response Schema

#### Enumerated Values

|Property|Value|Description|
|---|---|---|
|notional_type|vanilla|Contract is quoted, settled, and margined in the quote currency|
|notional_type|inverse|Contract is quoted in the quote currency but settled and margined in the base currency|
|state|live|Product is currently active and tradable|
|state|expired|Product has expired and is no longer tradable|
|state|upcoming|Product is scheduled to go live in the future|
|trading_status|operational|Trading is fully operational; orders can be placed and cancelled|
|trading_status|disrupted_cancel_only|Trading is disrupted; only order cancellations are allowed|
|trading_status|disrupted_post_only|Trading is disrupted; only post-only orders are accepted|
|deposit_status|enabled|Deposits are currently allowed for the asset|
|deposit_status|disabled|Deposits are currently not allowed for the asset|
|withdrawal_status|enabled|Withdrawals are currently allowed for the asset|
|withdrawal_status|disabled|Withdrawals are currently not allowed for the asset|
|index_type|spot_pair|Index based on a spot trading pair|
|index_type|fixed_interest_rate|Index based on a fixed interest rate|
|index_type|floating_interest_rate|Index based on a floating interest rate|

> **Note:** This operation does not require authentication.

## Get product by symbol

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('https://api.india.delta.exchange/v2/products/{symbol}', params={

}, headers = headers)

print r.json()
```

```shell
# You can also use wget
curl -X GET https://api.india.delta.exchange/v2/products/{symbol} \
  -H 'Accept: application/json'
```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get 'https://api.india.delta.exchange/v2/products/{symbol}',
  params: {
  }, headers: headers

p JSON.parse(result)
```

`GET /products/{symbol}`

The endpoint retrieves details of a specific product identified by its symbol (e.g., BTCUSD, ETHUSD).

### Parameters

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|symbol|path|string|true|symbol of the desired product like BTCUSD, ETHUSD|

> Example responses
>
> 200 Response

```json
{
  "success": true,
  "result": {
    "id": 27,
    "symbol": "BTCUSD",
    "description": "Bitcoin Perpetual futures, quoted, settled & margined in USD",
    "created_at": "2023-12-18T13:10:39Z",
    "updated_at": "2024-11-15T02:47:50Z",
    "settlement_time": null,
    "notional_type": "vanilla",
    "impact_size": 10000,
    "initial_margin": "0.5",
    "maintenance_margin": "0.25",
    "contract_value": "0.001",
    "contract_unit_currency": "BTC",
    "tick_size": "0.5",
    "product_specs": {
      "funding_clamp_value": 0.05,
      "only_reduce_only_orders_allowed": false,
      "expiry_interval": 28800,
      "isolated_liq_penalty_factor": 0.01,
      "rate_exchange_interval": 28800,
      "tags": [
        "layer_1"
      ]
    },
    "state": "live",
    "trading_status": "operational",
    "max_leverage_notional": "100000",
    "default_leverage": "200",
    "initial_margin_scaling_factor": "0.0000025",
    "maintenance_margin_scaling_factor": "0.00000125",
    "taker_commission_rate": "0.0005",
    "maker_commission_rate": "0.0002",
    "liquidation_penalty_factor": "0.5",
    "contract_type": "perpetual_futures",
    "position_size_limit": 229167,
    "basis_factor_max_limit": "10.95",
    "is_quanto": false,
    "funding_method": "mark_price",
    "annualized_funding": "10.95",
    "price_band": "2.5",
    "underlying_asset": {
      "id": 14,
      "symbol": "USD",
      "precision": 8,
      "deposit_status": "enabled",
      "withdrawal_status": "enabled",
      "base_withdrawal_fee": "0.000000000000000000",
      "min_withdrawal_amount": "0.000000000000000000"
    },
    "quoting_asset": {
      "id": 14,
      "symbol": "USD",
      "precision": 8,
      "deposit_status": "enabled",
      "withdrawal_status": "enabled",
      "base_withdrawal_fee": "0.000000000000000000",
      "min_withdrawal_amount": "0.000000000000000000"
    },
    "settling_asset": {
      "id": 14,
      "symbol": "USD",
      "precision": 8,
      "deposit_status": "enabled",
      "withdrawal_status": "enabled",
      "base_withdrawal_fee": "0.000000000000000000",
      "min_withdrawal_amount": "0.000000000000000000"
    },
    "spot_index": {
      "id": 14,
      "symbol": ".DEXBTUSD",
      "constituent_exchanges": [
        {
          "name": "ExchangeA",
          "weight": 0.25
        }
      ],
      "underlying_asset_id": 13,
      "quoting_asset_id": 14,
      "tick_size": "0.5",
      "index_type": "spot_pair"
    }
  }
}
```

### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|[Product](25-schemas.md#tocSproduct)|Inline|

### Response Schema

#### Enumerated Values

|Property|Value|Description|
|---|---|---|
|notional_type|vanilla|Contract is quoted, settled, and margined in the quote currency|
|notional_type|inverse|Contract is quoted in the quote currency but settled and margined in the base currency|
|state|live|Product is currently active and tradable|
|state|expired|Product has expired and is no longer tradable|
|state|upcoming|Product is scheduled to go live in the future|
|trading_status|operational|Trading is fully operational; orders can be placed and cancelled|
|trading_status|disrupted_cancel_only|Trading is disrupted; only order cancellations are allowed|
|trading_status|disrupted_post_only|Trading is disrupted; only post-only orders are accepted|
|deposit_status|enabled|Deposits are currently allowed for the asset|
|deposit_status|disabled|Deposits are currently not allowed for the asset|
|withdrawal_status|enabled|Withdrawals are currently allowed for the asset|
|withdrawal_status|disabled|Withdrawals are currently not allowed for the asset|
|index_type|spot_pair|Index based on a spot trading pair|
|index_type|fixed_interest_rate|Index based on a fixed interest rate|
|index_type|floating_interest_rate|Index based on a floating interest rate|

> **Note:** This operation does not require authentication.

## Get tickers for products

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('https://api.india.delta.exchange/v2/tickers', params={

}, headers = headers)

print r.json()
```

```shell
# You can also use wget
curl -X GET https://api.india.delta.exchange/v2/tickers \
  -H 'Accept: application/json'
```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get 'https://api.india.delta.exchange/v2/tickers',
  params: {
  }, headers: headers

p JSON.parse(result)
```

`GET /tickers`

This endpoint retrieves the live tickers for available trading products, with an optional filter by specified contract types. The contract types should be provided as a comma-separated list (e.g., futures, perpetual_futures, call_options). If no contract type is specified, data for all available products will be returned.

### Parameters

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|contract_types|query|string|false|A comma-separated list of contract types to filter the tickers. Example values include perpetual_futures, call_options, put_options.|
|underlying_asset_symbols|query|string|false|A comma-separated list of underlying asset symbols to filter the tickers. Example values include BTC, ETH, SOL etc.|
|expiry_date|query|string|false|Expiry date(format: DD-MM-YYYY) to filter the tickers.|

> Example responses
>
> 200 Response

```json
{
  "success": true,
  "result": [
    {
      "close": 67321,
      "contract_type": "futures",
      "greeks": {
        "delta": "0.25",
        "gamma": "0.10",
        "rho": "0.05",
        "theta": "-0.02",
        "vega": "0.15"
      },
      "high": 68500.5,
      "low": 66300.25,
      "ltp_change_24h": "0.7061",
      "mark_price": "67000.00",
      "mark_vol": "500",
      "oi": "15000",
      "oi_value": "1000000",
      "oi_value_symbol": "USD",
      "oi_value_usd": "1050000",
      "open": 67000,
      "price_band": {
        "lower_limit": "61120.45",
        "upper_limit": "72300.00"
      },
      "product_id": 123456,
      "quotes": {
        "ask_iv": "0.25",
        "ask_size": "100",
        "best_ask": "150.00",
        "best_bid": "148.00",
        "bid_iv": "0.22",
        "bid_size": "50"
      },
      "size": 100,
      "spot_price": "67000.00",
      "strike_price": "68000.00",
      "symbol": "BTCUSD",
      "timestamp": 1609459200,
      "turnover": 5000000,
      "turnover_symbol": "USD",
      "turnover_usd": 5200000,
      "volume": 25000
    }
  ]
}
```

### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|List of live [tickers](25-schemas.md#tocSticker) for all products, including implied volatility (IV) for option strikes.|Inline|

### Response Schema

> **Note:** This operation does not require authentication.

## Get ticker for a product by symbol

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('https://api.india.delta.exchange/v2/tickers/{symbol}', params={

}, headers = headers)

print r.json()
```

```shell
# You can also use wget
curl -X GET https://api.india.delta.exchange/v2/tickers/{symbol} \
  -H 'Accept: application/json'
```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get 'https://api.india.delta.exchange/v2/tickers/{symbol}',
  params: {
  }, headers: headers

p JSON.parse(result)
```

`GET /tickers/{symbol}`

This endpoint retrieves the ticker data for a specific product, identified by its symbol. The ticker data includes live price data, open interest, implied volatility (IV) for options, and other related market data.

### Parameters

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|symbol|path|string|true|The symbol(s) of the product, comma-separated. Maximum 10 symbols allowed. Example: (e.g., BTCUSD, ETHUSD).|

> Example responses
>
> 200 Response

```json
{
  "success": true,
  "result": {
    "close": 67321,
    "contract_type": "futures",
    "greeks": {
      "delta": "0.25",
      "gamma": "0.10",
      "rho": "0.05",
      "theta": "-0.02",
      "vega": "0.15"
    },
    "high": 68500.5,
    "low": 66300.25,
    "ltp_change_24h": "0.7061",
    "mark_price": "67000.00",
    "mark_vol": "500",
    "oi": "15000",
    "oi_value": "1000000",
    "oi_value_symbol": "USD",
    "oi_value_usd": "1050000",
    "open": 67000,
    "price_band": {
      "lower_limit": "61120.45",
      "upper_limit": "72300.00"
    },
    "product_id": 123456,
    "quotes": {
      "ask_iv": "0.25",
      "ask_size": "100",
      "best_ask": "150.00",
      "best_bid": "148.00",
      "bid_iv": "0.22",
      "bid_size": "50"
    },
    "size": 100,
    "spot_price": "67000.00",
    "strike_price": "68000.00",
    "symbol": "BTCUSD",
    "timestamp": 1609459200,
    "turnover": 5000000,
    "turnover_symbol": "USD",
    "turnover_usd": 5200000,
    "volume": 25000
  }
}
```

### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|[Ticker](25-schemas.md#tocSticker) data for the requested product, including implied volatility (IV) for option strikes, if applicable.|Inline|

### Response Schema

> **Note:** This operation does not require authentication.

## Get option chain

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('https://api.india.delta.exchange/v2/tickers?contract_types=call_options,put_options&underlying_asset_symbols={underlying_asset_symbols}&expiry_date={expiry_date}', params={

}, headers = headers)

print r.json()
```

```shell
# You can also use wget
curl -X GET https://api.india.delta.exchange/v2/tickers?contract_types=call_options,put_options&underlying_asset_symbols={underlying_asset_symbols}&expiry_date={expiry_date} \
  -H 'Accept: application/json'
```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get 'https://api.india.delta.exchange/v2/tickers?contract_types=call_options,put_options&underlying_asset_symbols={underlying_asset_symbols}&expiry_date={expiry_date}',
  params: {
  }, headers: headers

p JSON.parse(result)
```

`GET /tickers?contract_types=call_options,put_options&underlying_asset_symbols={underlying_asset_symbols}&expiry_date={expiry_date}`

Fetch option chain data for a given product and expiry date.

For example, to get BTC call and put options expiring on 04-04-2025, use:

**contract_types=call_options,put_options&underlying_asset_symbols=BTC&expiry_date=04-04-2025**

### Parameters

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|contract_types|query|string|false|A comma-separated list of contract types to filter the products. Only `call_options` and `put_options` are supported.|
|underlying_asset_symbols|query|string|false|The underlying asset symbol (single value) for the option chain. Examples: `BTC`, `ETH`, `SOL`.|
|expiry_date|query|string|false|Expiry date of the contracts in `DD-MM-YYYY` format to filter by current & future expiry date.|

> Example responses
>
> 200 Response

```json
{
  "success": true,
  "result": [
    {
      "close": 67321,
      "contract_type": "futures",
      "greeks": {
        "delta": "0.25",
        "gamma": "0.10",
        "rho": "0.05",
        "theta": "-0.02",
        "vega": "0.15"
      },
      "high": 68500.5,
      "low": 66300.25,
      "ltp_change_24h": "0.7061",
      "mark_price": "67000.00",
      "mark_vol": "500",
      "oi": "15000",
      "oi_value": "1000000",
      "oi_value_symbol": "USD",
      "oi_value_usd": "1050000",
      "open": 67000,
      "price_band": {
        "lower_limit": "61120.45",
        "upper_limit": "72300.00"
      },
      "product_id": 123456,
      "quotes": {
        "ask_iv": "0.25",
        "ask_size": "100",
        "best_ask": "150.00",
        "best_bid": "148.00",
        "bid_iv": "0.22",
        "bid_size": "50"
      },
      "size": 100,
      "spot_price": "67000.00",
      "strike_price": "68000.00",
      "symbol": "BTCUSD",
      "timestamp": 1609459200,
      "turnover": 5000000,
      "turnover_symbol": "USD",
      "turnover_usd": 5200000,
      "volume": 25000
    }
  ]
}
```

### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Returns a list of live [tickers](25-schemas.md#tocSticker) for all products, including **implied volatility (IV)** for option strikes.|Inline|

### Response Schema

> **Note:** This operation does not require authentication.
