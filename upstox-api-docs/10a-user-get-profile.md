# Get Profile API

## Overview

The Get Profile API retrieves user profile information including enabled exchanges, product offerings, and permitted order types.

## Endpoint

**GET** `https://api.upstox.com/v2/user/profile`

## Request Headers

```
Content-Type: application/json
Accept: application/json
Authorization: Bearer {your_access_token}
```

## Response (200)

```json
{
  "status": "success",
  "data": {
    "email": "******",
    "exchanges": ["NSE", "NFO", "BSE", "CDS", "BFO", "BCD"],
    "products": ["D", "CO", "I"],
    "broker": "UPSTOX",
    "user_id": "******",
    "user_name": "******",
    "order_types": ["MARKET", "LIMIT", "SL", "SL-M"],
    "user_type": "individual",
    "poa": false,
    "ddpi": false,
    "is_active": true
  }
}
```

## Response Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| email | string | User's email address |
| exchanges | string[] | Active exchanges (NSE, NFO, BSE, CDS, BFO, BCD) |
| products | string[] | Available products (I, D, CO, MTF) |
| broker | string | Broker identifier |
| user_id | string | Unique user identifier (UCC) |
| user_name | string | User's registered name |
| order_types | string[] | Supported order types (MARKET, LIMIT, SL, SL-M) |
| user_type | string | User role ("individual" for retail users) |
| poa | boolean | Power of attorney authorization status |
| ddpi | boolean | DDPI authorization status |
| is_active | boolean | Account active status |

## Error Codes

| Code | Description |
|------|-------------|
| UDAPI100058 | No segments for these users are active. Manual reactivation is recommended from Upstox app/web. |

## Python Example

```python
import requests

url = 'https://api.upstox.com/v2/user/profile'
headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Authorization': 'Bearer {your_access_token}'
}
response = requests.get(url, headers=headers)
print(response.json())
```

## Node.js Example

```javascript
const axios = require('axios');
const url = 'https://api.upstox.com/v2/user/profile';
const headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': 'Bearer {your_access_token}'
};
axios.get(url, { headers })
  .then(response => console.log(response.data))
  .catch(error => console.error(error));
```
