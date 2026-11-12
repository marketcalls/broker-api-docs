# Errors

> Source: https://docs.delta.exchange/#errors

Delta API uses the following error codes:

| Error Code | Meaning                                                                                   |
| ---------- | ----------------------------------------------------------------------------------------- |
| 400        | Bad Request -- Your request is invalid.                                                   |
| 401        | Unauthorized -- Your API key/Signature is wrong.                                          |
| 403        | Forbidden Error -- Request blocked by CDN (e.g., missing User-Agent header or hidden/blocked IP from certain hosted environments).                                          |
| 404        | Not Found -- The specified resource could not be found.                                     |
| 405        | Method Not Allowed -- You tried to access a resource with an invalid method.                |
| 406        | Not Acceptable -- You requested a format that isn't json.                                 |  |  |
| 429        | Too Many Requests -- You have exhausted your rate limits! Slow down!                      |
| 500        | Internal Server Error -- We had a problem with our server. Try again later.               |
| 503        | Service Unavailable -- We're temporarily offline for maintenance. Please try again later. |
