# Workflow: `--lang` (interview / output language)

Set the interview + output language to English. The switch is **content-localized,
identity-preserved**:

## What localizes

- Interview questions + the LLM's conversational phrasing.
- Body-view facets/labels + in-view value labels.
- `--export` headings.

## What stays English (never localized)

- **IDs** (`BRD-G1`, `PRD-AUTH-E1-S1`) and **all frontmatter keys/values** — they are the
  machine contract; localizing them would break traceability and every script.
- Graph/HTML-native page chrome: page `<title>`, panel headers.

## Notes

- A standing language preference can be set once (the PO sets it; `--lang` overrides per run).
- `--lang` changes presentation only — it never changes which artifact/flag is selected, nor any
  stored structure.

Distinct from `--voice` (records the PO's wording *style*, not the language itself).
