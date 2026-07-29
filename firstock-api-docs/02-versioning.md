# Versioning

> Source: https://firstock.in/api/docs/versioning/

Versioning is a key aspect of Firstock’s development cycle, ensuring that each release delivers improvements, new features, and enhanced security without disrupting existing implementations more than necessary. In this document, we highlight the evolution from Connect V3 and Connect V4 to the brand-new Developer API, detailing what has changed, what has improved, and how you can benefit from upgrading.

## Developer API

**Developer API**a major leap forward in architecture, security, and developer-centric design. It refines and reimagines many aspects of the older product (Connect V3 and V4) to deliver a smoother, more robust experience, with minimal breaking changes.

## Key Innovations in Developer **API**

- **Streamlined Architecture**

  - Faster response times and reduced latency, thanks to an optimized backend and improved server infrastructure.
  - Support for near-real-time data feeds and agile order placements.
- **Advanced Authentication**

  - Secure token-based auth flows and streamlined session management (drastically cutting down on re-auth needs).
  - Reinforced encryption standards, ensuring compliance with modern security practices.
- **Extensive WebSocket Support**

  - Developer API provides real-time updates for both orders and market data—less reliance on frequent REST polling.
  - Ideal for building reactive UIs, alert systems, or algorithmic strategies requiring up-to-the-second event data.
- **Enhanced Developer Experience**

  - Clearer, more detailed error messages (and consistent error structures).
  - Expanded code examples and tutorials, plus a newly organized documentation set.
  - Strong focus on backward compatibility—legacy endpoints remain functional where possible.
- **Scalability & Modularity**

  - Designed to handle everything from personal projects to enterprise-level trading platforms.
  - More modular approach, letting you integrate only the components you need.

**Migration & Backward Compatibility**

- **Minimal Changes**: For the majority of endpoints, your old Connect V4 integrations should require little more than a config update or slight parameter name adjustments.
- **Deprecated Endpoints**: A small subset of older routes might be deprecated or consolidated; consult our Upgrading Guidelines for details.
- **Upgrade Path**: We recommend gradually testing your existing flows on Developer API’s sandbox, ensuring performance and feature gains before fully switching over.

**Why Switch to Developer API**

- **Performance**: Enjoy drastically reduced latency and a more efficient data pipeline—especially noticeable for high-volume or real-time apps.
- **Security**: Benefit from advanced token-based authentication, better encryption, and more refined user session management.
- **Real-Time**: Leverage robust WebSocket channels for instantaneous market and order updates.
- **Dev-Focused**: Explore a cleaner documentation structure, with in-depth examples and improved error clarity.
- **Future-Proof**: As the new standard, Developer API is where upcoming enhancements, new features, and official support will concentrate.

## Version Comparison Table

| Aspect | Connect V3 | Connect V4 | Developer API |
|---|---|---|---|
| **Performance** | Baseline performance with essential brokerage APIs. | Moderate performance enhancements. Faster data fetching. | **Highly optimized backend** yielding near real-time speeds and reduced latency. |
| **Authentication** | Basic session-based auth. | Improved session management, lesser auth prompts. | **Advanced token- based auth,** robust encryption, minimized re-auth overhead. |
| **Real-Time Data** | Early-stage data integration. Minimal socket support. | Enhanced data throughput, better real-time fetching. | **Extensive WebSocket support** delivering live market & order updates instantly. |
| **Error Handling** | Basic error messages with limited debug info. | More structured messages, better logging. | **Clearer, standardized error structures,** detailed debugging info. |
| **Documentation** | Minimal references, essential guides. | Expanded docs, improved examples, better coverage. | **Comprehensive, reorganized docs** within-depth examples, best practices, etc. |
| **Backward Compatibility** | Foundational approach. | Most Connect V3 calls remain intact, some refined naming. | **Largely backward- compatible;** existing Connect V3/V4integrations require minimal changes. |
| **Recommended Usage** | Suitable for legacy projects with basic needs. | Good balance of performance and reliability. | **Preferred release** for all new dev. High performance, strong security, future-facing. |
