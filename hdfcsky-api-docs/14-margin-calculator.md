# Margin Calculator

> Source: https://developer.hdfcsky.com/sky-docs/docs/margin_calculator

This API is used for Margin Calculator

## HTTP Request

```js
     Method: POST
     Endpoint: /oapi/v1/margin
```

## Headers

```js
{
    "Content-Type": "application/json",
    "Authorization": "<access_token>",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
}
```

## Request Curl

```js
curl --location 'https://uat-developer.hdfcsky.com/oapi/v1/margin' \
--header 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36' \
--header 'Content-Type: application/json' \
--data '{
    "data": [
        {
            "segment": "FutOpt",
            "series": "OPTIDX",
            "exchange": "BFO",
            "side": "SELL",
            "mode": "NEW",
            "symbol": "SENSEX24AUG24200CE",
            "underlying": "76000",
            "token": "74643",
            "quantity": "25",
            "price": "332.85",
            "product": "0"
        }
    ]
}'
```

## Response

```js
{
    "error": {
        "code": 0,
        "message": ""
    },
    "result": {
        "combined_margin": {
            "delivery_margin": 0,
            "span": 0,
            "somtier_margin": 0,
            "additional_margin": 0,
            "span_spread_margin": 0,
            "var_margin": 0,
            "exposure_margin": 12162.225,
            "premium_margin": 2788.75,
            "premium_benefit": 0,
            "extreme_loss_margin": 0,
            "max_span": 0,
            "net_span": 0,
            "net_span_array": [
                0,
                0,
                0,
                0
            ],
            "composite_delta": 0,
            "setl_price": 0,
            "future_buy_quantity": 0,
            "future_sell_quantity": 0,
            "option_sell_quantity": 0,
            "option_buy_quantity": 0,
            "underlying_token": 0,
            "som_rate": 0,
            "spread_rate": 0
        },
        "individual_margin_values": [
            {
                "delivery_margin": 0,
                "span": 52982.75,
                "additional_margin": 0,
                "span_spread_margin": 0,
                "var_margin": 0,
                "exposure_margin": 12162.225,
                "premium_margin": 0,
                "premium_benefit": 8321.25,
                "extreme_loss_margin": 0,
                "max_span": 0,
                "net_span": 0,
                "net_span_array": [
                    -69.14,
                    113.75,
                    -511,
                    -360.25
                ],
                "composite_delta": 0.4768,
                "setl_price": 0,
                "future_buy_quantity": 0,
                "future_sell_quantity": 0,
                "option_sell_quantity": 0,
                "option_buy_quantity": 0,
                "underlying_token": 0,
                "som_rate": 0,
                "spread_rate": 0
            },
            {
                "delivery_margin": 0,
                "span": 0,
                "somtier_margin": 0,
                "additional_margin": 0,
                "span_spread_margin": 0,
                "var_margin": 0,
                "exposure_margin": 0,
                "premium_margin": 11110,
                "premium_benefit": 0,
                "extreme_loss_margin": 0,
                "max_span": 0,
                "net_span": 0,
                "net_span_array": [
                    -68.21,
                    114.19,
                    -555.77,
                    -427.34
                ],
                "composite_delta": 0.53,
                "setl_price": 0,
                "future_buy_quantity": 0,
                "future_sell_quantity": 0,
                "option_sell_quantity": 0,
                "option_buy_quantity": 0,
                "underlying_token": 0,
                "som_rate": 0,
                "spread_rate": 0
            }
        ]
    }
}
```

## Error Response

```js
    {
      "status": "error",
      "message": "Request forbidden",
      "error_code": 40000,
      "data":{
      }
    }
```
