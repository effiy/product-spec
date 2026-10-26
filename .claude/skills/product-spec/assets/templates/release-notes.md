<!--
TEMPLATE: release-notes.md — `--summary --audience release-notes` output.
"What changed since the last approved snapshot", pulled from the audit trail.
Same source-of-truth + render path as the exec one-pager; different audience.
English headers.
-->
---
id: RELEASE-NOTES
type: release_notes
status: {{status}}
lang: {{lang}}
owner: {{owner}}
version: {{version}}
created: {{created}}
updated: {{updated}}
generated_at: {{generated_at}}
---

# Release Notes — {{name}}

## Since Last Approved

{{changes_since_approved}}

## Open Risks

{{top_risks}}
