<!-- Source: https://vortex.rupeezy.in/docs/2.2/withdrawal/ -->

# Fund Withdrawals

Use the below apis to see and manage funds:

| method | endpoint | use case | Rate Limit |
| --- | --- | --- | --- |
| `POST` | [{{base_url}}/user/funds/withdrawal](#withdraw-funds) | Withdraw funds | 1/sec |
| `GET` | [{{base_url}}/user/funds/withdrawal](#list-fund-withdrawals) | Fetch Fund Withdrawals | 1/sec |
| `PUT` | [{{base_url}}/user/funds/withdrawal](#cancel-fund-withdrawal) | Cancel Fund Withdrawal | 1/sec |

## List fund withdrawals

```
Endpoint: {{base_url}}/user/funds/withdrawal
```

### List withdraw funds response

```
{
    "status": "success",
    "message": "Success message",
    "data": [
        {
            "transaction_id": "23122125000001500",
            "amount": 100,
            "created_at": "2023-12-21T17:23:49.077+05:30",
            "status": "CANCELLED",
            "exchange": "NSE_EQ"
        },
        {
            "transaction_id": "23122124700001499",
            "amount": 100,
            "created_at": "2023-12-21T17:23:48.373+05:30",
            "status": "PENDING",
            "exchange": "NSE_EQ"
        },
        {
            "transaction_id": "23122118000000936",
            "amount": 100,
            "created_at": "2023-12-21T14:34:11.193+05:30",
            "status": "ACCEPTED",
            "exchange": "MCX_FO"
        }]
}
```

## Withdraw Funds

```
Endpoint: {{base_url}}/user/funds/withdrawal
```

### Withdraw funds object

```
{
    "bank_account_number": "111111111111",
    "ifsc": "SBIN0000001",
    "amount": 100,
    "exchange": "NSE_EQ"
}
```

### Withdraw funds response

```
{
    "status": "success",
    "message": "Success message",
    "transaction_id": "23122124700001499"
}
```

## Cancel Fund withdrawal

```
Endpoint: {{base_url}}/user/funds/withdrawal
```

### Cancel Withdraw funds object

```
{
    "transaction_id": "23122124700001499",
    "amount": 100,
    "exchange": "NSE_EQ"
}
```

### Cancel Withdraw funds response

```
{
    "status": "success"
}
```
