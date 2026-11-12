<!-- Source: https://vortex.rupeezy.in/docs/2.2/holdings/ -->

# Holdings

Use the below apis to see and manage positions:

| method | endpoint | use case | Rate Limit |
| --- | --- | --- | --- |
| `GET` | [{{base_url}}/trading/portfolio/holdings](#fetch-holdings) | Fetch holdings | 10/sec |

## Fetch Holdings

```
Endpoint: {{base_url}}/trading/portfolio/holdings
```

### Holdings Response

```
{
"status": "success",
"data": [
    {
        "isin": "IN0020210244",
        "nse": {
            "ticker": "NSE:654GS2032",
            "token": 7843,
            "exchange": "NSE_EQ",
            "symbol": "654GS2032",
        },
        "bse": {
            "ticker": "BSE:654GS2032",
            "token": 800440,
            "exchange": "BSE_EQ",
            "symbol": "654GS2032",
        },
        "total_free": 1,
        "dp_free": 1,
        "pool_free": 0,
        "t1_quantity": 0,
        "average_price": 95.00,
        "collateral_quantity": 0,
        "collateral_value": 0.00
    },
    {
        "isin": "INE721Z01010",
        "nse": {
            "ticker": "NSE:AARON",
            "token": 1030,
            "exchange": "NSE_EQ",
            "symbol": "AARON",
        },
        "bse": {},
        "total_free": 1,
        "dp_free": 1,
        "pool_free": 0,
        "t1_quantity": 0,
        "average_price": 137.70,
        "collateral_quantity": 0,
        "collateral_value": 0.00
    }]
}
```

| field | description |
| --- | --- |
| `isin` | ISIN of the stock as registered with SEBI |
| `nse` | Scrip details as registered with NSE |
| `bse` | Scrip details as registered with BSE |
| `total_free` | Total free quantity that can be sold |
| `dp_free` | Free quantity that can be sold present in trader's demat account |
| `pool_free` | Free quantity that can be sold present in broker's pool account |
| `t1_quantity` | Quantity which is bought by the trader in previous trading days but not yet settled in demat account |
| `collateral_quantity` | Quantity that is blocked as collateral for margin |
| `collateral_value` | Trading limit increased by keeping collateral |

> [!NOTE]
>
> - Collateral value is not a multiplication of `collateral_quantity` and price. Brokers are required to first take a haircut out of the stock's value and then increase margin.
> - There may be some holdings present in a trader's account which are not listed in either one of the exchanges. Equities listed only in BSE cannot be sold as Rupeezy is not affiliated with BSE.
> - Even if Rupeezy is not registered with BSE, holdings can contain BSE only stocks. Ususally these are stocks which have come in our depoitory by means of transfer from another broker's depository.
> - If stock is present in both broker's pool account and trader's demat account, stocks will first be sold from pool account and then from demat account
