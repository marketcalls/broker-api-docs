# Schemas

> Source: https://docs.delta.exchange/#schemas

## ApiSuccessResponse

<a id="schemaapisuccessresponse"></a>

```json
{
  "success": true
}
```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|success|boolean|false|none|none|

## ApiErrorResponse

<a id="schemaapierrorresponse"></a>

```json
{
  "success": false,
  "error": {}
}
```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|success|boolean|false|none|none|
|error|object|false|none|none|

## Index

<a id="schemaindex"></a>

```json
{
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
```

*Details of an index used in trading, including its constituents and characteristics.*

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|integer(int64)|false|none|Unique identifier for the index.|
|symbol|string|false|none|Symbol representing the index, typically prefixed by '.DE' followed by base asset and quoting asset.|
|constituent_exchanges|[object]|false|none|Details of constituent exchanges, including their names and weights in the index.|
|» name|string|false|none|Name of the constituent exchange.|
|» weight|number|false|none|Weight of the exchange in the index.|
|underlying_asset_id|integer|false|none|ID of the underlying asset for the index.|
|quoting_asset_id|integer|false|none|ID of the quoting asset for the index.|
|tick_size|string|false|none|Precision of the spot price in decimal format.|
|index_type|string|false|none|Type of the index.|

#### Enumerated Values

|Property|Value|Description|
|---|---|---|
|index_type|spot_pair|Index based on a spot trading pair|
|index_type|fixed_interest_rate|Index based on a fixed interest rate|
|index_type|floating_interest_rate|Index based on a floating interest rate|

## ArrayOfIndices

<a id="schemaarrayofindices"></a>

```json
[
  {
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
]
```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[Index](#schemaindex)]|false|none|[Details of an index used in trading, including its constituents and characteristics.]|

## ProductSpecs

<a id="schemaproductspecs"></a>

```json
{
  "funding_clamp_value": 0.05,
  "only_reduce_only_orders_allowed": false,
  "expiry_interval": 28800,
  "isolated_liq_penalty_factor": 0.01,
  "rate_exchange_interval": 28800,
  "tags": [
    "layer_1"
  ]
}
```

*Specifications related to the specific product or contract.*

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|funding_clamp_value|number|false|none|The maximum allowable funding rate clamp value.|
|only_reduce_only_orders_allowed|boolean|false|none|Indicates whether only reduce-only orders are allowed.|
|expiry_interval|number|false|none|The time interval, in seconds, after which the product or contract expires or settles.|
|isolated_liq_penalty_factor|number|false|none|The penalty factor applied when an isolated margin position is liquidated.|
|rate_exchange_interval|number|false|none|The time interval, in seconds, at which funding rates are exchanged between long and short positions.|
|tags|[string]|false|none|Tags associated with the product specifications.|

## Asset

<a id="schemaasset"></a>

```json
{
  "id": 14,
  "symbol": "USD",
  "precision": 8,
  "deposit_status": "enabled",
  "withdrawal_status": "enabled",
  "base_withdrawal_fee": "0.000000000000000000",
  "min_withdrawal_amount": "0.000000000000000000"
}
```

*Details of the asset used in the product or contract.*

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|integer(int64)|false|none|Unique identifier for the asset.|
|symbol|string|false|none|Symbol representing the asset.|
|precision|integer|false|none|Number of decimal places supported for the asset.|
|deposit_status|string|false|none|Indicates if deposits are enabled for the asset.|
|withdrawal_status|string|false|none|Indicates if withdrawals are enabled for the asset.|
|base_withdrawal_fee|string|false|none|Fixed withdrawal fee for the asset.|
|min_withdrawal_amount|string|false|none|Minimum allowable withdrawal amount for the asset.|

#### Enumerated Values

|Property|Value|Description|
|---|---|---|
|deposit_status|enabled|Deposits are currently allowed for the asset|
|deposit_status|disabled|Deposits are currently not allowed for the asset|
|withdrawal_status|enabled|Withdrawals are currently allowed for the asset|
|withdrawal_status|disabled|Withdrawals are currently not allowed for the asset|

## ArrayOfAssets

<a id="schemaarrayofassets"></a>

```json
[
  {
    "id": 14,
    "symbol": "USD",
    "precision": 8,
    "deposit_status": "enabled",
    "withdrawal_status": "enabled",
    "base_withdrawal_fee": "0.000000000000000000",
    "min_withdrawal_amount": "0.000000000000000000"
  }
]
```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[Asset](#schemaasset)]|false|none|[Details of the asset used in the product or contract.]|

## Product

<a id="schemaproduct"></a>

```json
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
```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|integer(int64)|false|none|Unique identifier of a product or contract.|
|symbol|string|false|none|Symbol of the product or contract like BTCUSD, ETHUSD.|
|description|string|false|none|Detailed description of the product or contract.|
|created_at|string|false|none|Creation timestamp of the product or contract.|
|updated_at|string|false|none|Last update timestamp of the product or contract.|
|settlement_time|string|false|none|Settlement timestamp for futures contracts.|
|notional_type|string|false|none|Type of notional calculation.|
|impact_size|integer|false|none|Size of a typical trade used for mark price computation.|
|initial_margin|string|false|none|Margin required to open a position.|
|maintenance_margin|string|false|none|Minimum margin required to maintain a position.|
|contract_value|string|false|none|Notional value of the contract (spot price x contract amount).|
|contract_unit_currency|string|false|none|Unit of the contract (underlying asset or settling asset).|
|tick_size|string|false|none|Minimum price interval between two successive prices.|
|product_specs|[ProductSpecs](#schemaproductspecs)|false|none|Specifications related to the specific product or contract.|
|state|string|false|none|Current state of the product.|
|trading_status|string|false|none|Trading status of the contract.|
|max_leverage_notional|string|false|none|Maximum notional position size at the highest leverage.|
|default_leverage|string|false|none|Default leverage assigned to the product.|
|initial_margin_scaling_factor|string|false|none|Scaling factor for initial margin.|
|maintenance_margin_scaling_factor|string|false|none|Scaling factor for maintenance margin.|
|taker_commission_rate|string|false|none|Commission rate for taker trades.|
|maker_commission_rate|string|false|none|Commission rate for maker trades.|
|liquidation_penalty_factor|string|false|none|Factor used to calculate liquidation penalty.|
|contract_type|string|false|none|Type of contract (e.g., futures, perpetual).|
|position_size_limit|integer|false|none|Maximum size for a single contract order.|
|basis_factor_max_limit|string|false|none|Maximum value for annualized basis.|
|is_quanto|boolean|false|none|Indicates if the contract is quanto.|
|funding_method|string|false|none|Method used for funding calculation.|
|annualized_funding|string|false|none|Maximum allowed annualized funding rate.|
|price_band|string|false|none|Price range allowed around the mark price (percentage).|
|underlying_asset|[Asset](#schemaasset)|false|none|Details of the asset used in the product or contract.|
|quoting_asset|[Asset](#schemaasset)|false|none|Details of the asset used in the product or contract.|
|settling_asset|[Asset](#schemaasset)|false|none|Details of the asset used in the product or contract.|
|spot_index|[Index](#schemaindex)|false|none|Details of an index used in trading, including its constituents and characteristics.|

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

## ProductCategories

<a id="schemaproductcategories"></a>

```json
{
  "PutOptions": "string",
  "CallOptions": "string",
  "MoveOptions": "string",
  "Spot": "string",
  "Futures": "string",
  "Perpetual Futures": "string"
}
```

*List of all the product category names on delta exchange. Please refer to this list while subscribing to various public and private channels on delta exchange websocket*

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|PutOptions|string|false|none|put_options|
|CallOptions|string|false|none|call_options|
|MoveOptions|string|false|none|move_options|
|Spot|string|false|none|spot|
|Futures|string|false|none|futures|
|Perpetual Futures|string|false|none|perpetual_futures|

## ArrayOfProducts

<a id="schemaarrayofproducts"></a>

```json
[
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
```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[Product](#schemaproduct)]|false|none|none|

## Order

<a id="schemaorder"></a>

```json
{
  "id": 123,
  "user_id": 453671,
  "size": 10,
  "unfilled_size": 2,
  "side": "buy",
  "order_type": "limit_order",
  "limit_price": "59000",
  "stop_order_type": "stop_loss_order",
  "stop_price": "55000",
  "paid_commission": "0.5432",
  "commission": "0.5432",
  "reduce_only": false,
  "client_order_id": "my_signal_34521712",
  "state": "open",
  "created_at": "1725865012000000",
  "product_id": 27,
  "product_symbol": "BTCUSD"
}
```

*An Order object*

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|integer|false|none|Genraeted order id|
|user_id|integer|false|none|Client id|
|size|integer|false|none|Order size|
|unfilled_size|integer|false|none|Order size which is not filled yet|
|side|string|false|none|Side for which to place order|
|order_type|string|false|none|Order type - limit_order/market_order|
|limit_price|string|false|none|Price level on which order must be triggered|
|stop_order_type|string|false|none|Stop order type - stop loss or take profit|
|stop_price|string|false|none|Stop price level for the stop order|
|paid_commission|string|false|none|Commission paid for filled order|
|commission|string|false|none|Commission blocked for order|
|reduce_only|string|false|none|if set, will only close positions. New orders will not be placed|
|client_order_id|string|false|none|custom id provided by user when creating order (max 32 length)|
|state|string|false|none|Order Status|
|created_at|string|false|none|Created at unix timestamp of the order in micro seconds|
|product_id|integer|false|none|Product id of the ordered product|
|product_symbol|string|false|none|Product symbol of the ordered product|

#### Enumerated Values

|Property|Value|Description|
|---|---|---|
|side|buy|Buy order on the product|
|side|sell|Sell order on the product|
|order_type|limit_order|Order placed at a specified limit price|
|order_type|market_order|Order executed at the best available market price|
|stop_order_type|stop_loss_order|Order triggered when stop price is hit to limit losses|
|reduce_only|false|Order can open or increase a position|
|reduce_only|true|Order can only reduce or close an existing position|
|state|open|Order is active and resting in the orderbook|
|state|pending|Order is waiting for its trigger condition to be met|
|state|closed|Order has been fully filled|
|state|cancelled|Order was cancelled before being fully filled|

## ArrayOfOrders

<a id="schemaarrayoforders"></a>

```json
[
  {
    "id": 123,
    "user_id": 453671,
    "size": 10,
    "unfilled_size": 2,
    "side": "buy",
    "order_type": "limit_order",
    "limit_price": "59000",
    "stop_order_type": "stop_loss_order",
    "stop_price": "55000",
    "paid_commission": "0.5432",
    "commission": "0.5432",
    "reduce_only": false,
    "client_order_id": "my_signal_34521712",
    "state": "open",
    "created_at": "1725865012000000",
    "product_id": 27,
    "product_symbol": "BTCUSD"
  }
]
```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[Order](#schemaorder)]|false|none|[An Order object]|

## CreateOrderRequest

<a id="schemacreateorderrequest"></a>

```json
{
  "product_id": 27,
  "product_symbol": "BTCUSD",
  "limit_price": "59000",
  "size": 10,
  "side": "buy",
  "order_type": "limit_order",
  "stop_order_type": "stop_loss_order",
  "stop_price": "56000",
  "trail_amount": "50",
  "stop_trigger_method": "last_traded_price",
  "bracket_stop_trigger_method": "last_traded_price",
  "bracket_stop_loss_limit_price": "57000",
  "bracket_stop_loss_price": "56000",
  "bracket_trail_amount": "50",
  "bracket_take_profit_limit_price": "62000",
  "bracket_take_profit_price": "61000",
  "time_in_force": "gtc",
  "mmp": "disabled",
  "post_only": false,
  "reduce_only": false,
  "client_order_id": "my_signal_345212",
  "cancel_orders_accepted": false
}
```

*A create order object*

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|product_id|integer|true|none|Only one of either product_id or product_symbol must be sent.|
|product_symbol|string|true|none|Only one of either product_id or product_symbol must be sent.|
|limit_price|string|false|none|Price level for limit orders|
|size|integer|true|none|Order size|
|side|string|true|none|Buy order or Sell order|
|order_type|string|true|none|Limit order(limit_price must be defined) or Market order|
|stop_order_type|string|false|none|Stop order type - stop loss or take profit|
|stop_price|string|false|none|Stop loss price level if the order is stop order|
|trail_amount|string|false|none|Use trail amount if you want a trailing stop order. Required if stop price is empty.|
|stop_trigger_method|string|false|none|Stop order trigger method - mark_price/last_traded_price/spot_price|
|bracket_stop_trigger_method|string|false|none|stop order trigger method for bracket orders - mark_price/last_traded_price/spot_price|
|bracket_stop_loss_limit_price|string|false|none|Bracket order stop loss limit price|
|bracket_stop_loss_price|string|false|none|Bracket order stop loss trigger price|
|bracket_trail_amount|string|false|none|use bracket trail amount if you want a trailing stop order. Required if bracket stop price is empty|
|bracket_take_profit_limit_price|string|false|none|Bracket order take profit limit price|
|bracket_take_profit_price|string|false|none|take profit trigger price for bracket order|
|time_in_force|string|false|none|GTC/IOC order type|
|mmp|string|false|none|MMP level for the order - disabled/mmp1/mmp2/mmp3/mmp4/mmp5|
|post_only|string|false|none|Post only order|
|reduce_only|string|false|none|if set, will only close positions. New orders will not be placed|
|client_order_id|string|false|none|custom id provided by user when creating order (max 32 length)|
|cancel_orders_accepted|string|false|none|if set, will cancel all existing orders for the product|

#### Enumerated Values

|Property|Value|Description|
|---|---|---|
|side|buy|Buy order on the product|
|side|sell|Sell order on the product|
|order_type|limit_order|Order placed at a specified limit price|
|order_type|market_order|Order executed at the best available market price|
|stop_order_type|stop_loss_order|Order triggered when stop price is hit to limit losses|
|stop_order_type|take_profit_order|Order triggered when take profit price is hit to lock in gains|
|stop_trigger_method|mark_price|Order triggered against the mark price|
|stop_trigger_method|last_traded_price|Order triggered against the last traded price|
|stop_trigger_method|spot_price|Order triggered against the spot index price|
|bracket_stop_trigger_method|mark_price|Bracket order triggered against the mark price|
|bracket_stop_trigger_method|last_traded_price|Bracket order triggered against the last traded price|
|bracket_stop_trigger_method|spot_price|Bracket order triggered against the spot index price|
|time_in_force|gtc|Good-till-cancelled; order stays open until filled or cancelled|
|time_in_force|ioc|Immediate-or-cancel; unfilled portion is cancelled immediately|
|mmp|disabled||
|mmp|mmp1||
|mmp|mmp2||
|mmp|mmp3||
|mmp|mmp4||
|mmp|mmp5||
|post_only|true|Order is rejected if it would take liquidity from the orderbook|
|post_only|false|Order is allowed to take liquidity from the orderbook|
|reduce_only|true|Order can only reduce or close an existing position|
|reduce_only|false|Order can open or increase a position|
|cancel_orders_accepted|true|User accepts that existing orders for this product may be cancelled to free margin|
|cancel_orders_accepted|false|Existing orders should not be cancelled to free margin|

## BatchCreateOrder

<a id="schemabatchcreateorder"></a>

```json
{
  "limit_price": "59000",
  "size": 10,
  "side": "buy",
  "order_type": "limit_order",
  "time_in_force": "gtc",
  "mmp": "disabled",
  "post_only": false,
  "client_order_id": "my_signal_34521712"
}
```

*A create order object*

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|limit_price|string|false|none|Price level for limit orders|
|size|integer|true|none|Order size|
|side|string|true|none|Buy order or Sell order|
|order_type|string|true|none|Limit order(limit_price must be defined) or Market order|
|time_in_force|string|false|none|GTC/IOC order type|
|mmp|string|false|none|MMP level for the order - disabled/mmp1/mmp2/mmp3/mmp4/mmp5|
|post_only|string|false|none|Post only order|
|client_order_id|string|false|none|custom id provided by user when creating order (max 32 length)|

#### Enumerated Values

|Property|Value|Description|
|---|---|---|
|side|buy|Buy order on the product|
|side|sell|Sell order on the product|
|order_type|limit_order|Order placed at a specified limit price|
|order_type|market_order|Order executed at the best available market price|
|time_in_force|gtc|Good-till-cancelled; order stays open until filled or cancelled|
|time_in_force|ioc|Immediate-or-cancel; unfilled portion is cancelled immediately|
|mmp|disabled||
|mmp|mmp1||
|mmp|mmp2||
|mmp|mmp3||
|mmp|mmp4||
|mmp|mmp5||
|post_only|true|Order is rejected if it would take liquidity from the orderbook|
|post_only|false|Order is allowed to take liquidity from the orderbook|

## BatchCreateOrdersRequest

<a id="schemabatchcreateordersrequest"></a>

```json
{
  "product_id": 27,
  "product_symbol": "BTCUSD",
  "orders": [
    {
      "limit_price": "59000",
      "size": 10,
      "side": "buy",
      "order_type": "limit_order",
      "time_in_force": "gtc",
      "mmp": "disabled",
      "post_only": false,
      "client_order_id": "my_signal_34521712"
    }
  ]
}
```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|product_id|integer|false|none|Only one of either product_id or product_symbol must be sent.|
|product_symbol|string|false|none|Only one of either product_id or product_symbol must be sent.|
|orders|[[BatchCreateOrder](#schemabatchcreateorder)]|false|none|[A create order object]|

*oneOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|

*xor*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|

## ArrayOfCreateOrderRequest

<a id="schemaarrayofcreateorderrequest"></a>

```json
[
  {
    "product_id": 27,
    "product_symbol": "BTCUSD",
    "limit_price": "59000",
    "size": 10,
    "side": "buy",
    "order_type": "limit_order",
    "stop_order_type": "stop_loss_order",
    "stop_price": "56000",
    "trail_amount": "50",
    "stop_trigger_method": "last_traded_price",
    "bracket_stop_trigger_method": "last_traded_price",
    "bracket_stop_loss_limit_price": "57000",
    "bracket_stop_loss_price": "56000",
    "bracket_trail_amount": "50",
    "bracket_take_profit_limit_price": "62000",
    "bracket_take_profit_price": "61000",
    "time_in_force": "gtc",
    "mmp": "disabled",
    "post_only": false,
    "reduce_only": false,
    "client_order_id": "my_signal_345212",
    "cancel_orders_accepted": false
  }
]
```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[CreateOrderRequest](#schemacreateorderrequest)]|false|none|[A create order object]|

## EditOrderRequest

<a id="schemaeditorderrequest"></a>

```json
{
  "id": 34521712,
  "product_id": 27,
  "product_symbol": "BTCUSD",
  "limit_price": "59000",
  "size": 15,
  "mmp": "disabled",
  "post_only": false,
  "stop_price": "56000",
  "trail_amount": "50"
}
```

*edit order object*

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|integer|true|none|existing order id to be edited|
|product_id|integer|true|none|Only one of either product_id or product_symbol must be sent.|
|product_symbol|string|true|none|Only one of either product_id or product_symbol must be sent.|
|limit_price|string|false|none|Price level for limit orders|
|size|integer|true|none|total size after editing order|
|mmp|string|false|none|MMP level for the order - disabled/mmp1/mmp2/mmp3/mmp4/mmp5|
|post_only|string|false|none|Post only order|
|stop_price|string|false|none|price to trigger stop order|
|trail_amount|string|false|none|Use trail amount if you want a trailing stop order. Required if stop price is empty.|

#### Enumerated Values

|Property|Value|Description|
|---|---|---|
|mmp|disabled||
|mmp|mmp1||
|mmp|mmp2||
|mmp|mmp3||
|mmp|mmp4||
|mmp|mmp5||
|post_only|true|Order is rejected if it would take liquidity from the orderbook|
|post_only|false|Order is allowed to take liquidity from the orderbook|

## BatchEditOrder

<a id="schemabatcheditorder"></a>

```json
{
  "id": 34521712,
  "limit_price": "59000",
  "size": 15,
  "mmp": "disabled",
  "post_only": false
}
```

*edit order object*

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|integer|true|none|existing order id to be edited|
|limit_price|string|false|none|Price level for limit orders|
|size|integer|true|none|total size after editing order|
|mmp|string|false|none|MMP level for the order - disabled/mmp1/mmp2/mmp3/mmp4/mmp5|
|post_only|string|false|none|Post only order|

#### Enumerated Values

|Property|Value|Description|
|---|---|---|
|mmp|disabled||
|mmp|mmp1||
|mmp|mmp2||
|mmp|mmp3||
|mmp|mmp4||
|mmp|mmp5||
|post_only|false|Order is allowed to take liquidity from the orderbook|
|post_only|true|Order is rejected if it would take liquidity from the orderbook|

## BatchEditOrdersRequest

<a id="schemabatcheditordersrequest"></a>

```json
{
  "product_id": 27,
  "product_symbol": "BTCUSD",
  "orders": [
    {
      "id": 34521712,
      "limit_price": "59000",
      "size": 15,
      "mmp": "disabled",
      "post_only": false
    }
  ]
}
```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|product_id|integer|false|none|Only one of either product_id or product_symbol must be sent.|
|product_symbol|string|false|none|Only one of either product_id or product_symbol must be sent.|
|orders|[[BatchEditOrder](#schemabatcheditorder)]|false|none|[edit order object]|

*oneOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|

*xor*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|

## CreateBracketOrderRequest

<a id="schemacreatebracketorderrequest"></a>

```json
{
  "product_id": 27,
  "product_symbol": "BTCUSD",
  "stop_loss_order": {
    "order_type": "limit_order",
    "stop_price": "56000",
    "trail_amount": "50",
    "limit_price": "55000"
  },
  "take_profit_order": {
    "order_type": "limit_order",
    "stop_price": "65000",
    "limit_price": "64000"
  },
  "bracket_stop_trigger_method": "last_traded_price"
}
```

*bracket order object*

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|product_id|integer|true|none|Only one of either product_id or product_symbol must be sent.|
|product_symbol|string|true|none|Only one of either product_id or product_symbol must be sent.|
|stop_loss_order|object|false|none|none|
|» order_type|string|false|none|Limit order(limit_price must be defined) or Market order|
|» stop_price|string|false|none|Stop loss price level|
|» trail_amount|string|false|none|Use trail amount if you want a trailing stop order. Required if stop price is empty.|
|» limit_price|string|false|none|required for limit orders|
|take_profit_order|object|false|none|none|
|» order_type|string|false|none|Limit order(limit_price must be defined) or Market order|
|» stop_price|string|false|none|Stop price level|
|» limit_price|string|false|none|required for limit orders|
|bracket_stop_trigger_method|string|false|none|stop order trigger method for bracket orders- mark_price/last_traded_price/spot_price|

#### Enumerated Values

|Property|Value|Description|
|---|---|---|
|order_type|limit_order|Stop loss is placed as a limit order at the specified limit price|
|order_type|market_order|Stop loss is placed as a market order at the best available price|
|order_type|limit_order|Take profit is placed as a limit order at the specified limit price|
|order_type|market_order|Take profit is placed as a market order at the best available price|
|bracket_stop_trigger_method|mark_price|Bracket order triggered against the mark price|
|bracket_stop_trigger_method|last_traded_price|Bracket order triggered against the last traded price|
|bracket_stop_trigger_method|spot_price|Bracket order triggered against the spot index price|

## EditBracketOrderRequest

<a id="schemaeditbracketorderrequest"></a>

```json
{
  "id": 34521712,
  "product_id": 27,
  "product_symbol": "BTCUSD",
  "bracket_stop_loss_limit_price": "55000",
  "bracket_stop_loss_price": "56000",
  "bracket_take_profit_limit_price": "65000",
  "bracket_take_profit_price": "64000",
  "bracket_trail_amount": "50",
  "bracket_stop_trigger_method": "last_traded_price"
}
```

*bracket order object*

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|integer|true|none|Order ID for which bracket params are being updated|
|product_id|integer|true|none|Only one of either product_id or product_symbol must be sent.|
|product_symbol|string|true|none|Only one of either product_id or product_symbol must be sent.|
|bracket_stop_loss_limit_price|string|false|none|stop loss limit price for bracket order|
|bracket_stop_loss_price|string|false|none|stop loss trigger price for bracket order|
|bracket_take_profit_limit_price|string|false|none|take profit limit price for bracket order|
|bracket_take_profit_price|string|false|none|take profit trigger price for bracket order|
|bracket_trail_amount|string|false|none|trail amount of bracket order|
|bracket_stop_trigger_method|string|false|none|stop order trigger method for bracket orders- mark_price/last_traded_price/spot_price|

#### Enumerated Values

|Property|Value|Description|
|---|---|---|
|bracket_stop_trigger_method|mark_price|Bracket order triggered against the mark price|
|bracket_stop_trigger_method|last_traded_price|Bracket order triggered against the last traded price|
|bracket_stop_trigger_method|spot_price|Bracket order triggered against the spot index price|

## BatchDeleteOrder

<a id="schemabatchdeleteorder"></a>

```json
{
  "id": 13452112,
  "client_order_id": "my_signal_34521712"
}
```

*A delete order object*

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|integer|false|none|use bracket trail amount if you want a trailing stop order. Required if bracket stop price is empty|
|client_order_id|string|false|none|custom id provided by user when creating order (max 32 length)|

## DeleteOrderRequest

<a id="schemadeleteorderrequest"></a>

```json
{
  "id": 13452112,
  "client_order_id": "my_signal_34521712",
  "product_id": 27
}
```

*A delete order object*

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|integer|false|none|use bracket trail amount if you want a trailing stop order. Required if bracket stop price is empty|
|client_order_id|string|false|none|custom id provided by user when creating order (max 32 length)|
|product_id|integer|false|none|product_id of the product in the order|

## CancelAllFilterObject

<a id="schemacancelallfilterobject"></a>

```json
{
  "product_id": 27,
  "contract_types": "perpetual_futures,put_options,call_options",
  "cancel_limit_orders": false,
  "cancel_stop_orders": false,
  "cancel_reduce_only_orders": false
}
```

*Cancel all request filter object*

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|product_id|integer|false|none|Only one of either product_id or product_symbol must be sent.|
|contract_types|string|false|none|comma separated list of desired contract types|
|cancel_limit_orders|string|false|none|set true to cancel open limit orders|
|cancel_stop_orders|string|false|none|set as true to cancel stop orders|
|cancel_reduce_only_orders|string|false|none|set as true to cancel reduce only orders|

#### Enumerated Values

|Property|Value|Description|
|---|---|---|
|cancel_limit_orders|true|Include open limit orders in the cancellation|
|cancel_limit_orders|false|Exclude open limit orders from the cancellation|
|cancel_stop_orders|true|Include open stop orders in the cancellation|
|cancel_stop_orders|false|Exclude open stop orders from the cancellation|
|cancel_reduce_only_orders|true|Include open reduce-only orders in the cancellation|
|cancel_reduce_only_orders|false|Exclude open reduce-only orders from the cancellation|

## BatchDeleteOrdersRequest

<a id="schemabatchdeleteordersrequest"></a>

```json
{
  "product_id": 27,
  "product_symbol": "BTCUSD",
  "orders": [
    {
      "id": 13452112,
      "client_order_id": "my_signal_34521712"
    }
  ]
}
```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|product_id|integer|false|none|Only one of either product_id or product_symbol must be sent.|
|product_symbol|string|false|none|Only one of either product_id or product_symbol must be sent.|
|orders|[[BatchDeleteOrder](#schemabatchdeleteorder)]|false|none|[A delete order object]|

*oneOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|

*xor*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|

## Position

<a id="schemaposition"></a>

```json
{
  "user_id": 0,
  "size": 0,
  "entry_price": "string",
  "margin": "string",
  "liquidation_price": "string",
  "bankruptcy_price": "string",
  "adl_level": 0,
  "product_id": 0,
  "product_symbol": "string",
  "commission": "string",
  "realized_pnl": "string",
  "realized_funding": "string"
}
```

*A position object*

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|user_id|integer|false|none|none|
|size|integer|false|none|Position size, negative for short and positive for long|
|entry_price|string|false|none|none|
|margin|string|false|none|none|
|liquidation_price|string|false|none|none|
|bankruptcy_price|string|false|none|none|
|adl_level|integer|false|none|none|
|product_id|integer|false|none|none|
|product_symbol|string|false|none|none|
|commission|string|false|none|commissions blocked in the position|
|realized_pnl|string|false|none|Net realized pnl since the position was opened|
|realized_funding|string|false|none|Net realized funding since the position was opened|

## ArrayOfPositions

<a id="schemaarrayofpositions"></a>

```json
[
  {
    "user_id": 0,
    "size": 0,
    "entry_price": "string",
    "margin": "string",
    "liquidation_price": "string",
    "bankruptcy_price": "string",
    "adl_level": 0,
    "product_id": 0,
    "product_symbol": "string",
    "commission": "string",
    "realized_pnl": "string",
    "realized_funding": "string"
  }
]
```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[Position](#schemaposition)]|false|none|[A position object]|

## Fill

<a id="schemafill"></a>

```json
{
  "id": 0,
  "size": 0,
  "fill_type": "normal",
  "side": "buy",
  "price": "string",
  "role": "taker",
  "commission": "string",
  "created_at": "string",
  "product_id": 0,
  "product_symbol": "string",
  "order_id": "string",
  "settling_asset_id": 0,
  "settling_asset_symbol": "string",
  "meta_data": {
    "commission_deto": "string",
    "commission_deto_in_settling_asset": "string",
    "effective_commission_rate": "string",
    "liquidation_fee_deto": "string",
    "liquidation_fee_deto_in_settling_asset": "string",
    "order_price": "string",
    "order_size": "string",
    "order_type": "string",
    "order_unfilled_size": "string",
    "tfc_used_for_commission": "string",
    "tfc_used_for_liquidation_fee": "string",
    "total_commission_in_settling_asset": "string",
    "total_liquidation_fee_in_settling_asset": "string"
  }
}
```

*A fill object*

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|integer|false|none|none|
|size|integer|false|none|none|
|fill_type|string|false|none|none|
|side|string|false|none|none|
|price|string|false|none|Price at which the fill happened, BigDecimal sent as string|
|role|string|false|none|none|
|commission|string|false|none|Commission paid on this fill, negative value means commission was earned because of maker role|
|created_at|string|false|none|none|
|product_id|integer|false|none|none|
|product_symbol|string|false|none|none|
|order_id|string|false|none|Will be order_id(Integer) in most cases. Will be UUID string of order when fill_type is settlement|
|settling_asset_id|integer|false|none|none|
|settling_asset_symbol|string|false|none|none|
|meta_data|[FillMetaData](#schemafillmetadata)|false|none|Meta data inside fill|

#### Enumerated Values

|Property|Value|Description|
|---|---|---|
|fill_type|normal|Regular fill from matching against the orderbook|
|fill_type|adl|Fill from auto-deleveraging to balance counterparty exposure|
|fill_type|liquidation|Fill resulting from forced liquidation of a position|
|fill_type|settlement|Fill generated at contract settlement or expiry|
|fill_type|otc|Off-exchange (over-the-counter) fill|
|side|buy|Buy order on the product|
|side|sell|Sell order on the product|
|role|taker|Fill where the user removed liquidity from the orderbook|
|role|maker|Fill where the user added liquidity to the orderbook|

## ArrayOfFills

<a id="schemaarrayoffills"></a>

```json
[
  {
    "id": 0,
    "size": 0,
    "fill_type": "normal",
    "side": "buy",
    "price": "string",
    "role": "taker",
    "commission": "string",
    "created_at": "string",
    "product_id": 0,
    "product_symbol": "string",
    "order_id": "string",
    "settling_asset_id": 0,
    "settling_asset_symbol": "string",
    "meta_data": {
      "commission_deto": "string",
      "commission_deto_in_settling_asset": "string",
      "effective_commission_rate": "string",
      "liquidation_fee_deto": "string",
      "liquidation_fee_deto_in_settling_asset": "string",
      "order_price": "string",
      "order_size": "string",
      "order_type": "string",
      "order_unfilled_size": "string",
      "tfc_used_for_commission": "string",
      "tfc_used_for_liquidation_fee": "string",
      "total_commission_in_settling_asset": "string",
      "total_liquidation_fee_in_settling_asset": "string"
    }
  }
]
```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[Fill](#schemafill)]|false|none|[A fill object]|

## FillMetaData

<a id="schemafillmetadata"></a>

```json
{
  "commission_deto": "string",
  "commission_deto_in_settling_asset": "string",
  "effective_commission_rate": "string",
  "liquidation_fee_deto": "string",
  "liquidation_fee_deto_in_settling_asset": "string",
  "order_price": "string",
  "order_size": "string",
  "order_type": "string",
  "order_unfilled_size": "string",
  "tfc_used_for_commission": "string",
  "tfc_used_for_liquidation_fee": "string",
  "total_commission_in_settling_asset": "string",
  "total_liquidation_fee_in_settling_asset": "string"
}
```

*Meta data inside fill*

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|commission_deto|string|false|none|none|
|commission_deto_in_settling_asset|string|false|none|none|
|effective_commission_rate|string|false|none|none|
|liquidation_fee_deto|string|false|none|none|
|liquidation_fee_deto_in_settling_asset|string|false|none|none|
|order_price|string|false|none|none|
|order_size|string|false|none|none|
|order_type|string|false|none|none|
|order_unfilled_size|string|false|none|none|
|tfc_used_for_commission|string|false|none|none|
|tfc_used_for_liquidation_fee|string|false|none|none|
|total_commission_in_settling_asset|string|false|none|none|
|total_liquidation_fee_in_settling_asset|string|false|none|none|

## OrderLeverage

<a id="schemaorderleverage"></a>

```json
{
  "leverage": 10,
  "order_margin": "563.2",
  "product_id": 27
}
```

*Order Leverage for a product*

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|leverage|string|false|none|Leverage of all open orders for this product|
|order_margin|string|false|none|Margin blocked in open orders for this product|
|product_id|integer|false|none|Product id of the ordered product|

## L2Orderbook

<a id="schemal2orderbook"></a>

```json
{
  "buy": [
    {
      "depth": "983",
      "price": "9187.5",
      "size": 205640
    }
  ],
  "last_updated_at": 1654589595784000,
  "sell": [
    {
      "depth": "1185",
      "price": "9188.0",
      "size": 113752
    }
  ],
  "symbol": "BTCUSD"
}
```

*L2 orderbook*

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|buy|[object]|false|none|none|
|» depth|string|false|none|sum of size till that price level|
|» price|string|false|none|none|
|» size|integer|false|none|for derivatives -> number of contracts, for spot -> amount in underlying|
|last_updated_at|integer|false|none|none|
|sell|[object]|false|none|none|
|» depth|string|false|none|sum of size till that price level|
|» price|string|false|none|none|
|» size|integer|false|none|for derivatives -> number of contracts, for spot -> amount in underlying|
|symbol|string|false|none|none|

## Trades

<a id="schematrades"></a>

```json
{
  "trades": [
    {
      "side": "buy",
      "size": 0,
      "price": "string",
      "timestamp": 0
    }
  ]
}
```

*trades of a symbol*

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|trades|[object]|false|none|none|
|» side|string|false|none|none|
|» size|integer|false|none|none|
|» price|string|false|none|none|
|» timestamp|integer|false|none|none|

#### Enumerated Values

|Property|Value|Description|
|---|---|---|
|side|buy|Trade where the aggressor was a buyer|
|side|sell|Trade where the aggressor was a seller|

## Wallet

<a id="schemawallet"></a>

```json
{
  "asset_id": 0,
  "asset_symbol": "string",
  "available_balance": "string",
  "available_balance_for_robo": "string",
  "balance": "string",
  "blocked_margin": "string",
  "commission": "string",
  "cross_asset_liability": "string",
  "cross_commission": "string",
  "cross_locked_collateral": "string",
  "cross_order_margin": "string",
  "cross_position_margin": "string",
  "id": 0,
  "interest_credit": "string",
  "order_margin": "string",
  "pending_referral_bonus": "string",
  "pending_trading_fee_credit": "string",
  "portfolio_margin": "string",
  "position_margin": "string",
  "trading_fee_credit": "string",
  "unvested_amount": "string",
  "user_id": 0
}
```

*Wallet Data for each asset.*

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|asset_id|integer|false|none|Id for assets like BTC|
|asset_symbol|string|false|none|Symbol for assets like BTC|
|available_balance|string|false|none|Balance available for trading|
|available_balance_for_robo|string|false|none|Balance available for robo trading|
|balance|string|false|none|Total wallet balance|
|blocked_margin|string|false|none|Total blocked margin including commissions for all modes|
|commission|string|false|none|Commissions blocked in Isolated Mode|
|cross_asset_liability|string|false|none|Asset liability in Cross margin mode|
|cross_commission|string|false|none|Commision blocked in Cross margin mode|
|cross_locked_collateral|string|false|none|collateral blocked in Cross margin mode|
|cross_order_margin|string|false|none|margin blocked for open orders in Cross margin mode|
|cross_position_margin|string|false|none|margin blocked for open positions in Cross margin mode|
|id|integer|false|none|Wallet Id|
|interest_credit|string|false|none|Total interest credited|
|order_margin|string|false|none|margin blocked for open positions in isolated mode|
|pending_referral_bonus|string|false|none|Pending referral bonus|
|pending_trading_fee_credit|string|false|none|Credit of trading fee pending|
|portfolio_margin|string|false|none|Total margin blocked including commissions in portfolio margin mode|
|position_margin|string|false|none|Margin blocked in open positions in isolated mode|
|trading_fee_credit|string|false|none|Credit of trading fee|
|unvested_amount|string|false|none|Amount currently unvested|
|user_id|integer|false|none|User Id linked to this wallet|

## WalletPayload

<a id="schemawalletpayload"></a>

```json
{
  "meta": {
    "net_equity": "string",
    "robo_trading_equity": "string"
  },
  "result": [
    {
      "asset_id": 0,
      "asset_symbol": "string",
      "available_balance": "string",
      "available_balance_for_robo": "string",
      "balance": "string",
      "blocked_margin": "string",
      "commission": "string",
      "cross_asset_liability": "string",
      "cross_commission": "string",
      "cross_locked_collateral": "string",
      "cross_order_margin": "string",
      "cross_position_margin": "string",
      "id": 0,
      "interest_credit": "string",
      "order_margin": "string",
      "pending_referral_bonus": "string",
      "pending_trading_fee_credit": "string",
      "portfolio_margin": "string",
      "position_margin": "string",
      "trading_fee_credit": "string",
      "unvested_amount": "string",
      "user_id": 0
    }
  ],
  "success": true
}
```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|meta|[WalletMetaData](#schemawalletmetadata)|false|none|Meta data for robo trading|
|result|[ArrayOfWallets](#schemaarrayofwallets)|false|none|Array of wallet for every asset|
|success|boolean|false|none|none|

## WalletMetaData

<a id="schemawalletmetadata"></a>

```json
{
  "net_equity": "string",
  "robo_trading_equity": "string"
}
```

*Meta data for robo trading*

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|net_equity|string|false|none|Net equity for robo trading|
|robo_trading_equity|string|false|none|trading equity for robo trading|

## ArrayOfWallets

<a id="schemaarrayofwallets"></a>

```json
[
  {
    "asset_id": 0,
    "asset_symbol": "string",
    "available_balance": "string",
    "available_balance_for_robo": "string",
    "balance": "string",
    "blocked_margin": "string",
    "commission": "string",
    "cross_asset_liability": "string",
    "cross_commission": "string",
    "cross_locked_collateral": "string",
    "cross_order_margin": "string",
    "cross_position_margin": "string",
    "id": 0,
    "interest_credit": "string",
    "order_margin": "string",
    "pending_referral_bonus": "string",
    "pending_trading_fee_credit": "string",
    "portfolio_margin": "string",
    "position_margin": "string",
    "trading_fee_credit": "string",
    "unvested_amount": "string",
    "user_id": 0
  }
]
```

*Array of wallet for every asset*

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[Wallet](#schemawallet)]|false|none|Array of wallet for every asset|

## AssetTransferSubaccountReq

<a id="schemaassettransfersubaccountreq"></a>

```json
{
  "transferrer_user_id": "string",
  "transferee_user_id": "string",
  "asset_symbol": "string",
  "amount": null
}
```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|transferrer_user_id|string|false|none|Debit account|
|transferee_user_id|string|false|none|Credit account|
|asset_symbol|string|false|none|Asset to transfer|
|amount|big_decimal|false|none|Amount to transfer. Only postive values allowed.|

## SubaccountTransferHistory

<a id="schemasubaccounttransferhistory"></a>

```json
{
  "subaccount_user_id": "string",
  "before": "string",
  "after": "string",
  "page_size": 10
}
```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|subaccount_user_id|string|false|none|subaccount user id|
|before|string|false|none|before cursor for pagination|
|after|string|false|none|after cursor for pagination|
|page_size|big_decimal|false|none|records per page|

## TransactionTypes

<a id="schematransactiontypes"></a>

```json
"string"
```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|string|false|none|none|
|transaction_type|string|false|none|none|

#### Enumerated Values

|Property|Value|Description|
|---|---|---|
|transaction_type|cashflow|Generic cash credit or debit on the wallet|
|transaction_type|deposit|Funds deposited into the wallet|
|transaction_type|withdrawal|Funds withdrawn from the wallet|
|transaction_type|commission|Trading commission charged on a fill|
|transaction_type|conversion|Currency or asset conversion entry|
|transaction_type|funding|Perpetual funding payment exchanged between long and short|
|transaction_type|settlement|Wallet entry generated at contract settlement|
|transaction_type|liquidation_fee|Fee charged when a position is liquidated|
|transaction_type|spot_trade|Wallet entry from a spot trade|
|transaction_type|withdrawal_cancellation|Reversal of a previously requested withdrawal|
|transaction_type|referral_bonus|Bonus credited from the referral program|
|transaction_type|sub_account_transfer|Transfer between a main account and a subaccount|
|transaction_type|commission_rebate|Rebate paid back on previously charged commission|
|transaction_type|promo_credit|Promotional credit added to the wallet|
|transaction_type|trading_credits|Trading credits granted to the user|
|transaction_type|trading_credits_forfeited|Trading credits forfeited (e.g. on expiry)|
|transaction_type|trading_credits_paid|Trading credits applied toward trading fees|
|transaction_type|trading_fee_credits_paid_liquidation_fee|Trading credits applied toward a liquidation fee|
|transaction_type|trading_credits_reverted|Reversal of previously applied trading credits|
|transaction_type|interest_credit|Interest credited on the wallet balance|
|transaction_type|external_deposit|Deposit from an external/off-exchange source|
|transaction_type|credit_line|Credit line adjustment on the wallet|
|transaction_type|trading_competition|Wallet entry related to a trading competition|
|transaction_type|fund_deposit|Deposit into a managed fund|
|transaction_type|fund_withdrawal|Withdrawal from a managed fund|
|transaction_type|fund_wallet_deposit|Deposit into the fund wallet|
|transaction_type|fund_wallet_withdrawal|Withdrawal from the fund wallet|
|transaction_type|fund_reward|Reward credited from a managed fund|
|transaction_type|trade_farming_reward|Reward credited from the trade farming program|
|transaction_type|interest_credit|Interest credited on the wallet balance|
|transaction_type|revert|Reversal of a prior wallet transaction|
|transaction_type|raf_bonus|Refer-a-friend bonus credited to the wallet|
|transaction_type|fill_appropriation|Adjustment from appropriation of a fill|
|transaction_type|incident_compensation|Compensation credited due to an incident|

## Transaction

<a id="schematransaction"></a>

```json
{
  "id": 0,
  "amount": "string",
  "balance": "string",
  "transaction_type": "string",
  "meta_data": {},
  "product_id": 0,
  "asset_id": 0,
  "asset_symbol": 0,
  "created_at": "string"
}
```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|integer|false|none|none|
|amount|string|false|none|amount credited/debited in this transaction (+ for credited, - for debited)|
|balance|string|false|none|net wallet balance after this transaction|
|transaction_type|[TransactionTypes](#schematransactiontypes)|false|none|none|
|meta_data|object|false|none|none|
|product_id|integer|false|none|none|
|asset_id|integer|false|none|none|
|asset_symbol|integer|false|none|none|
|created_at|string|false|none|none|

## ArrayOfTransactions

<a id="schemaarrayoftransactions"></a>

```json
[
  {
    "id": 0,
    "amount": "string",
    "balance": "string",
    "transaction_type": "string",
    "meta_data": {},
    "product_id": 0,
    "asset_id": 0,
    "asset_symbol": 0,
    "created_at": "string"
  }
]
```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[Transaction](#schematransaction)]|false|none|none|

## SubaccountTransferLog

<a id="schemasubaccounttransferlog"></a>

```json
{
  "transferrer_user_id": "string",
  "transferee_user_id": "string",
  "asset_symbol": "string",
  "amount": null,
  "created_at": "string",
  "transferee_user": {},
  "transferrer_user": {}
}
```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|transferrer_user_id|string|false|none|User id of the account debited with the asset.|
|transferee_user_id|string|false|none|User id of the account credited with the asset.|
|asset_symbol|string|false|none|Asset symbol transferred.|
|amount|big_decimal|false|none|Amount transferred.|
|created_at|string|false|none|transfer creation date and time|
|transferee_user|object|false|none|User details|
|transferrer_user|object|false|none|User details|

## ArrayOfSubaccountTransferLog

<a id="schemaarrayofsubaccounttransferlog"></a>

```json
[
  {
    "transferrer_user_id": "string",
    "transferee_user_id": "string",
    "asset_symbol": "string",
    "amount": null,
    "created_at": "string",
    "transferee_user": {},
    "transferrer_user": {}
  }
]
```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[SubaccountTransferLog](#schemasubaccounttransferlog)]|false|none|none|

## greeks

<a id="schemagreeks"></a>

```json
{
  "delta": "0.25",
  "gamma": "0.10",
  "rho": "0.05",
  "theta": "-0.02",
  "vega": "0.15"
}
```

*The Greeks represent different factors that influence the pricing of options. These are key measures for assessing risk and managing option positions.*

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|delta|string|false|none|The rate of change of the option price with respect to changes in the underlying asset price. A measure of sensitivity to the asset price movement.|
|gamma|string|false|none|The rate of change of delta with respect to changes in the underlying asset price. A measure of the curvature of the option’s price sensitivity to the asset price.|
|rho|string|false|none|The rate of change of the option price with respect to changes in the risk-free interest rate. A measure of interest rate sensitivity.|
|theta|string|false|none|The rate of change of the option price with respect to time, often referred to as time decay. A measure of how the option's price declines as expiration approaches.|
|vega|string|false|none|The rate of change of the option price with respect to changes in the volatility of the underlying asset. A measure of volatility sensitivity.|

## price_band

<a id="schemaprice_band"></a>

```json
{
  "lower_limit": "61120.45",
  "upper_limit": "72300.00"
}
```

*The price band defines the permissible price range for a product. The lower and upper limits represent the boundaries within which the product's price can fluctuate.*

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|lower_limit|string|false|none|The minimum price limit for the product. It defines the lowest allowable price before triggering a price band constraint.|
|upper_limit|string|false|none|The maximum price limit for the product. It defines the highest allowable price before triggering a price band constraint.|

## quotes

<a id="schemaquotes"></a>

```json
{
  "ask_iv": "0.25",
  "ask_size": "100",
  "best_ask": "150.00",
  "best_bid": "148.00",
  "bid_iv": "0.22",
  "bid_size": "50"
}
```

*The 'quotes' object contains the latest bid and ask prices, their respective implied volatilities (IV), and order sizes for an asset. It provides key market data for understanding liquidity and pricing.*

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|ask_iv|string|false|none|The implied volatility (IV) for the ask price. Represents the market's expectation of the future volatility of the underlying asset.|
|ask_size|string|false|none|The size of the ask order, representing the quantity of the asset available for sale at the ask price.|
|best_ask|string|false|none|The best (lowest) ask price available in the market for the asset.|
|best_bid|string|false|none|The best (highest) bid price available in the market for the asset.|
|bid_iv|string|false|none|The implied volatility (IV) for the bid price. Represents the market's expectation of future volatility for the bid side of the order book.|
|bid_size|string|false|none|The size of the bid order, representing the quantity of the asset that buyers are willing to purchase at the bid price.|

## Ticker

<a id="schematicker"></a>

```json
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
```

*The 'Ticker' object provides real-time trading data for a specific product, including prices, volumes, open interest, and Greek values (for options). This data is essential for analyzing market trends and asset performance.*

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|close|integer|false|none|The closing price of the last trade for the product.|
|contract_type|string|false|none|Comma-separated list of contract types, such as futures, perpetual_futures, call_options, put_options.|
|greeks|[greeks](#schemagreeks)|false|none|The Greeks represent different factors that influence the pricing of options. These are key measures for assessing risk and managing option positions.|
|high|number|false|none|The highest price reached during the trading session.|
|low|number|false|none|The lowest price reached during the trading session.|
|ltp_change_24h|string|false|none|The percentage change in the last traded price over the last 24 hours.|
|mark_price|string|false|none|The market price of the product, reflecting the most recent transaction.|
|mark_vol|string|false|none|The market volume at the most recent trade price.|
|oi|string|false|none|The open interest, or the number of outstanding contracts, for the product.|
|oi_value|string|false|none|The value of the open interest in the base currency.|
|oi_value_symbol|string|false|none|The symbol representing the currency of the open interest value.|
|oi_value_usd|string|false|none|The open interest value converted to USD.|
|open|number|false|none|The opening price at the start of the trading session.|
|price_band|[price_band](#schemaprice_band)|false|none|The price band defines the permissible price range for a product. The lower and upper limits represent the boundaries within which the product's price can fluctuate.|
|product_id|number|false|none|A unique identifier for the product.|
|quotes|[quotes](#schemaquotes)|false|none|The 'quotes' object contains the latest bid and ask prices, their respective implied volatilities (IV), and order sizes for an asset. It provides key market data for understanding liquidity and pricing.|
|size|number|false|none|The size of the most recent order executed in the market.|
|spot_price|string|false|none|The current spot price of the underlying asset.|
|strike_price|string|false|none|The strike price for options contracts associated with the product.|
|symbol|string|false|none|The ticker symbol for the product.|
|timestamp|number|false|none|The timestamp of the last trade or update to the ticker.|
|turnover|number|false|none|The total turnover (value traded) for the product during the trading session.|
|turnover_symbol|string|false|none|The symbol representing the currency in which the turnover is measured.|
|turnover_usd|number|false|none|The turnover value converted to USD.|
|volume|integer|false|none|The total trading volume for the product during the trading session.|

## ArrayOfTickers

<a id="schemaarrayoftickers"></a>

```json
[
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
```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[Ticker](#schematicker)]|false|none|[The 'Ticker' object provides real-time trading data for a specific product, including prices, volumes, open interest, and Greek values (for options). This data is essential for analyzing market trends and asset performance.]|

## PaginationMeta

<a id="schemapaginationmeta"></a>

```json
{
  "after": "g3QAAAACZAAKY3JlYXRlZF9hdHQAAAAN",
  "before": "a2PQRSACZAAKY3JlYXRlZF3fnqHBBBNZL"
}
```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|after|string|false|none|after cursor for pagination; becomes null if page after the current one does not exist|
|before|string|false|none|before cursor for pagination; becomes null if page before the current one does not exist|

## OHLCData

<a id="schemaohlcdata"></a>

```json
{
  "time": 0,
  "open": 0,
  "high": 0,
  "low": 0,
  "close": 0,
  "volume": 0
}
```

*A ohlc object*

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|time|integer|false|none|none|
|open|number|false|none|none|
|high|number|false|none|none|
|low|number|false|none|none|
|close|number|false|none|none|
|volume|number|false|none|none|

## ArrayOfOHLCData

<a id="schemaarrayofohlcdata"></a>

```json
[
  {
    "time": 0,
    "open": 0,
    "high": 0,
    "low": 0,
    "close": 0,
    "volume": 0
  }
]
```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[OHLCData](#schemaohlcdata)]|false|none|[A ohlc object]|

## SparklineData

<a id="schemasparklinedata"></a>

```json
{
  "ETHUSD": [
    [
      1594214051,
      0.00003826
    ],
    [
      1594214051,
      0.00003826
    ]
  ],
  "MARK:BTCUSD": [
    [
      1594215270,
      0.00003826
    ]
  ]
}
```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|**additionalProperties**|[integer]|false|none|array of timestamp and closing value|

## Stats

<a id="schemastats"></a>

```json
{
  "last_30_days_volume": 0,
  "last_7_days_volume": 0,
  "total_volume": 0
}
```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|last_30_days_volume|integer|false|none|sum of turnover usd in the last 30 days|
|last_7_days_volume|integer|false|none|sum of turnover usd in the last 7 days|
|total_volume|integer|false|none|sum of turnover usd in the last 24 hours|

## MMPConfigUpdateRequest

<a id="schemammpconfigupdaterequest"></a>

```json
{
  "asset": "string",
  "window_interval": 0,
  "freeze_interval": 0,
  "trade_limit": "string",
  "delta_limit": "string",
  "vega_limit": "string",
  "mmp": "mmp1"
}
```

*MMP config for an underlying*

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|asset|string|false|none|none|
|window_interval|integer|false|none|Window interval in seconds|
|freeze_interval|integer|false|none|MMP freeze interval in seconds. Setting this to zero will require a manual reset once mmp is triggered.|
|trade_limit|string|false|none|Notional trade limit for mmp to trigger (in USD)|
|delta_limit|string|false|none|Delta Adjusted notional trade limit for mmp to trigger (in USD)|
|vega_limit|string|false|none|vega traded limit for mmp to trigger (in USD)|
|mmp|string|false|none|Specify mmp flag for the config update|

#### Enumerated Values

|Property|Value|Description|
|---|---|---|
|mmp|mmp1||
|mmp|mmp2||
|mmp|mmp3||
|mmp|mmp4||
|mmp|mmp5||

## MMPResetRequest

<a id="schemammpresetrequest"></a>

```json
{
  "asset": "string",
  "mmp": "mmp1"
}
```

*MMP config for an underlying*

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|asset|string|false|none|none|
|mmp|string|false|none|specify mmp flag to reset|

#### Enumerated Values

|Property|Value|Description|
|---|---|---|
|mmp|mmp1||
|mmp|mmp2||
|mmp|mmp3||
|mmp|mmp4||
|mmp|mmp5||

## ChangeMarginModeRequest

<a id="schemachangemarginmoderequest"></a>

```json
{
  "margin_mode": "isolated",
  "subaccount_user_id": "5112346"
}
```

*Request to change the margin mode for a main or subaccount.*

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|margin_mode|string|false|none|The target margin mode: 'isolated' or 'portfolio'.|
|subaccount_user_id|string|false|none|The user ID of the account. Provide the main user ID for the main account or the respective subaccount user ID.|

#### Enumerated Values

|Property|Value|Description|
|---|---|---|
|margin_mode|isolated|Margin is allocated per position; loss on one position cannot draw from others|
|margin_mode|portfolio|Portfolio margin is shared across positions to net out risk|

## UserPreference

<a id="schemauserpreference"></a>

```json
{
  "user_id": 57354187,
  "default_auto_topup": true,
  "mmp_config": null,
  "deto_for_commission": false,
  "vip_level": 0,
  "vip_discount_factor": "0.00",
  "volume_30d": "1060.675333",
  "email_preferences": {
    "adl": true,
    "liquidation": true,
    "margin_topup": false,
    "marketing": true,
    "order_cancel": true,
    "order_fill": true,
    "stop_order_trigger": true
  },
  "notification_preferences": {
    "adl": true,
    "liquidation": true,
    "margin_topup": false,
    "marketing": true,
    "order_cancel": false,
    "order_fill": true,
    "price_alert": true,
    "stop_order_trigger": true
  },
  "price_alert_assets": [
    "BTC",
    "ETH"
  ],
  "enabled_portfolios": {},
  "interest_credit": false
}
```

*User trading preferences*

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|user_id|integer|false|none|Unique identifier for the user|
|default_auto_topup|boolean|false|none|Default auto top-up setting for newly acquired positions (only for isolated mode)|
|mmp_config|object¦null|false|none|Config object for market maker protection (only for MMP-enabled accounts)|
|deto_for_commission|boolean|false|none|Flag to determine whether to pay commissions in DETO|
|vip_level|integer|false|none|VIP level for this account. Customers get better fee discounting for higher VIP levels|
|vip_discount_factor|string|false|none|Discount factor based on the VIP level|
|volume_30d|string|false|none|30-day trading volume for the user|
|email_preferences|object|false|none|Email preferences for different events|
|» adl|boolean|false|none|none|
|» liquidation|boolean|false|none|none|
|» margin_topup|boolean|false|none|none|
|» marketing|boolean|false|none|none|
|» order_cancel|boolean|false|none|none|
|» order_fill|boolean|false|none|none|
|» stop_order_trigger|boolean|false|none|none|
|notification_preferences|object|false|none|Notification preferences for different events|
|» adl|boolean|false|none|none|
|» liquidation|boolean|false|none|none|
|» margin_topup|boolean|false|none|none|
|» marketing|boolean|false|none|none|
|» order_cancel|boolean|false|none|none|
|» order_fill|boolean|false|none|none|
|» price_alert|boolean|false|none|none|
|» stop_order_trigger|boolean|false|none|none|
|price_alert_assets|[string]|false|none|Assets for which price alerts are set|
|enabled_portfolios|object|false|none|Enabled portfolios for the user|
|interest_credit|boolean|false|none|Whether the user is receiving interest credits|

## EditUserPreference

<a id="schemaedituserpreference"></a>

```json
{
  "default_auto_topup": true,
  "showMarketOrdersForOptionsInBracket": true,
  "interest_credit": false,
  "email_preferences": {
    "adl": true,
    "liquidation": true,
    "order_fill": true,
    "stop_order_trigger": true,
    "order_cancel": true,
    "marketing": true
  },
  "notification_preferences": {
    "adl": false,
    "liquidation": true,
    "order_fill": true,
    "stop_order_trigger": true,
    "price_alert": true,
    "marketing": true
  }
}
```

*Edit User Preference Object*

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|default_auto_topup|boolean|false|none|Default auto top-up setting for newly acquired positions|
|showMarketOrdersForOptionsInBracket|boolean|false|none|Flag to display market orders for options in bracket orders|
|interest_credit|boolean|false|none|Whether the user is receiving interest credits|
|email_preferences|object|false|none|Email preferences for different events|
|» adl|boolean|false|none|none|
|» liquidation|boolean|false|none|none|
|» order_fill|boolean|false|none|none|
|» stop_order_trigger|boolean|false|none|none|
|» order_cancel|boolean|false|none|none|
|» marketing|boolean|false|none|none|
|notification_preferences|object|false|none|Notification preferences for different events|
|» adl|boolean|false|none|none|
|» liquidation|boolean|false|none|none|
|» order_fill|boolean|false|none|none|
|» stop_order_trigger|boolean|false|none|none|
|» price_alert|boolean|false|none|none|
|» marketing|boolean|false|none|none|

## User

<a id="schemauser"></a>

```json
{
  "id": "98765432",
  "email": "[email protected]",
  "account_name": "Main",
  "first_name": "Rajesh",
  "last_name": "Sharma",
  "dob": "1985-08-25",
  "country": "India",
  "phone_number": "9876543210",
  "margin_mode": "isolated",
  "pf_index_symbol": ".DEXBTUSD",
  "is_sub_account": false,
  "is_kyc_done": true
}
```

*Represents a user account with personal and account-related details.*

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string|false|none|Unique user identifier, which can be an integer or string.|
|email|string|false|none|User's email address.|
|account_name|string|false|none|The main account or subaccount name.|
|first_name|string|false|none|User's first name.|
|last_name|string|false|none|User's last name.|
|dob|string(date)|false|none|Date of birth in YYYY-MM-DD format.|
|country|string|false|none|User's country of residence.|
|phone_number|string|false|none|User's phone number with country code.|
|margin_mode|string|false|none|The user's margin mode, which can be 'isolated' or 'portfolio'.|
|pf_index_symbol|string|false|none|Portfolio index symbol if the account is in portfolio margin mode.|
|is_sub_account|boolean|false|none|Indicates if the user account is a sub-account.|
|is_kyc_done|boolean|false|none|Indicates if the user's KYC verification is completed.|

## ChangeMarginModeResponse

<a id="schemachangemarginmoderesponse"></a>

```json
{
  "id": "5112346",
  "margin_mode": "isolated"
}
```

*Response returned after changing the user's margin mode*

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string|false|none|Unique identifier of the user(user_id) whose margin mode was updated|
|margin_mode|string|false|none|The updated margin mode. Possible values: isolated, portfolio, or cross|

## CreateHeartbeat

<a id="schemacreateheartbeat"></a>

```json
{
  "heartbeat_id": "string",
  "impact": "low",
  "contract_types": [
    "string"
  ],
  "underlying_assets": [
    "string"
  ],
  "product_symbols": [
    "string"
  ],
  "config": [
    {
      "action": "cancel_orders",
      "unhealthy_count": 0,
      "tag": "string"
    }
  ]
}
```

*Create Heartbeat Request Object*

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|heartbeat_id|string|true|none|Unique identifier for the heartbeat|
|impact|string|true|none|Impact level|
|contract_types|[string]|false|none|Array of contract types to monitor|
|underlying_assets|[string]|false|none|Array of underlying assets to monitor|
|product_symbols|[string]|false|none|Array of specific product symbols to monitor|
|config|[[HeartbeatConfig](#schemaheartbeatconfig)]|true|none|Array of action configurations|

#### Enumerated Values

|Property|Value|Description|
|---|---|---|
|impact|low|Low-impact heartbeat; missed beats trigger minimal protective action|
|impact|medium|Medium-impact heartbeat; missed beats trigger standard protective action|
|impact|high|High-impact heartbeat; missed beats trigger the strongest protective action|

## HeartbeatConfig

<a id="schemaheartbeatconfig"></a>

```json
{
  "action": "cancel_orders",
  "unhealthy_count": 0,
  "tag": "string"
}
```

*Heartbeat Configuration Object*

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|action|string|true|none|Action to take when heartbeat expires|
|unhealthy_count|integer|true|none|Number of unhealthy heartbeats before action|
|tag|string|false|none|Tag for the action (e.g., 'mmp')|

#### Enumerated Values

|Property|Value|Description|
|---|---|---|
|action|cancel_orders|Cancel the user's open orders when the heartbeat goes unhealthy|
|action|spreads|Widen quote spreads when the heartbeat goes unhealthy|

## HeartbeatResponse

<a id="schemaheartbeatresponse"></a>

```json
{
  "heartbeat_id": "string",
  "status": "string"
}
```

*Heartbeat Response Object*

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|heartbeat_id|string|false|none|none|
|status|string|false|none|none|

## HeartbeatAck

<a id="schemaheartbeatack"></a>

```json
{
  "heartbeat_id": "string",
  "ttl": 0
}
```

*Heartbeat Acknowledgment Request Object*

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|heartbeat_id|string|true|none|Heartbeat identifier|
|ttl|integer|true|none|Time to live in milliseconds|

## HeartbeatAckResponse

<a id="schemaheartbeatackresponse"></a>

```json
{
  "process_enabled": "string",
  "heartbeat_timestamp": "string"
}
```

*Heartbeat Acknowledgment Response Object*

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|process_enabled|string|false|none|Acknowledgement status (true/false)|
|heartbeat_timestamp|string|false|none|Expiry timestamp after which actions will be triggered|

## ArrayOfHeartbeats

<a id="schemaarrayofheartbeats"></a>

```json
[
  {
    "heartbeat_id": "string",
    "impact": "string",
    "contract_types": [
      "string"
    ],
    "underlying_assets": [
      "string"
    ],
    "product_symbols": [
      "string"
    ],
    "config": [
      {
        "action": "cancel_orders",
        "unhealthy_count": 0,
        "tag": "string"
      }
    ],
    "status": "string",
    "last_ack": "string",
    "next_ack_required_by": "string"
  }
]
```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[Heartbeat](#schemaheartbeat)]|false|none|[Heartbeat Object]|

## Heartbeat

<a id="schemaheartbeat"></a>

```json
{
  "heartbeat_id": "string",
  "impact": "string",
  "contract_types": [
    "string"
  ],
  "underlying_assets": [
    "string"
  ],
  "product_symbols": [
    "string"
  ],
  "config": [
    {
      "action": "cancel_orders",
      "unhealthy_count": 0,
      "tag": "string"
    }
  ],
  "status": "string",
  "last_ack": "string",
  "next_ack_required_by": "string"
}
```

*Heartbeat Object*

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|heartbeat_id|string|false|none|none|
|impact|string|false|none|none|
|contract_types|[string]|false|none|none|
|underlying_assets|[string]|false|none|none|
|product_symbols|[string]|false|none|none|
|config|[[HeartbeatConfig](#schemaheartbeatconfig)]|false|none|[Heartbeat Configuration Object]|
|status|string|false|none|none|
|last_ack|string|false|none|none|
|next_ack_required_by|string|false|none|none|

## ArrayOfSubaccouns

<a id="schemaarrayofsubaccouns"></a>

```json
[
  {
    "id": "98765432",
    "email": "[email protected]",
    "account_name": "Main",
    "first_name": "Rajesh",
    "last_name": "Sharma",
    "dob": "1985-08-25",
    "country": "India",
    "phone_number": "9876543210",
    "margin_mode": "isolated",
    "pf_index_symbol": ".DEXBTUSD",
    "is_sub_account": false,
    "is_kyc_done": true
  }
]
```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[User](#schemauser)]|false|none|[Represents a user account with personal and account-related details.]|

## RateLimitQuotaResponse

<a id="schemaratelimitquotaresponse"></a>

```json
{
  "current_quota": 42,
  "remaining_time_in_milliseconds": 120632
}
```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|current_quota|integer|false|none|none|
|remaining_time_in_milliseconds|integer|false|none|none|
