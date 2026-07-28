# NEO WebSocket (Market Data)

The Kotak Neo WebSocket ZIP (`Websocket (2).zip`, ~29.5 KiB) contains 4 major files:

1. `HSLib`
2. `Demo.html`
3. `Demo.js`
4. `Neo.js`

To start the WebSocket, make sure the position of these files is aligned as shown in the ZIP's example layout.

Open `demo.html` — it opens a web page in your browser to drive the connection.

## Establishing the Connection

To establish the connection the user passes 3 parameters:

- **Token** — final token (session token) received after running the login API
- **sid** — session sid received after running the login API
- **Data Center** — returned in the login API response (e.g. `E43`, `E41`, ...), passed as `'dataCenter': '123'`

> If you're using Postman for testing, `https://mis.kotaksecurities.com/login/1.0/tradeApiValidate` returns all 3 of the above values.

## Connect to Market Feed (HSM)

HSM is the stream that delivers market data. When you pass Session Token, SID and Data Center, you can connect with HSM — click **"Connect HSM"**.

### Subscribe Scrip

Provide the exchange identifier to start receiving feeds.

Format: `nse_cm|11536&`

One scrip input consists of the exchange name, a pipe separator (`|`), then the scrip identifier. To add another scrip in the same input, use an ampersand (`&`) separator.

### Subscribe Index

Provide the exchange identifier of indices to start receiving feeds.

Format: `nse_cm|Nifty 50&`

Same pipe + ampersand structure as scrips.

### Subscribe Depth

Format: `nse_cm|11536&`

One market-depth input consists of the exchange name, a pipe separator (`|`), then the scrip identifier. Add another with an ampersand (`&`) separator.

## Connect to Order Feed (HSI)

HSI is the stream that delivers order updates. Connect with HSI to view feeds of orders you have placed. The feeds reflect in the **Streaming Orders** column.

## Integrating market/order feed in code

By running Inspect on the `demo.html` file you can get the WebSocket string.

## Limits

- Total number of channels a user can use at a time: **16**
- Total number of scrips a user can subscribe to at a time: **200**

## Field Mapping in the WebSocket Response

| Field | Meaning |
| --- | --- |
| tk | Exchange Token |
| ts | Trading Symbol |
| e | Exchange |
| ltp | Last Traded Price |
| ltq | Last Traded Quantity |
| tbq | Total Buy Qty |
| tsq | Total Sell Qty |
| bp | Best Bid Price |
| bq | Best Bid Qty |
| sp | Best Ask Price |
| bs | Best Ask Qty |
| op | Open |
| h | High |
| lo | Low |
| c | Previous Close |
| cng | Change |
| nc | % Change |
| ap | Average Traded Price |
| to | Turnover |
| oi | Open Interest |
| ltt | Last Trade Time |
| fdtm | Feed Time |
| prec | Price Precision |
| lcl | Lower Circuit |
| ucl | Upper Circuit |
| yh | 52 Week High |
| yl | 52 Week Low |
| mul | Price/Contract Multiplier |
| name | Feed Type (sf) |
