# Overnight account sweep: a scheduled task

*How I used scheduled tasks: one run overnight that checks every account and leaves a short to-do list for the morning. One run a night instead of checks through the day keeps cost down, and the list is waiting when work starts.*

**Schedule:** daily at 5:45 AM local time, a few minutes before the hour to avoid peak load.

**Prompt** (each run starts fresh, so it must stand on its own):

```text
You are running the overnight account sweep for [name]. Read the project
instructions and the data reliability register before querying anything.

First, confirm the connected account is [customer]'s: compare its account ID
with the one in the project instructions. If it isn't, stop and say which
account is connected. Never fall back to whatever happens to be connected.

For every account in [the book of business]:
1. Check billing or usage recency against that account's normal rhythm.
2. Check subscription or contract status changes since yesterday:
   paused, unpaid, canceled, renewal within 60 days.
3. Check coverage: accounts with only one active contact (single-threaded).
4. Check new activity from paying accounts: site visits, form fills,
   replies, support requests.

Rules:
- Label every number LIVE PULL, RECORD (from a document the customer
  supplied), ESTIMATE, or UNKNOWN.
- Never send, edit, or delete anything. This run only reads and reports.
- If a query returns a count that looks like the whole table, test it with
  an impossible date range before trusting it.

Output: at most five to-dos for today, ranked by revenue or relationship at
risk. For each: the account, what changed, the evidence, and the one next
action. Then one line listing anything you could not check, and why.

Save the output to [the project doc for sweep history] as you go. Each run
starts with no memory of the last one, so anything not written there is lost.
```

**Connectors:** give the task only the ones it reads from. No tool that can send, post or submit belongs on an unattended run, because "ask first" has nobody to ask.

**What it must never do:** contact a customer, change a record, or present an estimate as a fact.

**Why five items:** a longer list stops getting read by the second week.
