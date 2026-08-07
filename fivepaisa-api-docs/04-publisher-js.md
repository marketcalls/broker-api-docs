# Publisher JS

Browser-side trade buttons that hand an order off to the 5paisa web terminal.

> Source: https://xstream.5paisa.com/dev-docs/docFundamentals/publisher-js

## What is Publisher JS?

Publisher JS allows you to Embed Trade button on your Web or App with very less development efforts. All you have to do is copy paste few lines of code and you are good to go.

Advantages –

- Inbuild User Login Flow.
- In App Experience for Order Placement
- Quick Integration with less coding efforts.
- No Exchange Approval for Order Placement Screens.
- Free of cost

**Publisher JS** [**Demo**](https://www.5paisa.com/technology/publisher-library)

## Integration Steps

**Please follow below Steps for Publisher JS Integration.**

Data Parameters

- data-fivepvendorkey: API Key to be provided by 5paisa upon integration. (e.g.YJ4YpdZwCOX2zCXeWiOg7EkV4)
- Order Type – Fields Mapping
- data-price : The order price (e.g. 0 for market orders)
- data-IsIntraday : Order validity (e.g. ”true" or "false” )
- data-IsStopLossOrder: StopLoss (e.g. ”true" or "false” )
- data-StopLossPrice:"20"
- data-scripdata: Instrument Symbol (e.g. “ITC_EQ”)
- data-scripcode: Instrument Code (e.g. “1660”)

ScritpData or ScriptCode one of the field is required, these fields can you can obtain from ScripMasterAPI, ScripData fomat is also mentioned in ScripMastetAPI documentation.

## Library Plugin

You need to add below line of code in your Website or App. Copy below line just before closing body tag and including it once should suffice.

```
<script src="https://tradechart.5paisa.com/plugin/plugin.js"></script>
```

## Branded Button

To render Branded 5paisa Button on your app use <FIVEP-BUTTON> HTML tag and copy paste below data points.

```
<FIVEP-BUTTON
           data-fivepvendorkey="YnJ4JYpdZweCOhX2zCXeWiOg7EZwkVd4"
           data-scripdata="RELIANCE_EQ"
           data-exchange="NSE"
           data-transaction_type="BUY"
           data-exchange_type= "C"
           data-price="2535.65"
           data-qty="5"
></FIVEP-BUTTON>
```

## Custom Button

You can create your own trade button using any HTML element. To convert it into a trade button, simply include the following data attributes:

```
<button
 data-fivepvendorkey="YnJ4JYpdZweCOhX2zCXeWiOg7EZwkVd4"
           data-scripdata="RELIANCE_EQ"
           data-transaction_type="BUY"
           data-exchange_type= "C"
           data-price="2535.65"
           data-qty="5"
>
 Buy RELIANCE
</button>
```

## Dynamic Button - Single/Multiple Scrip (Basket)

You can create a dynamic trade button that links to a single order or a list of orders (basket) on your website. This allows you to create a button with a dynamic stock list. When the user clicks on the button, they will see the desired stocks.

Please note you need to add the stock details after ready() function.

## Dynamic Button

```
// the stocks will be linked to this Button on Click
<button id="custom-button">Buy the stocks</button>
//include the plugin 
<script src="https://tradechart.5paisa.com/plugin/plugin.js"></script>

<script>
     fivePaisaConnect.ready(function () {
 
//Initialize an instance, multiple instances can be initialized
       var fivePaisa = new fivePaisaConnect(
         "YnJ4JYpdZweCOhX2zCXeWiOg7EZwkVd4"
       );
//Add Single Stock
       fivePaisa.add({
         scripdata: "SBIN_EQ",
         exchange: BSE,
         transaction_type: "BUY",
         script_code: "500112",
         price: 590.00,
         qty: 10,
         exchange_type: "C",
         intraday: false,
       });
// Add Multiple Stocks
fivePaisa.Multipleadd([
         {
           scripdata: "RELIANCE",
           exchange: BSE,
           transaction_type: "SELL",
           script_code: "500325",
           order_type: "LIMIT",
           product: "MIS",
           price: 2485.0,
           qty: 15,
           variety: "co",
           readonly: true,
           exchange_type: "C",
           is_intraday: false,
         },
         {
           scripdata: "AXISBANK",
           exchange: NSE,
           transaction_type: "SELL",
           script_code: "3456",
           order_type: "LIMIT",
           product: "MIS",
           price: 384.4,
           qty: 5,
           variety: "co",
           readonly: true,
           exchange_type: "C",
           is_intraday: false,
         },
       ]);
// link stocks to any custom button
       fivePaisa.fivepButton("#custom-button");
     });
</script>
```
