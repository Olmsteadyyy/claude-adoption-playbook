# Skills

Eleven Skills I wrote and used on a live client engagement. Ten are published as I used them, with client figures replaced by generic wording. The eleventh, a voice Skill built from a client executive's real email, stays private; [`client-voice-template`](client-voice-template/) is its structure with the content removed.

They're tuned for B2B services companies on HubSpot. The methods travel; the platform details may not.

## What each one does, and its customer success equivalent

| Skill | What it does | The problem it solved for me | The same job in customer success |
| --- | --- | --- | --- |
| [`lifecycle-diagnostics`](lifecycle-diagnostics/SKILL.md) | Audits a program and checks whether reported numbers are real | The CRM's revenue figure was a fraction of what was actually billed | An account health assessment that starts from billing or usage truth |
| [`hubspot-portal-queries`](hubspot-portal-queries/SKILL.md) | Pulls and labels data from HubSpot before any number is used | Filters failed silently and counts looked right when they weren't | Verifying usage data before it goes into a QBR |
| [`lifecycle-data-architect`](lifecycle-data-architect/SKILL.md) | Designs fields, segments and the customer definition | "Customer" in the CRM didn't match who was actually paying | Getting a new customer's data model right during onboarding |
| [`lifecycle-workflow-engineer`](lifecycle-workflow-engineer/SKILL.md) | Specs automations with entry rules, exits, suppression and holdouts | Flows were designed on fields that were never filled in | Implementation planning that checks dependencies first |
| [`lifecycle-operating-rhythm`](lifecycle-operating-rhythm/SKILL.md) | Runs the weekly, monthly and quarterly review cadence | Without a rhythm, the program drifted between client requests | Success plans and the QBR cadence |
| [`expansion-and-cross-sell`](expansion-and-cross-sell/SKILL.md) | Finds growth inside existing accounts, plus coverage and churn risk | Nobody had looked at what customers actually bought | Expansion plays, multi-threading, and at-risk detection |
| [`incrementality-and-holdouts`](incrementality-and-holdouts/SKILL.md) | Separates what the work caused from what would have happened anyway | Strong-looking results were mostly selection effects | Documenting value realized in a way finance believes |
| [`deliverability-engineer`](deliverability-engineer/SKILL.md) | Diagnoses email authentication and sender reputation | Email was at risk of landing in spam before any campaign ran | Spotting technical risk before it becomes a customer escalation |
| [`lifecycle-copywriter`](lifecycle-copywriter/SKILL.md) | Writes lifecycle messages to one goal, in the client's voice | Drafts sounded generic and offered things the client didn't sell | Customer communications that sound like the account team |
| [`cre-domain-context`](cre-domain-context/SKILL.md) | Commercial real estate vocabulary, buyers and purchase triggers | Claude wrote like an outsider to the client's industry | Learning a customer's vertical fast, such as banking or insurance |
| [`client-voice-template`](client-voice-template/) | Builds a voice Skill from one person's real sent messages | Every draft needed rewriting before an executive would send it | Keeping an executive sponsor's communications consistent |

## Using them

Each folder is a Skill: a `SKILL.md` file with a name and description at the top, followed by instructions. Descriptions are kept under the Claude apps' 200-character limit; the fuller trigger text I wrote for each one sits under "When to use" in the file.

- **Claude apps:** run `python scripts/package_skills.py` from the repository root. It checks every Skill against the upload requirements and writes a ready-to-upload zip for each one to `dist/`. Upload the zip as a custom Skill, then turn it on under Customize > Skills. Code execution must be enabled. See [Use custom Skills](https://support.claude.com/en/articles/12512198-use-custom-skills).
- **Claude Code:** copy the folder to `~/.claude/skills/<skill-name>/` for yourself, or to `.claude/skills/` inside a repository to share it with your team. See [Claude Code Skills](https://code.claude.com/docs/en/skills).

Read a Skill before you use it. Several assume HubSpot, invoices as the source of truth, and a services business; change those assumptions to fit yours.
