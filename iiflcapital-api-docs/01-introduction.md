# Introduction

IIFL Markets' APIs provide fast, efficient, and easy-to-use trading solutions for retail traders and fintech platforms. These REST-like APIs support real-time order execution, modification, and cancellation, portfolio management, live market data, and order-status monitoring. Requests accept JSON or form-encoded bodies and responses are JSON, using standard HTTP status codes. Official SDKs are available in multiple languages.

## Base URL

```
https://api.iiflcapital.com/v1
```

> The [Brokerage and Charges APIs](10-brokerage-and-charges.md) use a different base URL — see that page for details.

## Video Tutorials

1. **Trading API Document overview** — a walkthrough of the documentation: <https://youtu.be/t7TMp4SldJ4>
2. **Daily client login flow** — step-by-step daily login guide: <https://youtu.be/DMvSVncJOZA>

## Instrument Details

Exchange- and segment-wise data for all active market instruments, available in CSV and JSON.

### CSV Links

| Exchange & Segment | CSV File |
| --- | --- |
| NSEEQ | <https://api.iiflcapital.com/v1/contractfiles/NSEEQ.csv> |
| NSEFO | <https://api.iiflcapital.com/v1/contractfiles/NSEFO.csv> |
| NSECOMM | <https://api.iiflcapital.com/v1/contractfiles/NSECOMM.csv> |
| MCXCOMM | <https://api.iiflcapital.com/v1/contractfiles/MCXCOMM.csv> |
| INDICES | <https://api.iiflcapital.com/v1/contractfiles/INDICES.csv> |
| NSECURR | <https://api.iiflcapital.com/v1/contractfiles/NSECURR.csv> |
| BSEEQ | <https://api.iiflcapital.com/v1/contractfiles/BSEEQ.csv> |
| BSEFO | <https://api.iiflcapital.com/v1/contractfiles/BSEFO.csv> |
| BSECURR | <https://api.iiflcapital.com/v1/contractfiles/BSECURR.csv> |

### JSON Links

| Exchange & Segment | JSON File |
| --- | --- |
| NSEEQ | <https://api.iiflcapital.com/v1/contractfiles/NSEEQ.json> |
| NSEFO | <https://api.iiflcapital.com/v1/contractfiles/NSEFO.json> |
| NSECOMM | <https://api.iiflcapital.com/v1/contractfiles/NSECOMM.json> |
| MCXCOMM | <https://api.iiflcapital.com/v1/contractfiles/MCXCOMM.json> |
| INDICES | <https://api.iiflcapital.com/v1/contractfiles/INDICES.json> |
| NSECURR | <https://api.iiflcapital.com/v1/contractfiles/NSECURR.json> |
| BSEEQ | <https://api.iiflcapital.com/v1/contractfiles/BSEEQ.json> |
| BSEFO | <https://api.iiflcapital.com/v1/contractfiles/BSEFO.json> |
| BSECURR | <https://api.iiflcapital.com/v1/contractfiles/BSECURR.json> |

> The JSON links double as APIs — call them directly with `GET` to fetch instrument details. No authorization is required for these calls.

## Postman Collection & SDKs

The official Postman collection and pre-built SDKs (for interacting with the APIs without raw HTTP calls) are linked from the [developer portal](https://developers.iiflcapital.com/apidocs/introduction).

## Developer's Community

Bugs and issues can be raised on IIFL's GitHub Issues page, or via email at `openapisupport@iiflcapital.com` / phone & WhatsApp at `+91-7718830851`.
