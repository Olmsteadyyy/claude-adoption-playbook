# Running a one-person consultancy on Claude: what worked, what broke, and how I caught it

*Kyle Olmstead, October 2026. Written with Claude, edited by me.*

From May to October 2026 I was the embedded HubSpot and lifecycle owner for a commercial real estate marketing agency, reporting to the CEO and VP of Sales. It was a solo engagement, billed through Upwork: 222 hours, ending with a 5.0 review. I did almost all of it with Claude open beside the portal.

This isn't a story about Claude doing the work. It's about the operating rules I had to build so I could trust what it produced, and the places it broke before I had them.

## By the numbers

| Measure | Value | Label |
| --- | --- | --- |
| Time with Claude, April to July 2026 | About 175 active hours across 280 conversations | Measured from my account export's message timestamps |
| Tool actions Claude ran for me in that period | About 1,250 (code, file work, web research, live connectors) | Measured from the export |
| Time with Claude, April to October 2026 | About 300 hours | Estimate: the measured 175, plus the current account at the same pace |
| Custom Skills | 11 | Counted |
| Client engagement | 222 hours, 5.0 rating | Verified by Upwork |

## The setup

**One Project per client, written as rules.** The instructions weren't a persona. They were an operating manual: how the business makes money, which data could be trusted, how every number had to be labeled, and what never went to the client without my review. The template is in [`templates/project-instructions.md`](../templates/project-instructions.md).

**Eleven custom Skills.** Six carried the lifecycle method: diagnostics, deliverability, data architecture, workflows, copy, and a weekly operating rhythm. Five were for this account: the client's voice, commercial real estate vocabulary, safe querying of the HubSpot portal, measurement design, and expansion analysis. Ten are in [`skills/`](../skills/); the voice Skill stays private because it's built from a real person's email.

**Live connections.** Claude queried the client's HubSpot portal directly through its connector. Gmail held my sent recaps, which became the ground truth for voice. Google Drive held state files, and Slack carried lead alerts.

**Claude in Chrome, for screens with no API.** HubSpot's report builder can't be driven through the API, so Claude built reports in the browser. It took practice:

- Dragging fields worked only with slow, stepped mouse movements, not a single drag.
- Formula fields had to be inserted through the property picker; typed references failed.
- Some report types can't be built from scratch at all. Learning that early saved hours of trying.

**Scheduled tasks that ran overnight.** One run a night checked the work and left a short to-do list for the morning, instead of checks through the day. That kept usage down and meant the day started with a list, not a blank screen. The template is in [`templates/overnight-account-sweep.md`](../templates/overnight-account-sweep.md).

**Artifacts for anything the client would see.** Dashboards, the handoff document, and proposals were built as artifacts, so they could be reviewed and shared before anything was sent.

**Memory.** Lessons went into a running "learnings and constraints" file, so the next session started from what the last one had found.

## The rules that made it trustworthy

1. **Label every number** LIVE PULL, ESTIMATE, or UNKNOWN. A number recalled from an earlier conversation was never presented as current.
2. **Re-pull, don't recall.** Saved documents drifted from each other within weeks. When a saved figure and a live one disagreed, the rule was to say so out loud, because the gap showed how stale the documents had become.
3. **Find the source of truth first.** In this business, the deal records captured only a small fraction of real revenue. Invoices were the truth, so every segment and trigger was built on invoices.
4. **Strip out bot traffic.** Security scanners open emails automatically. Raw open rates read several times higher than real human opens, so engagement was always reported with bots excluded and labeled.
5. **Check what automation depends on.** A workflow that creates tasks assumes someone works a task queue. A branch on a field assumes the field is filled in.
6. **Report attributed, incremental, and the gap.** Never the attributed number alone.
7. **Nothing reaches the client unread.**

## What broke

This is the part I'd most want a hiring manager to read, because every failure was silent. Nothing errored. The output just looked plausible and was wrong.

### Filters that were silently ignored

The HubSpot query tool accepted filters it didn't apply. Querying invoices with a date filter on a contact field returned the full dataset, with no warning. Filtering companies by whether they had invoices returned every company in the portal, thousands of records, instead of the few hundred that had actually been billed. Sorting on grouped queries was ignored too.

**How I caught it:** the counts were too round, or too close to the total. The fix became a standing test: run the same query with an impossible date range. If the count doesn't change, the filter is being dropped.

### Previews that didn't match reality

HubSpot's list builder showed an estimated size before saving. One list previewed at 1,338 contacts and held 293 once saved. **The rule:** save first, then trust the count.

### Fields that looked usable and weren't

- Payment status was blank on most synced invoices. It wasn't bad data entry: a sync setting between the accounting system and HubSpot was switched off. Finding the setting fixed the cause instead of patching around it.
- Meeting outcome was empty on every meeting, so nothing could be automated from it.
- Lifecycle stage was decorative: a few dozen companies were marked Customer while hundreds were paying.
- HubSpot's own lead score was hidden from the query tool, so scoring logic had to live in fields I could actually read.

Each one went into a reliability register that Claude checked before building anything. The template is in [`templates/reliability-register.md`](../templates/reliability-register.md).

### Platform limits found the hard way

Invoice workflows couldn't read line items. Rollup fields couldn't filter on dates. The client's sales tier couldn't enroll contacts into sequences automatically. Each was a design that looked right on paper and was impossible in the portal, found only by testing in the portal.

### Claims Claude made that I caught

- **A trend reported backwards.** Claude summarized active clients as flat for the quarter. The report showed a small increase. A small error, but in a CEO recap it's exactly the kind that costs trust.
- **Projections presented as results.** Early recap drafts included an expected inbox-placement lift and a revenue figure that nothing had measured. Both came out before anything went to the client.
- **Credit given to the wrong fix.** A deliverability catch was credited to one security setting when another had made it. Corrected before the handoff shipped.
- **Old notes treated as current facts.** While I built my own website, Claude wrote that I'd served "mid-market companies and agencies since 2024." It came from stale notes. I'd had one client, starting in 2025. I caught it, and we rewrote every place it appeared.

None of these were dramatic. That's the point. A confident, plausible, slightly wrong sentence is the most expensive kind, because nobody double-checks it.

## What I changed before the next client

When the engagement ended, I audited my own Claude setup the way I'd audit a customer's. It was built for one client.

- **The client was visible everywhere.** Their voice Skill and notes sat at the account level, where any future client's work could see them. Now each client gets its own Project, account-level Skills hold methods only, and everything about a client is deleted when the engagement ends. That's [`client-engagement-ops`](../skills/client-engagement-ops/SKILL.md).
- **One portal at a time.** HubSpot's connector holds one portal per Claude account, and I was about to offer two builds at once. Every session and scheduled run now checks the portal ID first and stops on a mismatch.
- **Rules lived in prompts.** "Never send" and "read-only" now live in each connector's tool settings, because an overnight run has nobody there to ask.
- **History that never existed.** Two scheduled tasks saved their history inside a run that starts empty every time. State now lives in Project docs.
- **The audit I sell wasn't runnable.** It existed as a sales page and a sample. Now it's a Skill: [`hubspot-revenue-audit`](../skills/hubspot-revenue-audit/SKILL.md).

Before I saved the new Skills, a separate Claude agent reviewed them cold. It found that the audit's read-only promise depended on Claude behaving, and that my offboarding timing contradicted my own privacy terms. Both are fixed.

## What it taught me about customer success

I spent six months as Claude's customer, with my own client depending on the output. What made adoption stick wasn't a clever prompt. It was the same things a customer success manager builds for a customer's team:

- **A first workflow that wins visibly,** so the habit forms.
- **Written rules and a reliability register,** so trust survives the first wrong answer.
- **The expert's method turned into Skills,** so quality doesn't depend on one person.
- **Work that runs on a schedule,** so usage grows without anyone remembering to open a chat.
- **Value reported honestly,** labeled and measured, so leaders keep paying for it.
- **A review of your own setup after every customer,** so the lessons land in the method and the customer's data doesn't stay behind.

That's the playbook in [`playbook/adoption-playbook.md`](../playbook/adoption-playbook.md).

## What it added up to

The client's review, unprompted, said the work "ultimately touched nearly every part of our CRM, automation and email infrastructure," and that the handoff documented "what had been completed, what should be monitored going forward, and anything that may need attention in the future." What I can and can't prove from the engagement is in the [evidence ledger](evidence-ledger.md).
