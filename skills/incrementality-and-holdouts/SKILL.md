---
name: incrementality-and-holdouts
description: Design holdouts and separate attributed from incremental revenue before a result is reported. Use when asked what something drove, or when a result looks too strong.
license: MIT
metadata:
  version: 1.0.0
---

# Incrementality & Holdouts

## When to use

Design holdouts, size experiments, and separate attributed revenue from incremental revenue before any lifecycle result is reported to a client or stakeholder. Use whenever the user says "how much did this drive," "what did the flow generate," "attributed revenue," "did it actually work," "holdout," "control group," "A/B test," "is this significant," "report the results," or is about to ship a flow that will later need a defensible number. Also use when a reported result looks strong, because strong lifecycle numbers are usually selection effects. For pulling the underlying data, see hubspot-portal-queries. For the reporting cadence itself, see lifecycle-operating-rhythm.

## Role

You are the person who asks whether it would have happened anyway.

Lifecycle marketing has a structural credibility problem: the flows that look
best are the ones that trigger on the strongest buying signal. A post-purchase
cross-sell fires at people who just bought. A cart flow fires at people who
already chose the product. A reactivation flow fires when someone came back to
the site. Attribution credits the email; the buying intent preceded it.

This is not a rounding error. In lifecycle programs the attributed figure
routinely runs several times the incremental one. **The most common way this
work gets discredited is not underperformance — it is presenting an attributed
number, having someone eventually test it, and losing the whole program's
credibility at once.**

Get ahead of it by reporting both from month one, when the gap is a
methodological fact rather than a confession.

---

## The three numbers

Report all three, always. Never attributed alone.

| Number | Definition | What it is good for |
|---|---|---|
| **Attributed** | What the platform credits to the channel under its own attribution window | Comparability with the client's other dashboards |
| **Incremental** | Treatment minus holdout, scaled to full population | The actual value of the work |
| **Gap** | Attributed minus incremental, stated plainly | Credibility. Naming it is what makes the incremental figure believable |

The gap is not an embarrassment. It is the measurement. Presenting it as a
normal property of lifecycle attribution — which it is — converts a future
objection into present-day evidence of rigor.

---

## Protocol 1 — Decide the measurement design before the flow ships

Retrofitting a holdout is expensive and usually impossible, because the
population has already been treated. Decide at spec time, not at launch.

**Every flow ships with a persistent randomized holdout where entry volume
supports one.** Where it does not, say so out loud and fall back deliberately.

### Choosing the design

| Situation | Design | Read |
|---|---|---|
| High, steady entry volume | Persistent randomized holdout, 10% | Causal |
| Moderate volume, one-time campaign | Randomized holdout, 20–30% to reach a decision faster | Causal, wide interval |
| Low volume, high value per entry | Named holdout is wasteful; use pre/post baseline | Directional. Label it |
| Entry volume in single digits | No statistical read exists | Report qualitatively. Do not compute a lift percentage |
| Flow cannot ethically withhold (billing, AR, service) | Time-staggered rollout, or hold out on timing rather than on treatment | Causal-ish, state the caveat |

**Persistent beats one-shot.** A holdout that stays held out across the whole
program measures the program, not one send, and it keeps accumulating power
instead of being re-randomized into noise every campaign.

**Randomize at the account level, not the contact level,** where the buying unit
is an account. Two contacts at one firm are not independent observations; one
gets the email, the other hears about it at their desk, and the holdout leaks.

### Sizing, honestly

Before running anything, ask what effect size the available volume could
actually detect. If the flow enters 40 accounts a month and the realistic lift
is a few percentage points on conversion, no design detects it within the
engagement's lifetime.

That is a fine outcome to reach — it just needs saying at spec time. "This will
not produce a statistically readable result; here is the operational signal
we'll watch instead" is a defensible position. Reporting a lift percentage from
n=40 as though it were measured is not.

---

## Protocol 2 — Interrogate a result before believing it

Run every one of these before a number leaves the building.

**Did the holdout hold?** Confirm nobody in the control received the treatment
through another flow, a batch send, a sales touch, or a list upload. Leaked
controls compress lift toward zero and make a working flow look dead.

**Is the population comparable?** Randomization at low n produces unbalanced
groups by chance. Compare the two groups on the obvious pre-period covariates —
prior spend, recency, account size. If they differ meaningfully, the difference
in outcome may be the imbalance.

**Is the window long enough?** In episodic businesses the purchase arrives when
an external event arrives. A 14-day window on a business with a six-month
purchase cycle measures nothing except who happened to be mid-cycle. Set the
window to the observed inter-purchase interval, pulled from data, not assumed.

**Is it one account?** In a business with high revenue concentration, a single
large transaction lands in one arm and swings the result. Report the median and
the count alongside the sum, and say explicitly when one record drives the
outcome.

**What else happened?** Sales activity, a price change, a seasonal cycle, or a
deliverability change during the window. Name the confounder rather than waiting
to be asked.

**Would you believe this if it were negative?** If a favorable result would be
reported and an unfavorable one investigated, the process is not measurement.

---

## Protocol 3 — Attribution is a convention, not a fact

Attribution models are agreements about how to divide credit, chosen before
looking at the data. They are not discoveries. Say which model is in use and do
not switch models between reports — switching mid-program is how a flat quarter
becomes a good one without anything happening.

Known distortions to name when they apply:

- **Last-touch over-credits the final email** and structurally over-credits
  whichever channel sits closest to purchase.
- **Any model over-credits flows triggered on high intent.** The trigger is the
  signal; the email is downstream of it.
- **Click-based windows miss the reader who never clicks** and buys through
  another route. In low-click-rate programs this is most of the audience.
- **Reply-driven conversions frequently attribute to nothing at all** when the
  conversation moves to phone or to a direct thread.

Where attribution and incrementality disagree, incrementality is the answer and
attribution is the context.

---

## Reporting format

```
<Flow or campaign name> — <period>

  Entered:        <n> (treatment <n> / holdout <n>)
  Attributed:     $<a>
  Incremental:    $<i>   (<treatment rate> vs <holdout rate>)
  Gap:            $<a - i>

  Read:           <causal / directional / not yet readable>
  Window:         <n> days, chosen because <reason>
  Caveats:        <named, or "none material">
```

Where the read is not yet causal, say so in the same line as the number, not in
a footnote.

**Report what did not work.** A results review with no failures reads as
marketing rather than measurement, and it undermines the credibility of every
figure printed next to it. A named failure with what was learned from it is the
single strongest signal that the favorable numbers were measured rather than
selected.

---

## Prohibited

- Reporting attributed revenue alone
- A lift percentage computed on a population too small to support one
- Changing the attribution model or window between reporting periods
- A forecast, or a projected percentage of any kind. State what will be known
  and when
- Describing a pre/post baseline as though it were a holdout
- Quietly dropping a flow from the report in a period where it underperformed
