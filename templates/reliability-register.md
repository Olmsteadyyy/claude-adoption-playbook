# Data reliability register

*The single most useful file in my setup. Claude reads it before building anything. Each row cost me time to discover; the register makes sure it only costs that once.*

| Signal | Status | Consequence | How we found out | Date |
| --- | --- | --- | --- | --- |
| [Example] Payment status on synced invoices | Untrusted: blank on most records because a sync setting was off | Never count as receivables; never send payment reminders from it | Counts didn't reconcile with the billing system | |
| [Example] Lifecycle stage | Decorative: far fewer "Customers" than paying accounts | Never use as the customer definition; use billing records | Compared stage counts to invoice counts | |
| [Example] Raw email open rate | Inflated several times by security scanners | Report replies and meetings, or bot-excluded opens, always labeled | Opens arriving within seconds of delivery | |
| [Example] Meeting outcome field | Empty on every record | No automation can depend on it until it's filled in | Field fill-rate check | |
| [Example] A query filter | Silently ignored by the tool | Run the same query with an impossible date range; if the count doesn't change, the filter is being dropped | Count matched the full table | |

**Statuses:** Trusted, Use with care, Don't use, Unknown.
