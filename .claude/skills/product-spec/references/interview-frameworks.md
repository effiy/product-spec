# Interview — Framework Prompts (5-Why · MoSCoW · Story Mapping)

Prompts the LLM weaves into other banks to deepen vague answers, force prioritization, and structure use-case discovery. All in English.

## 5-Why

Use when an answer is vague, generic, or marketing-speak.

### Trigger Phrases (EN)

EN vagueness: "easy", "fast", "better", "more efficient", "delight", "world-class", "robust", "scalable", "intuitive".

### Prompt Template

- **Round 1 (EN):** "What does '{vague_word}' look like specifically — what does the user see or do?"
- **Round 2 (EN):** "Why is that the right outcome — what changes for them?"
- **Round 3 (EN):** "And why does that matter to the business — link it to a BRD goal."

### Stop Rule

Stop after Round 3 OR when the PO provides a measurable, specific answer. On stop, the LLM proposes a quantified rewrite the PO can accept or edit.

## Engineering-Jargon → Product Reframe

Use when the PO slips into **engineering framing** — describing the solution's mechanics instead of the user's problem and value. The PO is non-technical; when they reach for build-language it usually means they have a real need underneath that hasn't been said in product terms yet. Reframe it back to persona / problem / value — don't follow them into the engineering layer.

### Trigger Phrases (EN)

EN engineering-speak: "database", "schema", "table", "API", "endpoint", "microservice", "cache", "story points", "sprint", "velocity", "tech stack", "framework", "CI/CD", "deploy", "refactor".

### Reframe Template

- **Round 1 — recover the user (EN):** "Let's hold the build details for the team — who is this for, and what are they trying to get done?"
- **Round 2 — recover the value (EN):** "And what changes for them when it works — what's the outcome they'd notice?"
- **Story-points / sizing slip (EN):** "We don't size in points here. Is this slice something the team could ship in about a week, or does it feel bigger? Small / Medium / Large." *(maps to the story `size: S | M | L` enum — never points, never hours.)*

### Stop Rule

Stop once the PO has restated the item as **persona + problem + value** (or chosen a `size` for a sizing slip). The LLM then captures it in product terms and continues; the engineering detail the PO mentioned is **not** recorded in the spec — this skill writes stories + AC, the engineering team owns the build (see `references/guardrails-and-boundaries.md`). If the PO insists the technical constraint is a real product requirement (e.g. "must work offline"), record it as an acceptance criterion in user-observable terms, not as an implementation note.

## MoSCoW Gate

Use during PRD functional-requirements interview.

### Prompt Template

- **EN:** "If '{requirement}' delays launch by a month, do we still ship without it?"

### Rules

- Answer "yes, still ship" → tag = `should`, `could`, or `wont` (PO picks).
- Answer "no, must have" → tag = `must`.
- If >60% of requirements are `must`, the LLM iterates: "of these MUSTs, which 3 are the absolute minimum to be useful at all?"
- The MUST set after the second iteration is the MVP scope.

### MoSCoW Definitions (PO-friendly, EN)

- **Must:** the product is not viable without it.
- **Should:** important but not launch-blocking.
- **Could:** nice-to-have if there's room.
- **Won't:** out of scope for this round (still recorded for visibility).

## Story Mapping

Use when a PRD's use cases are abstract or jumbled.

### Prompt Template

- **EN:** "Walk me through one user's day with this product, from waking up to going to sleep. Where in the day does our product show up?"

### Follow-Ups

- **EN:** "At each touchpoint, what triggers them to use it? What's the first thing they do? Then?"

### Output Shape

The LLM organizes the answer as a backbone of user activities + sub-steps. Each sub-step becomes a candidate story; activities become candidate epics.

```
Activity 1 (epic candidate)
  Step 1.1 (story candidate)
  Step 1.2 (story candidate)
Activity 2 (epic candidate)
  Step 2.1 (story candidate)
```

## INVEST Reminders (LLM self-check on stories)

The LLM mentally checks each story:

- **I**ndependent — does it depend on another in this batch?
- **N**egotiable — is it a contract or a conversation?
- **V**aluable — does the persona care?
- **E**stimable — could someone size it?
- **S**mall — fits in ≤ a week of work?
- **T**estable — is the AC observable?

If any fails, the LLM flags it in `--validate` as an `invest_quality` finding (warn-level).
