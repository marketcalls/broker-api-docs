# Publisher

Embed one-click trade buttons on your own website using the Samco Publisher JS plugin and offsite order execution.

## Samco Publisher

Easily copy and paste trade buttons to embed them on your website.

### What is its purpose?

Integrating buttons into websites and apps to enable users to execute trades. The Samco Publisher buttons can seamlessly become part of your website by copying and pasting a few lines of HTML and JavaScript code.

### Why?

Enhance the user experience for your audience, whether they're readers of your financial blog or consumers of your market analysis. Offer them a unique trading experience while also presenting the opportunity for additional revenue for you.

### Is there any fees?

No, Samco Publisher is available free of charge.

### How do I get my trade buttons?

First create a Publisher app and obtain API keys via `[/publihser/createApp](#samco-publisher) API`. Use these keys along with the necessary HTML/Javascript lines to embed buttons on your website as documented [here](#js-plugin).

### Create App

This Publisher create API is to create a Publisher app and obtain API keys. `POST /publisher/createApp`

#### Code Sample

**cURL**

```bash
curl -X POST 'https://tradeapi.samco.in/publisher/createApp' \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -d '{"appName":"My App","redirectURL":"https://www.example.com/","description":"Description about the App"}'
```

**Java**

```java
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

public class Sample {
  public static void main(String[] args) throws Exception {
    String requestBody = """
        {
          "appName": "My App",
          "redirectURL": "https://www.example.com/",
          "description": "Description about the App"
        }
        """;

    HttpClient client = HttpClient.newHttpClient();

    HttpRequest request = HttpRequest.newBuilder()
        .uri(URI.create("https://tradeapi.samco.in/publisher/createApp"))
        .header("Content-Type", "application/json")
        .header("Accept", "application/json")
        .POST(HttpRequest.BodyPublishers.ofString(requestBody))
        .build();

    HttpResponse<String> response =
        client.send(request, HttpResponse.BodyHandlers.ofString());
    System.out.println(response.body());
  }
}
```

**NodeJs**

```js
(async () => {
  const headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
  };

  const requestBody = {
    appName: "My App",
    redirectURL: "https://www.example.com/",
    description: "Description about the App"
  };

  const response = await fetch('https://tradeapi.samco.in/publisher/createApp', {
    method: 'POST',
    headers,
    body: JSON.stringify(requestBody),
  });

  const data = await response.json();
  console.log(data);
})();
```

**Python**

```py
import requests
import json

headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
}

requestBody = {
  "appName": "My App",
  "redirectURL": "https://www.example.com/",
  "description": "Description about the App"
}

r = requests.post('https://tradeapi.samco.in/publisher/createApp',
  data=json.dumps(requestBody),
  headers=headers)

print(r.json())
```

#### Sample Request Body

```json
requestBody={
  "appName": "My App",
  "redirectURL": "https://www.example.com/",
  "description": "Description about the App"
}
```

#### Parameters

| **Name** | **Type** | **Required** | **Description** |
| --- | --- | --- | --- |
| `body` | object | false | Contains the details for creating the app. |
| `appName` | string | true | The name of the app you want to create. |
| `redirectURL` | string | true | URL to which the user will be redirected after the order execution. |
| `description` | string | true | A description of the app, providing details or information about its purpose or functionality. |

#### Sample Response

```json
{
    "serverTime": "06/02/24 14:02:03",
    "msgId": "d3001338-4312-45ca-8195-9edc6873577a",
    "status": "Success",
    "apiKey": "5TmpmCtzBnxq2MbDb",
    "statusMessage": "Publisher App created & api key generated"
}
```

#### Response Schema

Status Code **200**

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| `serverTime` | string | The current time at the server when the response was generated. |
| `msgId` | string | A unique identifier for the request. Use this ID when contacting support about any issues. |
| `status` | string | Indicates whether the login attempt was successful or failed. |
| `statusMessage` | string | Provides additional information about the status of the login attempt. |
| `apiKey` | string | The API key required for creating HTML/JSON trade buttons. |

---

## Offsite order execution

The offsite order execution functionality enables users to be redirected to Samco's order execution page from your application, allowing them to seamlessly place orders and return, similar to a payment gateway. This eliminates the need for you to develop or upkeep order execution screens. [Samco's Publisher](#samco-publisher-demo) program leverages offsite order execution to offer embeddable Javascript+HTML trade buttons, eliminating the need for any API integrations.

### Please review the code sample on the right for preparing orders and submitting the JSON basket data via an HTML form.

Sending multiple orders is feasible, where users confirm them via a shopping basket-like interface. To do this, you need to assemble a JSON list of stocks to be traded, complete with the necessary order parameters. Then, `POST` this list as a form field named `data` along with your `api_key` to **[https://web2.samco.in/publisher/basket](https://web2.samco.in/publisher/basket)**.

This request needs to happen on the user's device, either through a web browser or a mobile app's webview. While the backend can handle preparing the shopping basket, the easiest way to send the request is by creating a hidden form, adding the JSON data to it, and using JavaScript to submit it automatically.

If you're setting up the basket directly on your web application, you can simplify the process by utilizing Samco's Publisher [JavaScript plugin](#js-plugin).

> **INFO** — ![Excel Icon](https://docs-tradeapi.samco.in/assets/bulb.png) You don't necessarily need to start a login process using the login API to engage in offsite order execution. If a user isn't logged in yet, they'll be prompted to do so, whereas if they're already logged in, they'll be directed straight to the order basket. Regardless, you'll ultimately receive status updates.

### Parameters

| **Name** | **Type** | **Required** | **Description** |
| --- | --- | --- | --- |
| `body` | object | false | This parameter can be used to include additional data in the request. |
| `trading_symbol` | string | true | For Equity Cash symbols, use "symbol"; for F&O contracts, use "Trading Symbol". Both can be found in ScripMaster.csv. |
| `exchange` | string | true | The exchange where the order is to be placed. Valid values include BSE, NSE, NFO, MCX, CDS. Default is NSE if not provided. |
| `transaction_type` | string | true | Specifies the transaction type: BUY or SELL. |
| `order_type` | string | true | The type of order. Possible values are MARKET (Market Order), LIMIT (Limit Order), SL (Stop Loss Limit), SL-M (Stop Loss Market). |
| `quantity` | string | true | The quantity for which the order is being placed. |
| `product` | string | false | The product type of the order. Options include CNC (Cash and Carry), NRML (Normal), MIS (Intraday), CO (Cover Order), BO (Bracket Order). Default is CNC if not specified. |
| `price` | string | true | The price at which the order is to be placed. |
| `trigger_price` | string | false | The price at which the order should be triggered, applicable for SL and SL-M orders. |
| `disclosed_quantity` | string | true | The disclosed quantity should be a minimum of 10% of the actual order quantity. |
| `validity` | string | true | Order validity. Can be DAY (valid for the whole trading day) or IOC (Immediate Or Cancel). |
| `is_amo` | string | true | After Market Order flag. Use YES (1) or NO (0) to indicate if the order is an after-market order. |

### Sample JSON basket

```json
let json_data = [
  {
    "transaction_type": "BUY",
    "exchange": "NSE",
    "trading_symbol": "TCS",
    "order_type": "MARKET",
    "quantity": 10
  },
  {
    "transaction_type": "SELL",
    "exchange": "NFO",
    "trading_symbol": "NIFTY24FEBFUT",
    "order_type": "LIMIT",
    "price": 21803,
    "quantity": 50
  },
  {
    "transaction_type": "BUY",
    "exchange": "NSE",
    "trading_symbol": "IDEA",
    "order_type": "LIMIT",
    "product": "CO",
    "price": 14.15,
    "quantity": 1,
    "trigger_price": 13
  }
]
```

### Post the JSON data

```html
<form
  method="post"
  id="basket-form"
  action="https://web2.samco.in/publisher/basket"
>
  <input type="hidden" name="api_key" value="xxx" />
  <input type="hidden" id="basket" name="data" value="" />
</form>

<script>
  document.getElementById("basket").value = JSON.stringify(json_data);
  document.getElementById("basket-form").submit();
</script>
```

---

## JS Plugin

The [Samco Publisher](#samco-publisher-demo) JavaScript plugin allows you to integrate one-click trade buttons into your webpage. Operating similar to a combination of a shopping basket and a payment gateway, it initiates a new window on your webpage, assisting users through the trading process before returning them to your page.

Using the JavaScript plugin, you have the flexibility to dynamically add one or more stocks to the basket, with a maximum limit of 10. Alternatively, you can embed straightforward static buttons using plain HTML for a simpler approach.

### Create your buttons

```js
<script src="https://web2.samco.in/publisher.js?v=1"></script>
```

To integrate Samco Publisher into your webpage, simply insert the above script tag at the end of your webpage, right before the closing `</body>` tag. You only need to include this script once, and it will enable the rendering of any number of buttons on the page.

To render branded Samco buttons that initiate a trade with a single click, you can use the custom HTML5 tag `<samco-button>`. These buttons function similarly to social media buttons and can be included as many times as needed on a page.

### Branded HTML5 buttons

```html
<!--  Here's a simple HTML link that would initiate a market buy of the IDEA stock:  -->
<samco-button
  href="#"
  data-samco="your-api-key"
  data-exchange="NSE"
  data-trading_symbol="IDEA"
  data-transaction_type="BUY"
  data-quantity="1"
  data-order_type="MARKET"
  >Buy IDEA stock</samco-button>
```

### Custom HTML5 buttons

You can leverage HTML5 data attributes on any HTML element to transform it into a trade button, which can then be activated with a single click. The examples below demonstrate how a link and a button can be converted into trade buttons.

```html
<!--  Here's a simple HTML link that would initiate a MARKET BUY of the IDEA stock:  -->
<a
  href="#"
  data-samco="your-api-key"
  data-exchange="NSE"
  data-transaction_type="BUY"
  data-trading_symbol="IDEA"
  data-order_type="MARKET"
  data-quantity="1"
  >Buy IDEA stock</a>

<!--  Here's a simple HTML button that would initiate a LIMIT SELL of the TCS stock: //-->
<button
  data-samco="your-api-key"
  data-exchange="NSE"
  data-transaction_type="SELL"
  data-trading_symbol="TCS"
  data-order_type="LIMIT"
  data-quantity="1"
  data-price="4095"
>
  Sell TCS
</button>

<!--  Here's a simple HTML button that would initiate a CO order of the RELIANCE stock: //-->
<button
  data-samco="your-api-key"
  data-exchange="NSE"
  data-transaction_type="BUY"
  data-trading_symbol="RELIANCE"
  data-order_type="LIMIT"
  data-quantity="1"
  data-product="CO"
  data-price="2860"
  data-trigger_price="2840"
>
  Buy RELIANCE (Cover Order)
</button>
```

### Generating dynamic buttons with Javascript

```html
<!-- A Samco button will be generated within the specified container. //-->
<p id="default-button"></p>

<!-- The basket will be linked to the 'onClick' event of this element. //-->
<button id="custom-button">Buy the basket</button>

<!-- Include the plugin //-->
<script src="https://web2.samco.in/js/publisher/publisher.js?v=1"></script>

<script>
  // Only run your custom code once SamcoPublisher has fully initialised.
  // Use SamcoPublisher.ready() to achieve this.
  SamcoPublisher.ready(function () {
    // Initialize a new Publisher instance.
    // You can initialize multiple instances if you need.
    var publisher = new SamcoPublisher("your-api-key");

    // Add a stock to the basket
    publisher.add({
      exchange: "NSE",
      transaction_type: "BUY",
      trading_symbol: "IDEA",
      order_type: "MARKET",
      quantity: 1,
    });

    // Add another stock (Intra day)
    publisher.add({
      exchange: "NSE",
      transaction_type: "SELL",
      trading_symbol: "TCS",
      order_type: "LIMIT",
      quantity: 1,
      price: 4080,
      product: "MIS"
    });

    //Add a Cover Order
    publisher.add({
      exchange: "NSE",
      transaction_type: "BUY",
      trading_symbol: "RELIANCE",
      order_type: "LIMIT",
      product: "CO",
      price: 2862.5,
      quantity: 1,
      stoploss: 2850
    });

    //Add a Bracket Order
    publisher.add({
      exchange: "NSE",
      transaction_type: "BUY",
      trading_symbol: "SBIN",
      order_type: "LIMIT",
      product: "BO",
      quantity: 1,
      squareoff : 680,
      price: 670,
      stoploss: 660,
      trailing_stoploss : 5
    });

    // Register an (optional) callback.
    publisher.finished(function (status) {
      alert("Finished. Status is " + status);
    });

    // Render the in-built button inside a given target
    publisher.renderButton("#default-button");

    // OR, link the basket to any existing element you want
    publisher.link("#custom-button");
  });
</script>
```

You have the option to create a basket of stocks and have the plugin render a Samco button that executes it. Alternatively, you can link the basket to your own button or any HTML element of your choice.

To ensure proper initialization of your custom SamcoPublisher calls, it's essential to execute them after the plugin's assets have loaded asynchronously. You can achieve this by utilizing the `SamcoPublisher.ready()` function. This function ensures that your custom calls are executed only when the plugin is fully loaded and ready to be utilized.

#### Parameters

| **Name** | **Type** | **Required** | **Description** |
| --- | --- | --- | --- |
| `body` | object | false | This parameter can include additional data as needed. |
| `trading_symbol` | string | true | For Equity Cash symbols, use "symbol"; for F&O contracts, use "Trading Symbol". Both can be found in ScripMaster.csv. |
| `exchange` | string | true | The exchange for placing the order. Valid values are BSE, NSE, NFO, MCX, CDS. Default is NSE if not provided. |
| `transaction_type` | string | true | Specifies the transaction type. Options are BUY or SELL. |
| `order_type` | string | true | Type of order. Can be MARKET (Market Order), LIMIT (Limit Order), SL (Stop Loss Limit), SL-M (Stop Loss Market). |
| `quantity` | string | true | The quantity for which the order is being placed. |
| `product` | string | false | Product type of the order. Options include CNC (Cash and Carry), NRML (Normal), MIS (Intraday), CO (Cover Order), BO (Bracket Order). Default is CNC. |
| `price` | string | true | The price at which the order will be placed. |
| `trigger_price` | string | false | The price at which the order should be triggered for SL or SL-M orders. |
| `disclosed_quantity` | string | true | If provided, should be at least 10% of the actual order quantity. |
| `validity` | string | true | Order validity. Can be DAY (valid for the trading day) or IOC (Immediate Or Cancel). |
| `is_amo` | string | true | After Market Order flag. Use YES (1) or NO (0) to indicate if it is an after-market order. |

#### Methods

| **Method** | **Arguments** | **Description** |
| --- | --- | --- |
| `body` | false | none |
| `SamcoPublisher.ready()` | function() | A secure wrapper for all API calls that asynchronously waits for all assets to load. |
| `add()` | entry | Adds a trading entry to the basket. The `entry` should be an object literal `{}` containing the parameters needed. |
| `get()` |  | Returns an array of all added entries in the basket. |
| `count()` |  | Returns the number of entries added to the basket. |
| `setOption()` | key, value | Sets the value for certain supported keys. |
| `renderButton()` | element_selector | Displays a branded Samco button within the specified target HTML element. The button initiates the transaction when clicked. The `element_selector` should be an HTML selector like `#buy-button` or `.buttons`. |
| `link()` | element_selector | Associates the basket with the designated HTML element. Clicking this element will initiate the transaction in a new window tab. The `element_selector` should be an HTML selector like `#buy-button` or `.buttons`. |
| `html()` |  | Generates an HTML form with required hidden fields and the basket payload serialized. Append this form to the document body and submit it to initiate the transaction. |
| `finished()` | function(status) | Sets up a callback function that activates after the order placement process is completed. The `status` provides the result of the order process. |

---

## Samco Publisher Demo

Easily add trade buttons to your website. Copy and paste the code where needed.

### Samco Publisher

The Samco Publisher JavaScript plugin enables seamless integration of one-click trade buttons on your webpage. This powerful tool functions as both a basket and payment gateway, facilitating a user-friendly experience where a popup guides users through the trading process before directing them back to your site.

You have the flexibility to dynamically add one or more stocks to the basket (up to a maximum of 10) using the JavaScript plugin, or you can opt for static buttons embedded in plain HTML for a simpler setup.

If you have already secured an [**API key**](#samco-publisher), you can begin implementing this functionality immediately by consulting the comprehensive [**documentation**](#js-plugin) provided. This ensures that you can offer your users an efficient and streamlined trading experience.

### Getting Started with the Samco Publisher: A User Guide

When you click the button, a window will pop up asking you to enter your client ID and password to log in. After logging in, you will see all the details of the stock you want to buy or sell. This window is designed to make trading easy and straightforward.

In this window, you can also modify or delete your order requests. There are two main buttons: "Place" and "Cancel." If you want to go ahead with your order, click the "Place" button, and your order will be processed. If you decide not to continue, clicking the "Cancel" button will take you back to the URL you provided when you set up your application.

Once your order is placed, you will see an option to refresh the order status. This lets you check the current status of your order at any time. If your order is rejected for any reason, you can find out why by hovering over the "Rejected" status.

The system is user-friendly and suitable for everyone, whether you are new to trading or have experience. It provides all the tools you need to place and manage orders easily.

### Branded button examples

SELL a single share of Idea

Buy a single share of Reliance

Trade a basket of multiple stocks

### Custom buttons and links

Buy a basket of stocks

### Dynamic Input Example

IDEA

RELIANCE

8

ABB

TCS

INFY

Buy

Sell
