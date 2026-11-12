# IPO

Endpoints for discovering IPOs and for applying to mainboard and SME issues. Applications block the bid amount through a UPI mandate on the linked bank account.

---

## Get IPOs

API to retrieve a list of IPOs available on Indian exchanges. By default it returns currently open IPOs. Use the `status` and `issue_type` parameters to filter by lifecycle stage or market segment.

Use the `id` from each listing item as the path parameter in [Get IPO Details](https://upstox.com/developer/api-documentation/get-ipo-details) to fetch the full data for that IPO — including price band, lot size, event timeline, registrar info, and live subscription figures.

### Endpoint

**GET** `https://api.upstox.com/v2/ipos`

### IPO lifecycle

An IPO moves through four stages. The `status` parameter maps directly to these stages:

| Status | Description |
| --- | --- |
| `upcoming` | IPO is announced but the bidding window has not opened. Price band and dates may not be finalised yet. |
| `open` | Bidding is active. Investors can apply during this period. |
| `closed` | Bidding has ended. Allotment and refund processing is underway. |
| `listed` | Shares are trading on the exchange. |

### Issue types

| Issue type | Description |
| --- | --- |
| `regular` | Mainboard IPO. Larger companies listed on NSE/BSE under standard SEBI norms. |
| `sme` | Small and Medium Enterprise IPO. Listed on NSE Emerge or BSE SME under relaxed eligibility criteria. |

### Query Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| status | Optional | string | IPO status filter. Allowed values: `open` , `closed` , `listed` , `upcoming` . Default: `open` . |
| issue_type | Optional | string | Issue type filter. Allowed values: `regular` (mainboard IPOs), `sme` (SME IPOs). Default: It returns both. |
| page_number | Optional | integer | Page number for pagination. Default: `1` . |
| records | Optional | integer | Number of IPO records to return per page. Default: `20` . Maximum: `30` . |

### Response

```json
{
  "status": "success",
  "data": [
    {
      "id": "yaashvi-jewellers-limited-ipo",
      "symbol": "YAASHVI",
      "name": "Yaashvi Jewellers IPO",
      "status": "open",
      "isin": "INE1T6L01010",
      "issue_type": "sme",
      "issue_size": 44,
      "industry": "Diamond & Jewellery",
      "minimum_price": 83,
      "maximum_price": 83,
      "bidding_start_date": "2026-05-25",
      "bidding_end_date": "2026-05-27",
      "total_subscription": "0.0"
    },
    {
      "id": "m-r-maniveni-foods-limited-ipo",
      "symbol": "MANIVENI",
      "name": "M R Maniveni Foods IPO",
      "status": "open",
      "isin": "INE0YD301010",
      "issue_type": "sme",
      "issue_size": 27,
      "industry": "Consumer Food",
      "minimum_price": 51,
      "maximum_price": 52,
      "bidding_start_date": "2026-05-22",
      "bidding_end_date": "2026-05-26",
      "total_subscription": "1.27"
    }
  ],
  "meta_data": {
    "page": {
      "page_number": 1,
      "total_pages": 1,
      "records": 2,
      "total_records": 2
    }
  }
}
```

| Name | Type | Description |
| --- | --- | --- |
| status | string | Outcome of the request. Possible values: `success` , `error` . |
| data | array | Array of IPO objects matching the filter criteria. |
| data[].id | string | Unique identifier for the IPO (e.g., `hero-fincorp-ipo` ). Use this as the `{id}` path parameter in [Get IPO Details](https://upstox.com/developer/api-documentation/get-ipo-details) . |
| data[].symbol | string | Stock exchange ticker symbol. |
| data[].name | string | Full name of the IPO. |
| data[].status | string | Current IPO status. Possible values: `open` , `closed` , `listed` , `upcoming` . |
| data[].isin | string | International Securities Identification Number of the company. |
| data[].issue_type | string | Issue type. Possible values: `regular` (mainboard), `sme` . |
| data[].issue_size | number | Total issue size in crores (INR). |
| data[].industry | string | Industry sector of the company. |
| data[].minimum_price | number | Minimum price of the price band (in INR). `0` if not yet announced. |
| data[].maximum_price | number | Maximum price of the price band (in INR). `0` if not yet announced. |
| data[].bidding_start_date | string | Bidding open date in `YYYY-MM-DD` format. |
| data[].bidding_end_date | string | Bidding close date in `YYYY-MM-DD` format. |
| data[].total_subscription | string | Overall subscription multiple as a decimal string (e.g., `"10.0"` means 10x subscribed). |
| meta_data.page.page_number | integer | Current page number returned. |
| meta_data.page.total_pages | integer | Total number of pages available. |
| meta_data.page.records | integer | Number of records in the current page. |
| meta_data.page.total_records | integer | Total number of IPOs matching the filter. |

### Error Codes

| Error code | Description |
| --- | --- |
| UDAPI1219 | **Invalid IPO status** - The provided `status` value is not valid. Allowed values: `open` , `closed` , `listed` , `upcoming` . |
| UDAPI1220 | **Invalid issue type** - The provided `issue_type` value is not valid. Allowed values: `regular` , `sme` . |

---

## Get IPO Details

API to retrieve full details for a specific IPO using its slug identifier. The response includes the price band, lot size, bidding schedule, daily bidding hours, key event timeline, registrar contact information, prospectus URLs, and live subscription data.

To get the `id` for an IPO, first call [Get IPOs](https://upstox.com/developer/api-documentation/get-ipos) and use the `id` field from any item in the response.

### Endpoint

**GET** `https://api.upstox.com/v2/ipos/{id}`

### Path Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| id | Required | string | IPO identifier. Example: `autofurnish-limited-ipo` . Obtain from the `id` field in [Get IPOs](https://upstox.com/developer/api-documentation/get-ipos) . |

### Response

```json
{
  "status": "success",
  "data": {
    "id": "autofurnish-limited-ipo",
    "symbol": "AFLTD",
    "name": "Autofurnish IPO",
    "status": "open",
    "isin": "INE18HI01019",
    "issue_type": "sme",
    "issue_size": 15,
    "industry": "Automobile Two & Three Wheelers",
    "minimum_price": 41,
    "maximum_price": 41,
    "bidding_start_date": "2026-05-21",
    "bidding_end_date": "2026-05-25",
    "daily_start_time": "10:00:00",
    "daily_end_time": "17:00:00",
    "face_value": 10,
    "tick_size": null,
    "lot_size": 3000,
    "minimum_quantity": 6000,
    "cut_off_price": 41,
    "listing_price": null,
    "listing_exchange": "BSE",
    "rhp_url": null,
    "drhp_url": "https://www.bsesme.com/download/325882/SME_IPO%20InPrinciple/DP_Autofurnish_Final_20250930195434.pdf",
    "timeline": {
      "pre_apply_start_date": "2026-05-20",
      "application_start_date": "2026-05-21",
      "application_end_date": "2026-05-25",
      "allotment_start_date": "2026-05-26",
      "allotment_date": "2026-05-27",
      "refund_initiation_date": "2026-05-27",
      "listing_date": "2026-05-29",
      "mandate_end_date": "2026-07-06"
    },
    "registrar_info": {
      "name": "SKYLINE FINANCIAL SERVICES PRIVATE LIMITED",
      "email": "virenr@skylinerta.com",
      "contact_name": "Mr. Anuj Rana",
      "contact_number": "+91-11-40450193-97",
      "website": "https://www.skylinerta.com/",
      "registrar": "SKYLINE"
    },
    "total_subscription": "0.68"
  }
}
```

| Name | Type | Description |
| --- | --- | --- |
| status | string | Outcome of the request. Possible values: `success` , `error` . |
| data.id | string | Unique identifier for the IPO. |
| data.symbol | string | Stock exchange ticker symbol. |
| data.name | string | Full name of the IPO. |
| data.status | string | Current IPO status. Possible values: `open` , `closed` , `listed` , `upcoming` . |
| data.isin | string | International Securities Identification Number of the company. |
| data.issue_type | string | Issue type. Possible values: `regular` (mainboard), `sme` . |
| data.issue_size | number | Total issue size in INR crore. |
| data.industry | string | Industry sector of the company. |
| data.minimum_price | number | Lower bound of the price band (in INR). `0` if not yet announced. |
| data.maximum_price | number | Upper bound of the price band (in INR). `0` if not yet announced. |
| data.bidding_start_date | string | Bidding open date in `YYYY-MM-DD` format. |
| data.bidding_end_date | string | Bidding close date in `YYYY-MM-DD` format. |
| data.daily_start_time | string | Daily bidding window start time in `HH:MM:SS` format (IST). |
| data.daily_end_time | string | Daily bidding window end time in `HH:MM:SS` format (IST). |
| data.face_value | number | Face value per share (in INR). |
| data.tick_size | number | Minimum price movement increment (in INR). `null` if not applicable. |
| data.lot_size | integer | Number of shares per lot. |
| data.minimum_quantity | integer | Minimum number of shares an investor must apply for. |
| data.cut_off_price | number | Price at which allotment is made. Relevant for retail investors who apply at cut-off. |
| data.listing_price | number | Price at which the stock listed on the exchange (in INR). `null` until listing. |
| data.listing_exchange | string | Exchange(s) where the stock will be listed (e.g., `BSE` , `NSE,BSE` ). |
| data.rhp_url | string | URL to the Red Herring Prospectus (RHP). `null` if not yet available. |
| data.drhp_url | string | URL to the Draft Red Herring Prospectus (DRHP). `null` if not yet available. |
| data.timeline.pre_apply_start_date | string | Date from which pre-applications can be submitted, in `YYYY-MM-DD` format. |
| data.timeline.application_start_date | string | Bidding open date in `YYYY-MM-DD` format. |
| data.timeline.application_end_date | string | Bidding close date in `YYYY-MM-DD` format. |
| data.timeline.allotment_start_date | string | Date on which allotment processing begins, in `YYYY-MM-DD` format. |
| data.timeline.allotment_date | string | Date on which share allotment is finalised, in `YYYY-MM-DD` format. |
| data.timeline.refund_initiation_date | string | Date on which refunds for unallotted applications are initiated, in `YYYY-MM-DD` format. |
| data.timeline.listing_date | string | Stock exchange listing date in `YYYY-MM-DD` format. |
| data.timeline.mandate_end_date | string | Last date for ASBA mandate execution by the bank, in `YYYY-MM-DD` format. |
| data.registrar_info.name | string | Full name of the IPO registrar. |
| data.registrar_info.email | string | Contact email for the registrar. |
| data.registrar_info.contact_name | string | Name of the contact person at the registrar. |
| data.registrar_info.contact_number | string | Contact phone number for the registrar. |
| data.registrar_info.website | string | Website URL of the registrar. |
| data.registrar_info.registrar | string | Short identifier for the registrar. |
| data.total_subscription | string | Overall subscription multiple as a decimal string (e.g., `"10.0"` = 10x subscribed). |

### Error Codes

| Error code | Description |
| --- | --- |
| UDAPI100500 | **IPO data not found for Id** - No IPO found for the provided `id` . Verify the using [Get IPOs](https://upstox.com/developer/api-documentation/get-ipos) . |

---

## Apply IPO

API to submit an IPO application. Each application contains one to three bids and is backed by a UPI mandate that blocks the required amount in the applicant's bank account. Here's how the process works in detail:

**Step 1: Discovering open IPOs**

Call [Get IPOs](https://upstox.com/developer/api-documentation/get-ipos) to list the IPOs currently in the market. Only those with `status` set to `open` accept applications — `upcoming` ones have not started bidding, and `closed` or `listed` ones are past it.

**Step 2: Reading the IPO's bidding rules**

Pass that `id` to [Get IPO Details](https://upstox.com/developer/api-documentation/get-ipo-details) . Every IPO sets its own bidding rules, and an application that violates any of them is rejected, so read these fields before building the payload:

- **lot_size and minimum_quantity:** Bid quantities must be a multiple of lot size and at least minimum quantity.
- **minimum_price, maximum_price and cut_off_price:** The bid price must fall inside the price band or match the cut-off price exactly. Retail applicants commonly bid at cut off price, which means accepting whatever price the IPO is finally allotted at.
- **investors[].category:** The categories this IPO accepts. Applying under a category the IPO does not offer fails validation.
**Step 3: Submitting the application**

Call apply IPO API with `id` , the applicant's UPI ID, the investor category, and one to three bids that satisfy the rules from the previous step. Multiple bids let the applicant spread the application across different price points within the same IPO.

A successful response returns an `order_id` . This confirms the application reached the exchange; it does not mean the money has been blocked yet.

**Step 4: Approving the mandate and tracking the application**

Submission raises a UPI mandate request in the applicant's bank. Until the applicant approves it in their UPI app, the application remains unfunded and carries `payment_status: pending` .

- **Checking status:** Pass the `order_id` to [Get IPO Order Details](https://upstox.com/developer/api-documentation/get-ipo-order-details) for a single application, or use [Get IPO Orders](https://upstox.com/developer/api-documentation/get-ipo-orders) to list all applications for the user.
- **Withdrawing:** Pass the `order_id` to [Cancel IPO Order](https://upstox.com/developer/api-documentation/cancel-ipo-order) to withdraw the application while the IPO is still open.

### Endpoint

**POST** `https://api.upstox.com/v2/ipos/orders`

### Request Body

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| id | Required | string | IPO identifier. Obtain from the `id` field in [Get IPOs](https://upstox.com/developer/api-documentation/get-ipos) or [Get IPO Details](https://upstox.com/developer/api-documentation/get-ipo-details) . |
| upi | Required | string | UPI ID against which the mandate is raised and the application amount is blocked. |
| category | Required | string | Investor category to apply under. Possible values: `IND` (individual), `HNI` . Must be a category the IPO accepts — see `investors[].category` in [Get IPO Details](https://upstox.com/developer/api-documentation/get-ipo-details) . |
| bids | Required | array | Bids submitted with the application. One to three bids are allowed. |
| bids[].quantity | Required | integer | Number of shares bid for. Must be a multiple of `lot_size` and at least `minimum_quantity` . |
| bids[].price | Required | number | Bid price per share (in INR). Must fall within the `minimum_price` – `maximum_price` band, or equal `cut_off_price` . |

### Bid validation

Both bid fields are validated against the IPO's own parameters, so read them from [Get IPO Details](https://upstox.com/developer/api-documentation/get-ipo-details) before building the payload.

| Constraint | Rule |
| --- | --- |
| Quantity | A multiple of `lot_size` , and greater than or equal to `minimum_quantity` . |
| Price | Within the `minimum_price` – `maximum_price` band, or exactly `cut_off_price` . |
| Bid count | One to three bids per application. |

For an IPO with lot size 20, minimum quantity 20, a price band of ₹366–₹385, and a cut off price of ₹385:

| Bid | Valid | Reason |
| --- | --- | --- |
| quantity: 20, price: 385 | Yes | One lot at the cut-off price. |
| quantity: 40, price: 370 | Yes | Two lots at a price inside the band. |
| quantity: 30, price: 380 | No | 30 is not a multiple of lot_size 20. |
| quantity: 20, price: 350 | No | 350 is below minimum_price. |

A successful response means the application reached the exchange, not that it is funded. The applicant must approve the mandate request in their UPI app before `timeline.mandate_end_date` from [Get IPO Details](https://upstox.com/developer/api-documentation/get-ipo-details) . Until then the application stays at `payment_status: pending` . Track it with [Get IPO Orders](https://upstox.com/developer/api-documentation/get-ipo-orders) .

### Response

```json
{
  "status": "success",
  "data": {
    "order_id": "UPCHK500000020"
  }
}
```

| Name | Type | Description |
| --- | --- | --- |
| status | string | Outcome of the request. Possible values: `success` , `error` , `partial_success` . |
| data.order_id | string | Application ID created for this IPO application. Pass it as the `order_id` path parameter to [Get IPO Order Details](https://upstox.com/developer/api-documentation/get-ipo-order-details) and [Cancel IPO Order](https://upstox.com/developer/api-documentation/cancel-ipo-order) . |

### Error Codes

| Error code | Description |
| --- | --- |
| UDAPI1226 | **id is required** - Provide the IPO identifier in the `id` field. Obtain it from [Get IPOs](https://upstox.com/developer/api-documentation/get-ipos) or [Get IPO Details](https://upstox.com/developer/api-documentation/get-ipo-details) . |
| UDAPI1227 | **upi is required** - Provide the UPI ID against which the mandate is raised. |
| UDAPI1228 | **category is required** - Provide the investor category to apply under. |
| UDAPI1229 | **Invalid category. Allowed values: IND, HNI** - The supplied `category` is not recognized. |
| UDAPI1231 | **At least one bid is required** - The `bids` array must contain at least one bid. |
| UDAPI1232 | **Bid quantity is required** - Each bid must specify a `quantity` . |
| UDAPI1233 | **Bid price is required** - Each bid must specify a `price` . |
| UDAPI1235 | **A maximum of three bids is allowed** - The `bids` array contains more than three bids. |
| UDAPI1236 | **Invalid UPI id** - The supplied `upi` is not a valid UPI ID. |

---

## Get IPO Orders

API to retrieve IPO applications ordered newest first. Each record contains the submitted bids, the status of the UPI mandate backing the application, the exchange submission timestamps, and the allotment outcome once available. To read a single application by its ID, use the [Get IPO Order Details](https://upstox.com/developer/api-documentation/get-ipo-order-details)

### Endpoint

**GET** `https://api.upstox.com/v2/ipos/orders`

### Application status

The status field tracks the lifecycle stage of the application.

| Status | Description |
| --- | --- |
| awaiting_mandate | The application reached the exchange and is waiting for the applicant to approve the UPI mandate. |
| ipo_allotted | Allotment completed and shares were allotted. Check `units_allotted` for the quantity. |
| ipo_not_allotted | Allotment completed and no shares were allotted. The blocked amount is released. |
| application_deleted | The application was cancelled, either by the user through [Cancel IPO Order](https://upstox.com/developer/api-documentation/cancel-ipo-order) or by the exchange. |

### Order status

The order_status field records the outcome of the application.

| Order status | Description |
| --- | --- |
| scheduled | The application is waiting for the applicant to approve the UPI mandate or it is not yet confirmed with the exchange. |
| success | The application was accepted by the exchange. Allotment has not been processed yet. |
| allotted | Shares were allotted against this application. |
| not_allotted | No shares were allotted against this application. |

### Payment status

The payment_status field reflects the state of the UPI mandate that blocks the application amount.

| Payment status | Description |
| --- | --- |
| pending | The mandate request has been raised and is awaiting approval in the applicant's UPI app. |
| mandate_accepted | The mandate was approved and the application amount is blocked in the bank account. |

The status, order_status, and payment_status fields are returned as free-form strings rather than fixed enums. The values above are the ones currently returned; handle unrecognised values gracefully.

### Query Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| page_number | Optional | integer | Page number for pagination, starting at `1` . Default: `1` . |
| records | Optional | integer | Number of application records to return per page. Default: `10` . Maximum: `30` . |

### Response

```json
{
  "status": "success",
  "data": [
    {
      "id": "mandb-engineering-limited-ipo",
      "symbol": "MANDB",
      "exchange": "nse",
      "order_id": "UPCHK500000020",
      "status": "awaiting_mandate",
      "order_status": "success",
      "payment_status": "pending",
      "category": "IND",
      "issue_type": "regular",
      "reason": null,
      "upi": "91xxxxxxxx@ybl",
      "upi_amount_blocked": "0",
      "nse_submitted_date": "2026-08-10T10:14:20",
      "bse_submitted_date": null,
      "mandate_approved_date": null,
      "rejection_date": null,
      "mandate_rejection_date": null,
      "cancel_requested_date": null,
      "cancel_accepted_date": null,
      "units_allotted": 0,
      "bids": [
        {
          "quantity": 20,
          "price": 385,
          "amount": 7700,
          "message": null
        }
      ],
      "created_at": "2026-08-10T10:14:18",
      "last_updated_at": "2026-08-10T10:14:20"
    },
    {
      "id": "deepak-builders-engineers-india-ipo",
      "symbol": "DBEIL",
      "exchange": "nse",
      "order_id": "UPROYAL00000003",
      "status": "ipo_allotted",
      "order_status": "allotted",
      "payment_status": "mandate_accepted",
      "category": "IND",
      "issue_type": "regular",
      "reason": "alloted",
      "upi": "91xxxxxxxx@ybl",
      "upi_amount_blocked": "14819",
      "nse_submitted_date": "2026-07-21T08:14:20",
      "bse_submitted_date": "2026-07-21T08:14:20",
      "mandate_approved_date": "2026-07-21T09:02:11",
      "rejection_date": null,
      "mandate_rejection_date": null,
      "cancel_requested_date": null,
      "cancel_accepted_date": null,
      "units_allotted": 73,
      "bids": [
        {
          "quantity": 30,
          "price": 150.3,
          "amount": 4509,
          "message": "Bid accepted"
        }
      ],
      "created_at": "2026-07-21T08:14:18",
      "last_updated_at": "2026-07-30T17:36:36"
    }
  ],
  "meta_data": {
    "page": {
      "page_number": 1,
      "total_pages": 1,
      "records": 2,
      "total_records": 2
    }
  }
}
```

| Name | Type | Description |
| --- | --- | --- |
| status | string | Outcome of the request. Possible values: `success` , `error` , `partial_success` . |
| data | array | IPO applications belonging to the authenticated user. |
| data[].id | string | Identifier of the IPO the application was placed against. Pass it to [Get IPO Details](https://upstox.com/developer/api-documentation/get-ipo-details) . |
| data[].symbol | string | Stock exchange ticker symbol of the issuer. |
| data[].exchange | string | Exchange the application was submitted to. |
| data[].order_id | string | Application ID. Pass it as the `order_id` path parameter to [Get IPO Order Details](https://upstox.com/developer/api-documentation/get-ipo-order-details) and [Cancel IPO Order](https://upstox.com/developer/api-documentation/cancel-ipo-order) . |
| data[].status | string | Lifecycle stage of the application. See Application status . |
| data[].order_status | string | Outcome of the application. See Order status . |
| data[].payment_status | string | State of the UPI mandate backing the application. See Payment status . |
| data[].category | string | Investor category the application was placed under. `IND` (individual) and `HNI` can be applied for; `EMP` appears on employee-quota applications. |
| data[].issue_type | string | Issue type of the IPO. Possible values: `regular` (mainboard), `sme` . |
| data[].reason | string | Free-text reason from the exchange or registrar explaining the current status. `null` when none was returned. |
| data[].upi | string | UPI ID the mandate was raised against. |
| data[].upi_amount_blocked | string | Amount blocked in the applicant's bank account for this application (in INR), returned as a string. `"0"` until the mandate is approved. |
| data[].nse_submitted_date | string | Timestamp of submission to NSE in `YYYY-MM-DDTHH:MM:SS` format. `null` if not submitted there. |
| data[].bse_submitted_date | string | Timestamp of submission to BSE in `YYYY-MM-DDTHH:MM:SS` format. `null` if not submitted there. |
| data[].mandate_approved_date | string | Timestamp at which the UPI mandate was approved. `null` until approved. |
| data[].rejection_date | string | Timestamp at which the application was rejected. `null` unless rejected. |
| data[].mandate_rejection_date | string | Timestamp at which the UPI mandate was rejected. `null` unless rejected. |
| data[].cancel_requested_date | string | Timestamp at which cancellation was requested. `null` unless a cancellation was raised. |
| data[].cancel_accepted_date | string | Timestamp at which the cancellation completed. `null` unless the cancellation was accepted. |
| data[].units_allotted | integer | Number of shares allotted. `0` until allotment completes, and on applications that were not allotted. |
| data[].bids | array | Bids submitted with this application. |
| data[].bids[].quantity | integer | Number of shares bid for. |
| data[].bids[].price | number | Bid price per share (in INR). |
| data[].bids[].amount | number | Value of the bid (in INR), calculated as quantity × price. |
| data[].bids[].message | string | Message returned by the exchange for this bid. `null` when none was returned. |
| data[].created_at | string | Timestamp at which the application was created, in `YYYY-MM-DDTHH:MM:SS` format. |
| data[].last_updated_at | string | Timestamp at which the application was last updated, in `YYYY-MM-DDTHH:MM:SS` format. |
| meta_data.page.page_number | integer | Current page number returned. |
| meta_data.page.total_pages | integer | Total number of pages available. |
| meta_data.page.records | integer | Number of records in the current page. |
| meta_data.page.total_records | integer | Total number of applications on the account. |

---

## Get IPO Order Details

API to retrieve a single IPO application by its application ID. The response contains the same fields as [Get IPO Orders](https://upstox.com/developer/api-documentation/get-ipo-orders) , returned as a single object instead of a paginated array.

Use this endpoint to poll one application after applying for ipo — for example, to confirm that `payment_status` has moved to `mandate_accepted` once the applicant approves the UPI mandate.

For the meaning of the `status` , `order_status` , and `payment_status` values, see the status tables on [Get IPO Orders](https://upstox.com/developer/api-documentation/get-ipo-orders) .

### Endpoint

**GET** `https://api.upstox.com/v2/ipos/orders/{order_id}`

### Path Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| order_id | Required | string | IPO application ID. Obtain it from `data.order_id` in [Apply IPO](https://upstox.com/developer/api-documentation/apply-ipo) or `data[].order_id` in [Get IPO Orders](https://upstox.com/developer/api-documentation/get-ipo-orders) . |

### Response

```json
{
  "status": "success",
  "data": {
    "id": "deepak-builders-engineers-india-ipo",
    "symbol": "DBEIL",
    "exchange": "nse",
    "order_id": "UPROYAL00000003",
    "status": "ipo_allotted",
    "order_status": "allotted",
    "payment_status": "mandate_accepted",
    "category": "IND",
    "issue_type": "regular",
    "reason": "alloted",
    "upi": "91xxxxxxxx@ybl",
    "upi_amount_blocked": "14819",
    "nse_submitted_date": "2026-07-21T08:14:20",
    "bse_submitted_date": "2026-07-21T08:14:20",
    "mandate_approved_date": "2026-07-21T09:02:11",
    "rejection_date": null,
    "mandate_rejection_date": null,
    "cancel_requested_date": null,
    "cancel_accepted_date": null,
    "units_allotted": 73,
    "bids": [
      {
        "quantity": 30,
        "price": 150.3,
        "amount": 4509,
        "message": "Bid accepted"
      }
    ],
    "created_at": "2026-07-21T08:14:18",
    "last_updated_at": "2026-07-30T17:36:36"
  }
}
```

| Name | Type | Description |
| --- | --- | --- |
| status | string | Outcome of the request. Possible values: `success` , `error` , `partial_success` . |
| data.id | string | Identifier of the IPO the application was placed against. Pass it to [Get IPO Details](https://upstox.com/developer/api-documentation/get-ipo-details) . |
| data.symbol | string | Stock exchange ticker symbol of the issuer. |
| data.exchange | string | Exchange the application was submitted to. |
| data.order_id | string | Application ID. Pass it as the `order_id` path parameter to [Cancel IPO Order](https://upstox.com/developer/api-documentation/cancel-ipo-order) . |
| data.status | string | Lifecycle stage of the application. See [Application status](https://upstox.com/developer/api-documentation/get-ipo-orders#application-status) . |
| data.order_status | string | Outcome of the application. See [Order status](https://upstox.com/developer/api-documentation/get-ipo-orders#order-status) . |
| data.payment_status | string | State of the UPI mandate backing the application. See [Payment status](https://upstox.com/developer/api-documentation/get-ipo-orders#payment-status) . |
| data.category | string | Investor category the application was placed under. `IND` (individual) and `HNI` can be applied for; `EMP` appears on employee-quota applications. |
| data.issue_type | string | Issue type of the IPO. Possible values: `regular` (mainboard), `sme` . |
| data.reason | string | Free-text reason from the exchange or registrar explaining the current status. `null` when none was returned. |
| data.upi | string | UPI ID the mandate was raised against. |
| data.upi_amount_blocked | string | Amount blocked in the applicant's bank account for this application (in INR), returned as a string. `"0"` until the mandate is approved. |
| data.nse_submitted_date | string | Timestamp of submission to NSE in `YYYY-MM-DDTHH:MM:SS` format. `null` if not submitted there. |
| data.bse_submitted_date | string | Timestamp of submission to BSE in `YYYY-MM-DDTHH:MM:SS` format. `null` if not submitted there. |
| data.mandate_approved_date | string | Timestamp at which the UPI mandate was approved. `null` until approved. |
| data.rejection_date | string | Timestamp at which the application was rejected. `null` unless rejected. |
| data.mandate_rejection_date | string | Timestamp at which the UPI mandate was rejected. `null` unless rejected. |
| data.cancel_requested_date | string | Timestamp at which cancellation was requested. `null` unless a cancellation was raised. |
| data.cancel_accepted_date | string | Timestamp at which the cancellation completed. `null` unless the cancellation was accepted. |
| data.units_allotted | integer | Number of shares allotted. `0` until allotment completes, and on applications that were not allotted. |
| data.bids | array | Bids submitted with this application. |
| data.bids[].quantity | integer | Number of shares bid for. |
| data.bids[].price | number | Bid price per share (in INR). |
| data.bids[].amount | number | Value of the bid (in INR), calculated as quantity × price. |
| data.bids[].message | string | Message returned by the exchange for this bid. `null` when none was returned. |
| data.created_at | string | Timestamp at which the application was created, in `YYYY-MM-DDTHH:MM:SS` format. |
| data.last_updated_at | string | Timestamp at which the application was last updated, in `YYYY-MM-DDTHH:MM:SS` format. |

### Error Codes

| Error code | Description |
| --- | --- |
| UDAPI1226 | **id is required** - The application ID is missing from the request. Obtain it from [Get IPO Orders](https://upstox.com/developer/api-documentation/get-ipo-orders) or the [Apply IPO](https://upstox.com/developer/api-documentation/apply-ipo) response. |

---

## Cancel IPO Order

API to withdraw an IPO application. Identify the application by its `order_id` in the path — [Apply IPO](https://upstox.com/developer/api-documentation/apply-ipo) returns it in the response, and you can also read it from [Get IPO Orders](https://upstox.com/developer/api-documentation/get-ipo-orders) or [Get IPO Order Details](https://upstox.com/developer/api-documentation/get-ipo-order-details) .

Once the cancellation is accepted, the application reports `status: application_deleted` on [Get IPO Order Details](https://upstox.com/developer/api-documentation/get-ipo-order-details) , with `cancel_requested_date` and `cancel_accepted_date` populated.

An application can only be withdrawn while the issue is still accepting bids. Once the bidding window closes — see `bidding_end_date` in [Get IPO Details](https://upstox.com/developer/api-documentation/get-ipo-details) — the exchange no longer accepts withdrawal requests and the application proceeds to allotment.

### Endpoint

**DELETE** `https://api.upstox.com/v2/ipos/orders/{order_id}`

### Path Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| order_id | Required | string | IPO application ID. Obtain it from `data.order_id` in [Apply IPO](https://upstox.com/developer/api-documentation/apply-ipo) or `data[].order_id` in [Get IPO Orders](https://upstox.com/developer/api-documentation/get-ipo-orders) . |

### Response

```json
{
  "status": "success",
  "data": {
    "order_id": "UPROYAL00000003",
    "status": "Application cancelled successfully"
  }
}
```

| Name | Type | Description |
| --- | --- | --- |
| status | string | Outcome of the request. Possible values: `success` , `error` , `partial_success` . |
| data.order_id | string | Application ID that was cancelled. |
| data.status | string | Free-text message returned by the IPO service for the cancellation request. Treat it as a display message, not a fixed value — check `status` on [Get IPO Order Details](https://upstox.com/developer/api-documentation/get-ipo-order-details) to confirm the application reached `application_deleted` . |

### Error Codes

| Error code | Description |
| --- | --- |
| UDAPI1226 | **id is required** - The application ID is missing from the request. Obtain it from [Get IPO Orders](https://upstox.com/developer/api-documentation/get-ipo-orders) or the [Apply IPO](https://upstox.com/developer/api-documentation/apply-ipo) response. |
