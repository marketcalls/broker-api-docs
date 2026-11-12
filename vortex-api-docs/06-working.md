<!-- Source: https://vortex.rupeezy.in/docs/2.2/working/ -->

# Working with Orders

When the place order/modify order API is called and the api returns success, it simply means that the Order has been submitted to us. It does not mean that the order has been placed on the exchange. We provide several checks before placing the order, including but not limited to:

- Funds availability of the trader
- Products and exchanges allowed to the trader
- Timings
- Availability of equity sold

This means that you can never be sure of the order's fate if you don't listen to the Postback url configured during developer onboarding or the websocket messages. Alternatively, you can call the orderbook api or the order detail api with some delay to know the latest status.
