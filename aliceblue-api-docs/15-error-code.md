# Error Code

> Source: https://v2api.aliceblueonline.com/Error%20Code/

## Error Codes

| S.No | Error Codes | Description |
| --- | --- | --- |
| 1 | EC003 | An error occurred. Please try again later. |
| 2 | EC900 | 'exchange' cannot be empty or null. |
| 3 | EC901 | 'exchange' should be one of the following values: { 'NSE', 'BSE', 'MCX', 'NFO', 'BFO', 'CDS', 'BCD'}. |
| 4 | EC902 | 'tradingSymbol' cannot be empty or null. |
| 5 | EC903 | 'quantity' cannot be empty or null. |
| 6 | EC904 | 'quantity' should be a positive number. |
| 7 | EC906 | 'product' cannot be empty or null. |
| 8 | EC907 | 'transactionType' cannot be empty or null. |
| 9 | EC908 | 'token' cannot be empty or null. |
| 10 | EC909 | 'disclosedQty' cannot be empty or null. |
| 11 | EC910 | 'price' cannot be empty or null. |
| 12 | EC911 | 'triggerPrice' cannot be empty or null. |
| 13 | EC912 | Failed to place the order. |
| 14 | EC913 | Failed to retrieve user details. |
| 15 | EC914 | 'Request parameter' cannot be empty or null. |
| 16 | EC915 | Failed to retrieve the order book. |
| 17 | EC916 | No orders found for this user. |
| 18 | EC917 | Failed to retrieve order history. |
| 19 | EC918 | No order history found for the given order ID. |
| 20 | EC919 | Failed to retrieve the position book. |
| 21 | EC920 | No positions found for this user. |
| 22 | EC921 | Failed to retrieve holdings. |
| 23 | EC922 | No holdings found for this user. |
| 24 | EC923 | Failed to retrieve profile details. |
| 25 | EC924 | Failed to retrieve RMS limits. |
| 26 | EC925 | 'nestOrderNo' cannot be empty or null. |
| 27 | EC926 | No trades found for this user. |
| 28 | EC927 | Failed to retrieve the trade book. |
| 29 | EC929 | 'transactionType' should be one of the following values: {'BUY', 'SELL'}. |
| 30 | EC930 | 'orderType' should be one of the following values: {'LIMIT', 'MARKET', 'SL', 'SLM'}. |
| 31 | EC932 | 'validity' should be one of the following values: {'DAY', 'IOC'}. |
| 32 | EC933 | 'priceType' cannot be empty or null. |
| 33 | EC934 | 'orderType' cannot be empty or null. |
| 34 | EC935 | Failed to retrieve the single order margin. |
| 35 | EC936 | 'product' cannot be empty or null. |
| 36 | EC937 | Failed to cancel all orders. |
| 37 | EC938 | No open orders to cancel from the order book. |
| 38 | EC939 | Failed to retrieve the span margin. |
| 39 | EC941 | 'instrumentId' cannot be empty or null. |
| 40 | EC942 | 'orderComplexity' cannot be empty or null. |
| 41 | EC944 | 'validity' cannot be empty or null. |
| 42 | EC945 | 'brokerOrderId' cannot be empty or null. |
| 43 | EC946 | Invalid 'instrumentId'. It must contain only numeric characters. |
| 44 | EC947 | 'instrumentId' does not exist. |
| 45 | EC948 | 'quantity' cannot exceed 50,000,000. |
| 46 | EC949 | 'quantity' should be a positive number. |
| 47 | EC950 | 'price' is required and cannot be empty or null. |
| 48 | EC951 | 'slTriggerPrice' is required and cannot be empty or null. |
| 49 | EC953 | 'targetPrice' is required and cannot be empty or null. |
| 50 | EC954 | 'quantity' should be a multiple of the lot size. |
| 51 | EC957 | Invalid 'price'. |
| 52 | EC958 | 'price' cannot be zero or negative. |
| 53 | EC959 | Invalid 'slTriggerPrice'. |
| 54 | EC960 | 'slTriggerPrice' cannot be zero or negative. |
| 55 | EC962 | 'stopLossPrice' cannot be zero or negative. |
| 56 | EC963 | Invalid 'targetPrice'. |
| 57 | EC964 | 'targetPrice' cannot be zero or negative. |
| 58 | EC966 | 'trailingSlAmount' cannot be empty or null for SL order type. |
| 59 | EC967 | 'trailingSlAmount' should be a positive number. |
| 60 | EC968 | 'trailingSlAmount' cannot be zero or negative. |
| 61 | EC969 | 'Product' should be either 'NORMAL' or 'INTRADAY'. |
| 62 | EC970 | 'disclosedQuantity' is not applicable for this segment. |
| 63 | EC971 | 'orderTag' should not exceed 50 characters |
| 64 | EC972 | 'algoId' should not exceed 12 characters. |
| 65 | EC973 | For a buy order, 'slTriggerPrice' should be less than the 'price'. |
| 66 | EC974 | For a sell order, 'slTriggerPrice' should be greater than the 'price'. |
| 67 | EC975 | 'disclosedQuantity' cannot exceed the total order 'quantity'. |
| 68 | EC979 | Invalid 'brokerOrderId'. |
| 69 | EC980 | Invalid 'instrumentId'. |
| 70 | EC981 | Invalid 'disclosedQty'. |
| 71 | EC982 | For 'AMO', 'disclosedQuantity' should be zero. |
| 72 | EC983 | Invalid 'algoId'. |
| 73 | EC984 | Invalid 'orderTag'. |
| 74 | EC986 | SpanMargin is not allowed for 'NSEEQ' and 'BSEEQ'. |
| 75 | EC988 | 'marketProtection' should be a positive number. |
| 76 | EC990 | 'quantity' should be a multiple of the lot size. |
| 77 | EC991 | 'disclosedQuantity' should be a multiple of the lot size. |
| 78 | EC992 | Unable to modify the given order. 'brokerOrderId' is invalid. |
| 79 | EC993 | Provided 'brokerOrderId' is not in a valid state to modify the order. |
| 80 | EC994 | The given 'brokerOrderId' is not in your order book. |
| 81 | EC996 | 'validity' of IOC is not allowed for AMO orders. |
| 82 | EC997 | The specified order is not available in the order book and cannot be canceled. Please verify the order details and try again. |
| 83 | EC998 | The specified order is not available in the order book, and order history cannot be retrieved. Please verify the order ID and try again. |
| 84 | EC999 | The specified order is not available in the order book and cannot be modified. Please verify the order details and try again. |
| 85 | EC801 | Orders with exchange 'BSEEQ/BSEFO/BSECURR' cannot be modified to order type 'SL' (Stop Loss). |
| 86 | EC806 | 'exchange' accepts only {'NSEEQ', 'BSEEQ'}. |
| 87 | EC807 | 'product' - 'NORMAL' is not allowed in cash segment. |
| 88 | EC813 | 'deviceId' cannot exceed 98 characters. |
| 89 | EC814 | 'brokerOrderId' cannot be empty or null. |
| 90 | EC815 | Invalid 'brokerOrderId'. |
| 91 | EC819 | Only the trigger price field can be modified. |
| 92 | EC822 | SL trigger price should be lower than price. |
| 93 | EC823 | SL trigger price should be higher than price. |
| 94 | EC824 | SL trigger price should be %.2f%% below price. |
| 95 | EC825 | SL trigger price should be %.2f%% above price. |
| 96 | EC826 | Please enter a price. |
| 97 | EC827 | Please enter a target price. |
| 98 | EC828 | Please enter an SL trigger price. |
| 99 | EC829 | AMO is not allowed for this product. |
| 100 | EC830 | AMO is not allowed for this order type. |
| 101 | EC831 | AMO is not allowed for this validity. |
| 102 | EC832 | AMO is not allowed for this segment. |
| 103 | EC834 | Market protection cannot be modified. |
| 104 | EC837 | This product is not allowed for this segment. |
| 105 | EC838 | This order type is not allowed. |
| 106 | EC842 | 'disclosedQuantity' should be at least %.2f%% of the total order quantity. |
| 107 | EC843 | Only price and quantity fields can be modified. |
| 108 | EC844 | Only price and order type fields can be modified. |
| 109 | EC846 | SL trigger price should be %.2f%% or %.2f paise below price. |
| 110 | EC847 | SL trigger price should be %.2f%% or %.2f paise above price. |
| 111 | EC848 | Price should be higher than the SL trigger price. |
| 112 | EC849 | Price should be lower than the SL trigger price. |
| 113 | EC850 | Price should be %.2f%% or %.2f paise above the SL trigger price. |
| 114 | EC851 | Price should be %.2f%% or %.2f paise below the SL trigger price. |
| 115 | EC852 | This product is not allowed. |
| 116 | EC855 | Modification is not allowed. |
| 117 | EC856 | SL trigger price should be less than main leg price. |
| 118 | EC857 | SL trigger price should be more than main leg price. |
| 119 | EC858 | Order placement not allowed for this exchange. |
| 120 | EC865 | 'product' - 'Delivery' is not allowed in FnO segment. |
| 121 | EC868 | Position not found for the specified instrument. |
| 122 | EC869 | Insufficient buy quantity available for conversion. |
| 123 | EC870 | Insufficient sell quantity available for conversion. |
| 124 | EC871 | Conversion of overnight BUY positions in options is not allowed. |
| 125 | EC873 | Failed to convert positions. |
| 126 | EC082 | Invalid parameter: 'deviceId' cannot be empty or null. |
| 127 | EC086 | You are a read-only user and are not allowed to place, modify, or cancel orders. |
| 128 | EC087 | Session Expired |
| 129 | EC088 | Single order slicing limit exceeded |
| 130 | EC089 | 'disclosedQuantity' cannot be same the total order 'quantity'. |
| 131 | EC090 | 'exchange' should be one of the following values: { 'NSE', 'BSE', 'MCX', 'NFO', 'BFO'}. |
| 132 | EC091 | 'orderComplexity' should be one of the following values: {'REGULAR', 'AMO'}. |
| 133 | EC092 | 'product' should be one of the following values: {'INTRADAY', 'LONGTERM', 'MTF'}. |
