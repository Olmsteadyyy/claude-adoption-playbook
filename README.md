# Claude adoption playbook

**How I ran a client engagement on Claude, and how I'd help a customer's team do the same.**

I'm Kyle Olmstead. I started in sales (President's Club at Smartsheet, the largest deal in Zipwhip's history), moved into lifecycle marketing and CRM, and I'm now moving into customer success. For the past six months I've been Claude's customer: I ran a client engagement on it end to end, with my own client depending on the output. This repository is what I built, what broke, and the playbook I'd bring to a customer's team.

## Start here

| If you have | Read |
| --- | --- |
| 5 minutes | [The case study](case-study/running-a-consultancy-on-claude.md): the setup, the rules, and every silent failure I caught |
| 10 minutes | [The adoption playbook](playbook/adoption-playbook.md): how I'd roll Claude out to a team, phase by phase |
| A consumption-priced product | [Reading usage for expansion and risk](playbook/usage-signals.md) |
| A Claude account | [The Skills](skills/) and [templates](templates/) you can use today |

## By the numbers

| Measure | Value | Label |
| --- | --- | --- |
| Time with Claude since April 2026 | About 300 hours | Estimate; 175 of it measured from my account export |
| Conversations, April to July | 280 | Measured |
| Tool actions Claude ran for me, April to July | About 1,250 | Measured |
| Custom Skills written and used | 11 | Counted |
| Client engagement run on it | 222 hours, 5.0 rating | Verified by Upwork |

What I used: Projects, custom Skills, memory, connectors (HubSpot, Gmail, Google Drive, Slack, Stripe), Claude in Chrome for screens with no API, scheduled tasks that ran overnight, artifacts, and Claude Code.

## Why this is customer success work

Lifecycle marketing is keeping and growing customers through software. Customer success is the same job done through a relationship. The overlap is most of this repository:

| What a CSM does | Where it shows up here |
| --- | --- |
| Drive adoption and change management | [Adoption playbook](playbook/adoption-playbook.md), phases 1 to 5, including train-the-trainer and a small center of excellence |
| Spot underuse and expansion in usage data | [Usage signals](playbook/usage-signals.md) and [`expansion-and-cross-sell`](skills/expansion-and-cross-sell/SKILL.md) |
| Prove value in a way finance believes | [`incrementality-and-holdouts`](skills/incrementality-and-holdouts/SKILL.md) and the [evidence ledger](case-study/evidence-ledger.md) |
| Run success plans and business reviews | [`lifecycle-operating-rhythm`](skills/lifecycle-operating-rhythm/SKILL.md) and the [Friday recap](templates/weekly-recap.md) |
| Learn a customer's industry fast | [`cre-domain-context`](skills/cre-domain-context/SKILL.md), the pattern for any vertical |
| Earn trust with executives | The [case study's](case-study/running-a-consultancy-on-claude.md) review rules, and the client's 5.0 review |
| Build with AI daily | All of it |

## What's here

```text
case-study/   The engagement: setup, rules, failures, and an evidence ledger
playbook/     Rolling Claude out to a team; reading usage for expansion and risk
skills/       Ten Skills I used in production, plus a voice-Skill template
templates/    Project instructions, reliability register, overnight sweep, Friday recap
docs/         How I prompt now, with real before-and-after examples
scripts/      Checks every Skill and packages it as an upload-ready zip
```

## What's not here

No client data, no client figures, and not the client's voice Skill, which is built from a real person's email and stays private. Every number in this repository is labeled with where it comes from. The client is available as a reference on request.

## Built with Claude

I built this repository with Claude, which seemed like the only honest way to make it. Claude drafted from my project records and Skills; I chose what went in and checked every claim against my records.

## License

MIT. Use anything here; credit is appreciated.

**Contact:** [linkedin.com/in/kyleolmstead](https://www.linkedin.com/in/kyleolmstead)
