# RMS Order Rejections

All Risk Management System (RMS) rejections start with the string `RMS:` — if a rejection message doesn't start with `RMS:`, it wasn't rejected by RMS. RMS rejection reasons are generated dynamically from block details, rules, and/or the order validation level, so exact text varies.

Rejection message prefixes and how to interpret them:

| Prefix | Meaning |
| --- | --- |
| `RMS:Blocked for ` | Followed by block details |
| `RMS:Rule: ` | Followed by the rule name and order validation level |
| `RMS:Margin Exceeds, Required:<Value>, Available:<Value>` | Followed by the order validation level |
| `RMS:MtoM Exceeds, Required:<Value>, Available:<Value>` | Followed by the order validation level |
| `RMS:Lt rate not found for rule:` | Followed by the rule name and order validation level |
| `RMS:Asset exchange segment not found for rule:` | Asset/segment lookup failed for the rule |
| `RMS:Field Not Found <MNM_ID>` | Required field missing |
| `RMS:Bad Input` | Malformed input |
| `RMS:Scrip Not found in Mrv master` | Scrip missing from the margin/valuation master |
| `RMS:Mrv Master DOWN` | Margin/valuation master unavailable |
| `RMS:User not enabled on product` | User lacks access to the product |
| `RMS:Client not enabled on product` | Client lacks access to the product |
| `RMS:NO Last Trade Price` | No LTP available for the instrument |
| `RMS:Auto Square Off Block` | Blocked due to auto square-off |
| `RMS:Scrip <Symbol> is in Ban Period.` | Scrip is under an exchange ban |
| `RMS:Index value not found` | Index value unavailable |
| `RMS:Index close value not found` | Index close value unavailable |
| `RMS:Entity is not loaded properly` | Entity failed to load |
