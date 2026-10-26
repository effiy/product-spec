<!--
TEMPLATE: vision.md
Narrative product vision. Long-form (read once); pairs with the labels-only PRODUCT.md.
English headers.
-->
---
id: VISION
type: vision
status: {{status}}
lang: {{lang}}
owner: {{owner}}
version: {{version}}
created: {{created}}
updated: {{updated}}
personas: {{personas}}
---
<!--
Note: vision.md intentionally omits `horizon`. The horizon enum (now/next/later)
describes WHEN work happens; vision is timeless strategy. Roadmap horizon lives
on PRDs/epics/stories. Keeping `horizon: {{horizon}}` here meant a fresh init
always landed `horizon: TBD` which fails the closed-enum check.
-->

# Vision — {{name}}

## Problem Narrative

{{problem_narrative}}

## Personas

{{personas_detail}}

## Value Proposition

{{value_proposition}}

## North-Star

{{north_star}}

## 1–3 Year Direction

{{direction_1_to_3_years}}

<!-- OPTIONAL: principles -->
## Principles

{{principles}}
<!-- /OPTIONAL -->

<!-- OPTIONAL: non_goals -->
## Non-Goals

{{non_goals}}
<!-- /OPTIONAL -->

<!-- OPTIONAL: differentiation -->
## Differentiation

{{differentiation}}
<!-- /OPTIONAL -->
