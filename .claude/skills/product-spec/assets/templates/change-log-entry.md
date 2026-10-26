<!--
TEMPLATE: change-log-entry.md — fragment appended to docs/product/change-log.md
on every --update / --approve / generate flow.
Format: one entry per change, append-only, newest at top.
-->

## {{date}} — {{change_type}}

- **Artifact:** {{artifact_id}} ({{file}})
- **Action:** {{action}}
- **Reason:** {{reason}}
- **Affected downstream:** {{affected_set}}
- **Dimensions touched:** {{dims}}
- **Author:** {{author}}

<!-- OPTIONAL: detail -->
**Detail:**

{{detail}}
<!-- /OPTIONAL -->

<!-- OPTIONAL: po_decision -->
**PO decision:** {{po_decision}}
<!-- /OPTIONAL -->
