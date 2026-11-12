# General Information

> Source: https://docs.delta.exchange/#general-information

## Definitions
  **Assets:** are cryptocurrencies or fiat currencies. Each asset has a 3/4 letter code (e.g. BTC, USDC). A derivative contract on Delta Exchange will entail multiple assets, namely:

   - **Underlying Asset:** This is the asset over which a futures or perpetual contract is defined. For e.g. the underlying asset of the BTCUSD perpetual contract is BTC. 

   - **Quoting Asset:** The asset in which price of the quoting is called the quoting asset. For e.g. the BTCUSD contract is quoted in USD. Therefore, the quoting asset of the contract is USD.
   
   - **Settling Asset:** The asset in which the margin and Profit/ Loss of a contract is denominated. For e.g. the BTCUSD contract is margined and settled in USD. Therefore, the settling asset of the contract is USD.

**Products**: are the derivative contracts listed on Delta Exchange. Each contract can be referred by either its Product ID (e.g. 27 is the Product ID of BTCUSD contract) or Symbol (BTCUSD is the symbol for BTCUSD contract). It is worth noting that Orders, Orderbook APIs expect Product IDs. 
e.g.

product_id| symbol |product_type| description
--|--|--|--
27  |BTCUSD|perpetual_futures|Bitcoin Perpetual futures margined and settled in INR
3136|ETHUSD|perpetual_futures|Ethereum perpetual futures margined and settled in INR
2000|P-BTC-38100-230124|put_options|BTC put option strike price $38100 and expiring on 23/01/2024
5000|C-BTC-55800-170224|call_options|BTC call option strike price $55800 and expiring on 17/02/2024

## Symbology

**Contract symbol:** has the following format

    Underlying Asset| Quoting Asset|_|Matruity Date (optional, applicable only for futures contracts)
    
    e.g. BTCUSD, ETHUSD

    For Options symbol:  
    Option Type |-| Underlying Asset |-| Price Strikes |-| Expiry Date in ddMMYY   
    e.g. C-BTC-90000-310125: C (Call Option) BTC (Bitcoin) 90000 strike price expiring on 31st Jan 2025
    

  
**Mark Price:** Each contract has a unique [Mark Price](https://www.delta.exchange/user-guide/)  which can be referred to by: **MARK: Contract_Symbol (MARK:BTCUSD)** 

**Index Price:** The prices of the underlying assets for the contracts listed on Delta Exchange are obtained from various spot exchanges, and are computed by averaging prices from multiple exchanges. Details of all the indices are available on this [page](https://www.delta.exchange/indices/).
  

For a given Underlying Asset/ Quoting Asset pair, the Index price symbol is: ***.DE|Underlying Asset|Quoting Asset|*** 
e.g. **.DEBNBXBT**
It is important to note that the BTCUSD Index price doesn't follow this convention as its symbol is **.DEXBTUSD**.

  
## Pagination
Pagination allows to fetch data page-wise. We use cursor based pagination where each response metadata contains a before and after cursor. The cursor needs to passed on with the next request to paginate over the result. Please note that the cursors are updated with each new page.

Pagination can be called in following APIs

API|End point|
--|--
Products|/v2/products
Orders|/v2/orders
Orders History|/v2/orders/history
Fills|/v2/fills
Wallet transactions|/v2/wallet/transactions

**Pagination parameters**

  - after 
    - after cursor to fetch the next page
  - before 
    - before cursor to fetch the previous page
  - page_size
    - page size for pagination

In API response, meta data will contain the cursors as show below

```json
{
  "success": true,
  "result": [],
  "meta": {
    "after": "an_arbitary_string",
    "before": "another_arbitary_string"
  }
}
```
  
**Example**

https://api.india.delta.exchange/v2/products?page_size=30

https://api.india.delta.exchange/v2/products?page_size=30&after=after_cursor_from_last_request

## Data Centers 
Delta Exchange data centers are in **AWS Tokyo**
