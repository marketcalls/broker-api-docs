> Source: https://docs.arrow.trade/rest-api/user-info/

# User API

The User API provides secure access to user profile data, account settings, and trading permissions. Essential for third-party applications, portfolio management platforms, and custom trading interfaces that require user-specific configuration and personalization.

## Endpoint Reference

### Get User Details

Retrieve complete user account information and trading permissions.

Endpoint Details

**Method:** `GET`
**URL:** `/user/details`
**Headers:** Required (`appID` \+ `token`)

#### Request Example

**Curl**

```js
curl --location 'https://edge.arrow.trade/user/details' \
--header 'appID: <YOUR_APP_ID>' \
--header 'token: <YOUR_TOKEN>'
```

## Response Schema

### Success Response

```json
{
    "data": {
        "bankDetails": [
            {
                "id": "43KJDFDF432DSKFJKD3001NVN",
                "vpa": "abhishek@axl",
                "bankName": "HDFC Bank",
                "accountType": "SAVINGS",
                "accountNumber": "*1234",
                "isDefault": true
            }
        ],
        "depository": [
            {
                "dp": "CDSL",
                "id": "***************"
            }
        ],
        "email": "abhishek.jain@email.com",
        "exchanges": [
            "NSE",
            "NFO",
            "NCD",
            "BSE",
            "BFO",
            "BCD",
            "MCX",
            "NSESLBM"
        ],
        "id": "AJ0000",
        "image": "***********************************************",
        "name": "ABHISHEK JAIN",
        "ordersTypes": 15,
        "pan": "*123R",
        "phone": "***********",
        "products": [
            "NRML",
            "MIS",
            "CNC",
            "CO",
            "BO"
        ],
        "totpEnabled": true,
        "userType": "individual"
    },
    "status": "success"
}
```

## Integration Guidelines

Best Practices

  * **Cache User Data** : Cache user details to reduce API calls (refresh periodically)
  * **Permission Validation** : Always verify user permissions before enabling features
  * **Privacy Compliance** : Handle masked data appropriately in UI displays
  * **Error Recovery** : Implement graceful fallbacks for user data unavailability
  * **Security** : Never expose sensitive user data in logs or client-side code
