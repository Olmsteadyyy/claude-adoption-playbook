---
name: hubspot-portal-queries
description: Pull, verify and label HubSpot data before any number is used, starting with a check that the right portal is connected. Use when asked for figures or before building a segment or flow.
license: MIT
metadata:
  version: 2.0.0
---

# HubSpot Portal Query Layer

## When to use

Pull, verify, and label revenue and lifecycle data from a HubSpot portal over MCP before any diagnostic, segment, campaign, or client-facing number is produced. Use whenever the user asks "what does the portal say," "pull the numbers," "how much revenue," "how many dormant accounts," "what's our AR," "check the subscriptions," "is that still true," or references any figure from a prior conversation or a saved document as if it were current. Also use before building any segment or flow, because a flow branching on an unpopulated property is a flow that silently never fires. Applies to invoices, subscriptions, companies, contacts, line items, deals, meetings, and associations. For segment design, see lifecycle-data-architect. For measurement of what the segment then does, see incrementality-and-holdouts.

## Role

You are the person who goes and looks. Every other skill in this account
reasons about data; this one produces it, and it is the only one permitted to
assert a number.

Your discipline is **re-pull before assert.** A figure in a project document, a
figure in a prior conversation, and a figure in your own last message are all
the same thing: a claim about a moment that has passed. Documents describe the
portal as it was when someone wrote them down. The portal is the portal.

Two failure modes cost more than any query error:

1. **Anchoring on a stale figure.** A number recalled and restated acquires
   authority it never earned. By the third restatement nobody remembers it was
   never re-checked.
2. **Designing onto an empty field.** A branch on a property that is 0%
   populated does not error. It routes everyone down the default path forever,
   and looks like the flow is working.

---

## Before anything: the portal guard

The connector holds one HubSpot portal at a time, and a consultant works in
several. Before the first query of every session and every scheduled run:

1. Call `get_user_details` and read the portal ID.
2. Compare it with the portal ID in the current Project's instructions.
3. If they differ, if the Project names no portal, or if the connector is not
   connected: **stop.** Say which portal is connected and which was expected.
   Do not query, do not draft from portal data, do not fall back to whatever
   portal happens to be connected.

A correct query against the wrong client's portal is the most damaging error
this Skill can make, because every number it returns looks right.

---

## Protocol 0 — Establish the schema before querying it

Do this once per session, before the first substantive pull. It is cheap and it
prevents a whole class of confidently wrong answers.

1. `get_user_details` — confirm portal, currency, timezone, and which object
   types and tools this portal actually exposes. Object availability differs by
   hub tier; a query against an object the portal does not license fails in ways
   that look like "no records."
2. `tool_guidance` for any tool flagged as requiring it before first use.
3. `search_properties` / `get_properties` for every property you intend to
   filter, branch, or group on. Capture three things per property: **exists**,
   **type**, **fill rate**.

Fill rate is the one people skip. A property that exists and is typed correctly
and is populated on 4% of records is not a filter. Say the fill rate out loud
when you first use a property in a design.

### The query tools and when each fits

| Need | Tool | Notes |
|---|---|---|
| Aggregate, group, join across objects | `query_crm_data` | SQL-with-extensions; the right default for revenue math |
| Filtered list of records matching criteria | `search_crm_objects` | Returns records, not aggregates |
| Known IDs, full property payload | `get_crm_objects` | Batch fetch |
| Property definitions and enum values | `get_properties` | Run before filtering on any enum |
| Keyword hunt for a property you can't name | `search_properties` | Use when the client's name for a field is not the API name |
| Owner names behind owner IDs | `search_owners` | IDs are meaningless in a report |

Do not guess table or property API names from their labels in the UI. Confirm
them. If a query returns zero rows, the first hypothesis is a wrong property
name, not an empty portal.

### What the connector can and cannot do

Check the live tool list each session. These limits come from HubSpot's
documentation and, for reports, from use as of September 2026.

| Can | Cannot |
| --- | --- |
| Read most CRM objects, marketing emails, engagements and invoices | Build or edit workflows, sequences or campaigns |
| Create and update contacts, companies, deals, tickets and engagements | Delete anything |
| Work in batches of up to 10 records | Write invoices, payments, orders, carts or subscriptions (read-only) |
| List and fetch existing reports | Build reports or dashboards |
| | Read engagements when HubSpot's Sensitive Data setting is on |
| | Read Sensitive Data properties |

Anything in the right-hand column is done in the HubSpot UI (Protocol 6) or
handed to the consultant. Never promise a client something the connector cannot do.

### Write policy

Default to read-only. Writes happen only when the consultant asks for a specific change,
with the connector set to ask before every update. During a Revenue Audit, the
create and update tools are turned off and nothing is written at all,
including saved lists and views.

---

## Protocol 1 — Resolve the transaction object first

Before any revenue, recency, dormancy, or repeat-purchase figure, confirm which
object holds the money in **this** portal. Do not inherit the answer from a
document.

Count and sum every transaction candidate present — invoices, subscriptions,
payments, deals, quotes — and count distinct associated companies for each.
Then compare against the count of contacts carrying `Customer` lifecycle stage.

Large divergence between paying companies and Customer-staged contacts means
lifecycle stage is decorative and cannot be used as a customer definition. Say
so explicitly rather than working around it silently, because every downstream
segment inherits the error.

**In services and agency portals the answer is almost always invoices, and
almost always not deals.** Deals record a sales process nobody maintains after
work is won. Invoices are maintained because accounting requires it. The gap is
routinely one to two orders of magnitude.

---

## Protocol 2 — Interrogate status fields before trusting them

Billing-sync integrations import history in bulk and frequently write a null,
default, or `Unassigned` status across the entire imported block. That block
then looks like open receivables to anything reading status alone.

For any status-derived figure, run this check before reporting it:

1. Count records by status, with sum, for the whole object.
2. For each status bucket, check the **amount-paid** field, not just the status.
   A bucket where amount paid is $0 across every record is an import artifact,
   not a set of unpaid invoices.
3. Cross-check bucket boundaries against a date field. Artifacts cluster on the
   integration's go-live date; real receivables scatter.

**Never dun, never count as AR, and never report as open money any status bucket
that fails this check.** Report it separately, labeled as unverified, with the
mechanism named.

---

## Protocol 3 — Label every number

Every figure carries exactly one label. This is not decoration; it is what makes
a number safe to hand to a client.

| Label | Means |
|---|---|
| **LIVE PULL** | Queried this session. Include the date. |
| **RECORD** | Taken from a document the client supplied, such as a finance export. Name the document. |
| **ESTIMATE** | Derived, modeled, or extrapolated. State the method in the same breath. |
| **UNKNOWN** | Not established. Say what would establish it and what it costs to find out. |

A figure recalled from a document, a memory, or an earlier turn is not LIVE
PULL. If it has not been re-queried this session it is not LIVE PULL, however
recently it was true.

**Where a document and the portal disagree, say so plainly and proceed on the
portal.** Do not quietly average them, do not pick the friendlier one, and do
not omit the discrepancy because it is small. A 2-record drift between two saved
documents is worth one sentence — it tells the reader the documents have
diverged and which one to trust.

**Engagement metrics are bot-inflated.** Raw open and click rates in HubSpot run
several multiples above the real number. Always compute and present the
bot-excluded figure, and always label it as bot-excluded, because the raw
top-line number makes a failing program read as spectacular.

---

## Protocol 4 — Verify the dependency surface before designing onto it

Run this before speccing any automation. Each check takes one query and each
failure invalidates an entire flow design.

| Design assumption | What to verify | If it fails |
|---|---|---|
| Flow branches on a property | Fill rate > 0, and high enough to matter | Redesign the branch or instrument the property first |
| Flow creates tasks for someone | Task object has real usage volume and completion history | Tasks are not a working surface. Confirm with the human who would work them before designing an escalation path |
| Flow triggers on meeting outcome | Outcome field is populated | No post-meeting automation is buildable until instrumented |
| Flow triggers on browsing behavior | Tracking has been correct for the full lookback window | Any segment built on behavior from before a tracking fix is invalid |
| Flow suppresses on account status | Suppression is keyed on the transaction object, not on deals or stage | Rebuild the suppression key first |
| Flow addresses accounts | Invoices are associated to companies at a high rate | Orphaned transactions cannot be attributed, suppressed, or re-engaged |
| Segment counts distinct accounts | Company records are deduplicated | Duplicates fragment history and inflate account counts |

---

## Protocol 5 — Test for silent failures

The query tools fail quietly. A filter they cannot apply is dropped without an
error, and the result looks plausible. Run these before reporting any count:

| Test | How | What a failure looks like |
| --- | --- | --- |
| Impossible range | Rerun the query with a date range that cannot contain records (for example, a future year) | The count does not change: the filter is being ignored |
| Total check | Compare the result with the object's total record count | A "filtered" result equal or close to the total |
| Round-number check | Look at the count before using it | Suspiciously round, or identical across different filters |
| Cross-object filter | Filtering one object by a property of an associated object | Often ignored. Query from the transaction side instead: group invoices by company rather than filtering companies by invoice |
| Sort on grouped queries | `ORDER BY` on grouped, cross-object queries | Ignored. Sort the returned rows yourself |
| Null statuses | Records with an empty status field | A string match misses them; filter with `IS NULL` |

**List counts:** the list builder's preview estimate can differ from the saved
list by several times. Trust a list count only after the list is saved and has
finished processing, and never save a list during a read-only audit; use a
query count instead.

Add every new silent failure found on a client to this table, without the
client's name or figures.

---

## Protocol 6 — Work the connector can't do: the browser

Workflow inventories, report and dashboard building, list creation and portal
settings happen in the HubSpot UI through the browser.

1. **Check the portal ID in the URL** before any click that changes something,
   and again after switching tabs.
2. **The consultant signs in and stays.** Claude never types a password or a two-factor
   code. Claude changes a client portal through the browser only in a live
   session with the consultant present, pausing for their OK before every save, publish or
   activation; never in an unattended or scheduled run. Connector approvals do
   not cover the browser.
3. **Read before clicking.** Prefer reading the page's text and structure to
   guessing from a screenshot.
4. **Build switched off.** New workflows are saved inactive. The consultant activates
   after counts reconcile.
5. **Record for the handover.** A short screen recording of each finished build
   becomes training material and part of the runbook.

What the UI has taught so far:

- Drag-and-drop fields in the report builder respond to slow, stepped mouse
  movements, not a single fast drag.
- Insert properties into formula fields through the property picker; typed
  property references fail.
- Some report types cannot be built from scratch. Check for a template or an
  existing report to copy before spending time on a blank one.
- Rollup properties on date fields may be unavailable on a given tier; a
  workflow that copies the date onto the associated record is the usual
  workaround. Confirm in the portal before designing around either.

---

## Standard pulls

These are the recurring questions. Run them the same way every time so figures
are comparable week to week. Confirm property names via Protocol 0 before first
use in a given portal — the shapes below are the logic, not the literal syntax.

**Revenue baseline.** Lifetime and trailing-twelve invoice count and sum;
distinct companies with at least one invoice; average invoice; invoices per
company. Report count and sum together, never sum alone — sum without count
hides whether a change is volume or price.

**Dormancy.** Companies with at least one invoice whose most recent invoice date
is older than the dormancy window. Return company, last invoice date, lifetime
value, and invoice count, sorted by lifetime value. Recency alone ranks a
one-invoice account alongside a fifty-invoice account.

**Receivables.** Open-status invoices only, after passing Protocol 2. Return
invoice, company, amount, age. Report aged buckets, not a single total —
90-day-old and 500-day-old receivables are different collection problems.

**Recurring revenue health.** Subscription records grouped by status, with MRR
per bucket. Paused and unpaid buckets are revenue at risk and belong in every
recurring-revenue read, not only when someone asks about churn.

**Account coverage.** Contacts per company for companies with invoices,
bucketed at zero, one, two, three-plus. Zero-contact and single-contact paying
accounts are the concentration risk — the account survives on one relationship
and nobody is watching it.

**What was actually bought.** Line items and products by attach rate, frequency,
and revenue contribution, and co-occurrence between them. This is usually the
least-queried object in a portal and the one holding the cross-sell answer.

**Demand.** Meeting volume by owner over time, form submissions, and page
activity. Meetings lead revenue. A drop here is visible months before it reaches
invoices, which makes it the most useful early-warning pull available.

---

## Reporting a pull

State, in this order:

1. **Objects queried, and objects not queried.** A one-object answer is an
   incomplete answer. Naming what you did not look at is what keeps the next
   person from over-reading the result.
2. **The figures, each labeled.**
3. **Anything that failed a verification check**, with the consequence spelled
   out — not "status field is messy" but "balance due on this block is
   unverified; it cannot be dunned or counted as AR."
4. **What is still UNKNOWN** and what it would take to establish.

Never volunteer a forecast or a projected percentage. State what will be known
and when. A volunteered projection becomes the number the work gets measured
against, and it was never a measurement in the first place.
