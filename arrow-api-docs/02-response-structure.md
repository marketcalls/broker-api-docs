> Source: https://docs.arrow.trade/rest-api/response-structure/

# API Response Structure

All API endpoints in our system follow a consistent response format to ensure predictable integration and error handling. This standardized approach helps developers understand and process responses efficiently across all endpoints.

## Overview

Every API response will be one of two types:

  * **Success Response** \- When the request is processed successfully
  * **Error Response** \- When the request fails due to validation, server errors, or other issues

## Response Types

### Successful Response

When an API call executes successfully, the response follows this structure:

**Successful Response Format**

```json
{
    "status": "success",
    "data": {
        // Response payload varies by endpoint
    }
}
```

**Field Descriptions:**

Field | Type | Description
---|---|---
`status` | string | Always `"success"` for successful requests
`data` | object | Contains the actual response data (structure varies by endpoint)

#### Example Success Response

**Example: User Profile Response**

```json
{
    "data": {

        "email": "abhishek.***********@gmail.com",
        "exchanges": [
            "NFO",
            "NSE",
            "BSE",
            "BFO",
            "MCX",
            "NSECO"
        ],
        "id": "AJ0001",
        "name": "ABHISHEK JAIN",
        "products": [
            "NRML",
            "MIS",
            "CNC",
            "CO",
            "BO",
            "MTF"
        ],
        ...
    },
    "status": "success"

}
```

### Failed Response

When an API call fails, the response includes error details to help with debugging and user feedback:

**Error Response Format**

```json
{
 {
    "message": "Human Readable Error Message",
    "status": "failure",
    "errorCode": <ERROR_CODE>,
    "errorData": "More Information about the Error"
}
}
```

**Field Descriptions:**

Field | Type | Description
---|---|---
`message` | string | Human-readable error message explaining what went wrong
`status` | string | Always `"failed"` for failed requests
`errorCode` | string | Standardized error code for programmatic error handling

#### Example Error Response

**Example: Validation Error**

```json
{

    "message": "invalid password",
    "status": "failure",
    "errorCode": 400,
}
```

Error Codes Reference

For a complete list of possible error codes and their meanings, see the [Error Codes Documentation](/documentation/error_codes#list-of-possible-error-codes).

## Data Types

The API responses use standard JSON data types with specific formatting conventions:

### Primitive Types

Type | Description | Example Values
---|---|---
**integer** | Whole numbers | `6`, `1`, `7`, `4`, `-10`
**float** | Decimal numbers | `1.729`, `3.14159`, `0.5`
**boolean** | True/false values | `true`, `false`
**string** | Text values | `"Hello World"`, `"API_KEY_123"`

### Formatted Types

Type | Format | Description | Example
---|---|---|---
**Timestamp** | `yyyy-mm-dd hh:mm:ss` | Date and time in 24-hour format | `"2023-01-31 09:30:00"`
**Date** | `yyyy-mm-dd` | Date only | `"2023-01-31"`

### Complex Types

Type | Description | Example
---|---|---
**Array** | List of values | `[1, 2, 3]`, `["apple", "banana"]`
**Object** | Nested JSON structure | `{"name": "John", "age": 30}`
**null** | Represents absence of value | `null`

## Best Practices

### For API Consumers

  1. **Always check the`status` field** before processing the `data` field
  2. **Handle error responses gracefully** by checking both the `message` and `errorCode`
  3. **Implement proper error logging** using the `errorCode` for categorization
  4. **Parse timestamps consistently** using the specified format
  5. **Validate data types** when processing the response data
