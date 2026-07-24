# Trading API Error Codes

Errors the trading APIs can throw, returned in `status`/`message` (see [Request and Response Structure](02-request-response-structure.md)). Order-rejection reasons are not API errors and are listed separately in [RMS Order Rejections](14-rms-rejections.md).

| Code | Message |
| --- | --- |
| EC001 | Invalid parameter: `UserIdentity` cannot be empty or null. |
| EC002 | Client does not exist. |
| EC003 | Something went wrong, please try after some time. |
| EC004 | User blocked. |
| EC005 | Invalid parameter: request is null or empty. |
| EC006 | Invalid parameter: `IsPANEntered` cannot be empty or null. |
| EC007 | Invalid parameter: `IsPANEntered` — must be `Y` or `N`. |
| EC008 | Invalid parameter: `UserId` cannot be empty or null. |
| EC009 | Invalid parameter: `Password` cannot be empty or null. |
| EC010 | Invalid parameter: `appName` cannot be empty or null. |
| EC011–EC013 | Multiple client IDs associated with the provided details — specify a client code to proceed. |
| EC014 | Account blocked by administrator (unblock via app won't work). |
| EC015 | Unable to send OTP to the registered mobile/email. |
| EC016 | Invalid userId or password. |
| EC017 | Invalid parameter: `osName` cannot be empty or null. |
| EC018 | OTP already initiated — retry after 60 seconds. |
| EC019 | Maximum OTP request limit exceeded — try again later. |
| EC020 | Unable to send OTP currently — contact the administrator. |
| EC021 | Invalid parameter: `ClientCode` cannot be empty or null. |
| EC022 | Invalid parameter: `ReceivedOTP` cannot be empty or null. |
| EC023 | Invalid parameter: `IsPANEntered` cannot be empty or null. |
| EC024 | OTP expired. |
| EC025 | Invalid OTP. |
| EC026 | Invalid parameter: `userId` cannot be empty or null. |
| EC027 | Invalid parameter: `pan` cannot be empty or null. |
| EC028 | Invalid parameter: `osName` cannot be empty or null. |
| EC029 | Invalid parameter: `dob` cannot be empty or null. |
| EC030 | Invalid user. |
| EC031, EC032 | Invalid PAN. |
| EC033 | Invalid parameter: `otp` cannot be empty or null. |
| EC034 | Invalid parameter: `totp` cannot be empty or null. |
| EC035 | T-OTP already enabled for this account. |
| EC036 | Invalid T-OTP. |
| EC037 | Only MOB keys accepted for this operation. |
| EC038 | Invalid parameter: `token` cannot be empty or null. |
| EC039 | Invalid parameter: `deviceId` cannot be empty or null. |
| EC040 | Invalid parameter: `deviceType` cannot be empty or null. |
| EC041 | Invalid parameter: `enable` cannot be empty or null. |
| EC042 | Generic error. |
| EC043 | T-OTP not enabled for this account. |
| EC044 | Token is not valid. |
| EC045 | Token is valid. |
| EC046 | Invalid parameter: `osName` cannot be empty or null. |
| EC047 | Invalid parameter: `versionNo` cannot be empty or null. |
| EC048 | Invalid parameter: `deviceId` cannot be empty or null. |
| EC049 | Invalid parameter: `deviceName` cannot be empty or null. |
| EC050 | Invalid parameter: `macAddress` cannot be empty or null. |
| EC051 | Only mobile OS clients may call this method. |
| EC052 | Max OTP limit reached — retry after 15 minutes. |
| EC053 | Invalid parameter: `appKey` cannot be empty or null. |
| EC054 | Incorrect `appKey`. |
| EC055 | Unauthorized access — authorize the application to obtain the auth code. |
| EC056 | Invalid parameter: `ceData` cannot be empty or null. |
| EC057 | Invalid parameter: `ceEncData` cannot be empty or null. |
| EC058 | Invalid `deviceId`. |
| EC059 | Invalid `versionNo`. |
| EC060 | Invalid `appName`. |
| EC061 | Invalid `osName`. |
| EC062 | Illegal or expired encryption key. |
| EC063 | `password` must not contain spaces. |
| EC064–EC066 | Multiple client IDs associated with the provided email/mobile/details — specify a client code. |
| EC067 | Provided PAN is not mapped to any client ID. |
| EC068 | Provided userId is not mapped to the given PAN. |
| EC069 | Password expired — change it to continue. |
| EC070 | Invalid parameter: `version` cannot be empty or null. |
| EC071 | Invalid parameter: `os` cannot be empty or null. |
| EC072 | Mobile number/email invalid — contact `cs@iifl.com` to update them. |
| EC073 | `dob` must be in `MMDDYYYY` format. |
| EC074 | Invalid `osName`. |
| EC075 | Unauthorized access. |
| EC076 | Service not available for this account type. |
| EC077, EC078 | Provided PAN is not mapped to the given user ID. |
| EC079 | Password must include a special character from `@ # $ % & * / \` |
| EC080 | Too many incorrect OTP attempts — request a new OTP after 15 minutes. |
| EC081 | Account in a voluntary freeze state — login not permitted; contact the administrator. |
| EC701 | Orders on BSEEQ/BSEFO/BSECURR cannot be modified to order type `SL`. |
| EC702 | Only `price` can be modified on sub-leg orders. |
| EC703–EC705 | Account is dormant — trading not permitted; contact support to reactivate. |
| EC801 | Invalid parameter: `interval` cannot be empty or null. |
| EC802 | Invalid parameter: `interval` — accepts only `1 minute`, `5 minutes`, `10 minutes`, `15 minutes`, `30 minutes`, `60 minutes`, `1 day`. |
| EC803 | Invalid parameter: `fromDate` cannot be empty or null. |
| EC804 | Invalid `fromDate` format — use `DD-MMM-YYYY` (e.g. `20-Sep-2020`). |
| EC805 | Invalid parameter: `toDate` cannot be empty or null. |
| EC806 | Invalid `toDate` format — use `DD-MMM-YYYY` (e.g. `20-Sep-2020`). |
| EC807 | `fromDate` cannot be greater than `toDate`. |
| EC808 | `instrumentId` must be greater than 0. |
| EC809 | Maximum permissible date range exceeded. |
| EC810 | `fromDate` must be less than `toDate`. |
| EC900 | Invalid parameter: `exchange`/`instrumentId` cannot be empty or null. |
| EC901 | Invalid parameter: `exchange` — accepts only `NSEEQ`, `NSEFO`, `BSEEQ`, `BSEFO`, `NSECURR`, `BSECURR`, `MCXCOMM`, `NCDEXCOMM`, `NSECOMM`, `BSECOMM`. |
| EC902 | Invalid parameter: `tradingSymbol` cannot be empty or null. |
| EC903, EC904 | Invalid parameter: `quantity` cannot be empty/null and must be a positive integer. |
| EC905 | Invalid parameter: `retention` cannot be empty or null. |
| EC906 | Invalid parameter: `product` cannot be empty or null. |
| EC907 | Invalid parameter: `transactionType` cannot be empty or null. |
| EC908 | Invalid parameter: `token` cannot be empty or null. |
| EC909 | Invalid parameter: `disclosedQty` cannot be empty or null. |
| EC910 | Invalid parameter: `price` cannot be empty or null. |
| EC911 | Invalid parameter: `triggerPrice` cannot be empty or null. |
| EC912 | Error placing order. |
| EC913 | Error fetching user details. |
| EC914 | Invalid parameter: request parameter cannot be empty or null. |
| EC915, EC916 | Error fetching order book / no orders found for this user. |
| EC917, EC918 | Error fetching order history / no order history found for the given order ID. |
| EC919, EC920 | Error fetching position book / no positions found for this user. |
| EC921, EC922 | Error fetching holdings / no holdings found for this user. |
| EC923 | Error fetching profile details. |
| EC924 | Error fetching RMS limits. |
| EC925 | Invalid parameter: `nestOrderNo` cannot be empty or null. |
| EC926, EC927 | No trades found for this user / error fetching trade book. |
| EC928 | Invalid parameter: `product` — accepts only `NORMAL`, `INTRADAY`, `DELIVERY`, `BNPL`. |
| EC929 | Invalid parameter: `transactionType` — accepts only `BUY`, `SELL`. |
| EC930 | Invalid parameter: `orderType` — accepts only `LIMIT`, `MARKET`, `SL`, `SLM`. |
| EC931 | Invalid parameter: `orderComplexity` — accepts only `REGULAR`, `BO`, `CO`, `MTF`, `AMO`, `BRACKETORDER`, `COVERORDER`, `MUTUALFUND`, `AFTERMARKETORDER`. |
| EC932 | Invalid parameter: `validity` — accepts only `DAY`, `IOC`. |
| EC933, EC934 | Invalid parameter: `priceType`/`orderType` cannot be empty or null. |
| EC935 | Error fetching the single-order margin. |
| EC936 | Invalid parameter: `product` cannot be empty or null. |
| EC937, EC938 | Error cancelling all orders / no open orders to cancel. |
| EC939 | Error fetching the span margin. |
| EC940 | Error logging out. |
| EC941 | Invalid parameter: `instrumentId` cannot be empty or null. |
| EC942, EC943 | Invalid parameter: `orderComplexity` cannot be empty/null; accepts only `REGULAR`, `AMO`, `BO`, `CO`. |
| EC944 | Invalid parameter: `validity` cannot be empty or null. |
| EC945 | Invalid parameter: `brokerOrderId` cannot be empty or null. |
| EC946 | `instrumentId` must contain only numeric characters. |
| EC947 | `instrumentId` does not exist. |
| EC948, EC949 | `quantity` must be a positive integer not exceeding 50,000,000. |
| EC950 | Invalid parameter: `price` is required. |
| EC951 | Invalid parameter: `slTriggerPrice` is required. |
| EC952 | `slLegPrice` cannot be null/empty for BO/CO orders. |
| EC953 | Invalid parameter: `targetLegPrice` is required. |
| EC954 | `quantity` must be a multiple of the lot size. |
| EC955 | Only `INTRADAY` product is allowed for BO/CO orders. |
| EC956 | DELIVERY/BNPL orders are only allowed on NSEEQ/BSEEQ. |
| EC957, EC958 | Invalid `price`; `price` cannot be zero or negative. |
| EC959, EC960 | Invalid `slTriggerPrice`; cannot be zero or negative. |
| EC961, EC962 | Invalid `slLegPrice`; cannot be zero or negative. |
| EC963, EC964 | Invalid `targetLegPrice`; cannot be zero or negative. |
| EC965 | BO orders only allow `LIMIT` or `SL` order type. |
| EC966, EC967, EC968 | `trailingSlAmount` required and must be a positive, non-zero number for `SL` orders. |
| EC969 | `product` only allows `NORMAL` and `INTRADAY`. |
| EC970 | `disclosedQuantity` only allowed for NSEEQ/BSEEQ/MCXCOMM/NSECURR/BSECURR; not applicable for F&O. |
| EC971 | `orderTag` must be ≤ 50 characters. |
| EC972 | `algoId` must be ≤ 12 characters. |
| EC973 | Buy order `slTriggerPrice` must be less than `price`. |
| EC974 | Sell order `slTriggerPrice` must be greater than `price`. |
| EC975 | `disclosedQuantity` cannot exceed total order `quantity`. |
| EC976 | `slLegPrice` cannot be zero or null. |
| EC977 | `slTriggerPrice` only valid for `SL`/`SLM` order types. |
| EC978 | `price` only valid for `LIMIT`/`SL` order types. |
| EC979, EC980, EC985 | Invalid `brokerOrderId` / `instrumentId`. |
| EC981, EC982 | Invalid `disclosedQty`; must be zero for AMO orders. |
| EC983, EC984 | Invalid `algoId` / `orderTag`. |
| EC986 | Span margin not allowed for NSEEQ/BSEEQ. |
| EC987 | Invalid parameter: `exchange` — accepts only NSEFO, BSEFO, NSECURR, BSECURR, MCXCOMM, NCDEXCOMM, NSECOMM, BSECOMM (for this endpoint). |
| EC988 | `marketProtectionPercent` must be a positive number. |
| EC989 | CO orders only allow `LIMIT` or `MARKET` order type. |
| EC990, EC991 | `quantity`/`disclosedQuantity` must be a multiple of the lot size. |
| EC992–EC994 | Order not able to be modified / not in a valid state to modify / not found in the order book. |
| EC995 | No order to cancel. |
| EC996 | `IOC` validity not allowed for AMO orders. |
| EC997 | Order not in the order book — cannot be cancelled. Verify the order details. |
| EC998 | Order not in the order book — history cannot be retrieved. Verify the order ID. |
| EC999 | Order not in the order book — cannot be modified. Verify the order details. |
