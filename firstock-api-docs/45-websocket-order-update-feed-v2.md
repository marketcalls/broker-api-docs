# Order Update Feed V2

> Source: https://firstock.in/api/docs/order-update-feed-v/

> This document details how to get order feed on the Firstock Websockets.

## Overview

The Order‑Feed delivers real-time updates on the status of your orders via a persistent WebSocket connection. It pushes notifications for activities like new orders, cancellations, success, and pending orders.

### Example Usage

**Python**

```python
from firstock import Firstock, FirstockWebSocket
import time

def order_book_data(data):
    print(data)

user_id = 'YOUR_USER_ID'

model = FirstockWebSocket(
    order_data=order_book_data
)

conn, err = Firstock.initialize_websockets(user_id, model)
print("Error:", err)

time.sleep(25)

close_err = Firstock.close_websocket(conn)
print("Close Error:", close_err)
```

**Nodejs**

```javascript
const { Firstock, FirstockWebSocket } = require("firstock");

// Define callback method
function orderBookData(data) {
    console.log(data);
}

const userId = 'YOUR_USER_ID';
const model = new FirstockWebSocket({
    order_data: orderBookData
});

async function main() {
    // Create the Firstock instance
    const firstock = new Firstock();

    const [conn, err] = await firstock.initializeWebsockets(userId, model);
    console.log("Error:", err);

    await new Promise(resolve => setTimeout(resolve, 25000));

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
func orderBookData(data map[string]string) {
  fmt.Println(data)
}

model := Firstock.WebSocketModel{
    OrderData:                   	  orderBookData,
    WebSocketConection:          webSocketConnection1,
  }

err = Firstock.InitializeWebSockets({{userId}}, model)
fmt.Println("Error:", err)
time.Sleep(25 * time.Second)
err = Firstock.CloseWebSocket(conn1)
fmt.Println(err)
```

### Response Structure

**Body**

On successful connection establishment, order updates will be received.

**Note:** Use `norenordno` to identify **Order Update Feed** and `brkname` to identify **Position Update Feed**.

| Parameter | Description |
|---|---|
| tsym | Trading Symbol |
| rejreason | Order Rejection Reason |
| prcftr | Price factor (used for fractional price scaling) |
| pcode | Product Code (e.g., C for CNC) |
| trantype | Transaction Type (B - Buy, S - Sell) |
| token | Scrip Token ID |
| prctyp | Price Type (e.g., LMT, MKT) |
| ret | Order Retention Type (e.g., DAY) |
| pp | Price Precision |
| ti | Tick Size |
| remarks | User Remarks |
| ntm | Nano Timestamp |
| kidid | identifier |
| dscqty | Disclosed Quantity |
| norenordno | Noren Order Number |
| mult | Multiplier (for price/quantity calculation) |
| uid | User ID |
| exch | Exchange Name |
| status | order status |
| reporttype | Report Type (NewAck, PendingNew etc.) |
| tm | Epoch Time (Seconds) |
| handlinst | Handling Instruction (UUID of system) |
| ls | Lot Size |
| actid | Account ID |
| qty | Order Quantity |
| prc | Price |

**Order Status**- give the status of the Order. Here the following are the **Transition Status**
1. ORDER ACK
2. ORDER PENDING
3. OPEN
4. TRIGGER_PENDING
5. AMO OPEN
6. AMO MODIFIED
7. AMO CANCELED
8. PENDING

the following are the **End States**
1. COMPLETE
2. REJECTED
3. CANCELED

**Response**

```json
{
  "tsym": "VIKASLIFE-EQ",
  "rejreason": " ",
  "prcftr": "1.000000",
  "pcode": "C",
  "trantype": "B",
  "token": "9931",
  "prctyp": "MKT",
  "ret": "DAY",
  "pp": "2",
  "ti": "0.01",
  "remarks": "",
  "ntm": "960322165",
  "kidid": "1",
  "dscqty": "0",
  "norenordno": "25042400010260",
  "mult": "1",
  "uid": "NP2997",
  "exch": "NSE",
  "status": "ORDER ACK",
  "reporttype": "NewAck",
  "tm": "1745483337",
  "handlinst": "20f217e1-daf4-4860-bc12-625d4f37d402",
  "ls": "1",
  "actid": "NP2997",
  "qty": "1",
  "prc": "0.00"
}

{
  "ntm": "960509785",
  "ret": "DAY",
  "rejreason": " ",
  "dscqty": "0",
  "pcode": "C",
  "exch": "NSE",
  "mult": "1",
  "prcftr": "1.000000",
  "qty": "1",
  "prctyp": "MKT",
  "handlinst": "20f217e1-daf4-4860-bc12-625d4f37d402",
  "pp": "2",
  "reporttype": "PendingNew",
  "kidid": "1",
  "prc": "0.00",
  "remarks": "",
  "trantype": "B",
  "norenordno": "25042400010260",
  "ls": "1",
  "ti": "0.01",
  "uid": "NP2997",
  "actid": "NP2997",
  "tsym": "VIKASLIFE-EQ",
  "token": "9931",
  "status": "ORDER PENDING",
  "tm": "1745483337"
}
```
