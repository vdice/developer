title = "FAQ and Known Limitations"
template = "cloud_main"
date = "2023-04-18T00:00:00Z"
enable_shortcodes = true
[extra]
url = "https://github.com/fermyon/developer/blob/main//content/cloud/faq.md"

---
- [Service Limits](#service-limits)
- [Known Limitations](#known-limitations)
  - [Spin Limitations](#spin-limitations)
  - [Other Limitations](#other-limitations)
- [Frequently Asked Questions](#frequently-asked-questions)
- [Next Steps](#next-steps)

## Service Limits

The following are the limits of the Fermyon Cloud

- A user account can have a maximum of 5 Spin applications deployed at any time
- A Spin application can have no more than 1,000 executions (inbound HTTP requests) every second
- A Spin application can have no more than 500 outbound requests per hour
- A Spin application request handler can take no more than 10 seconds to complete
- A Spin application package cannot exceed a total size of 100MB
- A custom Fermyon subdomain must be greater than 3 characters and less than 63 characters in length
- A custom Fermyon subdomain must be unique
- A user account can execute a maximum of 10 deployments in a minute
- A user account can execute a maximum of 100 deployments in an hour
- A user can execute a maximum of 3,000 requests per hour toward the Cloud API. This includes API requests from the CLI (`spin`) and navigating the Fermyon Cloud website.
- A key value store key can have a maximum size of 255 bytes
- A key value store value can have a maximum size of 1 MB
- A key value store can have a maximum of 1,024 keys 
- A Spin application can have a maximum of 1 key value store
- The device and browser token lifetime is 7 days

## Known Limitations

### Spin Limitations

Fermyon Cloud supports Spin CLI v0.6.0 or newer. That being said, there are certain Spin SDK triggers and APIs that are not yet supported on Fermyon Cloud. Please review the table below to see what is supported today on Fermyon Cloud: 

| Feature | SDK Supported? |
|-----|-----|
| **Triggers** |
| [HTTP](/spin/http-trigger) | Supported |
| [Redis](/spin/redis-trigger) | Not supported |
| **APIs** |
| [Outbound HTTP](/spin/rust-components.md#sending-outbound-http-requests) | Supported |
| [Key Value Storage](/spin/kv-store-api-guide) | Supported (only default store) |
| [MySQL](/spin/rdbms-storage#using-mysql-and-postgresql-from-applications) | Supported |
| [PostgreSQL](/spin/rdbms-storage#using-mysql-and-postgresql-from-applications) | Supported |
| [Outbound Redis](/spin/rust-components.md#storing-data-in-redis-from-rust-components) | Supported |
| **Extensibility** |
| [Custom Triggers](/spin/extending-and-embedding) | Not supported |

To learn more about what feature support looks like for various programming languages, visit the [Spin Language Support Guide](/spin/language-support-overview.md).

### Other Limitations

- You cannot communicate between Spin applications using local name resolution
- [Runtime configuration and secrets](/spin/dynamic-configuration#runtime-configuration) are not supported at this time

## Frequently Asked Questions

- **Why do I see mixed replies from my service during an upgrade?**
  - When doing an upgrade of an application, there is a gradual roll-out happening. This means that requests will hit both the existing and new modules, as the upgrade completes. You will see a pattern like the one below, showing the body reply from an HTTP request:

<!-- @nocpy -->

```text
11:08:13 : Hello from Rust
11:08:18 : Hello from Rust - updated
11:08:19 : Hello from Rust
11:08:23 : Hello from Rust - updated
11:08:24 : Bad Gateway
11:08:26 : Hello from Rust - updated
11:08:27 : Bad Gateway
11:08:29 : Hello from Rust - updated
```

- **How do I report a security concern, or concerns, with content hosted on the Fermyon Cloud?**
  - Please go to our [Feedback repo - Report Security Concern](https://github.com/fermyon/feedback/security/policy) for instructions on how to report any concerns.

## Next Steps

- Learn how to engage with Fermyon to get [support](support)
