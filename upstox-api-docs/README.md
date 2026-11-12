# Upstox API Documentation in Markdown

Complete Upstox Developer API documentation converted to Markdown format for use as context with AI tools like Claude Code, Cursor, GitHub Copilot, and other LLM-powered development assistants.

## What's Included

- **107 Markdown files** covering the entire Upstox API surface
- All REST API endpoints with methods, parameters, request/response formats
- WebSocket streaming documentation (Market Data Feed V3, Portfolio Stream)
- Error codes, rate limits, authentication flows
- Code examples in Python, Node.js, Java, PHP
- Quick reference table of all endpoints

## File Structure

Sections `00`-`25` keep the original per-endpoint split (`13a`, `13b`, ...). Sections `26`+ are single self-contained files, one per API family.

| Prefix | Section |
|--------|---------|
| `00` | Overview |
| `01` | Sandbox |
| `02` | Authentication |
| `03-03c` | API Structure (Request/Response/Error Codes) |
| `04` | Rate Limits |
| `05` | SDK |
| `06` | MCP Integration |
| `07-07b` | Instruments (Files, Search) |
| `08-08d` | Expired Instruments |
| `09-09e` | Login (Authorize, Token, Logout) |
| `10-10c` | User (Profile, Funds/Margin V2 & V3) |
| `11-11a` | Charges (Brokerage) |
| `12-12a` | Margins |
| `13-13n` | Orders (Place, Modify, Cancel, Multi, Exit, Details, Trades) |
| `14-14d` | GTT Orders |
| `15-15d` | Portfolio (Positions, Holdings, Convert) |
| `16-16b` | Trade P&L |
| `17-17d` | Historical Data (V3 and V2) |
| `18-18g` | Market Quotes (Full V2/V3, OHLC, LTP, Greeks) |
| `19-19c` | Market Information (Holidays, Timings, Status) |
| `20-20b` | Option Chain |
| `21-21e` | WebSocket (Market Data, Portfolio Stream, Streamer Functions) |
| `22` | WebSocket Implementation Guide |
| `23` | Webhook |
| `24-24e` | Appendix (incl. Changelog, Instant Withdrawal) |
| `25` | API Endpoints Quick Reference |
| `26` | Kill Switch |
| `27` | Static IP Management |
| `28` | Payments (Payins, Payouts) |
| `29` | IPO (Discovery, Applications) |
| `30` | Mutual Funds (Holdings, Orders, SIPs) |
| `31` | Fundamentals (Financials, Ratios, Corporate Actions) |
| `32` | News |
| `33` | Market Analytics (OI, PCR, Max Pain, FII/DII) |
| `34` | Smartlist (Futures, Options, MTF) |
| `35` | Backtesting |
| `36` | Agent Integration (Quickstart, Agent Skills) |

## Usage with AI Tools

### Claude Code
Add to your `CLAUDE.md`:
```
Reference the Upstox API docs in ./upstox-api-docs/ for API integration context.
```

### Cursor
Add the `upstox-api-docs/` directory to your project and reference it in `.cursorrules`.

## Source

Documentation sourced from [Upstox Developer API](https://upstox.com/developer/api-documentation/open-api).

Snapshot current as of **8 September 2026**. The dated update history is in `24d-appendix-changelog.md`; the upstream feed is at [Announcements](https://upstox.com/developer/api-documentation/announcements).

## License

MIT
