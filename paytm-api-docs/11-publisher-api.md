# Publisher API

- [Paytm Money Publisher](#paytm-money-publisher)

## Paytm Money Publisher

Source: https://developer.paytmmoney.com/docs/api/paytm-money-publisher/

### Description

> You can integrate trading execution buttons seamlessly into your websites and apps using Paytm Money Publisher buttons. Simply copy and paste a few lines of HTML and Javascript to incorporate them onto your platform. Enhance the user experience for your audience, whether they're readers of your financial blog or consumers of your market analysis. Offer them a unique trading experience while potentially increasing your revenue prospects.

### Notes

### How to use it ?

1. To generate a Publisher API, first, log in to your Paytm Money developer account. Then, click on the "Create New App" button to initiate the creation of a Publisher app and acquire the essential API keys.
2. Incorporate these keys into your website using the required HTML/Javascript code as outlined in the documentation.
3. Employing the custom HTML5 tag "<Paytm Money>" to display branded Paytm Money buttons facilitating one-click trade initiation. These branded buttons function akin to social media buttons and can be integrated in any desired quantity within a webpage.  

   #### Paytm Money HTML5 buttons

   ```
               <!DOCTYPE html>
               <html lang="en">
                   <head>
                       <title>Paytm Money Stocks</title>
                       <script src="https://www.paytmmoney.com/static/publisher/publisher.js"></script>
                   </head>
   		<body>
   			<pml-button isPtmButton=true apiKey="{{apiKey}}" 
   				exchange="NSE" 
   				productType="C" 
   				securityId="772" 
   				transactionType="B" 
   				orderType="MKT" 
   				class="pml-buy" 
   				btnText="Buy Dabur" 
   				segment="E">
   			</pml-button>
   		</body>	
               </html>
   ```

| Parameters | Description |
| --- | --- |
| transactionTypestring | The type of transaction that is being executed (Buy / Sell) |
| exchangestring | The exchange which is involved for this specific transaction ( NSE/BSE ) |
| segmentstring | This describes, to which segment the transaction belongs. (E→ Equity Cash / D→ Equity Derivative) |
| productTypestring | Type of product (C/I/M/B/V)  C ((Cash and Carry/Delivery) Valid only for Segment = 'E')  I (Intraday (Valid for Segment= E/D))  M (Margin (Valid for Segment='D')) |
| securityIdstring | security\_id of scrip in NSE / BSE |
| quantitystring | Quantity of stocks to be traded in NSE/BSE |
| validitystring | Validity of the Order, Day/IOC/GTC/GTD  DAY - valid for day only  IOC - Immediate or cancel  GTC - good till cancel  GTD - good till date |
| orderTypestring | LMT - Limit order(order is to be traded at mentioned price)  MKT - market order(order is to be traded at market price)  SL - Stop loss Limit(trigger which goes into trigger state when market reaches mentioned trigger price)  SLM - Stop Loss Market |
| initialPricestring | need to be passed for LMT and SL orders |
| triggerPricestring | Price at which stop loss is to be triggered (mandatory if it is stop loss order)  need to be passed for SLM and SL orders |
| btnTextstring | works only when isPtmButton = false |
| isPtmButtonboolean | to display the branded Paytm Money button |
