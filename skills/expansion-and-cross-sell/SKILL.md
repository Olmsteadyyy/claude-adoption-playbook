---
name: expansion-and-cross-sell
description: Find revenue inside existing accounts through attach rate, cross-sell, package design, coverage risk and retainer conversion. Use when growing accounts, not finding new ones.
license: MIT
metadata:
  version: 1.0.0
---

# Expansion & Cross-Sell

## When to use

Find and act on revenue inside the existing customer base — attach rate, product adjacency, package design, account coverage risk, and ad-hoc-to-retainer conversion. Use whenever the user says "cross-sell," "expand the account," "average order value," "attach rate," "what else do they buy," "bundle," "upsell," "retainer conversion," "grow existing accounts," or asks where revenue is hiding that is not new-customer acquisition. Also use when a transaction-value or purchase-frequency lever needs moving and nobody has looked at what was actually purchased. For pulling line-item data, see hubspot-portal-queries. For measuring whether the resulting motion worked, see incrementality-and-holdouts.

## Role

You work the three levers of customer lifetime value and you name which one a
proposal moves before it ships. A proposal that cannot name its lever does not
ship.

| Lever | Moved by | Measured on |
|---|---|---|
| **Average transaction value** | Attach rate, bundling, package design, price | Line items, products, quotes |
| **Purchase frequency** | Trigger detection, ad-hoc-to-recurring conversion | Transaction recency and interval |
| **Customer lifespan** | At-risk detection, coverage, retainer retention | Subscription status, contact coverage, absence |

**Lifespan is usually the least instrumented and the most valuable.** Churn in a
services business is not an event, it is an absence — nobody cancels, they just
stop calling. Absences are invisible unless something is built to see them.

The reflex in this work is to reach for acquisition. Resist it until the base is
worked. In a business with high repeat purchase, the cheapest revenue is
already inside the customer file.

---

## Protocol 1 — Read the line items before proposing anything

Line items and products are the most under-queried objects in most portals and
the only place that records what was actually bought. Everything below depends
on this pull.

Produce four tables:

1. **Frequency and revenue by product.** Count, sum, and average per product.
   Sort by revenue and separately by count — the highest-count product and the
   highest-revenue product are usually different, and they play different roles.
2. **Attach rate.** For each product, the share of transactions containing it,
   and the average number of distinct products per transaction. An average near
   1.0 means nothing is being cross-sold and the entire lever is unexploited.
3. **Co-occurrence.** For every ordered pair of products A and B, how often B
   appears in the same transaction as A, or within a defined window after it.
4. **First-purchase distribution.** Which product most often opens a
   relationship. That product is the acquisition wedge whether or not anyone
   designed it that way, and it deserves different treatment from the rest.

### Adjacency, done properly

Raw co-occurrence ranks popular products first and tells you nothing. Use lift:

```
lift(A → B) = P(B | A) / P(B)
```

A lift meaningfully above 1 means buying A genuinely predicts buying B. Then
weight by the revenue of B to get expected value per prompt, and rank pairs by
that rather than by frequency.

Guardrails: require a minimum support (a pair seen enough times to mean
anything — state your floor), check the direction of the pair separately since
A→B and B→A are different offers, and discard pairs where the association is
just bundling by the same invoice line rather than a real sequential purchase.

Where the data is too thin to compute lift, say so, use a
practitioner-constructed adjacency map as an explicit **provisional placeholder**,
and mark the date it should be replaced by computed values.

---

## Protocol 2 — Convert ad hoc to recurring

The highest-LTV transition in a services business, and typically the largest
single identified number in a base-revenue plan.

**Find the candidates by behavior, not by opinion.** The profile is high
transaction frequency, short and consistent inter-purchase interval, and
repeated purchase of the same one or two products. Those accounts are already
behaving like retainer clients while being billed like ad-hoc ones — which
means the conversion is an administrative change, not a sale.

Rank candidates by annualized value of the proposed recurring arrangement, not
by trailing spend.

Three things to state honestly when proposing this:

- **It requires a human sales motion.** Lifecycle can identify, prime, and time
  the conversation. It cannot close a retainer. Name the owner.
- **The stated value is an ESTIMATE with a method.** Annualizing a proposed
  monthly figure across candidate accounts is arithmetic, not a forecast.
  Present it as identified opportunity, never as expected revenue.
- **Recurring revenue leaks.** A manually administered retainer book loses
  accounts through paused billing, failed payment, and quiet non-renewal, none
  of which announce themselves. Audit the recurring object's status buckets
  before celebrating any conversion — paused and unpaid are revenue at risk and
  cheaper to recover than a new retainer is to sell.

---

## Protocol 3 — Coverage as an expansion constraint

Account coverage is the quietest risk in a base-revenue program.

Pull contacts per paying account and bucket at zero, one, two, three-plus.

- **Zero contacts:** revenue with no addressable relationship. Cannot be
  marketed to, cannot be suppressed, cannot be reactivated. This is a data
  reconciliation task before it is a marketing one.
- **One contact:** single-threaded. The account survives on one person. When
  they change firms — and in brokerage they do — the account leaves with them
  and nothing in the system registers a loss. Every top account sitting at one
  contact is a named risk, and coverage expansion is a legitimate expansion
  motion in its own right.
- **Duplicated companies:** fragment history, understate account value, and
  cause the same account to appear in two segments with two different stories.
  Dedupe before ranking accounts by value.

Coverage does not feel like revenue work. It is the precondition for all of it.

---

## Protocol 4 — At-risk detection

Build the flow that sees absence.

Define the at-risk threshold from **observed inter-purchase interval**, not from
a round number. Pull the distribution of gaps between consecutive transactions
per account, and set the threshold at a percentile of that distribution — an
account that historically buys every six weeks is at risk at ten weeks; an
account that buys twice a year is not.

Segment the threshold by account tier. Applying one dormancy window to a
95-transaction account and a 2-transaction account produces alerts nobody trusts.

Combine with the leading indicators that move before revenue does: sales
conversation volume, meeting frequency, site activity. Revenue is a lagging
measure of a relationship that cooled months earlier.

---

## Proposing an expansion motion

State each of these or do not ship it:

1. **Which CLV lever** it moves, and which object measures it.
2. **The size of the opportunity**, labeled ESTIMATE, with the method in the
   same sentence.
3. **Who owns the human step**, if there is one.
4. **How it will be measured** — holdout, or pre/post with the limitation
   stated. See incrementality-and-holdouts.
5. **What could make it not work**, named before anyone asks.

**When a new lever surfaces that carries quantifiable revenue — recurring
revenue at risk, cross-sell headroom, coverage risk on a top account — say so
and recommend it be added to the committed plan.** The identified-opportunity
list is not closed. Working silently outside the committed sources is how the
work becomes invisible; adding to the list is how it compounds.
