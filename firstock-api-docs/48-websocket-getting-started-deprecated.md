# Getting Started (Deprecated)

> Source: https://firstock.in/api/docs/getting-started-3/

### Introduction

- The WebSocket serves as an advanced technology that enables the establishment of a bi-directional communication channel between a user's browser and a server. Through this, users can seamlessly send messages to a server and receive responses driven by events, eliminating the need for continuous polling of the server for replies.
- With the WebSocket, users gain the capability to access real-time quotes for all scripts across various Indian Exchanges during market hours. These data feeds are broadly classified into three categories: Market Feed ,OrderUpdate Feed and PositionUpdate Feed. Upon initiating a new connection, users can anticipate receiving an acknowledgment for successful connection establishment.

### Create Session

- Copy the susertoken from the [login API](https://firstock.in/api/docs/login/)

### Connection String

Create Connection to Websocket using the following URL:

```
wss://socket.firstock.in/ws
```

Send the Following Data in the query params of Websockets

| Field | Type | Mandatory | Description | Example |
|---|---|---|---|---|
| userId | string | Yes | UserId of the client | AB1234 |
| jKey | string | Yes | susertoken from the Login API | 5763be188551a9da7bab9e0351a2004fea0a4042a8845b48b66ee2415556bf6 |
| source | string | Yes | Source of the websocket | developer-api |

```
wss://socket.firstock.in/ws?userId=AB1234&jKey=cae0e3af6f26583c0e19b83c91f207466199b7fef5e66160b8ff02511205d651&source=developer-api
```

**Note**: This WebSocket implementation includes a *ping-pong mechanism* to ensure connection liveness. The server periodically sends a `Ping` frame to the client, and expects a corresponding `Pong` response within **10 seconds**. This exchange serves as a heartbeat to verify that the connection is still active. Failure to receive a `Pong` within the specified timeout is interpreted by the server as a dead or unresponsive connection, leading to the termination of the WebSocket session.

Some WebSocket client libraries come with built-in support for handling `Ping` and `Pong` frames automatically. However, if the client library you are using does not provide this functionality out of the box, you will need to implement the handling logic manually to maintain a persistent and healthy connection.

## Response Structure

**Success Response**

If the credentials and API key are valid, you will receive a 200 OK status with a JSON response containing the following fields:

1. **status:** Indicates a successful request (e.g., *"success"*).
2. **message:** Provides a short description of the outcome (e.g., Authentication successful).

**Failure Response**

If any required fields are missing or invalid, you will receive a 401 status code with a structure like:

1. **status:** Typically *"failed"*.
2. **message:** Provides a short description of the outcome (e.g., unauthenticated).

**Response**

**success**

```json
{"status":"success","message":"Authentication successful"}
```

**failure**

```json
{"status":"failed","message":"unauthenticated"}
```

**Note**: Websocket will be disconnected upon failure in any case
