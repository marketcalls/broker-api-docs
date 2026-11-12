# Settlement Prices

> Source: https://docs.delta.exchange/#delta-exchange-api-v2-settlement-prices

## Get product settlement prices

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('https://api.india.delta.exchange/v2/products/?states=expired', params={

}, headers = headers)

print r.json()
```

```shell
# You can also use wget
curl -X GET https://api.india.delta.exchange/v2/products/?states=expired \
  -H 'Accept: application/json'
```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get 'https://api.india.delta.exchange/v2/products/?states=expired',
  params: {
  }, headers: headers

p JSON.parse(result)
```

`GET /products/?states=expired`

### Parameters

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|states|query|string|false|Comma separated list of states e.g. to get expired contracts https://api.india.delta.exchange/v2/products?contract_types=call_options&states=expired|
|page_size|query|string|false|size of a single page for paginated request, default: 100|

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
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|List of products|Inline|

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
