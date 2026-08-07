# Subscribe Feed V2

> Source: https://firstock.in/api/docs/subscribe-feed-v2/

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

Response structure represents a consolidated real-time market data snapshot for multiple financial instruments, for each subscribed security

```json
{
    "NSE:2885": {
        "best_buy": [
            {
                "price": 0,
                "quantity": 0,
                "orders": 0
            },
            {
                "price": 139690,
                "quantity": 5,
                "orders": 3
            },
            {
                "price": 139660,
                "quantity": 500,
                "orders": 10
            },
            {
                "price": 139610,
                "quantity": 361,
                "orders": 3
            },
            {
                "price": 0,
                "quantity": 439,
                "orders": 6
            }
        ],
        "best_sell": [
            {
                "price": 0,
                "quantity": 0,
                "orders": 0
            },
            {
                "price": 139170,
                "quantity": 138,
                "orders": 3
            },
            {
                "price": 139420,
                "quantity": 1503,
                "orders": 11
            },
            {
                "price": 138690,
                "quantity": 1902,
                "orders": 6
            },
            {
                "price": 139750,
                "quantity": 880,
                "orders": 6
            }
        ],
        "c_exch_feed_time": "30-Jan-2026 15:32:57",
        "c_exch_seg": "NSE",
        "c_net_change_indicator": "45",
        "c_symbol": "2885",
        "i_average_trade_price": 139124,
        "i_buy_depth_size": 5,
        "i_closing_price": 139100,
        "close_price": 139100,
        "i_feed_time": 1769767377,
        "i_high_price": 139800,
        "i_last_trade_quantity": 1,
        "i_last_trade_time": 1769767199,
        "i_last_traded_price": 139540,
        "i_low_price": 137850,
        "i_lower_circuit_limit": 125190.00000000001,
        "i_net_price_change_from_closing_price": -410,
        "i_open_price": 138260,
        "i_seconds_since_boe": 1769767377052296028,
        "i_sell_depth_size": 5,
        "i_total_buy_quantity": 0,
        "i_total_open_interest": 197996000,
        "i_total_sell_quantity": 0,
        "i_total_tradevalue": 1561491186388,
        "i_upper_circuit_limit": 153010.0,
        "i_usecs": 52296028,
        "i_volume_traded_today": 11238602,
        "i_yearly_high_price": 161180.0,
        "i_yearly_low_price": 111484.99999999999
    },
    "NSE:26000": {
        "best_buy": [
            {},
            {},
            {},
            {},
            {}
        ],
        "best_sell": [
            {},
            {},
            {},
            {},
            {}
        ],
        "c_exch_feed_time": "30-Jan-2026 15:36:00",
        "c_exch_seg": "NSE",
        "c_net_change_indicator": "45",
        "c_symbol": "26000",
        "i_average_trade_price": 0,
        "i_buy_depth_size": 5,
        "i_closing_price": 2541890,
        "close_price": 2541890,
        "i_feed_time": 1769767560,
        "i_high_price": 2537070,
        "i_last_trade_quantity": 0,
        "i_last_trade_time": 0,
        "i_last_traded_price": 2532065,
        "i_low_price": 2521420,
        "i_lower_circuit_limit": 0,
        "i_net_price_change_from_closing_price": 0,
        "i_open_price": 2524755,
        "i_seconds_since_boe": 1769767560622226145,
        "i_sell_depth_size": 5,
        "i_total_open_interest": 77318355,
        "i_upper_circuit_limit": 0,
        "i_usecs": 622226145,
        "i_yearly_high_price": 2637320,
        "i_yearly_low_price": 2174365
    },
    "BSE:1": {
        "best_buy": [
            {},
            {},
            {},
            {},
            {}
        ],
        "best_sell": [
            {},
            {},
            {},
            {},
            {}
        ],
        "c_exch_feed_time": "30-Jan-2026 15:30:52",
        "c_exch_seg": "BSE",
        "c_net_change_indicator": "43",
        "c_symbol": "1",
        "i_average_trade_price": 0,
        "i_buy_depth_size": 5,
        "i_closing_price": 8256637,
        "close_price": 8256637,
        "i_feed_time": 1769767252,
        "i_high_price": 8243082,
        "i_last_trade_quantity": 0,
        "i_last_trade_time": 0,
        "i_last_traded_price": 8226978,
        "i_low_price": 8194103,
        "i_lower_circuit_limit": 0,
        "i_net_price_change_from_closing_price": 0,
        "i_open_price": 8194731,
        "i_seconds_since_boe": 1769767252781588932,
        "i_sell_depth_size": 5,
        "i_total_open_interest": 0,
        "i_upper_circuit_limit": 0,
        "i_usecs": 781588932,
        "i_yearly_high_price": 8615902,
        "i_yearly_low_price": 7142500
    }
}
```

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
