# Agent Integration

Upstox ships first-party integrations for AI coding agents, alongside the MCP server documented in the MCP Integration section.

## Claude Plugin Marketplace

As of 7 July 2026 the MCP server and Agent Skill install from a single Claude plugin marketplace:

```
/plugin marketplace add upstox/upstox-plugin-marketplace
```

Then install `upstox-mcp` (read-only account access) or `upstox-skill` (trading workflows). Supported in Claude Code and the Claude desktop and web apps, with no config file or Node.js required for the plugin path.

---

## Agent Quickstart

Get an AI agent talking to your Upstox account in about five minutes. This guide wires up the hosted Upstox MCP server, points your agent at the full documentation set (including a machine-readable `llms.txt` ), adds drop-in rules files so the agent follows Upstox conventions, and covers the guardrails that keep an autonomous agent safe.

### Who this is for

This quickstart is for developers who want an AI coding agent or chat assistant — Claude, Claude Code, ChatGPT, Cursor, or VS Code with GitHub Copilot — to read from and reason about their Upstox account and the Upstox API.

You will get the most out of this guide if you:

- Build with an AI agent and want it grounded in accurate, up-to-date Upstox API knowledge.
- Want conversational, account-scoped access to holdings, orders, positions, and funds.
- Plan to automate research or trading workflows and need the agent to follow Upstox conventions.
If you only need programmatic API access without an AI agent, start with [Authentication](https://upstox.com/developer/api-documentation/authentication) and the official [SDKs](https://upstox.com/developer/api-documentation/sdk) instead.

### Prerequisites

Before you begin, make sure you have:

- An active, non-dormant Upstox trading account. See [Authentication](https://upstox.com/developer/api-documentation/authentication) to understand how OAuth links your account.
- One supported AI client: Claude Desktop or the Claude web app, Claude Code, ChatGPT with Developer mode, Cursor, or VS Code with GitHub Copilot.
- Node.js installed if your client connects over a local `npx` bridge. Claude Desktop and Claude Code connect natively and do not need Node.js.
- Basic familiarity with the Upstox API. The [SDK guide](https://upstox.com/developer/api-documentation/sdk) is a good primer.

### 5-minute quickstart

Follow these three steps in order. Each one is expanded in its own section below.

#### Step 1 — Connect the MCP server

Add the hosted Upstox MCP server to your AI client so the agent can read your account data. This is the single most important step — see Connect the MCP server .

#### Step 2 — Feed the docs to your agent

Give the agent the Upstox documentation and the `llms.txt` index so it answers with accurate, current API knowledge instead of guessing. See Feed the docs to your agent .

#### Step 3 — Drop in rules files

Add rules files so the agent follows Upstox conventions and, if you use an agent skill, can execute trading workflows. See Drop-in rules files .

### Connect the MCP server

The Upstox Model Context Protocol (MCP) server gives your AI assistant read-only access to your account data — holdings, orders, positions, mutual funds, funds, and profile — over a single hosted endpoint:

```text
https://mcp.upstox.com/mcp
```

Most clients only need this URL. For example, a `mcp-remote` bridge configuration looks like this:

```json
{
  "mcpServers": {
    "Upstox MCP": {
      "command": "npx",
      "args": ["mcp-remote", "https://mcp.upstox.com/mcp"]
    }
  }
}
```

On first tool use the agent opens your browser for the Upstox OAuth consent, and you re-authorize once per day for security. Client-by-client setup — Claude Desktop, Claude Code, ChatGPT, Cursor, and VS Code — is covered in the [MCP Integration guide](https://upstox.com/developer/api-documentation/mcp-integration) .

### Feed the docs to your agent

The MCP server exposes your account data, but the agent still needs to know how the Upstox API is shaped. Point it at the documentation so it writes correct requests and interprets responses accurately.

Two sources work well together:

- **This documentation site** — link the agent to the pages relevant to your task, such as [Authentication](https://upstox.com/developer/api-documentation/authentication) and the [SDK guide](https://upstox.com/developer/api-documentation/sdk) .
- **The `llms.txt` index** — a machine-readable map of the whole documentation set, published at [pathname:///llms.txt](https://upstox.com/developer/api-documentation/llms.txt) . Fetch it once and hand it to your agent as context.

#### Fetch the llms.txt index

Download the index and pass it to your agent as a context file. The tab order is cURL, Python, Node.js, Java, PHP.

- cURL
- Python
- Node.js
- Java
- PHP

```bash
curl -s https://upstox.com/developer/api-documentation/llms.txt -o upstox-llms.txt
```

```python
import requests

url = "https://upstox.com/developer/api-documentation/llms.txt"
response = requests.get(url)
response.raise_for_status()

with open("upstox-llms.txt", "w", encoding="utf-8") as file:
    file.write(response.text)
```

```javascript
import { writeFile } from "node:fs/promises";

const url = "https://upstox.com/developer/api-documentation/llms.txt";
const response = await fetch(url);

if (!response.ok) {
  throw new Error(`Failed to fetch llms.txt: ${response.status}`);
}

await writeFile("upstox-llms.txt", await response.text());
```

```java
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.nio.file.Files;
import java.nio.file.Path;

HttpClient client = HttpClient.newHttpClient();
HttpRequest request = HttpRequest.newBuilder()
    .uri(URI.create("https://upstox.com/developer/api-documentation/llms.txt"))
    .GET()
    .build();

HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
Files.writeString(Path.of("upstox-llms.txt"), response.body());
```

```php
<?php
$url = "https://upstox.com/developer/api-documentation/llms.txt";
$contents = file_get_contents($url);

if ($contents === false) {
    throw new RuntimeException("Failed to fetch llms.txt.");
}

file_put_contents("upstox-llms.txt", $contents);
```

With both the account data (via MCP) and the API knowledge (via the docs and `llms.txt` ), the agent can answer grounded questions about your portfolio and generate correct API calls.

### Drop-in rules files

Rules files tell your agent how to behave when it works with Upstox — which conventions to follow, which endpoints are read-only, and when to ask before acting. They keep an agent's output consistent across sessions and team members.

For agents that go beyond read-only analysis and actually place or manage orders, Upstox publishes a ready-made agent skill. See the [Agent Skills guide](https://upstox.com/developer/api-documentation/agent-skills) to install the `upstox-skill` package, which ships a `SKILL.md` rules file and uses the official Upstox SDK to execute trades and stream data inside a coding agent.

Use the MCP server for read-only analysis and questions; add the agent skill when you want the agent to build and run trading workflows.

### Safety & guardrails

An AI agent connected to a live trading account needs firm boundaries. Keep these guardrails in place:

- **Read-only by default.** The MCP server provides read-only access — the agent cannot place orders, modify positions, or move funds through it. Only the explicit agent skill can execute trades, so add it deliberately.
- **Daily re-authorization.** Account connections expire every day and require a fresh OAuth consent. This limits the window of any accidental or unauthorized access.
- **Verify before acting.** Treat AI output as research support, not investment advice. Cross-check important figures directly on the Upstox platform before you trade.
- **Least privilege.** Grant the agent only the access a task needs, and review the rules files so the agent asks for confirmation before any state-changing action.

### Next steps

Now that your agent is connected, grounded, and guarded, go deeper:

- [MCP Integration](https://upstox.com/developer/api-documentation/mcp-integration) — full client-by-client setup, capabilities, and troubleshooting.
- [Agent Skills](https://upstox.com/developer/api-documentation/agent-skills) — let a coding agent place and manage orders with the official SDK.
- [Authentication](https://upstox.com/developer/api-documentation/authentication) — the OAuth flow behind the MCP connection.
- [SDK guide](https://upstox.com/developer/api-documentation/sdk) — official libraries for building directly against the Upstox API.

---

## Upstox Agent Skills

The Upstox Agent Skill lets AI coding agents like Claude Code and Codex interact directly with your Upstox account. Built on the official `upstox-python-sdk` and the [Agent Skills](https://agentskills.io) open standard, it gives an agent the ability to place live orders, stream market data, and manage your portfolio across NSE, BSE, and MCX — equities, futures and options, and commodities.

Unlike a one-off script, the skill packages verified SDK patterns, pre-flight order validation, and built-in safety guardrails so an agent can execute trading workflows reliably and safely from natural language instructions.

### What are Agent Skills?

Agent Skills are self-contained capability packages that follow the `SKILL.md` open standard. A skill bundles documentation, reference material, helper scripts, and runnable examples that an agent loads on demand to perform a specific job — in this case, trading on Upstox.

The Upstox Agent Skill is compatible with:

- **Claude Code** — Anthropic's CLI coding agent
- **Codex** — OpenAI's coding agent
- Any agent framework that supports the `SKILL.md` standard

#### How Agent Skills differ from MCP

Both connect AI tools to your Upstox account, but they serve different workflows:

- **[MCP integration](https://upstox.com/developer/api-documentation/mcp-integration)** provides read-only, conversational access to your account data inside assistants like Claude Desktop and ChatGPT. It is ideal for portfolio analysis and market research.
- **Agent Skills** run inside coding agents and use the full `upstox-python-sdk` , so they can execute trades, run option strategies, and stream live feeds — not just read data.
Use MCP when you want to analyze and ask questions; use the Agent Skill when you want an agent to build and run trading workflows.

### Key Capabilities

Once installed, the skill enables an agent to handle the full trading workflow:

#### Order execution

- **Place, modify, and cancel orders** across segments using the v3 order APIs
- **GTT (good-till-triggered) orders** — single-leg and multi-leg conditional orders
- **Multi-order placement** and **square-off / exit positions**
- **Multi-leg option strategies** — bull call spread, short strangle, and bear put butterfly examples included

#### Market feeds

- **Live market data and order book depth** via `MarketDataStreamerV3`
- **Quotes** — last-traded price, OHLC, and full market quotes
- **Historical candles** through the v3 history API
- **Option chains** with Greeks, open interest, put-call ratio, and max pain

#### Portfolio access

- **Holdings and open positions** with live P&L
- **Available funds and margin requirements**
- **Position conversion** (for example, intraday to delivery)
- **Realised and unrealised P&L** calculation
The skill covers NSE, BSE, and MCX across equities ( `NSE_EQ` , `BSE_EQ` ), futures and options ( `NSE_FO` , `BSE_FO` , `MCX_FO` ), indices, currencies, and commodities.

### Prerequisites

Before installing the skill, ensure you have:

- **Node.js** installed (for the `skills` CLI) — download from [nodejs.org](https://nodejs.org)
- **Python 3.8+** with the SDK installed: `pip install upstox-python-sdk`
- An active Upstox account with API access - [Learn about Upstox API authentication](https://upstox.com/developer/api-documentation/authentication)
- An **access token** generated from the [Upstox developer portal](https://account.upstox.com/developer/apps)
- One of the supported agents: **Claude Code** or **Codex**

### Installing the Upstox Agent Skill

- Claude Code & app (plugin)
- Claude Code / Codex (npx)
- Global install
- Manual / Python

#### Claude Code & Claude app (plugin)

Install from the Upstox plugin marketplace — a one-time marketplace add, then install the skill plugin. This works in Claude Code and the Claude Desktop/web app.

**Claude Code (CLI)**

```text
/plugin marketplace add upstox/upstox-plugin-marketplace
/plugin install upstox-skill@upstox-plugins-official
```

**Claude Desktop / web app**

Open **Settings → Plugins** (or **Customize → Plugins** ), under **Personal plugins** click **+ → Add marketplace** , enter `upstox/upstox-plugin-marketplace` , click **Sync** , then install the **`upstox-skill`** plugin.

`/plugin marketplace add` takes the **repository** name ( `upstox-plugin-marketplace` ); `/plugin install` takes the **marketplace** name ( `@upstox-plugins-official` ). The same marketplace also offers [`upstox-mcp`](https://upstox.com/developer/api-documentation/mcp-integration) for read-only account access.

#### Claude Code or Codex

Add the skill directly with `npx` — no global install required (and the only path for Codex):

```bash
npx skills add upstox/upstox-skills --skill upstox
```

The agent will pick up the skill on its next run and load it automatically when a request involves Upstox trading or market data.

#### Global install

Install the `skills` CLI globally, then add the Upstox skill:

```bash
npm install -g skills
skills add upstox/upstox-skills --skill upstox
```

#### Manual setup

Clone the repository and install the Python dependency:

```bash
git clone https://github.com/upstox/upstox-skills.git
cd upstox-skills
pip install upstox-python-sdk
```

You can then point your agent at the `skills/upstox/SKILL.md` entry point. See the [`upstox-skills` README](https://github.com/upstox/upstox-skills) for the full directory layout.

### Authentication and Configuration

The skill needs only an **access token** to run. Provide it in one of two ways:

**Environment variable (recommended)**

```bash
export UPSTOX_ACCESS_TOKEN="your-daily-token"
export UPSTOX_SANDBOX_ACCESS_TOKEN="your-sandbox-token"
```

**Config file**

Copy `skills/upstox/config.json.example` to `skills/upstox/config.json` and fill in your token:

```json
{
  "access_token": "your-daily-token"
}
```

The environment variable takes precedence if both are set. `config.json` is git-ignored, so your token is never committed.

Upstox access tokens expire at the end of each trading day. Refresh your token daily from the [Upstox developer portal](https://account.upstox.com/developer/apps) . The skill never hardcodes credentials — they are always read from the environment or a git-ignored config file.

### Safety Guardrails

Because the skill can place **live, irreversible financial orders** , it enforces eight safety rules before any order is placed, modified, or cancelled:

- **Confirmation required** : Shows a full, human-readable order preview and waits for your explicit confirmation before placing, modifying, or cancelling.
- **Default order type is LIMIT** : Never places a MARKET order unless you explicitly ask for one.
- **Default quantity is 1** : Defaults to 1 share (equity) or 1 lot (F&O) when quantity is unspecified, so nothing is over-ordered.
- **Lot-size validation** : Rejects F&O orders whose quantity is not a valid multiple of the contract's lot size.
- **Market Price Protection (MPP)** : Market orders are auto-bounded by Upstox MPP; you can tighten the band with the `market_protection` parameter.
- **Kill switch** : Halt all trading in a segment via `UserApi.update_kill_switch(...)` — cancels pending orders and blocks new ones.
- **Sandbox first** : Encourages rehearsing order workflows in the sandbox before going live.
- **No hardcoded secrets** : Tokens are always read from the environment or a git-ignored config file.

### Sandbox and Paper Trading

Rehearse order-placement workflows without real money using the Upstox sandbox. The SDK exposes a single flag — no separate base URL is needed:

```python
import os
import upstox_client

configuration = upstox_client.Configuration(sandbox=True)
configuration.access_token = os.environ["UPSTOX_SANDBOX_ACCESS_TOKEN"]
```

Always test order flows in the sandbox before placing live trades. For details, see the [Upstox sandbox documentation](https://upstox.com/developer/api-documentation/sandbox) .

### Example Prompts

Once the skill is installed, you can interact with your agent in natural language. Here are some examples:

#### Orders

- "Buy 10 SBIN at 820"
- "Sell ITC at market, intraday"
- "Place a GTT to buy Wipro when it falls to 440"
- "Cancel order 240XXXXXX123"
- "Square off all my F&O positions"

#### Portfolio

- "What am I holding right now?"
- "Show my open positions"
- "How much cash do I have free?"
- "Move my ITC intraday position to delivery"

#### Market data

- "Last price of Bank Nifty"
- "Daily candles for SBIN this month"
- "Show the order book depth for Tata Motors"

#### Options

- "Pull the Nifty option chain for this week's expiry"
- "Put-call ratio for Bank Nifty"
- "Which Nifty strike is closest to spot?"
- "Where's max pain on Nifty?"

#### Option strategies

- "Build a bull call spread on Nifty"
- "Put on a short strangle on Bank Nifty"
- "Set up a bear put butterfly on Nifty"

### What's Included

The skill follows a progressive-disclosure model — an agent loads only what each task needs:

- **`SKILL.md`** : Entry point covering setup, the v2 vs v3 API split, safety rules, and core patterns.
- **`references/`** : Deep-dive docs loaded on demand — orders, GTT orders, portfolio, market data, option chain, margins, instruments, kill switch, WebSocket, and errors.
- **`scripts/`** : Shared utilities — a client factory ( `upstox_helpers.py` ), instrument resolution ( `instrument_search.py` ), and pre-flight order validation ( `validate_order.py` ).
- **`examples/`** : Ten runnable Python scripts demonstrating order placement, portfolio summaries, historical candles, option-chain analysis, and multi-leg option strategies.

### Responsible Usage

AI-generated trading actions and analysis serve as research and execution support, not investment advice. Always:

- Review every order preview carefully before confirming a trade
- Rehearse new workflows in the sandbox before going live
- Verify critical information directly through the Upstox platform
- Consult qualified financial advisors for major investment decisions
- Maintain proper risk management regardless of agent recommendations

The Agent Skill can place real orders that move real money. Confirm every order summary, start with small quantities, and keep the kill switch in mind for halting a segment when you need to step away.

### Resources

- [Upstox Agent Skills on GitHub](https://github.com/upstox/upstox-skills) - Source, references, and examples
- [upstox-python SDK](https://github.com/upstox/upstox-python) - Official Python SDK source
- [MCP Integration](https://upstox.com/developer/api-documentation/mcp-integration) - Read-only AI assistant access to your account
- [Upstox API Overview](https://upstox.com/developer/api-documentation/open-api) - Complete API documentation
- [Authentication Guide](https://upstox.com/developer/api-documentation/authentication) - OAuth flow and access tokens
- [Developer Community](https://community.upstox.com/c/developer-api/15) - Support and discussion

### Frequently Asked Questions (FAQ)

#### What is the Upstox Agent Skill?

The Upstox Agent Skill is a capability package built on the `SKILL.md` open standard that lets AI agents like Claude Code and Codex place orders, stream market data, and manage your portfolio on NSE, BSE, and MCX using the official `upstox-python-sdk` .

#### How is the Agent Skill different from Upstox MCP?

MCP integration provides read-only, conversational access to your account data inside assistants like Claude Desktop and ChatGPT. The Agent Skill runs inside coding agents and uses the full SDK, so it can execute trades and run strategies — not just read data.

#### Which AI agents support the Upstox Agent Skill?

The skill works with Claude Code, Codex, and any agent framework that supports the `SKILL.md` standard.

#### How do I install the Upstox Agent Skill?

The easiest way for Claude Code and the Claude app is the plugin marketplace: run `/plugin marketplace add upstox/upstox-plugin-marketplace` and `/plugin install upstox-skill@upstox-plugins-official` (or, in the Claude Desktop/web app, add the `upstox/upstox-plugin-marketplace` marketplace under Settings → Plugins and install `upstox-skill` ). Alternatively — and as the only path for Codex — run `npx skills add upstox/upstox-skills --skill upstox` , or for a global install run `npm install -g skills` followed by `skills add upstox/upstox-skills --skill upstox` .

#### Can the Agent Skill place real trades?

Yes. The skill can place live, irreversible orders using your access token. It enforces safety guardrails — confirmation prompts, LIMIT defaults, lot-size validation, and a sandbox mode — but you remain responsible for every confirmed order.

#### How does authentication work?

The skill reads your Upstox access token from the `UPSTOX_ACCESS_TOKEN` environment variable or a git-ignored `config.json` file. Tokens expire daily and must be refreshed from the Upstox developer portal. Credentials are never hardcoded.

#### Can I test without using real money?

Yes. The Upstox sandbox lets you place test orders with no real money. Initialize the client with `Configuration(sandbox=True)` and use a sandbox access token. Always rehearse order workflows in the sandbox before going live.
