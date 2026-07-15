# Static IPs and Algo App

## Overview

When placing orders through an Algo App, pass the configured **Algo Name** in the `X-Algo-Name` request header.

## Key Features

### IP Configuration
- Each user can configure 2 IPs: Primary and Secondary
- Orders accepted only from registered IP addresses
- IPs can be updated once weekly; existing tokens invalidate upon change

### Algo ID Setup
- Optional when creating/editing apps
- Add key-value pairs for Algo Name and exchange-approved Algo ID
- Multiple Algo IDs per app
- Pass only **Algo Name** in `X-Algo-Name` header (not the ID)

## Important Rules

- Changing an Algo ID resets status to _In Review_ and revokes tokens
- Rejected Algo IDs result in token revocation
- Orders fail if `X-Algo-Name` header is missing or doesn't match configured values
- New Algo IDs start as **In Review**, become **Approved** after verification
- Access tokens generate only after approval
