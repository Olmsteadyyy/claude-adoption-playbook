---
name: hubspot-revenue-audit
description: Run the fixed-price, read-only HubSpot Revenue Audit end to end, from intake and query pack to finance reconciliation, scorecard and client report. Use when an audit is bought, underway or due.
---

# HubSpot Revenue Audit

## What is being sold

A fixed-price, read-only audit of a B2B company's HubSpot portal, delivered in
10 business days (5 with Rush Delivery). The audit answers one question for
the CEO: **is HubSpot paying for itself, and if not, what would make it?** It
ends with a ranked 90-day plan and a 45-minute walkthrough. The fee is credited
toward the 90-Day Build if the client signs within 14 days of delivery.

The promises on the website and the Upwork listing are binding on this Skill:

- **Nothing in the portal changes.** No record edits, no list or view saves, no
  workflow toggles, no emails, no property changes. Reading only.
- **Every number is labeled** and the math behind every estimate is shown.
- **No ROI promise and no forecast.** State what was found and what fixing it
  takes. Never project a percentage.
- **The plan is the client's** whether they build it with the consultant, their team or
  anyone else.

The consultant reviews every number before anything reaches the client. Claude drafts;
the consultant sends.

## Inputs, and what to do when one is missing

| Input | Source | If missing |
| --- | --- | --- |
| User invite to the portal, two-factor sign-in | Client invites the consultant with the permissions in the kickoff checklist below | Clock-stop after 3 business days. Never ask for or accept a shared password |
| 12-month invoice export from finance | Client's accounting system, CSV or XLSX | Reconciliation becomes UNKNOWN; say so on page one rather than estimating it |
| Requirements answers | Upwork requirements or the intake form | Ask once in the kickoff message |
| Software list with annual costs | Finance or the client owner | Overspend section covers seats and contacts only, and says why |
| Ad targeting summary (optional) | Marketing | Skip the targeting mismatch line |

The seven intake questions: portal ID and hubs and tiers owned; accounting
system and whether it syncs to HubSpot; which revenue number leadership trusts
today and where it comes from; the three things about HubSpot that frustrate
them most; who signs off and how fast; any workflow or send that must not be
touched; whether they can invite the consultant today.

### Kickoff permission checklist

Plain view access does not reach everything the audit reads. Ask for these in
the kickoff message, and confirm the exact permission names on a HubSpot
developer test account before the first client, because they vary by tier:

- View access to contacts, companies, deals, invoices, line items and products
- View access to workflows
- View access to users and teams, or a seat and last-login export from their admin
- View access to marketing email and the sending domain's settings
- Permission to connect the Claude app to their portal, or a Super Admin who
  approves it. Tell the client the app is connected for the audit and removed
  at the end; connecting it is the only change the audit makes, and it is theirs
  to approve

## Before the first query

0. **Set up the client.** On day 0, run "Starting a client" in
   `client-engagement-ops` to create the client's Project. The portal guard
   reads the portal ID from it.
1. **Portal guard.** Run `get_user_details`. The portal ID must match the one
   in this client's Project instructions. If it doesn't, stop, say which portal
   is connected, and do nothing else. The HubSpot connector holds one portal at
   a time, so the wrong client's portal being connected is the most likely
   failure in a multi-client practice.
2. **Load `hubspot-portal-queries`** and follow its protocols: schema first,
   transaction object resolved, status fields interrogated, every number
   labeled, silent-failure tests run.
3. **Turn the connector's create and update tools off** for the length of the
   audit. "Ask first" is not enough, because overnight runs have nobody there
   to answer. The audit uses read tools only. If a step seems to need a write,
   it is out of scope for the audit.

## Labels

| Label | Means |
| --- | --- |
| **LIVE PULL** | Queried from the portal in this engagement, with the date |
| **RECORD** | Taken from a document the client supplied, such as the finance export or the software list |
| **ESTIMATE** | Derived. The method and inputs appear in the same place |
| **UNKNOWN** | Not established. Say what would establish it |

## The schedule

| Business day | Work | Output |
| --- | --- | --- |
| 0 | Requirements submitted, clock starts. Draft the kickoff message | Kickoff message for the consultant to send |
| 1 | Access confirmed, portal guard, schema, object inventory (Q0 to Q2) | Engagement notes in the client Project |
| 1 to 3 | Finance export received; reconciliation (Q3) | Reconciliation table with gap categories |
| 2 to 4 | Data trust, lead handling, adoption pulls (Q4 to Q7) | Draft reliability register |
| 3 to 4 | Browser inventory: workflows, lists, reports, integrations, users (Q8) | Automation inventory |
| 5 | Email health (Q10) and overspend (Q11) | Email checks, overspend math |
| 6 | Best customers (Q9) and plan capability (Q12) | Customer comparison, plan recommendation |
| 7 | Draft the report from the template; draft the 90-day plan | Draft report |
| 8 | **Gate G1: The consultant checks every number** | Corrections |
| 9 | Walkthrough deck, scope-of-work draft if a build is likely | Deck, draft SOW |
| 10 | Deliver, walkthrough call | Report link and PDF |

Rush Delivery compresses this to five business days: run Q0 to Q8 on days 1
and 2, the rest on day 3, draft on day 4, review and deliver on day 5. If
access or the finance export arrives late, the Rush guarantee is at risk; tell
the consultant the same day.

Heavy read-only pulls can run overnight as a scheduled task, provided the task
starts with the portal guard and writes results to the client Project.

## The query pack

Confirm property and table names with `hubspot-portal-queries` Protocol 0
before each first use. The shapes below are the logic, not literal syntax.

**Q0. Identity and plan.** Portal ID, hubs and tiers, currency, timezone, paid
seats, marketing contact tier and count.

**Q1. Object inventory.** Record counts for contacts (marketing and
non-marketing), companies, deals by pipeline, invoices, line items, products,
subscriptions, quotes, tickets, meetings, tasks, forms. An object with zero
records is a finding when the business clearly does that activity.

**Q2. Where the money is.** Resolve the transaction object (Protocol 1 of
`hubspot-portal-queries`). Count and sum every candidate and count distinct
paying companies for each. Compare with companies or contacts marked Customer.

**Q3. Revenue reconciled.** HubSpot's 12-month revenue against the finance
export total (RECORD). HubSpot's figure comes from the money object Q2 found,
and only that one: closed-won deal amounts by close date, or invoice amounts
by invoice date. Never add deals and invoices together; the same revenue would
be counted twice. Match finance lines to HubSpot companies by
normalized domain first, then normalized legal name. Classify the gap:

- renewals invoiced with no deal or invoice in HubSpot
- expansion or add-on work invoiced with no deal
- invoices that match no HubSpot company (new legal names, parents, typos)
- timing differences (closed in one period, invoiced in another)
- anything left over, stated as unexplained rather than forced into a bucket

The headline is the share of finance revenue HubSpot cannot see. The categories
must add up to the gap; show the arithmetic.

**Q4. Data trust.** Duplicate companies by normalized domain and name;
contacts and companies with no owner; fill rates for industry, employee count,
lifecycle stage, lead source, deal amount and meeting outcome; lifecycle stage
compared with actual paying companies. Each finding becomes a register row.

**Q5. Lead handling.** Inbound leads created last quarter by source; time from
create date to the first call, email or meeting; share untouched after 48
hours. If engagement data is unreadable (the connector cannot read engagements
when HubSpot's Sensitive Data setting is on), mark it UNKNOWN and say why.

**Q6. Lead definition.** Lifecycle stage and lead status values in use and how
many records sit in each; forms in use; how many workflows set lifecycle stage
(from Q8). Several conflicting definitions is the finding.

**Q7. Adoption.** Activities logged per user over 30 days; deals created per
rep; users with no sign-in for 60 days (users page, in the browser). Ask the
owner whether deals or leads also live in a spreadsheet.

**Q8. Automation inventory (browser, read-only).** The connector cannot build
or reliably inventory workflows, so read them in the HubSpot UI. Per workflow:
name, active or off, object, trigger in plain words, enrollments in the last
90 days, emails it sends. Flag dormant (active, no enrollments in 90 days),
overlapping (same trigger, same audience) and double-sending workflows. Open
nothing in edit mode and save nothing.

**Q9. Best customers, first read.** Join the finance export to companies. Rank
by 12-month revenue; take the top 20% of paying companies and their share of
revenue. Compare top against the rest on the traits that are actually filled
in: industry, employee band, original source, number of product lines bought,
renewal or repeat rate, region. Report only traits with enough fill to mean
something, and state the fill. If the client shared ad targeting, note any
mismatch between who they target and who pays.

**Q10. Email health.** SPF, DKIM and DMARC for the sending domain (public DNS
lookup, or HubSpot's domain settings in the browser); DMARC policy and whether
anyone reads the reports; spam complaint and bounce rates over 90 days; opens
reported bot-excluded, with the raw figure shown beside it so nobody is misled;
consent source on imported lists. Unknown consent means no volume increase.

**Q11. Overspend.** From the software list (RECORD): tools that duplicate
features the client's HubSpot tier already includes. From the portal: marketing
contacts with no open, click or visit in 12 months (ESTIMATE of tier savings,
using HubSpot's current contact-tier pricing, verified at the time); paid seats
with no sign-in for 60 days (ESTIMATE). Show each line's math.

**Q12. Plan capability.** List what the 90-day plan needs and check each item
against what the client's hubs and tiers include, using HubSpot's current
product catalog, not memory. Recommend staying, adding a seat type, or
upgrading, with the one feature that would justify an upgrade.

## The report

Build the client report from the sample audit artifact ("Revenue Audit: Sample
Co."). Copy it into a new artifact for the client and replace only the data:
the hero text and ledger, the reconciliation bars and detail text, the
scorecard rows, the money rows and their math, the register rows, the customer
comparison, the email checks, the plan steps and the plan recommendation.
Remove the "Sample" banner and the closing sales block; add "Prepared for" with
the client's name and the delivery date.

Sections, in order:

1. **Verdict.** The CEO's question and a two-sentence answer, then three
   headline numbers, each labeled with its source.
2. **Revenue, reconciled.** HubSpot's figure, finance's figure, and the gap
   categories (Q3).
3. **Scorecard.** The six build outcomes, each graded Fix first, Needs work or
   Solid, with the one fact that earned the grade, the fix and the phase:
   data you can trust; a clear picture of your best customers; one definition
   of a good lead; a system your team uses; follow-up that fires when buyers
   act; one dashboard you can read in a minute.
4. **What it's costing you.** Cold leads and overspend, math shown.
5. **Data you can trust.** The reliability register: Trusted, Use with care,
   Don't use, Unknown.
6. **Your best customers, first read.** Top 20% share, traits compared, any
   mismatch.
7. **Email health.** The checks from Q10.
8. **Your 90-day plan.** Ranked fixes, each tagged Diagnose, Foundation or
   Automation, plus the plan recommendation (Q12).
9. **This week.** Three things the client can do without the consultant.

Also deliver a PDF of the report (Upwork deliveries need a file). Send the
artifact link to the client only, and tell them the PDF is the copy that lasts:
the link is deleted with the rest of their data at offboarding. Never reuse a
client's figures in another client's work, the sample, or marketing.

## Writing rules

- Written for a CEO who skims. One idea per paragraph, short sentences.
- Name a technical term and translate it in the same breath.
- Explain any bad-looking number before the reader can ask.
- No vendor language: no "leverage," "streamline," "solutions," "unlock."
- The plan is ranked by what each problem is costing, not by how interesting it
  is to build.
- Every "This week" item is doable in an afternoon by the client's own team.

## Gate G1: The consultant's review checklist

Draft this list at the top of the review copy, then remove it before delivery:

- [ ] Portal ID on the report matches the client's portal
- [ ] The connector's create and update tools stayed off for the whole audit
- [ ] Every figure has a label, and every ESTIMATE shows its math
- [ ] Reconciliation categories add up to the gap
- [ ] No count came from a list preview
- [ ] Opens are bot-excluded wherever they appear
- [ ] No forecast, projection or promised percentage anywhere
- [ ] Plan recommendation checked against HubSpot's current catalog
- [ ] Nothing names another client or reuses another client's numbers

## After the walkthrough

If the client wants the build, the ranked plan becomes the blueprint. Size it
to the build's hour budget before the scope of work is drafted, list anything
that will not fit as a later phase, and note the credit deadline (14 days from
delivery). The work continues in the same client Project under
`client-engagement-ops`.

If the client does not want the build, the plan stands on its own. When they
say no, or the 14-day credit window closes without a signed build, run the
offboarding checklist in `client-engagement-ops`: access removed, the Claude
app disconnected, their data deleted.
