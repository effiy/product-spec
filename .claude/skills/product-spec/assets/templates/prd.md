<!--
TEMPLATE: prd.md (Product Requirements Document) — one per feature-area.
Multi-PRD per BRD. Carries narrative, scope, NFRs, success metrics.
Does NOT enumerate stories (that lives in epic/story files).
`risks:` is a YAML list of dicts; each entry:
  - description: "Third-party OAuth dependency"   # required free text
    impact: high          # enum: low | med | high
    likelihood: med       # enum: low | med | high
    mitigation: "Fallback provider on standby"     # optional free text
    status: open          # enum: open | mitigated | accepted

TIME dimension (both OPTIONAL — omit and the field defaults to empty/none):
  target_date: 2026-09-30      # ISO YYYY-MM-DD; the deadline for this PRD
  depends_on: [PRD-BILLING]    # IDs this PRD waits on (PRD+Epic only; a cycle is a dep_cycle error)

COMPETITION dimension — `competitive_parity` is an ID-keyed MAP referencing the
BRD's competitors (defined ONCE in brd.md's `competitors:`). Each KEY is a
competitor id (must resolve to a BRD competitor → else unknown_ref); each VALUE
is the parity enum ahead|parity|behind|none. Empty {} is fine (a v1 PRD):
  competitive_parity:
    COMP-ACME: behind
    COMP-SHOPIFY: parity
-->
---
id: {{id}}
type: prd
brd_goals: {{brd_goals}}
status: {{status}}
lang: {{lang}}
owner: {{owner}}
version: {{version}}
created: {{created}}
updated: {{updated}}
personas: {{personas}}
scope: {{scope}}
moscow: {{moscow}}
horizon: {{horizon}}
metrics: {{metrics}}
risks: {{risks}}
# COMPETITION (optional) — ID-keyed map of BRD competitor id → parity enum
# (ahead|parity|behind|none). Empty {} parses cleanly. Each key must resolve to
# a competitor defined in brd.md's `competitors:` list.
competitive_parity: {{competitive_parity}}
# TIME (optional) — uncomment to set; absence parses cleanly as none/empty:
# target_date: 2026-09-30
# depends_on: [PRD-OTHER]
---

# {{title}} — PRD {{id}}

## Overview & Problem

{{overview_problem}}

## Personas

{{personas_section}}

## Use Cases / Flows

{{use_cases}}

## Functional Requirements (MoSCoW)

### Must

{{must_have}}

### Should

{{should_have}}

### Could

{{could_have}}

### Won't (this round)

{{wont_have}}

## Non-Functional Requirements

{{nfrs}}

## Success Metrics → BRD Goals

{{success_metrics}}

<!-- OPTIONAL: scope_in_out -->
## Scope In / Out

**In scope:**

{{scope_in}}

**Out of scope**

{{scope_out}}
<!-- /OPTIONAL -->

<!-- OPTIONAL: dependencies_risks -->
## Dependencies & Risks

{{dependencies_risks}}
<!-- /OPTIONAL -->

<!-- OPTIONAL: open_questions -->
## Open Questions

{{open_questions}}
<!-- /OPTIONAL -->
