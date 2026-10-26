# cleanmatic:telemetry

A **read-only** skill that tells a (non-technical) product owner, **in plain English**, how their skills are being used, whether scripts and subagents are healthy, and whether the spec validate passed. Eight opinionated lenses + four output formats; no editing, no CI gate, no network calls.

---

## English

### What it is

Three things in one read-only window:

1. **Usage** — which skills are invoked, how often, approx. tokens per skill, and which owned skills are never touched.
2. **Health** — which scripts error, run slowly, whether subagents succeed, whether memory is tidy.
3. **A thin internal-quality proxy** — did `product-spec --validate` pass? (This is **not** market effectiveness — that is E3, deliberately deferred.)

### How to run

```bash
/cleanmatic:telemetry                    # default: all lenses, ascii format
/cleanmatic:telemetry --lens usage       # one lens at a time
/cleanmatic:telemetry --format md --top 10    # markdown, top-10 items
```

Flags (all optional):

| Flag | Values | Default | Purpose |
|------|--------|---------|---------|
| `--lens` | `usage` / `session` / `health` / `reliability` / `workflow` / `validate` / `memory` / `forensics` / `all` | `all` | Which lens to run |
| `--format` | `ascii` / `md` / `mermaid` / `json` | `ascii` | Output format |
| `--days` | integer | 30 | Lookback period (days) |
| `--top` | integer | (md only) | Limit markdown to top N items |
| `--lang` | `en` | `en` | Fixed label language (English) |
| `--session` | UUID | — | For forensics: reconstruct one session |
| `--all-sessions` | — | — | For forensics: list all session IDs |

### Install

```bash
./install.sh                    # ensures shared venv, registers telemetry hooks
./install.sh --no-hooks         # runtime only, does NOT auto-register hooks
```

Windows:

```powershell
powershell -ExecutionPolicy Bypass -File .\install.ps1
powershell -ExecutionPolicy Bypass -File .\install.ps1 -NoHooks
```

Requires Python 3.9+ and PyYAML (the bundle's single runtime dependency, shipped with product-spec). Runs on system `python3`; no telemetry-specific venv needed.

### The 8 lenses at a glance

| Lens | Reads | Shows | Gated? |
|------|-------|-------|--------|
| `usage` | Invocation logs + transcripts | Top invoked skills, token weight (approx), never-used | Below ~5 data points |
| `session` | Session summaries | Count, avg/median duration, co-occurrence, file+tool counts | Below ~5 data points |
| `health` | Script telemetry | Per-script run count, error rate, avg ms (approx) | Below ~5 data points |
| `reliability` | Subagent outcomes | Success / api_error / timeout / blocked / unknown per type | Below ~5 data points |
| `workflow` | Invocations + declared chains | Actual skill chains vs. routing-doc chains; deviations | Below ~5 data points |
| `validate` | Last-validate marker + script runs | Validate pass/fail (internal quality proxy, NOT E3) | Below ~5 data points |
| `memory` | `.claude/projects/*/memory/` | Orphans, dead index entries, broken `[[links]]`, staleness | Always visible (read-only) |
| `forensics` | Session transcript JSONL | One session reconstructed (skills, tools, tokens, duration) | Requires `--session <id>` |

### How lenses work (deterministic gather → LLM narrates)

The skill **never computes** — a Python script (`analyze_telemetry.py`) gathers deterministically, then the LLM **narrates** the results in plain English. The split:

- **Script** (`.claude/skills/telemetry/scripts/analyze_telemetry.py`): no judgment, produces JSON aggregates (stdlib + PyYAML).
- **Skill** (the LLM): reads the aggregates, narrates them honestly, phrases recommendations as **suggestions** only.

```bash
# In the cleanmatic dev repo, use the shared venv:
.claude/skills/.venv/bin/python3 .claude/skills/telemetry/scripts/analyze_telemetry.py \
  --lens all --format ascii --days 30

# On recipients (where system python3 is available):
python3 .claude/skills/telemetry/scripts/analyze_telemetry.py \
  --lens all --format ascii --days 30
```

### Data source

Append-only JSONL sinks under `.claude/telemetry/` (gitignored, runtime data only):

- `invocations.jsonl` — skill invocations.
- `sessions.jsonl` — session summaries.
- `hook-telemetry.jsonl` — script runs + errors.
- `subagent-outcomes.jsonl` — subagent success/failure.
- `last_validated.json` — validate marker snapshot.

Five fail-open hooks auto-register on install (opt out: `register_telemetry_hooks.py --remove`).

### Low-volume gate ("insufficient data")

Below ~5 data points, a lens shows raw counts + **"insufficient data"** and suppresses recommendations. On a thin repo, **most lenses ARE gated** — the report says so plainly; no trends are invented.

### The honesty gate (mandatory)

Every report **ends** with **"This CANNOT be measured"**:

- **E3 / market outcome** — whether the product wins in the market. Telemetry sees *usage*, not *value*.
- **Any gated lens** — named explicitly with "insufficient data".
- **Approx disclaimers** — tokens, ms, exit codes are directional (estimate), never exact.

### What it is NOT

- **Not** a market/user-outcome metric (E3). The validate proxy = "spec well-formed", not "users adopted".
- **Not** a writer — never edits specs, code, the catalog, or memory. No `--apply`, no fixes.
- **Not** billing-exact — token attribution and `ms` are directional estimates.
- **Not** a CI gate — opinion-free numbers for the PO to read; nothing blocks on it.
- **Not** a crash-log analyzer — instrumented scripts lack rich `errors.jsonl`; deferred to BACKLOG.

### Learning path

- **First run:** `/cleanmatic:telemetry` at the default (all lenses, ascii) and **read the report**. The structure: summary → usage → health → sessions → workflow → validate → memory → "This CANNOT be measured" (honesty section).
- **Then focus:** `--lens usage` to see which skills are cold, `--lens health` to spot script errors, `--lens validate` for internal quality.
- **Experiment:** try `--format md --top 5` for a concise markdown table, `--format mermaid` for a pie/bar chart.
- **Deep dive:** `--session <id>` to reconstruct a single session's skill/tool/token flow.

### Output

- **Report:** printed to terminal (or written if you redirect stdout).
- **Formats:**
  - `ascii` — terminal-friendly one-glance read.
  - `md` — markdown table + narrative (copy-paste friendly).
  - `mermaid` — pie/bar charts, fenced, no network/JS required.
  - `json` — raw aggregates for scripting.
- **Marker:** `/etc/claude/projects/<root>/memory/` (read-only; script gathers, does not write).

### Boundaries

- **Read-only.** No edits to spec/code/catalog/memory; no network; needs PyYAML (the bundle's one dep) but no telemetry-specific venv.
- **No `--apply`.** This is a diagnostic skill, not a fixer. Recommendations are suggestions only.
- **One dependency (PyYAML).** Runs on system `python3` with PyYAML present (shipped via the bundle); the cleanmatic dev repo provides it through the shared venv.
- **GATE-NEVER-ASSUME / GATE-NO-SILENT-REVERSAL:** Not applicable in the usual sense (nothing is written/approved), but the skill still never fabricates a metric — an absent signal is reported as absent.

### Caveats

- **Never-used external skills** (e.g., `ck:code-review`, `com:mcp-builder`) are **not listed** — PO doesn't own them, so non-use is normal. Only **never-used cleanmatic skills** (`cleanmatic:*`) are flagged.
- **Token weight is approximate.** Derived from transcript length + a rough per-skill coefficient; never exact, always labeled "estimate".
- **The validate proxy is internal quality only** — see the narration contract (`references/narration-contract.md`) for what "internal quality" means vs. E3.

### Deep links

- **Narration contract (rules for honest language):** `references/narration-contract.md`
- **Operating contract (full SKILL.md):** `SKILL.md`
- **Full walkthrough + use cases:** `GUIDE-EN.md`
- **Lens modules:** `.claude/skills/telemetry/scripts/lens_*.py`
- **Script (deterministic gather):** `.claude/skills/telemetry/scripts/analyze_telemetry.py`

### Worked examples

- (TBD in future releases)

