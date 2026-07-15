# Publisher JS Plugin

Embed one-click trading buttons on webpages via Kite Publisher.

**Note:** Does not work in iOS WebView due to Safari cookie policy. Use offsite order execution instead.

## Setup

```html
<script src="https://kite.trade/publisher.js?v=3"></script>
```

## Button Types

- **Branded:** `<kite-button>` HTML5 tags with data attributes
- **Custom:** Standard HTML elements with data attributes
- **Dynamic:** Generated via JavaScript after `KiteConnect.ready()`

## Parameters

Same as order parameters: variety, tradingsymbol, exchange, transaction_type, order_type, quantity, product, price, trigger_price, disclosed_quantity, validity, readonly, tag

## Core Methods

`add()`, `get()`, `count()`, `setOption()`, `renderButton()`, `link()`, `html()`, `finished()`, `authHoldings()`

## Limitations

- Max 10 stocks per basket
- iOS WebView incompatible
- Redirect URL limited to localhost or same-domain
