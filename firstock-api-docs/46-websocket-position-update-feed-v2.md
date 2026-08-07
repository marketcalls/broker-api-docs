# Position Update Feed V2

> Source: https://firstock.in/api/docs/position-update-feed-v2/

> This document details how to get Position Update Feed on the Firstock Websockets.

## Overview

The Position‑Update Feed delivers real-time updates on the status of your orders via a persistent WebSocket connection.

### Example Usage

**Python**

```python
from firstock import Firstock, FirstockWebSocket
import time

def position_book_data(data):
    print(data)

user_id = 'YOUR_USER_ID'

model = FirstockWebSocket(
    position_data=position_book_data
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
function positionBookData(data) {
    console.log(data);
}

const userId = 'YOUR_USER_ID';
const model = new FirstockWebSocket({
    position_data: positionBookData
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
func positionBookData(data map[string]interface{}) {
  fmt.Println(data)
}

model := Firstock.WebSocketModel{
    PositonData:                 	  positionBookData,
    WebSocketConection:          webSocketConnection1,
  }
err = Firstock.InitializeWebSockets("{{userId}}", model)
fmt.Println("Error:", err)
time.Sleep(25 * time.Second)
err = Firstock.CloseWebSocket(conn1)
fmt.Println(err)
```

### Response Structure

**Body**

On successful connection establishment, position updates will be received.

**Note:** Use `norenordno` to identify **Order Update Feed** and `brkname` to identify **Position Update Feed**.

| Parameter | Description |
|---|---|
| child_orders | List of child order objects |
| upload_prc | Uploaded price for the order |
| totsellamt | Total sell amount |
| daybuyqty | Quantity bought during the day |
| daybuyamt | Amount spent on buying during the day |
| sellavgprc | Average selling price |
| rpnl | Realized Profit and Loss |
| totbuyamt | Total amount spent on buying |
| daybuyavgprc | Day-wise average buy price |
| netqty | Net quantity |
| buyavgprc | Average buying price |
| totbuyavgprc | Total average buying price |
| opensellqty | Open sell quantity |
| openbuyamt | Open buy amount |
| opensellamt | Open sell amount |
| totsellavgprc | Total average sell price |
| uptm | Update timestamp |
| openbuyqty | Open buy quantity |
| brkname | Broker name or code |
| instname | Instrument name (e.g., EQ for Equity) |

**Response**

```json
{
  "child_orders": [
    {
      "ls": "1",
      "upload_prc": "00",
      "totsellamt": "0.00",
      "exch": "NSE",
      "pp": "2",
      "mult": "1",
      "prcftr": "1.000000",
      "daybuyqty": "1",
      "daybuyamt": "2.67",
      "sellavgprc": "0.00",
      "token": "9931",
      "tsym": "VIKASLIFE-EQ",
      "rpnl": "-0.00",
      "totbuyamt": "2.67",
      "ti": "0.01",
      "daybuyavgprc": "2.67",
      "netqty": "1",
      "buyavgprc": "2.67",
      "totbuyavgprc": "2.67"
    }
  ],
  "buyavgprc": "2.67",
  "sellavgprc": "0.00",
  "totbuyavgprc": "2.67",
  "rpnl": "-0.00",
  "opensellqty": "00",
  "uid": "NP2997",
  "prcftr": "1.000000",
  "daybuyavgprc": "2.67",
  "totsellamt": "0.00",
  "openbuyamt": "0.00",
  "netqty": "1",
  "pp": "2",
  "token": "VIKASLIFE",
  "pcode": "C",
  "brkname": "90047",
  "opensellamt": "0.00",
  "daybuyqty": "01",
  "totsellavgprc": "0.00",
  "totbuyamt": "2.67",
  "uptm": "11003337967278",
  "ti": "5.00",
  "daybuyamt": "2.67",
  "openbuyqty": "00",
  "upload_prc": "00",
  "actid": "NP2997",
  "exch": "EQT",
  "mult": "1",
  "ls": "1",
  "tsym": "VIKASLIFE-EQ",
  "instname": "EQ"
}
```
