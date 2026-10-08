# Reading usage for expansion and risk

*I first worked this out in a proposal for an AI company's enterprise growth team: how to turn product usage into a list of accounts worth a person's time. This is the general version, for any product priced by consumption or by seat.*

## The core idea

The same signal predicts growth and churn. An account hitting its limits is either about to buy more or about to evaluate a competitor. Whoever reaches them first decides which. So a strong usage signal is never just good news; it's a clock.

## Signals worth watching

**Intensity: is this account serious?**

| Signal | Why it matters |
| --- | --- |
| Spend or usage growth, month over month | Moving from trial to production |
| Depth: moving from basic to advanced features | Complexity signals commitment more than raw volume does |
| Active days in the last 30 | Habit, not a one-off spike |
| Rate-limit or capacity hits | Outgrowing the current plan, or about to go elsewhere |
| More users, keys or workspaces under the same company | Spreading beyond the first team |

**Underuse: is the customer getting what they paid for?**

| Signal | What to do |
| --- | --- |
| Seats with no activity in 30 days | Enablement for those users before renewal, not after |
| Consumption well below the committed amount | A use-case session with the team that bought it |
| Usage concentrated in one person | Find the second team before that person leaves |

**Context: is this account worth an hour of someone's time?** Company size, industry fit, and whether the users are a real team on a company domain or one person on a personal email.

## Three tiers, three clocks

| Tier | Entry | Response |
| --- | --- | --- |
| Watch | Intensity rising, context unclear | Automated enablement, weekly digest to the owner |
| Engage | Intensity and fit both strong | Owner reaches out within a day, with the usage summary attached |
| Act now | Sharp growth, repeated limit hits, or a renewal at risk | Alert the owner and call the same day |

## The half nobody builds: what not to route

A scoring model without suppression floods the team with noise, and they stop trusting it within weeks.

- Personal emails with very low usage: product-led nurture, not a person.
- Students and researchers: their own program.
- Competitors: never routed to outreach.
- Accounts already in a negotiation: nothing automated crosses an open deal.

## Proving it works

Hold back a share of qualifying accounts from routing for a quarter. Compare what happened to the routed accounts with the held-back ones. That gives an incremental number instead of an attributed one, which is the number that survives a skeptical review.
