# Source: https://groww.in/trade-api/docs/curl/annexures

# Annexures

## Order Status

| Value | Meaning |
| --- | --- |
| `NEW` | Newly created, pending further processing. |
| `ACKED` | Acknowledged by the system. |
| `TRIGGER_PENDING` | Waiting for a trigger event. |
| `APPROVED` | Approved and ready for execution. |
| `REJECTED` | Rejected by the system. |
| `FAILED` | Execution failed. |
| `EXECUTED` | Successfully executed. |
| `DELIVERY_AWAITED` | Executed and waiting for delivery. |
| `CANCELLED` | Cancelled. |
| `CANCELLATION_REQUESTED` | Cancellation requested. |
| `MODIFICATION_REQUESTED` | Modification requested. |
| `COMPLETED` | Completed. |

## After Market Order Status

| Value | Meaning |
| --- | --- |
| `NA` | Status unavailable. |
| `PENDING` | Pending execution. |
| `DISPATCHED` | Dispatched for execution. |
| `PARKED` | Parked for later execution. |
| `PLACED` | Placed in the market. |
| `FAILED` | Execution failed. |
| `MARKET` | Market order. |

## Exchange

| Value | Meaning |
| --- | --- |
| `BSE` | Bombay Stock Exchange. |
| `NSE` | National Stock Exchange. |

## Segment

| Value | Meaning |
| --- | --- |
| `CASH` | Equity market, including delivery trading. |
| `FNO` | Futures and Options. |

## Order Type

| Value | Meaning |
| --- | --- |
| `LIMIT` | Specify a price; execution is not guaranteed immediately. |
| `MARKET` | Execute at the best available price without a price guarantee. |
| `SL` | Stop-loss order triggered at a specified price. |
| `SL_M` | Stop-loss market order triggered at a specified price. |

## Product

| Value | Meaning |
| --- | --- |
| `CNC` | Delivery-based cash and carry. |
| `MIS` | Intraday margin product; close by day end. |
| `NRML` | Regular margin product allowing overnight positions. |

## Transaction Type

| Value | Meaning |
| --- | --- |
| `BUY` | Buy transaction. |
| `SELL` | Sell transaction. |

## Validity

| Value | Meaning |
| --- | --- |
| `DAY` | Valid until market close that day. |

## Candle Interval

| Value | Meaning |
| --- | --- |
| `1minute` | 1 minute |
| `2minute` | 2 minutes |
| `3minute` | 3 minutes |
| `5minute` | 5 minutes |
| `10minute` | 10 minutes |
| `15minute` | 15 minutes |
| `30minute` | 30 minutes |
| `1hour` | 1 hour |
| `4hour` | 4 hours |
| `1day` | 1 day |
| `1week` | 1 week |
| `1month` | 1 month |

## Instrument Type

| Value | Meaning |
| --- | --- |
| `EQ` | Equity. |
| `IDX` | Index. |
| `FUT` | Futures. |
| `CE` | Call option. |
| `PE` | Put option. |
