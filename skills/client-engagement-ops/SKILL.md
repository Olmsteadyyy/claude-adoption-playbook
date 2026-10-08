---
name: client-engagement-ops
description: Run a HubSpot client engagement in Claude from signed contract to offboarding, covering Project setup, portal guard, weekly rhythm, approval gates, handover and data deletion.
---

# Client Engagement Operations

## The one rule everything else follows

**One client, one Project.** Anything that names a client, quotes their data or
carries their voice lives in that client's Project: its instructions, its
docs, its memory. It never goes into an account-level Skill, account-level
memory, another client's Project, the practice Project, a public repository or
marketing. Account-level Skills hold methods only.

Claude drafts and the consultant sends. Every client-facing word and every change to a
client portal passes a gate only the consultant clears, by hand.

## Starting a client

Run this the day a contract starts, before any portal work. That includes an
audit-only client: the audit's portal guard reads the portal ID from this
Project.

1. **Create the Project.** Name it `<Client> | <Offer>`. Paste the instruction
   skeleton below and fill every bracket. Leave nothing as "TBD" without an
   owner and a date.
2. **Add the working docs**, empty to start:
   - `scope.md`: the signed audit order or build blueprint and SOW
   - `reliability-register.md`: which data can be trusted, updated as found
   - `decisions.md`: dated decisions, who made them, and open questions with
     their age
   - `build-log.md`: what shipped each day; the Friday recap is drafted from it
   - `time-log.md`: hours per session; the only way to know whether a fixed
     price holds
   - `history/`: Monday briefs, Friday recaps, overnight sweep results
   - `voice.md` only if Claude will draft anything the client sends in their
     own name, built from their real sent messages
3. **Connect the portal.** The HubSpot connector holds one portal at a time.
   Connect this client's portal using the invited user, and tell the client
   the Claude app is being connected and when it will be removed. For a build,
   set update actions to require approval. For an audit, turn the create and
   update tools off; "ask first" does not protect an overnight run.
4. **Set up the scheduled tasks** below, each limited to the connectors it
   needs, none with a send tool, each starting with the portal guard.
5. **Calendar:** the weekly checkpoint with the client's decision owner, and a
   Friday block for the recap.

### Project instruction skeleton

```markdown
# [Client] | [Revenue Audit / 90-Day Build / Monthly Tune-Up]

## Client
[What they sell, to whom, how they get paid. Size. Team.]
Decision owner: [name, role]. Other contacts: [names, roles].
Contract: [Upwork or direct]. Start [date]. Milestones [dates].

## Portal
HubSpot portal ID: [id]  ← the portal guard checks this
Hubs and tiers: [ ]. Timezone: [ ]. Currency: [ ].
Integrations: [accounting system and sync direction, others].

## How this business makes money
Money object: [invoices / deals / subscriptions], confirmed by live pull on [date].
[One paragraph on what drives repeat purchase or churn.]

## Scope
In scope: [from the signed blueprint]. Out of scope: [ ].
Anything new goes through change control.

## Non-negotiables
- Portal guard before any query or click.
- Label every number LIVE PULL, RECORD, ESTIMATE or UNKNOWN.
- No forecasts or promised percentages.
- Every workflow built off; the consultant activates after counts reconcile.
- Nothing reaches the client or their contacts without the consultant.
- [Client-specific rules.]

## Reliability register
See reliability-register.md. Check it before building on any field.

## Voice
The consultant's recaps: their own writing style. Copy sent in the client's name:
voice.md only, and flagged for the client's review.
```

Keep the instructions short. Long reference tables belong in the docs, where
they are read when needed instead of loaded into every conversation.

## The portal guard

Run it at the start of every session and every scheduled run that touches
HubSpot.

1. Call `get_user_details` and read the portal ID.
2. Compare it with the ID in this Project's instructions.
3. If they differ, or the connector is not connected: **stop**. Say which
   portal is connected and which was expected. Do not query, draft from
   portal data, or click anything.

In the browser, the portal ID appears in the HubSpot URL. Check it before any
click that changes something, every time, including after switching tabs.

## Who changes the portal

Connector approvals do not cover the browser. So Claude changes a client
portal through the browser only in a live session with the consultant present, and
pauses for their OK before every save, publish or activation. Never in an
unattended or scheduled run. "Every write is the consultant's click" means exactly that:
The consultant makes the change or approves it as it happens.

## Gates

| Gate | When | Claude | The consultant |
| --- | --- | --- | --- |
| G0 | Lead arrives | Drafts the reply | Reads, edits, sends. On Upwork, everything stays on Upwork until a contract starts |
| G1 | Audit delivery | Drafts findings and plan (`hubspot-revenue-audit`) | Checks every number, sends |
| G2 | Build offer | Drafts the SOW and the offer | Sends; client signs |
| G3 | Foundation | Drafts specs and the property dictionary | Client signs the blueprint; the consultant makes or approves every portal change, live |
| G4 | Automation | Drafts workflow specs and copy | Counts reconcile; every workflow still off |
| G5 | Launch | Drafts the activation checklist | Client approves copy in writing; the consultant seed-tests and activates |
| G6 | Handover | Drafts runbooks | The consultant runs walkthroughs; client removes the consultant's user |
| G7 | Fix window closes; 30 days after launch | Drafts the review request and readout | The consultant sends |

## The weekly rhythm

- **Monday brief (me to me).** What shipped against last week's three
  priorities, what slipped and for how long, this week's three priorities each
  tied to a number or a dependency, anything blocked and on whom. Blunt.
- **Mid-week checkpoint.** Draft an agenda from `decisions.md`: open decisions
  with their age, anything near the three-business-day clock-stop.
- **Friday recap.** Drafted from `build-log.md`, in the consultant's own writing style,
  as a Gmail draft addressed to the consultant (Gmail attached with its draft tool only;
  if a task can't be limited that way, save the recap to the Project
  instead). Subject: `Week [n] of 13 [what shipped]`.
  Shipped, next, the one decision needed and its date, on track or paused and
  why. A quiet week is reported as quiet.
- **Every session:** append to `time-log.md` and `build-log.md`.

## Scheduled tasks per client

Each one is its own scheduled task. Limit each to the connectors it needs.
Never attach a tool that can send email, post a message or submit anything on
a client's or Upwork's behalf; Gmail goes on with its draft tool only. State
lives in the client Project's docs, written as the run goes, because every run
starts fresh and keeps nothing.

**Overnight sweep** (weekdays, early morning): portal guard; read the
reliability register and build log; run only the checks the connector can
reach (new duplicate companies, records created without an owner, marketing
email bounces and unsubscribes, fill rates on the register's fields, new or
changed invoices); list anything it can't reach, such as workflow errors, as
"not checked"; write at most five to-dos to `history/YYYY-MM-DD-sweep.md`.
Read-only.

**Monday brief** (Monday morning): as above, saved to
`history/YYYY-MM-DD-monday.md`.

**Friday recap draft** (Friday late morning): portal guard; draft from the
build log; save as a Gmail draft to the consultant and to
`history/YYYY-MM-DD-friday.md`. Never addressed to the client.

**One-time reminders at handover:** the readout, 30 days after the actual
launch date, and the review request, when the 14-day fix window closes. Put
both on the consultant's calendar too, because offboarding deletes the client's tasks.
On Upwork, feedback opens when the contract ends: end it when the fix window
closes and ask the same day (check Upwork's current feedback window).

If two clients are active and only one portal can be connected, only the
connected client's tasks can read HubSpot. The other client's tasks either
skip the portal (and say so in their output) or run from a separate setup with
its own access. Never let a task fall back to whatever portal is connected.

## Change control

When a request falls outside the signed scope, draft the change order: the
request in one line, then three options (swap for equal planned work, add a
paid milestone, or hourly with a cap). Nothing out of scope starts until the
client picks one in writing.

## Handover

- A runbook page for every workflow, written from what is actually in the
  portal: trigger, exit, owner, dependencies, what breaks it, how to pause it.
- A property dictionary from the portal's live property definitions.
- The reliability register, updated to the handover date.
- Two recorded walkthroughs. Browser recordings of each workflow make good
  training material.
- Baseline numbers, each labeled and dated.
- Before the consultant's user is removed, reassign everything it owns: workflow
  notifications, report and dashboard owners, tasks, sequences. A workflow tied
  to a removed user can stop.
- The client removes the consultant's user. The consultant can't check the portal after that, so
  they give the client's owner a short check to run 24 hours later (each
  workflow's history shows enrollments and no errors) and ask them to reply.
- Schedule the readout and review-request reminders, and put both on the
  calendar.

## Offboarding

the consultant's privacy terms say client data is used only for that client and deleted
at handover, and that access is removed at handover. The readout comes 30 days
later, so offboarding runs in two steps. The SOW should say exactly this: what
is kept until the readout (aggregate baseline numbers and working notes, never
contact data) and that everything is deleted after it.

**At handover:**

- [ ] Final docs exported and handed to the client; tell them the PDFs are the
      copies that last, because links are deleted at the end
- [ ] Exports holding contact data, finance files, recordings and downloads
      deleted from Drive, Gmail attachments and the computer
- [ ] The consultant's user removed by the client; the HubSpot connector disconnected,
      or reconnected to the next client
- [ ] Any client-provided account (enrichment tools, Slack guest, DNS, DMARC
      report mailboxes) disconnected or handed back
- [ ] Client scheduled tasks disabled, except the readout and review reminders

**After the readout** (or when a Tune-Up ends, or when an audit-only client's
credit window closes without a build):

- [ ] The readout drafted from numbers the client provides: a temporary
      view-only invite for the readout week, or the specific reports exported
- [ ] Client artifacts deleted, the remaining scheduled tasks deleted, recap
      drafts deleted from Gmail
- [ ] Client voice doc deleted; no client-specific Skill left installed
- [ ] Account-level memory checked for the client's name; the consultant asks Claude to
      forget anything found
- [ ] The client Project deleted, with its chats and memory
- [ ] Lessons kept **without** names or figures: add new silent failures and
      platform limits to `hubspot-portal-queries`, and new patterns to the
      method Skills

The last item is how the system improves: every engagement leaves the method
Skills better and leaves no client data behind.

Files uploaded to Upwork stay in Upwork's records; that is Upwork's, not
the consultant's, to delete.

## Monthly Tune-Up

Up to 8 hours a month with a three-month minimum. Access continues under the
Tune-Up contract, and the client keeps its Project until the Tune-Up ends;
offboarding runs then. On the first business day of
each month, run the health check with `lifecycle-operating-rhythm` (data
quality, workflow errors, deliverability), list fixes in priority order with
time estimates, and stop planning at 8 hours. Track hours in `time-log.md`. The
monthly readout is one page: what was checked, what was fixed, what to watch.

## Never

- Client names, data or screenshots in marketing, the sample audit, public
  repositories or another client's work
- A shared password, or Claude typing any password
- A send tool on an unattended task
- A workflow switched on before its counts reconcile
- A forecast or promised percentage in anything the client reads
