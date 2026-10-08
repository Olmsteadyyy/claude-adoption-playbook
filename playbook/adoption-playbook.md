# Rolling Claude out to a team: the playbook I'd bring

*Where this comes from: about six months of running my own client work on Claude, alone. I haven't rolled Claude out across an enterprise. I have adopted it end to end as the customer, made most of the mistakes a team would make, and written down what fixed each one. This is the order I'd do it in for a customer's team.*

## Phase 0: Find the work worth handing over

Before any setup, list the team's recurring work with two numbers next to each item: hours a week, and the cost of an error.

Start with one workflow that is:

- **Frequent,** so the team feels the difference within two weeks.
- **Checkable,** so a person can tell quickly whether Claude got it right.
- **Visible to a leader,** so the win travels.

For me that was the weekly client recap and the data pulls behind it. It ran every Friday, every number could be checked against the source, and the CEO read it.

## Phase 1: One Project per account, written as rules (weeks 1 and 2)

Give each account or workstream its own Project, and write the instructions as an operating manual, not a persona. Mine said what the business sells, which data could be trusted, how every number had to be labeled, and what never reached the client without my review. Template: [`templates/project-instructions.md`](../templates/project-instructions.md).

Add a data reliability register on day one. It is the file that keeps Claude from confidently building on bad data. Template: [`templates/reliability-register.md`](../templates/reliability-register.md).

**Done when:** the first workflow runs in Claude every week, and the person who owns it would object if you took it away.

## Phase 2: Turn the best person's method into Skills (weeks 3 to 6)

A sign a Skill is needed: someone has pasted the same instructions into Claude three times.

Three kinds earned their place for me:

1. **Method Skills,** which carry how an expert does the work: how to audit an account, design a measurement, or check deliverability. Ten of mine are in [`skills/`](../skills/).
2. **Domain Skills,** which carry the customer's industry: its vocabulary, its buyers, what triggers a purchase. With one in place, Claude stopped writing like an outsider to commercial real estate. That's the same problem a customer in banking or insurance has.
3. **Voice Skills,** built from one person's real sent messages, with the evidence for every rule. Template: [`skills/client-voice-template/`](../skills/client-voice-template/).

**Done when:** a newer team member produces work the expert would sign off on, using the Skills.

## Phase 3: Connect the systems, then check them (weeks 4 to 8)

Connect the tools the work already lives in. I used connectors for HubSpot, Gmail, Google Drive, Slack and Stripe, and Claude in Chrome for the screens that had no API, like HubSpot's report builder.

Connections are where trust is won or lost, because a connected tool can fail without any error. The query tool I relied on silently ignored some filters and returned the whole table. So every connection gets three habits:

1. **Label every number** LIVE PULL, ESTIMATE, or UNKNOWN.
2. **Test with an impossible input.** If a query for an impossible date range returns the same count, the filter isn't working.
3. **Keep one human review gate** on anything a customer, an executive or an inbox will see.

**Done when:** the team trusts a number from Claude because of its label, not because of who asked.

## Phase 4: Let work run without anyone at the keyboard (week 6 onward)

Scheduled tasks moved my day. One run overnight checked every account and left at most five to-dos for the morning, ranked by what was at risk. Template: [`templates/overnight-account-sweep.md`](../templates/overnight-account-sweep.md).

This is also where usage grows on its own, because the work happens whether or not anyone opens a chat.

**Done when:** at least one recurring check runs on a schedule and someone acts on its output most days.

## Phase 5: Make it the team's, not one person's

- **Train the trainer.** The person who built the Skills teaches two others to build and edit them, not just to use them.
- **A small center of excellence.** One owner for the Skills library and the reliability register, with a standing 30 minutes a week to review what broke.
- **Shared, versioned Skills.** Skills live in a shared repository, so a fix reaches everyone at once.

## Measuring adoption and value

| Measure | What it tells you |
| --- | --- |
| People using Claude each week, by team | Whether adoption is spreading or stuck with one champion |
| Workflows running on a Skill or a schedule | Whether usage is habit or occasional |
| Errors caught by the review gate | Whether trust is earned, and where Skills need fixing |
| Hours returned, labeled as estimates | The value story leaders hear first |
| Business outcomes, with a holdout where volume allows | The value story finance believes |

Never forecast a number before it's measured. State what will be known, and when. The method for separating what Claude's work caused from what would have happened anyway is in [`skills/incrementality-and-holdouts`](../skills/incrementality-and-holdouts/SKILL.md).

## What usually goes wrong

- **One confident wrong number ends trust for weeks.** Evidence labels prevent most of it.
- **Instructions written as adjectives.** "Be accurate" does nothing. "Revenue means invoices, because deals capture a small fraction of it" generalizes.
- **Too many Skills at once.** Start with the one the team pastes most.
- **Automation built on empty fields.** Check that the data is filled in before designing anything that depends on it.
- **A single champion.** If one person leaves and usage drops, the rollout never happened.
