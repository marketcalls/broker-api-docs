# Rest Clients

> Source: https://docs.delta.exchange/#rest-clients

Delta API conforms to the Swagger spec for REST endpoints. Any Swagger-compatible client can connect to the Delta API and execute commands.

You can find the swagger spec json for Delta Api [here]
(https://docs.delta.exchange/api/swagger_v2.json)

We also have Rest Api Clients available for the following languages

- [Nodejs](https://www.npmjs.com/package/delta-rest-client)
- [Python](https://pypi.org/project/delta-rest-client)

## CCXT
CCXT is our authorized SDK provider and you may access our API through CCXT.

When initializing the exchange, set the `urls` config to point to the Delta API base URL.

```python
import ccxt

# Replace with your actual API keys
api_key = 'API_KEY'
api_secret = 'API_SECRET'

# Initialize exchange
exchange = ccxt.delta({
    'apiKey': api_key,
    'secret': api_secret,
    'enableRateLimit': True,
    'urls': {
        'api': {
            'public': 'https://api.india.delta.exchange',
            'private': 'https://api.india.delta.exchange',
        }
    }
})

# Load markets
exchange.load_markets()
```

For more information, please visit [ccxt website](https://ccxt.trade).
