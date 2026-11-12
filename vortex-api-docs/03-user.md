<!-- Source: https://vortex.rupeezy.in/docs/2.2/user/ -->

# User Details

Use the below apis to see and manage funds:

| method | endpoint | use case | Rate Limit |
| --- | --- | --- | --- |
| `GET` | [{{base_url}}/user/funds](#available-funds) | Fetch Available funds | 1/sec |
| `GET` | [{{base_url}}/user/profile/banks](#banks) | Fetch User's bank accounts | 1/sec |
| `GET` | [{{base_url}}/user/profile/brokerage](#available-funds) | Fetch User's brokerage charges | 1/sec |

## Available Funds

```
Endpoint: {{base_url}}/user/funds
```

This api returns details of funds utilizations and deposits across NSE and MCX. All `NSE` exchanges [`NSE_FO`, `NSE_EQ`, `NSE_CUR`] have common funds. `MCX_FO` has separate funds.

### Sample Response

```
{
    "nse": {
        "deposit": 22836.34,
        "funds_transferred": 0,
        "collateral": 14273.64,
        "credit_for_sale": 0,
        "option_credit_for_sale": 0,
        "limit_utilization": -80,
        "mtm_and_booked_loss": -20,
        "booked_profit": 0,
        "total_trading_power": 37009.98,
        "total_utilization": -100,
        "net_available": 36909.98,
        "funds_withdrawn": -100,
        "withdrawable_balance": 21636.34
    },
    "mcx": {
        "deposit": 9191.75,
        "funds_transferred": 0,
        "collateral": 0,
        "credit_for_sale": 0,
        "option_credit_for_sale": 0,
        "limit_utilization": 0,
        "mtm_and_booked_loss": 0,
        "booked_profit": 0,
        "total_trading_power": 9191.75,
        "total_utilization": 0,
        "net_available": 9191.75,
        "funds_withdrawn": 0,
        "withdrawable_balance": 9191.75
    }
}
```

| field | description |
| --- | --- |
| `deposit` | Cash deposit as of starting of the day |
| `funds_transferred` | Cash deposited during the day |
| `collateral` | Value of stocks kept as collateral |
| `credit_for_sale` | Credit for sale received after selling stocks |
| `option_credit_for_sale` | Credit for sale received after selling options |
| `limit_utilization` | Credit for sale received after selling options |
| `mtm_and_booked_loss` | Booked MTM loss |
| `booked_profit` | Booked Profit |
| `total_trading_power` | Total trading power considering all deposits and credits |
| `total_utilization` | Total utilization considering losses and withdrawals |
| `net_available` | Net funds available for trading |
| `funds_withdrawn` | Value of pending funds withdrawal requests |
| `withdrawable_balance` | Net funds that can be withdrawn |

## Banks

```
Endpoint: {{base_url}}/user/profile/banks
```

This api returns user's bank accounts

### Sample Response

```
{
    "data": {
        "nse": [
            {
                "account_number": "1111111111",
                "ifsc": "SBIN00000001",
                "is_primary": true,
                "account_type": "SAVINGS",
                "bank_name": "STATE BANK OF INDIA"
            }
        ],
        "mcx": [
            {
                "account_number": "1111111111",
                "ifsc": "SBIN00000001",
                "is_primary": true,
                "account_type": "SAVINGS",
                "bank_name": "STATE BANK OF INDIA"
            }
        ]
    },
    "status": "success"
}
```
