# Introduction

Pi is a collection of REST APIs that provides many required capabilities to build a modern stock market investment and trading platform. Using these API endpoints, you can execute orders in real time (equities, commodities, currency), stream live market data over WebSockets, and more.

## Base URL

```
https://piconnect.flattrade.in/PiConnectAPI
```

> **Note:** The REST base URL was changed from `PiConnectTP` to `PiConnectAPI`, and the WebSocket base URL was changed from `PiConnectWSTp` to `PiConnectWSAPI`. See [Change Log](15-changelog.md) for the full migration details.

## Registering Your App

To use these APIs, you need to register your app to generate your `apiKey` (App Key) and `apiSecret`.

1. Login to Wall: <https://wall.flattrade.in>
2. Navigate to **Pi** in the top menu bar and click **CREATE NEW API KEY**.
3. Select the order volume for the API key:
   - **Yes** — More than 10 orders per second
   - **No** — Less than 10 orders per second

Follow the corresponding step below based on the order volume you selected.

### Less Than 10 Orders Per Second

1. Enter your **IP Configuration** (Primary IP is required, Secondary is optional) → click **Next**.

   | Field | Description |
   | --- | --- |
   | Primary IP Address | IP address used for API requests |
   | Secondary IP Address | Optional secondary IP address for API requests |

2. Fill out the **URL Configuration**:

   | Field | Description |
   | --- | --- |
   | App Name | Your app name |
   | App ShortName | Short name of your app |
   | Redirect URL | URL to redirect to after successful login authentication. The `request_code` used to generate the token is sent as a parameter to this URL |
   | Postback URL | URL on which you will receive order updates for orders placed through the API |
   | Description | Short description about your app |

3. Review the Configuration Summary, tick the box to accept the Terms & Conditions, and submit.
4. Your request shows as **Pending** — once approved, your API key is ready.
5. Your API key is generated. Click the eye icon to reveal your Secret Key — copy both the API Key and Secret Key.

### More Than 10 Orders Per Second

1. Enter your **IP Configuration** (Primary IP is required, Secondary is optional) → click **Next**.
2. Fill out the same **URL Configuration** fields as above (App Name, App ShortName, Redirect URL, Postback URL, Description).
3. Upload your **Strategy**, **Algorithm Details**, and choose **Segments** → click **Upload**.

   | Field | Description |
   | --- | --- |
   | Strategy | Your strategy for this API key |
   | Segment | Segment(s) for this API key |
   | File | Uploaded file for the selected segment |

4. Review the Configuration Summary, tick the box to accept the Terms & Conditions, and submit.
5. Your request shows as **Pending** — once approved, your API key is generated.
6. Click the eye icon to reveal your Secret Key — copy both the API Key and Secret Key.

> Don't have an account? [Sign up](https://ekyc.flattrade.in/openaccount/?utm_source=pi&utm_content=pi).

## Postman Collections

A ready-to-import Postman collection is available to test the API. Define the required variables (`BaseUrl`, `ClientId`, `jKey`) on the collection before use.

```
BaseUrl - https://piconnect.flattrade.in/PiConnectAPI
ClientId - FT0000
jKey     - <token obtained on login>
```

Download: <https://flattrade.s3.ap-south-1.amazonaws.com/pidoc/collections/Piconnect.postman_collection.zip>

## MCP Server

Flattrade also publishes an MCP (Model Context Protocol) server for Pi: <https://github.com/flattrade/flattrademcp>
