# Wallet

> Source: https://docs.delta.exchange/#delta-exchange-api-v2-wallet

Get balances, Get transaction history

## Get Wallet Balances

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json',
  'api-key': '****',
  'signature': '****',
  'timestamp': '****'
}

r = requests.get('https://api.india.delta.exchange/v2/wallet/balances', params={

}, headers = headers)

print r.json()
```

```shell
# You can also use wget
curl -X GET https://api.india.delta.exchange/v2/wallet/balances \
  -H 'Accept: application/json' \
  -H 'api-key: ****' \
  -H 'signature: ****' \
  -H 'timestamp: ****'
```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'api-key' => '****',
  'signature' => '****',
  'timestamp' => '****'
}

result = RestClient.get 'https://api.india.delta.exchange/v2/wallet/balances',
  params: {
  }, headers: headers

p JSON.parse(result)
```

`GET /wallet/balances`

> Example responses
>
> 200 Response

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

### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|List of wallets attached to the user account|[WalletPayload](25-schemas.md#schemawalletpayload)|

> **Note:** To perform this operation, you must be sign the request using your api key and secret. See Authentication section for more details.

## Get Wallet transactions

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json',
  'api-key': '****',
  'signature': '****',
  'timestamp': '****'
}

r = requests.get('https://api.india.delta.exchange/v2/wallet/transactions', params={

}, headers = headers)

print r.json()
```

```shell
# You can also use wget
curl -X GET https://api.india.delta.exchange/v2/wallet/transactions \
  -H 'Accept: application/json' \
  -H 'api-key: ****' \
  -H 'signature: ****' \
  -H 'timestamp: ****'
```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'api-key' => '****',
  'signature' => '****',
  'timestamp' => '****'
}

result = RestClient.get 'https://api.india.delta.exchange/v2/wallet/transactions',
  params: {
  }, headers: headers

p JSON.parse(result)
```

`GET /wallet/transactions`

### Parameters

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|asset_ids|query|integer|false|comma separated list of asset_ids for which to get txns logs|
|start_time|query|integer|false|from time in micro-seconds in epoc|
|end_time|query|integer|false|from time in micro-seconds in epoc|
|after|query|string|false|after cursor for pagination|
|before|query|string|false|before cursor for pagination|
|page_size|query|integer|false|number of records per page|
|transaction_types|query|[TransactionTypes](25-schemas.md#schematransactiontypes)|false|transaction types to retrieve|

> Example responses
>
> 200 Response

```json
{
  "success": true,
  "result": [
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
  ],
  "meta": {
    "after": "g3QAAAACZAAKY3JlYXRlZF9hdHQAAAAN",
    "before": "a2PQRSACZAAKY3JlYXRlZF3fnqHBBBNZL"
  }
}
```

### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|list of [Wallet transactions](25-schemas.md#tocStransaction)|Inline|

### Response Schema

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

> **Note:** To perform this operation, you must be sign the request using your api key and secret. See Authentication section for more details.

## Download Wallet transactions

> Code samples

```python
import requests
headers = {
  'api-key': '****',
  'signature': '****',
  'timestamp': '****'
}

r = requests.get('https://api.india.delta.exchange/v2/wallet/transactions/download', params={

}, headers = headers)

print r.json()
```

```shell
# You can also use wget
curl -X GET https://api.india.delta.exchange/v2/wallet/transactions/download \
  -H 'api-key: ****' \
  -H 'signature: ****' \
  -H 'timestamp: ****'
```

```ruby
require 'rest-client'
require 'json'

headers = {
  'api-key' => '****',
  'signature' => '****',
  'timestamp' => '****'
}

result = RestClient.get 'https://api.india.delta.exchange/v2/wallet/transactions/download',
  params: {
  }, headers: headers

p JSON.parse(result)
```

`GET /wallet/transactions/download`

### Parameters

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|asset_ids|query|integer|false|comma separated list of asset_ids|
|start_time|query|integer|false|from time in micro-seconds in epoc|
|end_time|query|integer|false|from time in micro-seconds in epoc|
|after|query|string|false|after cursor for pagination|
|before|query|string|false|before cursor for pagination|
|page_size|query|integer|false|number of records per page|

### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|csv of transactions for that wallet|None|

> **Note:** To perform this operation, you must be sign the request using your api key and secret. See Authentication section for more details.

## Request asset transfer

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'api-key': '****',
  'signature': '****',
  'timestamp': '****'
}

r = requests.post('https://api.india.delta.exchange/v2/wallets/sub_account_balance_transfer', params={

}, headers = headers)

print r.json()
```

```shell
# You can also use wget
curl -X POST https://api.india.delta.exchange/v2/wallets/sub_account_balance_transfer \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'api-key: ****' \
  -H 'signature: ****' \
  -H 'timestamp: ****'
```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'api-key' => '****',
  'signature' => '****',
  'timestamp' => '****'
}

result = RestClient.post 'https://api.india.delta.exchange/v2/wallets/sub_account_balance_transfer',
  params: {
  }, headers: headers

p JSON.parse(result)
```

`POST /wallets/sub_account_balance_transfer`

This api transfers asset from one subaccount to another subaccount or to the main/parent account. Please ensure that the subaccounts involved in the transfer should belong to the same parent account. Requests to transfer assets across subaccounts that belong to different parent accounts will fail. Please make sure that the api key used to make this api request belongs to the main/parent account.

> Body parameter

```json
{
  "transferrer_user_id": "string",
  "transferee_user_id": "string",
  "asset_symbol": "string",
  "amount": null
}
```

### Parameters

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[AssetTransferSubaccountReq](25-schemas.md#schemaassettransfersubaccountreq)|true|none|

> Example responses
>
> 200 Response

```json
{
  "success": true,
  "result": null
}
```

### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Returns success message|Inline|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Returns error code|[ApiErrorResponse](25-schemas.md#schemaapierrorresponse)|

### Response Schema

> **Note:** To perform this operation, you must be sign the request using your api key and secret. See Authentication section for more details.

## Request subaccount balance transfer history.

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'api-key': '****',
  'signature': '****',
  'timestamp': '****'
}

r = requests.get('https://api.india.delta.exchange/v2/wallets/sub_accounts_transfer_history', params={

}, headers = headers)

print r.json()
```

```shell
# You can also use wget
curl -X GET https://api.india.delta.exchange/v2/wallets/sub_accounts_transfer_history \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'api-key: ****' \
  -H 'signature: ****' \
  -H 'timestamp: ****'
```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'api-key' => '****',
  'signature' => '****',
  'timestamp' => '****'
}

result = RestClient.get 'https://api.india.delta.exchange/v2/wallets/sub_accounts_transfer_history',
  params: {
  }, headers: headers

p JSON.parse(result)
```

`GET /wallets/sub_accounts_transfer_history`

This api returns the wallet balance transfers for subaccounts belonging to the parent/main account of an api user. Make sure you are calling this api from the main account. If no subaccount is mentioned in the request, data for all the subacounts will be returned. Use page size to get more entries in a single request.

> Body parameter

```json
{
  "subaccount_user_id": "string",
  "before": "string",
  "after": "string",
  "page_size": 10
}
```

### Parameters

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[SubaccountTransferHistory](25-schemas.md#schemasubaccounttransferhistory)|true|none|

> Example responses
>
> 200 Response

```json
{
  "success": true,
  "result": [
    {
      "transferrer_user_id": "string",
      "transferee_user_id": "string",
      "asset_symbol": "string",
      "amount": null,
      "created_at": "string",
      "transferee_user": {},
      "transferrer_user": {}
    }
  ],
  "meta": {
    "after": "g3QAAAACZAAKY3JlYXRlZF9hdHQAAAAN",
    "before": "a2PQRSACZAAKY3JlYXRlZF3fnqHBBBNZL"
  }
}
```

### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Returns success message|Inline|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Returns error code|[ApiErrorResponse](25-schemas.md#schemaapierrorresponse)|

### Response Schema

> **Note:** To perform this operation, you must be sign the request using your api key and secret. See Authentication section for more details.
