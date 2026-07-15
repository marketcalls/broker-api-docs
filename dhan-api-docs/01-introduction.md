<!-- Introduction - DhanHQ Ver 2.0 / API Document -->
# Source: https://dhanhq.co/docs/v2

# Introduction

## Getting Started

![alt](img/intro.svg)

DhanHQ API is a state-of-the-art platform for you to build trading and investment services & strategies.

It is a set of REST-like APIs that provide integration with our trading platform. Execute & modify orders in real time,
manage portfolio, access live market data and more, with lightning fast API collection.

We offer resource-based URLs that accept JSON or form-encoded requests. The response is returned as
JSON-encoded responses by using Standard HTTP response codes, verbs, and authentication.

![sandbox](img/btn2sandbox.png)

Developer Kit

[Explore Now
![sandbox](img/dhanhq-arrow.png)](https://api.dhan.co/v2/#)

![sandbox](img/btn2sandbox.png)

Developer Kit

[Explore Now](https://api.dhan.co/v2/#)
![sandbox](img/dhanhq-arrow.png)

![python](img/btn2pydhanhq.png)

DhanHQ Python Client

[Explore Now
![python](img/dhanhq-arrow.png)](https://pypi.org/project/dhanhq/)

![python](img/btn2pydhanhq.png)

DhanHQ Python Client

[Explore Now](https://pypi.org/project/dhanhq/)
![python](img/dhanhq-arrow.png)

## Structure

RESTPython

All GET and DELETE request parameters go as query parameters, and POST and PUT parameters as form-encoded.
User has to input an access token in the header for every request.

```
curl --request POST \
--url https://api.dhan.co/v2/ \
--header 'Content-Type: application/json' \
--header 'access-token: JWT' \
--data '{Request JSON}'
```

Install Python Package directly using following command in command line.

```
pip install dhanhq
```

This installs entire DhanHQ Python Client along with the required packages. Now, you can start using DhanHQ Client with your Python script.

You can now import 'dhanhq' module and connect to your Dhan account.

```
from dhanhq import dhanhq

dhan = dhanhq("client_id","access_token")
```

## Errors

Error responses come with the error code and message generated internally by the system. The sample structure of
error response is shown below.

```
{
    "errorType": "",
    "errorCode": "",
    "errorMessage": ""
}
```

You can find detailed error code and message under [Annexure](/docs/v2/annexure/#trading-api-error).

## Rate Limit

| Rate Limit | Order APIs | Data APIs | Quote APIs | Non Trading APIs |
| --- | --- | --- | --- | --- |
| per second | 10 | 5 | 1 | 20 |
| per minute | 250 | - | Unlimited | Unlimited |
| per hour | 1000 | - | Unlimited | Unlimited |
| per day | 7000 | 100000 | Unlimited | Unlimited |

Order Modifications are capped at 25 modifications/order
