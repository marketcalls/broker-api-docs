# HTML 5 Buttons

> Source: https://v2api.aliceblueonline.com/HTML%205%20Button/

The ANT Publisher Javascript plugin lets you add one-click trade buttons to your webpage. Provide some basic data while creating an ANT HTML5 Button and add the button to your desired web page or portal. Users can place hassle free orders with single click using AliceBlue ant web portal.

### Getting started

In the webpage or portal where the buttons are placed, make sure to add the following JavaScript file. Also users require an valid appcode (used in the button properties) to create these trade buttons. If the app code is not valid, the users will not be able to place the order.

`<script src="https://ant.aliceblueonline.com/jspublisher/publisher.js"></script>`

HTML Buttons work with a valid App Code (Used as appcode). To create appcode visit this link [https://developers.aliceblueonline.com.](https://developers.aliceblueonline.com) You can use your regular Aliceblue account credentials to login and create the app code.

The documentation on how to use the developer console can be found at [Developer's Console Documentation](09-vendors.md)

Also, symbol tokens provided by exchange is also mandatory. Various tokens for all symbols across exchanges can be downloaded from the following link Contract Master Data

Please note, scrip token will change on daily/weekly/monthly basis based on group change, expiry etc. Sending a wrong token will result in wrong trade or rejection of order.

There are three types of buttons provided.

- *Branded Buttons* - This will be populated with Aliceblue Logo.
- *Custom Buttons* - If you want to add custom color code and styling use Custom buttons.
- *Baskets* - If you want to place multiple orders, (Basket of orders) using a single button, you can use this basket option.

### Branded HTML5 buttons

```
        -- This Button initiate Buy SBIN Stock  --

<t5-button

   data-token="3045"
   data-appcode="<appcode>"
   data-exchange="NSE"
   data-tradingSymbol="SBIN-EQ"
   data-transactionType="BUY"
   data-quantity="1"
   data-orderType="MKT"
   data-price="0"
   data-validity="DAY"
   data-product="CNC"
   data-complexity="regular">

</t5-button>
```

**Example:**

Buy a single share of SBIN

Trade

```
      -- This Button initiate Sell SBIN Stock  --

<t5-button

   data-token="3045"
   data-appcode="<appcode>"
   data-exchange="NSE"
   data-tradingSymbol="SBIN-EQ"
   data-transactionType="SELL"
   data-quantity="1"
   data-orderType="MKT"
   data-price="0"
   data-validity="DAY"
   data-product="CNC"
   data-complexity="regular"

</t5-button>
```

**Example:**

Sell a single share of SBIN

Trade

```
      -- This Button initiate Basket of Orders  --

<t5-button

   data-appcode="<appcode>"
   :data-basket="JSON.stringify(basketList)" >

</t5-button>

basketList - Check below on how to create basket
list variable. Please note the difference between other
data-properties like data-token etc and :data-basket.
The :data-basket attribute value binded with basket
list variable.
```

**Example:**

Place the Basket of Orders

Trade

### Custom HTML5 buttons

```
       -- This Button initiate buy SBIN Stock --

<button

   data-token="3045"
   data-appcode="<appcode>"
   data-exchange="NSE"
   data-tradingSymbol="SBIN-EQ"
   data-transactionType="BUY"
   data-quantity="1"
   data-orderType="MKT"
   data-price="0"
   data-validity="DAY"
   data-product="CNC"
   data-complexity="regular" >

</button>
```

**Example:**

Buy a single share of SBIN

Buy

```
     -- This Button initiate buy SBIN Stock --

<button
   data-token="3045"
   data-appcode="<appcode>"
   data-exchange="NSE"
   data-tradingSymbol="SBIN-EQ"
   data-transactionType="SELL"
   data-quantity="1"
   data-orderType="MKT"
   data-price="0"
   data-validity="DAY"
   data-product="CNC"
   data-complexity="regular" >
</button>
```

**Example:**

Sell a single share of SBIN

Sell

### Basket buttons

```
   -- This link initiate buy SBIN and INFY Stocks --

<button

   data-appcode="<appcode>"
   :data-basket="JSON.stringify(basketList)" >

</button>
```

- **basketList** : Array of objects with the value of Basket (string)
- **data-appcode** is mandatory attribute with valid appcode

Example Basket value:

```
        var basketList = [

           {

             token: "3045",
             exchange: "NSE",
             tradingSymbol: "SBIN-EQ",
             instrument: "SBIN",
             transactionType: "BUY",
             orderType: "MKT",
             price: 0,
             quantity: 1,
             validity: "DAY",
             product: "MIS",
             complexity: "regular",

           },

           {

             token: "1594",
             exchange: "NSE",
             tradingSymbol: "INFY-EQ",
             instrument: "INFY",
             transactionType: "BUY",
             orderType: "L",
             price: "1450",
             quantity: 1,
             validity: "DAY",
             product: "MIS",
             complexity: "regular",

           },
        ],
```

**Example:**

Place the Basket of Orders

Trade

**Parameters:**

| Key | Description |
| --- | --- |
| complexity | Complexity of the order (regular, amo, co, bo) |
| tradingSymbol | Trading symbol of the instrument |
| exchange | Name of the exchange |
| transactionType | BUY or SELL |
| orderType | Order type ( MKT, L ,SL ,SL-M ) |
| quantity | Quantity to transact |
| product | Product type ( MIS - for Intraday, CNC - for Holdings, NRML- for Positions ) |
| price | For LIMIT orders |
| triggerPrice | For ( SL, SL-M ). |
| disclosedQuantity | Disclosed quantity |
| validity | Validity of the order ( DAY, IOC ) |
| token | Token of the Instrument |
