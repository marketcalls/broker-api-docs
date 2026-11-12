# Calculate Order Margin

> Source: https://tradingapi.mstock.com/docs/v1/typeB/calculate-order-margin/
>
> Section: Type B

### Calculate Order Margin APIs

| method | path | description |
| --- | --- | --- |
| POST | https://api.mstock.trade/openapi/typeb/margins/orders | This endpoint allows users to retrieve a list of their trading orders. Users can view all their existing orders. |

---

### Calculate Order Margin

This endpoint allows users to retrieve a list of their trading orders. Users can view all their existing orders.

**Request Headers -**

- **X-Mirae-Version :** Specifies the version of the API being used. In this case, it is set to 1.
- **Authorization :** A token-based authentication header. The format is token api_key:jwtToken.
- **Content-Type :** Indicated the media type of the resource. For this request, it is set to application/json.

**X-PrivateKey :** api_key

**cURL**

```bash
curl --location 'https://api.mstock.trade/openapi/typeb/margins/orders' \
    --header 'X-Mirae-Version: 1' \
    --header 'Authorization: Bearer jwtToken' \
    --header 'X-PrivateKey: api_key' \
    --header 'Content-Type: application/json' \
    --data '{
    "orders": [
        {
            "product_type": "DELIVERY",
            "transaction_type": "BUY",
            "quantity": "5",
            "price": "2250",
            "exchange": "NSE",
            "symbol_name": "ACC",
            "token": "22",
            "trigger_price": 0
        }
    ]
}'
```

**Node.js**

```javascript
import axios from 'axios';

const response = await axios.post(
'https://api.mstock.trade/openapi/typeb/margins/orders',
// '{\n    "orders": [\n        {\n            "product_type": "DELIVERY",\n            "transaction_type": "BUY",\n            "quantity": "5",\n            "price": "2250",\n            "exchange": "NSE",\n            "symbol_name": "ACC",\n            "token": "22",\n            "trigger_price": 0\n        }\n    ]\n}',
{
    'orders': [
    {
        'product_type': 'DELIVERY',
        'transaction_type': 'BUY',
        'quantity': '5',
        'price': '2250',
        'exchange': 'NSE',
        'symbol_name': 'ACC',
        'token': '22',
        'trigger_price': 0
    }
    ]
},
{
    headers: {
    'X-Mirae-Version': '1',
    'Authorization': 'Bearer jwtToken',
    'X-PrivateKey': 'api_key',
    'Content-Type': 'application/json'
    }
}
);
```

**Python**

```python
import http.client
import json

conn = http.client.HTTPConnection('api.mstock.trade')
headers = {
    'X-Mirae-Version': '1',
    'Authorization': 'Bearer jwtToken',
    'X-PrivateKey': 'api_key',
    'Content-Type': 'application/json',
}
json_data = {
    'orders': [
        {
            'product_type': 'DELIVERY',
            'transaction_type': 'BUY',
            'quantity': '5',
            'price': '2250',
            'exchange': 'NSE',
            'symbol_name': 'ACC',
            'token': '22',
            'trigger_price': 0,
        },
    ],
}
conn.request(
    'POST',
    'openapi/typeb/margins/orders',
    json.dumps(json_data),
    # '{\n    "orders": [\n        {\n            "product_type": "DELIVERY",\n            "transaction_type": "BUY",\n            "quantity": "5",\n            "price": "2250",\n            "exchange": "NSE",\n            "symbol_name": "ACC",\n            "token": "22",\n            "trigger_price": 0\n        }\n    ]\n}',
    headers
)
response = conn.getresponse()
```

**Java**

```java
import java.io.IOException;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpRequest.BodyPublishers;
import java.net.http.HttpResponse;

HttpClient client = HttpClient.newBuilder()
    .followRedirects(HttpClient.Redirect.NORMAL)
    .build();

HttpRequest request = HttpRequest.newBuilder()
    .uri(URI.create("https://api.mstock.trade/openapi/typeb/margins/orders"))
    .POST(BodyPublishers.ofString("{\n    \"orders\": [\n        {\n            \"product_type\": \"DELIVERY\",\n            \"transaction_type\": \"BUY\",\n            \"quantity\": \"5\",\n            \"price\": \"2250\",\n            \"exchange\": \"NSE\",\n            \"symbol_name\": \"ACC\",\n            \"token\": \"22\",\n            \"trigger_price\": 0\n        }\n    ]\n}"))
    .setHeader("X-Mirae-Version", "1")
    .setHeader("Authorization", "Bearer jwtToken")
    .setHeader("X-PrivateKey", "api_key")
    .setHeader("Content-Type", "application/json")
    .build();

HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
```

**Request Body -**

```json
{
    "exchange": "NSE",
    "qty": "10",
    "price": "2240",
    "productType": "DELIVERY",
    "token": "22",
    "tradeType": "BUY",
    "triggerPrice": 0
}
```

**Response Structure -**

The response of the request will be based on authentication outcome.

- Success (HTTP Status 200): On successful request execution, server will return the below json formated data.

```json
{
    "status": "true",
    "message": "SUCCESS",
    "errorcode": null,
    "data": {
        "summary": {
            "total_charges": 11250,
            "trade_value": 0,
            "breakup": [
                {
                    "name": "BROKERAGE",
                    "amount": 0,
                    "msg": "",
                    "breakup": []
                },
                {
                    "name": "BROKER_BROKERAGE",
                    "amount": 0,
                    "msg": "",
                    "breakup": []
                },
                {
                    "name": "EXPOMARGIN",
                    "amount": 0,
                    "msg": "",
                    "breakup": []
                },
                {
                    "name": "LEVIES_BROKERAGE",
                    "amount": 0,
                    "msg": "",
                    "breakup": []
                },
                {
                    "name": "OTHER_BROKERAGE",
                    "amount": 0,
                    "msg": "",
                    "breakup": []
                },
                {
                    "name": "SPANMARGIN",
                    "amount": 0,
                    "msg": "",
                    "breakup": []
                },
                {
                    "name": "VARELMMARGIN",
                    "amount": 0,
                    "msg": "",
                    "breakup": []
                }
            ]
        },
        "charges": [
            {
                "total_charges": 11250,
                "trade_value": 0,
                "breakup": [
                    {
                        "name": "BROKERAGE",
                        "amount": 0,
                        "msg": "",
                        "breakup": []
                    },
                    {
                        "name": "BROKER_BROKERAGE",
                        "amount": 0,
                        "msg": "",
                        "breakup": []
                    },
                    {
                        "name": "EXPOMARGIN",
                        "amount": 0,
                        "msg": "",
                        "breakup": []
                    },
                    {
                        "name": "LEVIES_BROKERAGE",
                        "amount": 0,
                        "msg": "",
                        "breakup": []
                    },
                    {
                        "name": "OTHER_BROKERAGE",
                        "amount": 0,
                        "msg": "",
                        "breakup": []
                    },
                    {
                        "name": "SPANMARGIN",
                        "amount": 0,
                        "msg": "",
                        "breakup": []
                    },
                    {
                        "name": "VARELMMARGIN",
                        "amount": 0,
                        "msg": "",
                        "breakup": []
                    }
                ]
            }
        ]
    }
}
```

-

Failure (HTTP Status 200):

If authentication fails, the server will return an error message

```json
{
    "status": "false",
    "message": "Invalid request. Please try again.",
    "errorcode": "IA401",
    "data": null
}
```

- Failure (HTTP Status 400): If the API Key is Invalid or expired.

```json
{
    "status": "false",
    "message": "API is suspended/expired for use. Please check your API subscription and try again.",
    "errorcode": "IA403",
    "data": null
}
```
