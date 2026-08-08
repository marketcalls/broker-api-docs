# Streaming Data

WebSocket broadcast API at `wss://stream.samco.in` for live market depth and quote ticks.

## Streaming Market Data

`wss://stream.samco.in`

Samco Trade API platform provides the Broadcast API, as the most effective way to receive market data for instruments across all exchanges during live market hours. The API provides continuous streaming data of market data based on user request, and primarily consists of fields such as 5 levels of bid/offer market depth data etc.

The API uses WebSocket protocol to establish a dedicated TCP connection after an HTTP handshake to receive streaming quotes and thereby provides seamless streaming of market data. You need to use a WebSocket client to connect to our broadcast API. If you have already subscribed to our Trade API services, you will be able to access broadcast API too.

### Parameters

| **Name** | **Type** | **Required** | **Description** |
| --- | --- | --- | --- |
| `body` | object | false | none |
| `streaming_type` | string | true | Streaming type. Added for future use. Pass this value as “marketdata” always. |
| `symbols` | [string] | true | List of symbols containing listing numbers used to get market data. |
| `request_type` | string | true | Request type. This can be Subscribe/Unsubscribe. Subscribe - Receive continuous quote data. Unsubscribe - Stop receiving continuous quote data. \*It's important to unsubscribe when the streaming is no longer needed. |
| `response_format` | string | true | Response data format. Currently supports JSON only. |

### Sample Request Body

```json
requestBody={
  "streaming_type": "quote2",
  "symbols": "[{'symbol':'-23'},{'symbol':'30125_NSE'},{'symbol':'3880_NSE'}]",
  "request_type": "subscribe",
  "response_format": "JSON"
}
```

> **TIP** — Prefer a typed client? Use the official SDK
>
> The samples below speak the raw WebSocket protocol — copy them when you're integrating from a language without an SDK, or when you want to see exactly what frames go on the wire. For production integrations in Java, Node, or Python, the official SDKs wrap this same protocol with typed `DepthTick` objects, connect/reconnect plumbing, and per-stream subscribe helpers:
>
> - **Java** — [Java SDK README](https://github.com/samco-sdk/Java-SDK/blob/master/README.md) — `StreamingClient` + `StreamingListener.onDepth(DepthTick)`, subscribed via `subscribeMarketDepth(...)`.
> - **Node** — [Node SDK README](https://github.com/samco-sdk/NodeJS-SDK/blob/main/README.md) — `StreamingClient({ onDepth, ... })` + `subscribeMarketDepth([...])`.
> - **Python** — [Python SDK README](https://github.com/samco-sdk/Python-SDK/blob/master/README.md) — `SamcoBridge.set_streaming_data(value, streaming_type=STREAMING_TYPE_MARKET_DEPTH)` and `subscribe_market_data([...])`.
>
> The wire envelope each SDK produces is identical to the raw samples below, so the auth header (`x-session-token`), the `streaming_type: "quote2"` value, and the subscribe / unsubscribe semantics are the same.

### Sample Code

> **INFO** — Runtime requirements
>
> WebSocket clients only — `cURL` / `fetch` / `HttpClient` won't work for streaming. Minimum versions: **Postman** v10+ • **Java** 17 LTS+ • **Node** 22+ (`npm i ws`) • **Python** 3.8+ (`pip install websocket-client`).

> **WARNING** — End every subscribe / unsubscribe frame with `\n`
>
> The streamer parses incoming messages as newline-delimited JSON. Each subscribe (or unsubscribe) payload **must end with a trailing `\n`** — without it, the frame is buffered and the subscription never takes effect. The official SDKs append it for you; in raw examples below it's added explicitly.

**Postman**

```text
1.  Postman → File → New → "WebSocket Request"
2.  URL          : wss://stream.samco.in
3.  Headers tab  :
      Key   = x-session-token
      Value = <SESSION_TOKEN>
4.  Click "Connect" — the response panel should show "CONNECTED".
5.  In the Message editor (Body tab → JSON) paste the subscribe frame
    below and click "Send":

    {
      "request": {
        "streaming_type": "quote2",
        "data": {
          "symbols": [
            { "symbol": "3880_NSE" },
            { "symbol": "30125_NSE" }
          ]
        },
        "request_type": "subscribe",
        "response_format": "json"
      }
    }

    >>> Important: enable Postman's "Add newline at end of message"
        toggle (or press Enter once after the closing brace). The
        streamer needs the trailing \n to accept the subscription.

6.  Market-data frames will stream into the response panel. To stop,
    send the same frame (with the trailing newline) and
    "request_type": "unsubscribe".
```

**Java**

```java
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.WebSocket;
import java.util.concurrent.CompletionStage;

public class StreamingMarketData {
  public static void main(String[] args) throws Exception {
    String subscribe = """
        {"request":{"streaming_type":"quote2",\
"data":{"symbols":[{"symbol":"3880_NSE"},{"symbol":"30125_NSE"}]},\
"request_type":"subscribe","response_format":"json"}}""";

    HttpClient client = HttpClient.newHttpClient();

    WebSocket ws = client.newWebSocketBuilder()
        .header("x-session-token", "<SESSION_TOKEN>")
        .buildAsync(URI.create("wss://stream.samco.in"), new WebSocket.Listener() {
          @Override public void onOpen(WebSocket webSocket) {
            // Streamer parses newline-delimited JSON — the trailing \n is required.
            webSocket.sendText(subscribe + "\n", true);
            WebSocket.Listener.super.onOpen(webSocket);
          }
          @Override public CompletionStage<?> onText(WebSocket webSocket, CharSequence data, boolean last) {
            System.out.println("Market data :: " + data);
            return WebSocket.Listener.super.onText(webSocket, data, last);
          }
          @Override public void onError(WebSocket webSocket, Throwable error) {
            error.printStackTrace();
          }
        })
        .join();

    Thread.currentThread().join();
  }
}
```

**NodeJs**

```js
// Install once: npm i ws
const WebSocket = require('ws');

const ws = new WebSocket('wss://stream.samco.in', {
  headers: { 'x-session-token': '<SESSION_TOKEN>' }
});

ws.on('open', () => {
  const subscribe = {
    request: {
      streaming_type: 'quote2',
      data: { symbols: [{ symbol: '3880_NSE' }, { symbol: '30125_NSE' }] },
      request_type: 'subscribe',
      response_format: 'json'
    }
  };
  // Streamer parses newline-delimited JSON — the trailing \n is required.
  ws.send(JSON.stringify(subscribe) + '\n');
});

ws.on('message', (msg) => console.log('Market data ::', msg.toString()));
ws.on('error', (err) => console.error(err));
ws.on('close', () => console.log('Connection closed'));
```

**Python**

```py
# Install once: pip install websocket-client
import json
import websocket

SESSION_TOKEN = "<SESSION_TOKEN>"

def on_open(ws):
    subscribe = {
        "request": {
            "streaming_type": "quote2",
            "data": {"symbols": [{"symbol": "3880_NSE"}, {"symbol": "30125_NSE"}]},
            "request_type": "subscribe",
            "response_format": "json",
        }
    }
    # Streamer parses newline-delimited JSON — the trailing \n is required.
    ws.send(json.dumps(subscribe) + "\n")

def on_message(ws, msg):
    print("Market data ::", msg)

def on_error(ws, error):
    print(error)

def on_close(ws, code, reason):
    print("Connection closed")

ws = websocket.WebSocketApp(
    "wss://stream.samco.in",
    header={"x-session-token": SESSION_TOKEN},
    on_open=on_open,
    on_message=on_message,
    on_error=on_error,
    on_close=on_close,
)
ws.run_forever()
```

### Sample Response

```json
{
  "response": {
    "data": {
      "askValues": [
        {
          "no": "5",
          "price": "89.20",
          "qty": "4034"
        },
        {
          "no": "21",
          "price": "89.25",
          "qty": "11106"
        },
        {
          "no": "24",
          "price": "89.30",
          "qty": "8507"
        },
        {
          "no": "18",
          "price": "89.35",
          "qty": "12157"
        },
        {
          "no": "24",
          "price": "89.40",
          "qty": "17005"
        }
      ],
      "bidValues": [
        {
          "no": "10",
          "price": "89.15",
          "qty": "4779"
        },
        {
          "no": "82",
          "price": "89.10",
          "qty": "53802"
        },
        {
          "no": "69",
          "price": "89.05",
          "qty": "64430"
        },
        {
          "no": "390",
          "price": "89.00",
          "qty": "176882"
        },
        {
          "no": "17",
          "price": "88.95",
          "qty": "10078"
        }
      ],
      "delta": "0.00",
      "gamma": "0.00",
      "iv": "0.00",
      "ltt": "05/09/2023 12:33:44",
      "lttUTC": "05/09/2023 07:03:44",
      "symbol": "10753_NSE",
      "taq": "5471990",
      "tbq": "1778050",
      "theta": "0.00",
      "vega": "0.00"
    },
    "streaming_type": "quote2"
  }
}
```

### Response Schema

Status Code **200**

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| `askValues` | [object] | Get List of AskValues. |
| `no` | string | Sequence number for Bid/Ask. |
| `price` | string | Price asked for trading. |
| `qty` | string | Quantity asked for trading. |
| `bidValues` | [object] | Get List of BidValues. |
| `no` | string | Sequence number for Bid/Ask. |
| `price` | string | Price asked for trading. |
| `qty` | string | Quantity asked for trading. |
| `delta` | string | The change in an option’s price with respect to the underlying asset’s price movements. |
| `gamma` | string | Gamma is an Option Chain Greek, indicating the rate of change of delta with respect to the underlying asset’s price movements. |
| `iv` | string | Implied Volatility is the expected volatility in a stock or security or asset. |
| `ltt` | string | Last transaction time in milliseconds. |
| `lttUTC` | string | Last transaction time in UTC time zone format. |
| `symbol` | string | Actual symbol name of the scrip. |
| `taq` | string | Total ask quantity. |
| `tbq` | string | Total bid quantity. |
| `theta` | string | Change in an options contract's price with respect to the time left for expiry. |
| `vega` | string | The value of an options contract has a positive correlation with changes in the volatility of the underlying asset. |

---

## Streaming Quote Data

`wss://stream.samco.in`

Samco Trade API platform provides the Broadcast API, as the most effective way to receive quote data for instruments across all exchanges during live market hours. The API provides continuous streaming data of quote based on user request, and primarily consists of fields such as last traded price, open, high, low, close, last traded quantity, last traded volume, last traded time etc.

The API uses WebSocket protocol to establish a dedicated TCP connection after an HTTP handshake to receive streaming quotes and thereby provides seamless streaming of quote data. You need to use a WebSocket client to connect to our broadcast API. If you have already subscribed to our Samco Trade API services, you will be able to access broadcast API too.

### Parameters

| **Name** | **Type** | **Required** | **Description** |
| --- | --- | --- | --- |
| `body` | object | false | none |
| `streaming_type` | string | true | Streaming type. Added for future use. Pass this value as “quote” always. |
| `symbols` | [string] | true | List of symbols containing listing numbers used to get quote. |
| `request_type` | string | true | Request type. This can be Subscribe/Unsubscribe. Subscribe - Receive continuous quote data. UnSubscribe - Stop receiving the continuous quote data. \*It's important to unsubscribe when the streaming is no longer needed. |
| `response_format` | string | true | Response data format. Currently supports json only. |

### Sample Request Body

```json
requestBody={
  "streaming_type": "quote",
  "symbols": "[{'symbol':'-53'},{'symbol':'89017_NFO'}]",
  "request_type": "subscribe",
  "response_format": "JSON"
}
```

> **TIP** — Prefer a typed client? Use the official SDK
>
> The samples below speak the raw WebSocket protocol — copy them when you're integrating from a language without an SDK, or when you want to see exactly what frames go on the wire. For production integrations in Java, Node, or Python, the official SDKs wrap this same protocol with typed `QuoteTick` objects (LTP / OHLC / volume), connect/reconnect plumbing, and per-stream subscribe helpers:
>
> - **Java** — [Java SDK README](https://github.com/samco-sdk/Java-SDK/blob/master/README.md) — `StreamingClient` + `StreamingListener.onQuote(QuoteTick)`, subscribed via `subscribeQuote(...)`.
> - **Node** — [Node SDK README](https://github.com/samco-sdk/NodeJS-SDK/blob/main/README.md) — `StreamingClient({ onQuote, ... })` + `subscribeQuote([...])`.
> - **Python** — [Python SDK README](https://github.com/samco-sdk/Python-SDK/blob/master/README.md) — `SamcoBridge.set_streaming_data(value, streaming_type=STREAMING_TYPE_QUOTE)` and `subscribe_quote([...])`.
>
> The wire envelope each SDK produces is identical to the raw samples below, so the auth header (`x-session-token`), the `streaming_type: "quote"` value, and the subscribe / unsubscribe semantics are the same.

### Sample Code

> **INFO** — Runtime requirements
>
> WebSocket clients only — `cURL` / `fetch` / `HttpClient` won't work for streaming. Minimum versions: **Postman** v10+ • **Java** 17 LTS+ • **Node** 22+ (`npm i ws`) • **Python** 3.8+ (`pip install websocket-client`).

> **WARNING** — End every subscribe / unsubscribe frame with `\n`
>
> The streamer parses incoming messages as newline-delimited JSON. Each subscribe (or unsubscribe) payload **must end with a trailing `\n`** — without it, the frame is buffered and the subscription never takes effect. The official SDKs append it for you; in raw examples below it's added explicitly.

**Postman**

```text
1.  Postman → File → New → "WebSocket Request"
2.  URL          : wss://stream.samco.in
3.  Headers tab  :
      Key   = x-session-token
      Value = <SESSION_TOKEN>
4.  Click "Connect" — the response panel should show "CONNECTED".
5.  In the Message editor (Body tab → JSON) paste the subscribe frame
    below and click "Send":

    {
      "request": {
        "streaming_type": "quote",
        "data": {
          "symbols": [
            { "symbol": "532826_BSE" }
          ]
        },
        "request_type": "subscribe",
        "response_format": "json"
      }
    }

    >>> Important: enable Postman's "Add newline at end of message"
        toggle (or press Enter once after the closing brace). The
        streamer needs the trailing \n to accept the subscription.

6.  Quote frames will stream into the response panel. To stop, send the
    same frame (with the trailing newline) and
    "request_type": "unsubscribe".
```

**Java**

```java
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.WebSocket;
import java.util.concurrent.CompletionStage;

public class StreamingQuoteData {
  public static void main(String[] args) throws Exception {
    String subscribe = """
        {"request":{"streaming_type":"quote",\
"data":{"symbols":[{"symbol":"532826_BSE"}]},\
"request_type":"subscribe","response_format":"json"}}""";

    HttpClient client = HttpClient.newHttpClient();

    WebSocket ws = client.newWebSocketBuilder()
        .header("x-session-token", "<SESSION_TOKEN>")
        .buildAsync(URI.create("wss://stream.samco.in"), new WebSocket.Listener() {
          @Override public void onOpen(WebSocket webSocket) {
            // Streamer parses newline-delimited JSON — the trailing \n is required.
            webSocket.sendText(subscribe + "\n", true);
            WebSocket.Listener.super.onOpen(webSocket);
          }
          @Override public CompletionStage<?> onText(WebSocket webSocket, CharSequence data, boolean last) {
            System.out.println("Quote :: " + data);
            return WebSocket.Listener.super.onText(webSocket, data, last);
          }
          @Override public void onError(WebSocket webSocket, Throwable error) {
            error.printStackTrace();
          }
        })
        .join();

    Thread.currentThread().join();
  }
}
```

**NodeJs**

```js
// Install once: npm i ws
const WebSocket = require('ws');

const ws = new WebSocket('wss://stream.samco.in', {
  headers: { 'x-session-token': '<SESSION_TOKEN>' }
});

ws.on('open', () => {
  const subscribe = {
    request: {
      streaming_type: 'quote',
      data: { symbols: [{ symbol: '532826_BSE' }] },
      request_type: 'subscribe',
      response_format: 'json'
    }
  };
  // Streamer parses newline-delimited JSON — the trailing \n is required.
  ws.send(JSON.stringify(subscribe) + '\n');
});

ws.on('message', (msg) => console.log('Quote ::', msg.toString()));
ws.on('error', (err) => console.error(err));
ws.on('close', () => console.log('Connection closed'));
```

**Python**

```py
# Install once: pip install websocket-client
import json
import websocket

SESSION_TOKEN = "<SESSION_TOKEN>"

def on_open(ws):
    subscribe = {
        "request": {
            "streaming_type": "quote",
            "data": {"symbols": [{"symbol": "532826_BSE"}]},
            "request_type": "subscribe",
            "response_format": "json",
        }
    }
    # Streamer parses newline-delimited JSON — the trailing \n is required.
    ws.send(json.dumps(subscribe) + "\n")

def on_message(ws, msg):
    print("Quote ::", msg)

def on_error(ws, error):
    print(error)

def on_close(ws, code, reason):
    print("Connection closed")

ws = websocket.WebSocketApp(
    "wss://stream.samco.in",
    header={"x-session-token": SESSION_TOKEN},
    on_open=on_open,
    on_message=on_message,
    on_error=on_error,
    on_close=on_close,
)
ws.run_forever()
```

### Sample Response

```json
{
  "aPr": "44561.00",
  "bPr": "44554.00",
  "aSz": "1",
  "bSz": "1",
  "sym": "2885_NSE",
  "avgPr": "44371.85",
  "c": "44119.00",
  "h": "44786.00",
  "l": "43969.00",
  "o": "44105.00",
  "oI": "361290",
  "oIChg": "22350.00",
  "ch": "435.00",
  "chPer": "0.99",
  "lTrdT": "01 Oct 2019, 06:47:03 PM",
  "ltp": "44554.00",
  "ltq": "1",
  "ltt": "01 Oct 2019, 06:47:03 PM",
  "lttUTC": "01 Oct 2019, 01:17:03 PM",
  "tBQ": "973",
  "tSQ": "610",
  "ttv": "782763833.41",
  "vol": "782763833.41",
  "yH": "44786.00",
  "yL": "0.00",
  "streaming_type": "quote"
}
```

### Response Schema

Status Code **200**

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| `aPr` | string | Ask Price that the seller is willing to accept for the scrip. |
| `bPr` | string | Bid Price that the buyer is willing to pay for the scrip. |
| `aSz` | string | Ask size/quantity available for trading. |
| `bSz` | string | Bid size/quantity offered for trading. |
| `sym` | string | Actual symbol name of the scrip. |
| `avgPr` | string | Average trading price of the equity or derivative. |
| `c` | string | Close value of the market snapshot. |
| `h` | string | High value of the market snapshot. |
| `l` | string | Low value of the market snapshot. |
| `o` | string | Opening price of the market snapshot. |
| `oI` | string | Open interest, which is the total number of outstanding derivative contracts that have not been settled. |
| `oIChg` | string | Change in open interest value. |
| `ch` | string | Change value, which is the difference between the current value and the previous day's market close. |
| `chPer` | string | Percentage change between the current value and the previous day's market close. |
| `lTrdT` | string | Time of the last transaction. |
| `ltp` | string | Last traded price at which the most recent transaction occurred. |
| `ltq` | string | Quantity of the last transaction. |
| `ltt` | string | Last transaction time in milliseconds. |
| `lttUTC` | string | Last transaction time in UTC time zone format. |
| `tBQ` | string | Total quantity of BUY transactions. |
| `tSQ` | string | Total quantity of SELL transactions. |
| `ttv` | string | Total trading volume done. |
| `vol` | string | Total amount of security traded today. |
| `yH` | string | 52-week high. |
| `yL` | string | 52-week low. |
| `streaming_type` | string | Streaming type. Added for future use. Pass this value as “quote” always. |
