# Subscribe Feed(Deprecated)

> Source: https://firstock.in/api/docs/subscribe-feed-3/

> *This version will be deprecated soon.*

> This document details how to subscribe to the market feed on the Firstock Websockets.

## Overview

The Subscribe Feed API enables you to initiate a persistent WebSocket connection to Firstock’s real-time market data stream. Through this connection, you can subscribe to price feeds (LTP, and more) for multiple instruments simultaneously, receiving bundled updates in a single message

**Body**

| Field | Type | Mandatory | Description | Example |
|---|---|---|---|---|
| action | string | Yes | Type of request | "subscribe" |
| tokens | string | Yes | Subscription parameter | "BSE:500470\|NSE:26000\|NSE:2885" |

### Request

**Multiple Token**

```json
{"action":"subscribe","tokens":"BSE:500470|NSE:26000"}
```

`action` = Type of request; `subscribe` indicates a live subscription to market data

`tokens` = Parameters for subscription. In Multiple Token, we can send multiple tokens in single request.

**Single Token**

```json
{"action":"subscribe","tokens":"NSE:2885"}
```

`action` = Type of request; `subscribe` indicates a live subscription to market data

`tokens` = Parameters for subscription. In Single Token, we can send only one tokens in single request.

**Note**: Use the following package versions for the old websockets.

**Python**

```python
pip install firstock==1.0.9
```

**Nodejs**

```javascript
npm install firstock@1.1.0
```

**Golang**

```go
go get github.com/the-firstock/firstock-developer-sdk-golang/Firstock@v1.3.0
```

### Example Usage

**Python**

```python
from firstock import Firstock, FirstockWebSocket
import time

def subscribe_feed_data(data):
    print(data)

user_id = 'YOUR_USER_ID'

model = FirstockWebSocket(
    subscribe_feed_data=subscribe_feed_data,
    tokens=["NSE:26000"]
)

conn, err = Firstock.initialize_websockets(user_id, model)
print("Error:", err)

if conn:
    err = Firstock.subscribe(conn, ["BSE:1"])
    print("Subscribe Error:", err)

time.sleep(25)

err = Firstock.unsubscribe(conn, ["NSE:26000", "BSE:1"])
print("Unsubscribe Error:", err)

time.sleep(5)

close_err = Firstock.close_websocket(conn)
print("Close Error:", close_err)
```

**Nodejs**

```javascript
const { Firstock, FirstockWebSocket } = require("firstock");

// Define callback method
function subscribeFeedData(data) {
    console.log(data);
}

const userId = 'YOUR_USER_ID';
const model = new FirstockWebSocket({
    subscribe_feed_data: subscribeFeedData,
    tokens: ["NSE:26000"]
});

async function main() {
    // Create the Firstock instance
    const firstock = new Firstock();

    const [conn, err] = await firstock.initializeWebsockets(userId, model);
    console.log("Error:", err);

    if (conn) {
        const subscribeErr = await firstock.subscribe(conn, ["BSE:1"]);
        console.log("Subscribe Error:", subscribeErr);
    }

    await new Promise(resolve => setTimeout(resolve, 25000));

    // Unsubscribe
    const unsubErr = await firstock.unsubscribe(conn, ["NSE:26000", "BSE:1"]);
    console.log("Unsubscribe Error:", unsubErr);

    await new Promise(resolve => setTimeout(resolve, 5000));

    // Close WebSocket connection
    const closeErr = await firstock.closeWebsocket(conn);
    console.log("Close Error:", closeErr);
}

main();
```

**Golang**

```go
import (
	"github.com/the-firstock/firstock-developer-sdk-golang/Firstock"
)

//Establishing WebSocket Connection
var conn1 *websocket.Conn

func webSocketConnection1(conn *websocket.Conn) {
  if conn != nil {
    conn1 = conn
  }
}

//CallBack method
func subscribeFeedData(data Firstock.SubscribeFeedModel) {
  fmt.Println(data)
}

model := Firstock.WebSocketModel{
    SubscribeFeedData:             subscribeFeedData,
    SubscribeFeedTokens:         []string{"NSE:26000"},
    WebSocketConection:          webSocketConnection1,
  }
err = Firstock.InitializeWebSockets("{{userId}}", model)
fmt.Println("Error:", err)
if conn1 != nil {
  err = Firstock.Subscribe(conn1, []string{"BSE:1"})
}
fmt.Println("Error:", err)
time.Sleep(25 * time.Second)
err = Firstock.Unsubscribe(conn1, []string{"NSE:26000", "BSE:1"})
fmt.Println("Error:", err)
time.Sleep(25 * time.Second)
err = Firstock.CloseWebSocket(conn1)
fmt.Println(err)
```

### Response Structure

1. **Acknowledgement Response**

**Body**

Number of Acknowledgements for a single subscription will be the same as the number of scrips mentioned in the key (k) field.

| Parameter | Description |
|---|---|
| best_buy | Array of top 5 buy orders with price, quantity, and number of orders. |
| best_sell | Array of top 5 sell orders with price, quantity, and number of orders. |
| c_exch_feed_time | Exchange feed time in human-readable format (e.g., 24-Apr-2025 13:45:24). |
| c_exch_seg | Exchange segment, such as NSE or BSE. |
| c_net_change_indicator | Indicator showing the direction or amount of net price change. |
| c_symbol | Scrip token symbol representing the instrument. |
| i_buy_depth_size | Depth size of buy orders (number of levels). |
| i_sell_depth_size | Depth size of sell orders (number of levels). |
| i_feed_time | Feed timestamp in milliseconds since Unix epoch. |
| i_last_trade_time | Time of the last trade in system timestamp format. |
| i_last_traded_price | Last traded price (usually in paise). |
| i_open_interest | Current open interest value for the contract. |
| i_total_open_interest | Total open interest for the underlying instrument. |
| i_total_buy_quantity | Sum of all buy quantities across order book. |
| i_total_sell_quantity | Sum of all sell quantities across order book. |
| i_total_tradevalue | Total traded value of the instrument today (in paise). |
| i_volume_traded_today | Total number of units traded today. |
| i_seconds_since_boe | Microsecond-precision time since beginning of exchange day. |
| i_usecs | Microseconds part of the timestamp for precise timing. |

**Response**:

```json
{
    "best_buy": [
        {
            "price": 728,
            "quantity": 556697,
            "orders": 31
        },
        {
            "price": 727,
            "quantity": 1500222,
            "orders": 124
        },
        {
            "price": 726,
            "quantity": 1446656,
            "orders": 100
        },
        {
            "price": 725,
            "quantity": 1547075,
            "orders": 172
        },
        {
            "price": 724,
            "quantity": 711615,
            "orders": 49
        }
    ],
    "best_sell": [
        {
            "price": 729,
            "quantity": 241310,
            "orders": 31
        },
        {
            "price": 730,
            "quantity": 651336,
            "orders": 50
        },
        {
            "price": 731,
            "quantity": 2035051,
            "orders": 42
        },
        {
            "price": 732,
            "quantity": 418208,
            "orders": 36
        },
        {
            "price": 733,
            "quantity": 869381,
            "orders": 171
        }
    ],
    "c_exch_feed_time": "11-Jul-2025 09:17:58",
    "c_exch_seg": "NSE",
    "c_net_change_indicator": 45,
    "c_symbol": "14366",
    "i_average_trade_price": 730,
    "i_buy_depth_size": 5,
    "i_closing_price": 733,
    "close_price": 733,
    "i_feed_time": 1752205678,
    "i_high_price": 733,
    "i_last_trade_quantity": 135,
    "i_last_trade_time": 1752205676,
    "i_last_traded_price": 729,
    "i_low_price": 727,
    "i_lower_circuit_limit": 659,
    "i_net_price_change_from_closing_price": 2,
    "i_open_price": 733,
    "i_seconds_since_boe": 1752205678660009700,
    "i_sell_depth_size": 5,
    "i_total_buy_quantity": 13658079,
    "i_total_open_interest": 2616021929,
    "i_total_sell_quantity": 26150279,
    "i_total_tradevalue": 6467553260,
    "i_upper_circuit_limit": 806,
    "i_usecs": 660009635,
    "i_volume_traded_today": 9770825,
    "i_yearly_high_price": 1767,
    "i_yearly_low_price": 629
}
```

1. **Updates Response**

**Body**

| Parameter | Description |
|---|---|
| best_buy | Array of top 5 buy orders containing price, quantity, and number of orders at each level. |
| best_sell | Array of top 5 sell orders containing price, quantity, and number of orders at each level. |
| c_exch_feed_time | Exchange feed time in readable format (e.g., 24-Apr-2025 13:45:24). |
| c_exch_seg | Exchange segment identifier (e.g., NSE). |
| c_net_change_indicator | Indicates net price change direction. |
| c_symbol | Internal symbol code used for identifying the security. |
| i_buy_depth_size | Number of levels in the buy order book. |
| i_sell_depth_size | Number of levels in the sell order book. |
| i_feed_time | Feed time in milliseconds since epoch. |
| i_last_trade_time | Timestamp of the last trade (if available). |
| i_last_traded_price | Last traded price (multiplied by 100). |
| i_open_interest | Current open interest on the contract. |
| i_total_open_interest | Total open interest across all contracts for the underlying. |
| i_total_buy_quantity | Sum of all buy quantities across order book levels. |
| i_total_sell_quantity | Sum of all sell quantities across order book levels. |
| i_total_tradevalue | Total value of trades executed today (in paise). |
| i_volume_traded_today | Total number of contracts traded today. |
| i_seconds_since_boe | Nanoseconds since beginning of exchange (BOE) day. |
| i_usecs | Microsecond part of the feed timestamp. |

**Response**:

```json
{
  "best_buy": [
        {},
        {},
        {},
        {},
        {}
    ],
    "best_sell": [
        {
            "price": 729,
            "quantity": 241310,
        },
        {},
        {
            "quantity": 2035051,
            "orders": 42
        },
        {},
        {
            "price": 733,
            "quantity": 869381,
            "orders": 171
        }
    ],
    "c_exch_feed_time": "11-Jul-2025 09:17:58",
    "c_exch_seg": "NSE",
    "c_net_change_indicator": 45,
    "c_symbol": "14366",
    "i_average_trade_price": 730,
    "i_buy_depth_size": 5,
    "i_closing_price": 733,
    "close_price": 733,
    "i_feed_time": 1752205678,
    "i_last_trade_quantity": 135,
    "i_last_trade_time": 1752205676,
    "i_low_price": 727,
    "i_lower_circuit_limit": 659,
    "i_net_price_change_from_closing_price": 2,
    "i_open_price": 733,
    "i_seconds_since_boe": 1752205678660009700,
    "i_sell_depth_size": 5,
    "i_total_buy_quantity": 13658079,
    "i_total_open_interest": 2616021929,
    "i_usecs": 660009635,
    "i_volume_traded_today": 9770825,
    "i_yearly_high_price": 1767,
    "i_yearly_low_price": 629
}
```

**Note**: Only delta values are included in the output. Default values such as`null` and large placeholder integers (e.g.,`9223372036854776000`) are automatically ignored, and their corresponding keys are omitted to ensure a concise and accurate data payload.

### **Unsubscribe Feed**

**Body**

Below is the general JSON body for the Unsubscribe Feed API request. All fields marked as Mandatory must be included.

| Field | Type | Mandatory | Description | Example |
|---|---|---|---|---|
| action | string | Yes | Type of request | "unsubscribe" |
| tokens | string | Yes | UnSubscription parameter | "BSE:500470\|NSE:26000\|NSE:2885" |

### Request

**Multiple Token**

```json
{"action":"unsubscribe","tokens":"BSE:500470|NSE:26000"}
```

`action` = Type of request; `unsubscribe` indicates you want to stop receiving live market data for the specified tokens.

**`tokens`** = Parameters for unsubscription. In Multi Token, we can multiple tokens in single request.

**Single Token**

```json
{"action":"unsubscribe","tokens":"NSE:2885"}
```

`action` = Type of request; `unsubscribe` indicates you want to stop receiving live market data for the specified tokens.

`tokens` = Parameters for unsubscription. In Single Token, we can send only one tokens in single request.

"No Response will be sent for Unsubscribe Action from Websockets for Acknowledgment"
