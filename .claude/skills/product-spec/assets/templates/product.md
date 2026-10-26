<!--
TEMPLATE: PRODUCT.md
Token convention: {{token}} substituted by generate_templates.py.
Optional sections wrapped in <!-- OPTIONAL: name --> ... <!-- /OPTIONAL -->.
generate_templates.py drops optional blocks the PO chose to skip.
English headers.
-->
---
id: PRODUCT
type: product
status: {{status}}
lang: {{lang}}
owner: {{owner}}
version: {{version}}
created: {{created}}
updated: {{updated}}
name: "{{name}}"
one_line_description: "{{one_line_description}}"
current_implementation: "{{current_implementation}}"
deployment: "{{deployment}}"
roadmap_one_liner: "{{roadmap_one_liner}}"
core_value: "{{core_value}}"
personas: {{personas}}
---

# {{name}} — Product Context

> Thin labels only. Narrative lives in `vision.md`. Stakeholders / business goals live in `brd.md`.

## One-Line Description

{{one_line_description}}

## Core Value

_(authoritative value lives in frontmatter `core_value` field — see top of file. Body deliberately blank to keep one source of truth.)_

## Current Implementation

{{current_implementation}}

## Deployment

{{deployment}}

## Roadmap One-Liner

{{roadmap_one_liner}}

## Personas

{{personas_bullets}}

<!-- OPTIONAL: contact -->
## Contact

{{contact}}
<!-- /OPTIONAL -->
