# How to Download and Use Postman

> Source: https://v2api.aliceblueonline.com/Postman%20Scrips/

## Downloading Postman

1. Go to [Postman Downloads](https://www.getpostman.com/downloads/)
2. Choose your desired platform among Mac, Windows, or Linux.

## Importing Postman Scripts

1. Go to [Postman Downloads](https://www.getpostman.com/downloads/)
2. Open Postman.
3. Click the "Import" button.
4. Select the import file or drag and drop the file into the box.

## Making HTTP Requests

### HTTP Request

- Clicking this would display a dropdown list of different requests such as GET, POST, COPY, DELETE, etc.
- In testing, the most commonly used requests are GET and POST.

### Params

- This is where you will write parameters needed for a request such as key values.

### Headers

- You can set headers such as content type JSON depending on the needs of the organization.

### Body

- This is where one can customize details in a request, commonly used in POST requests.

### Tests

- These are scripts executed during the request.
- It is important to have tests as they set up checkpoints to verify if the response status is ok, if the retrieved data is as expected, and other tests.

## Working with GET Requests

1. Set your HTTP request to GET.
2. In the request URL field, input the link.
3. Click "Send".
4. You will see a 200 OK message.

## Working with POST Requests

1. Set your HTTP request to POST.
2. Input the same link in the request URL field.
3. Switch to the "Body" tab.
4. In "Body", click "raw" and select "JSON".

## Pre-filled sample post man scripts can be downloaded here

1. Open the Post man
2. Click the import button
3. Select the import file or Drag and drop the file in the box

[Download](https://v2api.aliceblueonline.com/PDF/Aliceblue_Postman_Collection.json)

A copy of that collection is vendored in this repo at
[`postman/Aliceblue_Postman_Collection.json`](postman/Aliceblue_Postman_Collection.json).

### What the collection covers

Postman Collection v2.1.0, named `OPEN-API ALICEBLUE A3 Copy`, with 9 folders
against the `https://a3.aliceblueonline.com` base URL:

| Folder | Requests |
| --- | --- |
| AUTH USER SESSION | `POST /open-api/od/v1/vendor/getUserDetails` |
| ORDERS | `placeorder`, `modify`, `cancel`, `history`, `book`, `trades`, `checkMargin`, `basket/margin`, `exit/sno` |
| GTT ORDERS | `gtt/orderbook`, `gtt/execute`, `gtt/modify`, `gtt/cancel` |
| POSITIONS | `positions`, `orders/positions/sqroff`, `conversion` |
| HOLDINGS | `GET /open-api/od/v1/holdings/CNC` |
| LIMITS | `GET /open-api/od/v1/limits/` |
| PROFILE | `profile`, Create Session, Invalidate Session |
| OPTION CHAIN | `obrest/optionChain/getUnderlying`, `getUnderlyingExp`, `getOptionChain` |
| WEBSOCKET | `createWsToken` |

### Deviation from the upstream file

The upstream collection hard-codes real bearer JWTs in five places. Those tokens
are all expired, but a JWT payload is base64, not encryption, so it stays
readable regardless — and these payloads carry the name, broker client code
(UCC), and in one case the mobile number and email address of three real
Aliceblue account holders.

This vendored copy therefore **replaces all five token values with the Postman
variable `{{Open_token}}`**, and ships `Open_token` as an empty collection
variable. Nothing else is changed; the 9 folders and 26 requests are untouched.

Set `Open_token` once to the `userSession` you get from
[Authentication](02-authentication.md) and every request picks it up.

[Download](https://v2api.aliceblueonline.com/PDF/Aliceblue_Postman_Collection.json)
