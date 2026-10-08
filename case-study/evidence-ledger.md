# Evidence ledger: what I can prove, and what I can't

*The engagement from the [case study](running-a-consultancy-on-claude.md): embedded HubSpot and lifecycle owner for a commercial real estate marketing agency, May to October 2026.*

Every line carries one label:

- **VERIFIED:** confirmed by a third party (Upwork's records or the client's own review).
- **SHIPPED:** built and confirmed working in the portal at the time, from my project records. The client owns these now.
- **NOT MEASURED:** I can't claim a result, and the reason is stated.

## Verified

| What | Source |
| --- | --- |
| Engagement ran May to October 2026, 222 hours, billed through Upwork | Upwork contract record |
| 5.0 rating, "I would absolutely hire him again" | Client's public Upwork review |
| Endorsed for: Accountable for Outcomes, Committed to Quality, Detail Oriented, Solution Oriented | Upwork |
| Work "touched nearly every part of our CRM, automation and email infrastructure" | Client review |
| Workflows and automations, lead management and reporting, dashboards and segmentation | Client review |
| Accounting-to-HubSpot processes streamlined | Client review |
| Email authentication: DMARC, DKIM and MTA-STS implemented and monitored; legacy DNS cleaned up | Client review |
| Handoff "documenting what had been completed, what should be monitored going forward, and anything that may need attention" | Client review |

## Shipped

| What | Detail |
| --- | --- |
| Account segmentation by billing recency | Active, conversion window, lapsed, dormant and prospect lists at company and contact level, reconciled to source counts before going live |
| Collections alerts | Escalating internal alerts for overdue invoices, plus customer reminders at the due date and after |
| Paid-invoice-to-deal workflow | Going forward, every paid invoice creates a closed-won deal, so revenue reporting stops missing most of the business |
| Lead scoring rebuilt | Separate fit and intent scores, built alongside the live score instead of overwriting it; switching over was the client's call |
| Dashboards for the CEO and VP of Sales | A Monday dashboard for lead sources and site visits, plus product, billing and client-value reports |
| Meeting scheduler relaunched | Clearer expectations and a one-hour reminder before each meeting |
| Product library cleaned up | One naming convention and one category per product |
| Root cause of blank payment status found | A disabled accounting sync setting, not bad data entry |
| Handoff documentation | Every workflow, what to monitor, and known risks |

## Not measured

| What | Why I can't claim it |
| --- | --- |
| Revenue influenced | No automated flow ran long enough against a holdout group before the engagement ended. Any revenue figure would be attribution, not proof. |
| Email performance lift | Raw open rates were inflated six to eight times by security scanners, and replies and meetings weren't tracked long enough to compare. |
| Effect of the new lead scoring | Built near the end of the engagement, with no before-and-after period. |
| Meeting show and close rates | The meeting outcome field was empty on every meeting, so there was nothing to measure against. |
| Overdue invoices recovered | The alerts shipped. I didn't track individual invoices through to payment, so I don't claim recovered dollars. |

## What I'd measure with another 90 days

- Paid revenue from win-back and expansion lists, against a held-out group of similar accounts.
- Days from new lead to first touch, before and after routing.
- Share of invoices paid within terms, before and after the alerts.
- Reply and meeting rates by lead score tier, to check the score actually predicts anything.
