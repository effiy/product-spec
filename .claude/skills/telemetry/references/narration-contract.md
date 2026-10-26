# Narration Contract — cleanmatic:telemetry

How the skill turns the script's aggregate dicts into a plain-English read for a
non-technical product owner. The script gathers; this contract governs the words.

## Voice

- **English**, native quality: natural register, short sentences.
- Talk in **owner language** (skills, work, "usage", "errors", "slow"), not engineering
  jargon. Numbers stay numbers; skill ids / script paths stay ascii.
- **No hype.** This is a status read, not a pitch.

## Structure of a default report (`--lens all`)

1. **2-3 line summary** — the headline: how much was used, anything unhealthy, whether
   there's enough data at all.
2. **Usage** — top skills + token weight (estimate), never-used. **Only list never-used for skills the PO owns (`cleanmatic:*`)** — external skills (`ck:*`/`com:*`…) being unused is normal (PO didn't write them, not prune candidates); only state the count of external if needed, don't list each one.
3. **Health** — scripts that error or run slow (approx), subagent reliability.
4. **Sessions** — count, duration, co-occurrence — only if not gated.
5. **Workflow chains** — only when ≥ min sessions; otherwise say it's too thin.
6. **Validate proxy** — internal quality only; ALWAYS tagged "not E3".
7. **Memory** — orphans/dead/broken links, read-only.
8. **This CANNOT be measured** — the mandatory honesty section (below).

## MEASURED vs NOT-MEASURED

| MEASURED (report these) | NOT-MEASURED (must disclaim) |
|-------------------------|------------------------------|
| invocation counts, never-used | whether a skill is *valuable* |
| per-skill tokens (estimate) | exact billing cost |
| script error-rate, avg ms (approx) | root cause of an error |
| subagent outcome mix | why a subagent failed (unless transcript said) |
| validate-pass (spec well-formed) | **market / user outcome (E3)** |
| memory tidiness | whether a memory is *correct* |

## The honesty gate (hard requirement)

Every report ENDS with **"This CANNOT be measured"** that names, at minimum:

- **Market / user outcome (E3)** — telemetry cannot see adoption, revenue, or
  user satisfaction. The validate proxy is internal quality only.
- **Every gated / below-threshold lens** → state "insufficient data", do NOT infer a trend.
- **Estimated numbers** (tokens, ms, exit) → label as directional, not exact.

If the whole repo is thin (most lenses gated), the report LEADS with "insufficient data to
conclude" rather than dressing up a handful of points as insight.

## Recommendations

- Always **suggestions**, never an order. Example: "Suggestion: skill X was not used in 30 days —
  consider whether to keep it." The PO decides.
- **Never** propose to delete skills, edit memory, or change scope — the skill is read-only and
  has no such authority.
- Suppress recommendations entirely for any **gated** lens.

## Tone examples

- Good: "In 30 days, `product-spec` was used 8 times (most), costing ~450K tokens (estimate).
  3 skills never used."
- Good: "Insufficient data on subagents (only 3 runs) — cannot conclude reliability yet."
- Bad: "Skill X is the most effective skill." (effectiveness is not measured — usage ≠ value.)
- Bad: "Validate passes 100% so the product will succeed." (conflates internal quality with E3.)