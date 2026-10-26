<!--
TEMPLATE: sign-off.md — fragment appended to an artifact body when `--approve` runs.
Also adds the `approval:` block to the artifact frontmatter (handled by generate_templates.py).
-->

---

## Sign-Off

| Field | Value |
|-------|-------|--------|---------|
| Artifact | {{artifact_id}} |
| Approved by | {{approved_by}} |
| Approved at | {{approved_at}} |
| Approved version | {{approved_version}} |
| Stakeholders | {{stakeholders}} |

<!-- OPTIONAL: notes -->
**Notes** {{approval_notes}}
<!-- /OPTIONAL -->

> Open issues at approval time (warn-not-block): {{open_issues_at_approval}}
