# Request and Response Structure

## Request Structure

- Pass the generated access token (`userSession`) as a Bearer token to authorize every request.
- `GET` and `DELETE` requests take all parameters as query parameters:

  ```
  DELETE https://api.iiflcapital.com/v1/orders/{brokerOrderId}
  ```

- `POST` and `PUT` requests send parameters as a raw JSON body:

  ```
  POST https://api.iiflcapital.com/v1/orders
  ```

  ```json
  [
    {
      "instrumentId": "1594",
      "exchange": "NSEEQ",
      "transactionType": "BUY",
      "quantity": "1",
      "orderComplexity": "REGULAR",
      "product": "INTRADAY",
      "orderType": "MARKET",
      "validity": "DAY"
    }
  ]
  ```

## Response Structure

| Field | Description |
| --- | --- |
| `status` | Success, failure, or error of the overall API call |
| `message` | Additional explanation or error description for `status` |
| `result` | Array of individual results, one per operation, in the same order the requests were sent (e.g. leg A's response precedes leg B's for a multi-leg call) |
| `result[].status` | Status/error of the individual operation |
| `result[].message` | Additional detail or error description for the individual operation |

### Example

```json
{
  "status": "Ok",
  "message": "Success",
  "result": [
    {
      "status": "Success",
      "message": "Success",
      "brokerOrderId": "240919000000041",
      "requestTime": "19-Sep-2024 18:48:46"
    },
    {
      "status": "EC901",
      "message": "Invalid parameter: 'exchange' Accepts only { 'NSEEQ', 'NSEFO', 'BSEEQ', 'BSEFO', 'NSECURR', 'BSECURR', 'MCXCOMM', 'NCDEXCOMM', 'NSECOMM', 'BSECOMM' }"
    }
  ]
}
```

Here the overall call succeeded (`status: "Ok"`), the first leg placed successfully, and the second leg failed validation with error code `EC901` — see [Error Codes](12-error-codes.md) for the full list.
