---
name: client-voice-template
description: Template for a voice Skill built from one person's real sent messages. Copy it, rename it after the sender, and fill each section before Claude drafts anything in their name.
license: MIT
---

# [Sender] Voice

*Template. The Skill I used in production was built from a client executive's real sent email, so it stays private. This is its structure with the content removed.*

A voice Skill is not a tone description. It is a set of rules derived from what one person actually sends and actually rejects, with the evidence kept alongside. Write every rule so a stranger could check a draft against it.

## Read these before writing

- `references/capability-boundaries.md`: what this sender can and cannot offer. Most voice failures are capability failures.
- `references/channel-adaptation.md`: what carries over to channels beyond email.
- `references/corpus-evidence.md`: the sent messages and rejections every rule comes from.

## Who is writing

- Name, role, and what they are accountable for.
- How the reader knows them, and what the reader already trusts them on.

## The rule that matters most

The one rule that, if broken, makes a draft unsendable. Write it in one sentence, then show one failing and one passing example from the corpus.

## Who is reading

| Segment | What they need from this sender | What reads as wrong |
| --- | --- | --- |
| | | |

## Structure

- Typical length by relationship depth. (In my production Skill, length shrank as the relationship deepened.)
- Order of a message: opening, substance, ask.

## The ask ladder

From smallest to largest ask, with when each one is earned:

1.
2.
3.

## Greeting and personalization

- Greeting conventions, and the fallback when a first name is missing.
- Which details may be merged automatically, and which must be typed per send.

## Voice mechanics

- Sentence length and rhythm.
- Contractions, punctuation, formatting.
- Words and constructions this sender uses that a generic writer would not.

## Banned

- **Phrases:**
- **Punctuation and format:**
- **Structures:**

## The capability gate

Before any draft offers something, check it against `references/capability-boundaries.md`. A draft that offers what the sender does not sell fails, however good it sounds.

## Self-review

Before returning a draft, answer each in writing:

1. Which rule above could this draft break, and does it?
2. Does it offer anything outside the capability list?
3. Would the sender recognize every sentence as theirs?

## Standing decisions

Decisions the sender has made that Claude must not reopen, each with its date and source.

## What this Skill is derived from, and what it isn't

- The corpus: how many messages, which channels, which date range.
- What the corpus does not cover, so Claude says so instead of guessing.
