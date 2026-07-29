# Portfolio

Positions (daywise and netwise), demat holdings, position conversion and eDIS holding authorisation.

## Contents

- [Fetch positions Daywise](#fetch-positions-daywise)
- [Headers](#headers)
- [Fetch positions Netwise](#fetch-positions-netwise)
- [Headers](#headers)
- [Fetch Demat Holdings](#fetch-demat-holdings)
- [Headers](#headers)
- [Convert Positions API](#convert-positions-api)
- [Authorize Holdings](#authorize-holdings)
- [Getting Response](#getting-response)
- [After Response](#after-response)

---

## Fetch positions Daywise

> Source: https://developer.hdfcsky.com/sky-docs/docs/portfolio

This API is used to fetch Day wise positions. The query params are client_id and type is live. In response, it shows Day wise position data like Average Buy Price, Average Sell Price, Buy amount & quantity etc. In case of error, It shows 'Type is invalid'.

### HTTP Request

```js
     Method: GET
     Endpoint: /oapi/v1/positions
```

## Headers

```js
{
    "Authorization": "<access_token>",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
}
```

### Query Params

```js
{
    "client_id": "DEMO1",
    "api_key": "The API key used for authentication",
    "type": "live"
}
```

### Request Curl

```js
curl --location 'https://developer.hdfcsky.com/oapi/v1/positions?api_key=api_key&client_id=DEMO1&type=live' \
--header 'Authorization: <access_token>' \
--header 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36' \
--data ''
```

### Response

```js
{
  "data": [
  {
     "average_buy_price": 14.7,
     "average_price": 0,
     "average_sell_price": 0,
     "buy_amount": 14.7,
     "buy_quantity": 1,
     "cf_buy_amount": 0,
     "cf_buy_quantity": 0,
     "cf_sell_amount": 0,
     "cf_sell_quantity": 0,
     "client_id": "DEMO1",
     "close_price": 0,
     "exchange": "NSE",
     "instrument_token": 11915,
     "ltp": 14.6,
     "multiplier": 1,
     "net_amount": -14.7,
     "net_quantity": 1,
     "previous_close": 14.65,
     "pro_cli": "CLIENT",
     "prod_type": 2,
     "product": "MIS",
     "realized_mtm": 0,
     "segment": "Capital",
     "sell_amount": 0,
     "sell_quantity": 0,
     "symbol": "YESBANK",
     "token": 11915,
     "trading_symbol": "YESBANK-EQ",
     "v_login_id": "DEMO1"
  }],
  "message": "",
  "status": "success"
}
```

### Error Response

```js
{
  "status": "error",
  "message": "Request forbidden",
  "error_code": 40000,
  "data":{}
}
```

---

## Fetch positions Netwise

> Source: https://developer.hdfcsky.com/sky-docs/docs/portfolio/fetchpositionsnetwise

This API is used to fetch Net wise positions. The query params are client_id and type is historical. In response, it shows Net wise position data like Average Buy Price, Average Sell Price, Buy amount & quantity etc. In case of error, It shows 'Type is invalid'.

### HTTP Request

```js
     Method: GET
     Endpoint: /oapi/v1/positions
```

## Headers

```js
{
    "Authorization": "<access_token>",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
}
```

### Query Params

```js
{
    "client_id": "DEMO1",
    "api_key": "The API key used for authentication",
    "type": "historical"
}
```

### Request Curl

```js
curl --location 'https://developer.hdfcsky.com/oapi/v1/positions?api_key=api_key&client_id=DEMO1&type=historical' \
--header 'Authorization: <access_token>' \
--header 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36' \
--data ''
```

### Response

```js
{
   "data": [
   {
   "average_buy_price": 40520,
   "average_price": 0,
   "average_sell_price": 40538,
   "buy_amount": 40520,
   "buy_quantity": 1,
   "cf_buy_amount": 0,
   "cf_buy_quantity": 0,
   "cf_sell_amount": 0,
   "cf_sell_quantity": 0,
   "client_id": "DEMO1",
   "close_price": 0,
   "exchange": "MCX",
   "instrument_token": 222895,
   "ltp": 40520,
   "multiplier": 1,
   "net_amount": 18,
   "net_quantity": 0,
   "previous_close": 40697,
   "pro_cli": "CLIENT",
   "prod_type": 0,
   "product": "NRML",
   "realized_mtm": 0,
   "segment": "FutOpt",
   "sell_amount": 40538,
   "sell_quantity": 1,
   "symbol": "GOLDGUINEA",
   "token": 222895,
   "trading_symbol": "GOLDGUINEA20NOVFUT",
   "v_login_id": "DEMO1"
   }],
   "message": "",
   "status": "success"
}
```

### Error Response

```js
{
  "data":{
  },
  "error_code": 44000,
  "message": "`type` is invalid",
  "status": "error"
}
```

---

## Fetch Demat Holdings

> Source: https://developer.hdfcsky.com/sky-docs/docs/portfolio/fetchdematholdings

This API is used to fetch Demat Holdings. The query params is client_id only. In response, it shows holding data like Branch code, Averge buy, client id etc. In case of error, It shows 'Type is invalid'.

### HTTP Request

```js
     Method: GET
     Endpoint: /oapi/v1/holdings
```

## Headers

```js
{
    "Authorization": "<access_token>",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
}
```

### Query Params

```js
{
     "client_id": "DEMO1",
     "api_key": "The API key used for authentication",
}
```

### Request Curl

```js
curl --location 'https://developer.hdfcsky.com/oapi/v1/holdings?api_key=api_key&client_id=DEMO1' \
--header 'Authorization: <access_token>' \
--header 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36' \
--data ''
```

### Response

```js
{
     "data":{
      "holdings": [
        {
        "branch_code": "",
        "buy_avg": 240.2,
        "buy_avg_mtm": 277.7500000000006,
        "client_id": "DEMO1",
        "exchange": "NSE",
        "free_quantity": 55,
        "instrument_details":{
        "exchange": 1,
        "instrument_name": "EQ",
        "instrument_token": 3045,
        "trading_symbol": "SBIN-EQ"
        },
        "isin": "INE062A01020",
        "ltp": 245.25,
        "pending_quantity": 0,
        "pledge_quantity": 0,
        "previous_close": 240.2,
        "quantity": 55,
        "symbol": "SBIN",
        "t0_price": 0,
        "t0_quantity": 0,
        "t1_price": 0,
        "t1_quantity": 0,
        "t2_price": 0,
        "t2_quantity": 0,
        "today_pledge_quantity": 0,
        "token": 3045,
        "trading_symbol": "SBIN",
        "transaction_type": "",
        "used_quantity": 0
        }]
     },
     "message": "",
     "status": "success"
}
```

### Error Response

```js
      {
         "data":{
         }
         "error_code": 44000,
         "message": "`type` is invalid",
         "status": "error"
      }
```

---

## Convert Positions API

> Source: https://developer.hdfcsky.com/sky-docs/docs/portfolio/convertpositions

This API is used to convert existing positions to other by product category wise. If you have positions in CNC then you can convert it into MIS and as well as for CNC to MIS. also you can change the quantity how much you want to convert.

### HTTP Request

```js
     Method: PUT
     Endpoint: /oapi/v1/position/convert
```

### Headers

```js
{
    "Authorization": "<access_token>",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    "Content-Type": "application/json"
}
```

### Query Params

```js
{
    "api_key": "The API key used for authentication",
}

```

### Body Params

| FieldName | Datatype | Description |
|---|---|---|
| exchange | String | NSE,BSE,NFO,CDS,MCX |
| instrument_token | String | Represents the unique id of instrument. |
| client_id | String | Represents the unique id of user or username. |
| order_side | String | BUY,SELL |
| price | Number | It can't be Zero. |
| quantity | Number | It can't be Zero. |
| validity | String | DAY or IOC |
| product | String | CNC,MIS,NRML,MTF |
| new_product | String | CNC,MIS,NRML,MTF |
| oms_order_id | Number | Represents the unique id of order given by oms. |

### Request Curl

```js
curl --location --request PUT 'https://developer.hdfcsky.com/oapi/v1/position/convert?api_key=api_key' \
--header 'Authorization: <access_token>' \
--header 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36' \
--header 'Content-Type: application/json' \
--data '    {
        "client_id": "DEMO1",
        "exchange": "NSE",
        "instrument_token": 3045,
        "product": "MIS",
        "new_product": "CNC",
        "quantity": 100,
        "validity": "DAY",
        "order_side": "SELL"
    }  '
```

### Response

```js
    {
        "data": {},
        "message": "Conversion completed",
        "status": "success"
    }
```

### Error Response

```js
    {
        "data": {
        },
        "error_code": 45000,
        "message": "Error from backend: (1013)-template is not assigned for this client",
        "status": "error"
    }
```

---

## Authorize Holdings

> Source: https://developer.hdfcsky.com/sky-docs/docs/portfolio/edis

This API is used to authorize holdings in portfolio. It send client ID and selected holdings data as payload.

### HTTP Request

```js
     Method: POST
     Endpoint: /oapi/v1/edis/instrument_details
```

### Headers

```js
{
    "Authorization": "<access_token>",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    "Content-Type": "application/json"
}
```

### Query Params

```js
{
    "api_key": "The API key used for authentication",
}

```

### Body Params

| FieldName | Datatype | Description |
|---|---|---|
| client_id | String | Represents the unique id of client. |
| exchange | String | NSE,BSE,CDS,NFO,MCX |
| instrument_token | String | Represents unique id of particular instrument. |
| authorized | Number | Represents number of holdings authorized. |
| total | Number | Represents total number of holdings available. |

### Request Curl

```js
    curl --location 'https://developer.hdfcsky.com/oapi/v1/edis/instrument_details?api_key=api_key' \
--header 'Authorization: <access_token>' \
--header 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36' \
--header 'Content-Type: application/json' \
--data '    {
     "client_id": "DEMO1",
     "instruments": [
      {
        "instrument_token": 14366,
        "exchange": "NSE",
        "total": 1,
        "authorized": 1
       }
     ]
    }'
```

## Getting Response

In response the API will send encrypted details of holdings which the user wants to authorize.

### Response

```js
{
     "data": {
     "depository": "CDSL",
     "dp_id": "67300",
     "encrypted_dtls": "YAeqXSJ7lAWOO5i3ROO7WdvsepKlXay2mXccJQbZuXc8nF8jyYGOq3sg1OPT5MrotogMFAkM3UQJUmkA5EDh4VCJlZOYUDJDRO8+X6an8fygtWwcKlyGUMibsXcqtMz75FUgqAhifsIuK783xKCkz4ylV23pfSXi/kiebXasV1hH1w46B7b4lQss3jYVWOaDeHs7K+ZU3pryx2G6olSFJwN5wsBD3u3yrY6HA1R5wl2mjlZoABhjOrEKuyImoA9gZmplAAOxs2E+C3Z+B9ldZlBfOVeGZE5MWZ7gPRYksEM0Vd/fe9pJP/MUO+JbUx6yX4B5AOHYTPGZFV9bQlV6CsPz0z4fqvONQh2kwK/h9Z+cUOIC/H/knmgLQ2s7tSWfr70UNA0Y3vUoCENlCUeHSHHTVb55PoYRenr4cZrPd//UTuqdqQXriv0Sn7cmBh1XYHfnlhjr/AASEeVu6k0w+3QcTqV/JeR9p0A5NNUjKkmpRiI8lRQxBY/iFb2PkjThOfamea26kn6BwL/+Phe0CtwNQGJwRNxui5cET50b3o6tx+QdwI5UglqgK5LIPAUu",
     "request_id": "88a3-18-ab-91",
     "version": "1.1"
    },
    "html": true,
    "message": "Edis html response",
    "status": "success"
}
```

### Error Response

```js
{
    "status": "error",
    "message": "Request Unauthorised",
    "error_code": 40000,
    "data": {}
}
```

## After Response

After getting the response we will have to set the response to a HTML form and when the user confirms to authorize, it will redirect the user to CDSL website where the user have to enter it's T-Pin and then Mobile-OTP. When the user confirms OTP it will redirect the user to the trading platform.

### Sample HTML Form

```html
    <form name="frmDIS" method="post" action="https://edis.cdslindia.com/EDIS/VerifyDIS/">
    <input type="hidden" name="DPId" value="92300">
    <input type="hidden" name="ReqId" value="2e33-cb-3d-74">
    <input type="hidden" name="Version" value="1.2">
    <input type="hidden" name="TransDtls" value="ntF+AdMLSRnxniBSIYAh90d98LYahqhXlKVVoM3mPTgrYFwjEtw4v3JW7qpK+j6SbBWLTBCkfquZJVuhSbmY9Ul0Gatcbi4eR5ekGyrWg811e+aFgpfCv0edanrIE0WZ6Jjlb5Qjmed449XZIA+i+naKsWKhurrvkxs1D63Oanv4NXVbkipfd4fU3abvG2ldc0Q00d0J6eJDGHV1LBtlIw9KkViG592BMURpj7/HyFY+eson/NRinSvy6nOY/2JUbOrBa4O5kkxfIlfFqgrL8w5z3rIQkah4GWai6UAzEvZAXraKKYRVU6EgD44E03rYcZfsSAdMas0mjJtNCKl+dt9CIHPtoQv3ieULasrvwyiO/a7ddqxLxTfqnq907RLhuhfEVBRNsvAU6r/EFZcLtLoN9jG6D5GUUQdfunWRkr9rmQHHBrsPPdiwfbJhWH6uUfzXANRo4/OtPa+DuGiHFOENZoPFX9sZZ6mPAxa+vkdRSjAoiWwltS6jeWhjEzwtk6P4icMev5iZrPC11LmDh4iZh0HFjX+UGPixyg9n8Y/A0L23ouJS3AYka1Fmgy4QKqJmlHTTeUKGbbhP6XudTJKIiRPYjJsvrFz+dibnoHE=">
    <input class="button" type="submit" value="Continue to CDSL">
    </form>
```
