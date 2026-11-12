# Market Hours

Indian stock markets operate within fixed trading sessions. The equity segment trades from 9:15 AM to 3:30 PM IST, Monday to Friday — knowing these windows matters for integrations, since live market data and order placement are only available while a segment is in session.

### Equity (NSE / BSE)

| Session | Timing | Notes |
| --- | --- | --- |
| Block deal window (morning) | 8:45 AM – 9:00 AM | Institutional block deals |
| Pre-open — order entry | 9:00 AM – 9:08 AM | Orders can be placed, modified, and cancelled; no matching. Order entry may close randomly in the last minute. |
| Pre-open — order matching | 9:08 AM – 9:12 AM | Equilibrium (opening) price discovery; no new orders |
| Pre-open — buffer | 9:12 AM – 9:15 AM | Transition to normal market |
| **Normal market** | **9:15 AM – 3:30 PM** | Continuous trading |
| Closing price calculation | 3:30 PM – 3:40 PM | Closing price computed as the volume-weighted average of the last 30 minutes of trading |
| Post-close session | 3:40 PM – 4:00 PM | Market orders only, executed at the closing price |
| Block deal window (afternoon) | 2:05 PM – 2:20 PM | Institutional block deals |

### Equity Derivatives (NSE/BSE F&O)

| Session | Timing |
| --- | --- |
| Normal market | 9:15 AM – 3:30 PM |

### Currency Derivatives

| Session | Timing |
| --- | --- |
| Normal market | 9:00 AM – 5:00 PM |

### Commodity Derivatives (MCX)

| Segment | Timing |
| --- | --- |
| All segments — open | 9:00 AM |
| Agri commodities — close | 5:00 PM |
| Non-agri / internationally linked commodities — close | 11:30 PM (during US daylight saving, roughly Mar–Nov) / 11:55 PM (roughly Nov–Mar) |

### Special Sessions and Holidays

- **Muhurat trading** — a special one-hour session held on Diwali; timings are announced by the exchanges each year.
- **Exchange holidays** — trading and live streaming are unavailable on published exchange holidays. Refer to the official NSE/BSE/MCX holiday calendars.
- **Special/mock sessions** — exchanges occasionally announce shortened, extended, or mock trading sessions by circular.

**Note:** For API integrations
Outside market hours, streaming subscriptions succeed but deliver no live ticks; snapshot subscriptions return the last available data. Check `marketStatus` per exchange segment rather than hard-coding session times, since exchanges revise timings by circular.
