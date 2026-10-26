#!/usr/bin/env python3
"""
i18n_labels — minimal label map for visualization renderers (script layer only).

Scope is intentionally narrow: localize ONLY the 7-8 user-visible labels the
visualization-spec explicitly promises (`now/next/later` and MoSCoW). Prose
content (vision narrative, story descriptions, AC) is the LLM's job and uses
each artifact's `lang` frontmatter field, not this map.

Frontmatter keys and IDs always stay English regardless of `lang`.
"""

from typing import Dict


LABELS: Dict[str, Dict[str, str]] = {
    "en": {
        # horizon labels
        "now": "Now",
        "next": "Next",
        "later": "Later",
        # MoSCoW labels
        "must": "Must",
        "should": "Should",
        "could": "Could",
        "wont": "Won't",
        # tree label
        "product": "PRODUCT",
        # viewer UI chrome (board / explorer) — used by render_board / render_explorer
        "unassigned": "unassigned",
        "search": "Search…",
        "status": "Status",
        "moscow": "MoSCoW",
        "persona": "Persona",
        "layer": "Layer",
        "horizon": "Horizon",
        "board": "Board",
        "explorer": "Explorer",
        "export": "Spec Export",
        "tree": "Tree",
        "tabs": "Flat tabs",
        "table": "Table",
        "no_results": "No matching artifacts",
        "ac_count": "AC",
        # goal detail panel — goals carry no prose body, so the board/explorer
        # synthesize one from the goal's metrics (render_html.goal_detail_md).
        "metrics": "Metrics",
        # artifact-type labels — viewer Layer facet + explorer Flat-tabs tab names
        "goal": "Goal",
        "prd": "PRD",
        "epic": "Epic",
        "story": "Story",
        # TIME view (gantt title + ASCII header)
        "roadmap_deadlines": "Roadmap & Deadlines",
        "no_date": "no date",
        "time_no_dated": "No dated items yet — nothing to schedule on a timeline. Set a target_date on a PRD or epic.",
        # COMPETITION view — parity-matrix cell verdicts + threat-heatmap tiers.
        # Labels are the enum identity (the matrix renders the raw enum word).
        # Keys are distinct from the risk tiers to avoid clashes.
        "competition": "Competition",
        "parity_ahead": "ahead",
        "parity_parity": "parity",
        "parity_behind": "behind",
        "parity_none": "none",
        "threat_low": "low",
        "threat_med": "med",
        "threat_high": "high",
        # Reserved view-name labels; localized title/nav not yet wired — pinned by
        # tests for forward compat. No production path currently resolves these via
        # label(); they are kept so future wiring has a stable key contract.
        "time": "Time",
        "risk": "Risk",
        "dashboard": "Impact Dashboard",
        # --learn outcome views (scorecard / insight-gap / outcome-trend / learning-map)
        "scorecard": "Scorecard",
        "outcome_trend": "Outcome Trend",
        "insight_gap": "Insight Gap",
        "learning_map": "Learning Map",
        "learning": "Learning Dashboard",
        "verdict_hit": "hit",
        "verdict_partial": "partial",
        "verdict_miss": "miss",
        "unmeasured": "unmeasured",
        "blind_spot": "blind spot",
        "goal_removed": "goal removed",
        "target": "target",
        "actual": "actual",
        "gap": "gap",
        "verdict": "Verdict",
        "trend": "Trend",
        "no_outcomes": "No outcomes recorded yet — run --learn to measure a goal.",
    },
}


def label(key: str, lang: str = "en") -> str:
    """Return the English label for `key`, or fall back to the key itself.

    Uses explicit `in` membership tests instead of truthiness `or` chains so a
    label whose value is the empty string is returned as-is rather than being
    treated as a miss and falling through.

    Unhashable keys (list/dict from malformed frontmatter) can't be dict keys
    and would raise TypeError. Guard: non-str keys degrade to str(key) so the
    renderer keeps running and check_consistency flags the bad enum separately."""
    if not isinstance(key, str):
        return str(key)
    return LABELS["en"].get(key, key)
