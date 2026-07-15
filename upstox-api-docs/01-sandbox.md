# Sandbox APIs

Upstox provides a sandbox environment that mimics the live API experience, enabling developers to test trading applications comprehensively without real market risk or costs.

## Key Features

- Fully integrate and test applications end-to-end on the payload before connecting to the live market
- Test strategies without time restrictions (unlike live markets)
- Execute comprehensive testing at no cost

## Setup Instructions

### Creating a Sandbox App

1. Navigate to the [Upstox Developer Apps](https://account.upstox.com/developer/apps#sandbox) page
2. Click "New Sandbox App" to begin the creation form
3. Complete required fields (note: redirect and postback URLs are currently non-functional but recommended for future compatibility)
4. Click "Continue" to finalize app creation

### Generating Access Token

1. Access your newly created sandbox app
2. Click the "Generate" button
3. Copy the displayed token (valid for 30 days)
4. Use this token for sandbox API authentication

## Important Limitations

- Only one sandbox app permitted per user
- Sandbox tokens are exclusively for testing; they cannot execute live transactions

## Available Sandbox-Enabled APIs

The following endpoints support sandbox testing:

- Place Order
- Place Order V3
- Place Multi Order
- Modify Order
- Modify Order V3
- Cancel Order
- Cancel Order V3

Developers should regularly check documentation for additional sandbox APIs as the feature rolls out incrementally.
