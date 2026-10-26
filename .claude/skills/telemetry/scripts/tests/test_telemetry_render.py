"""test_telemetry_render.py — ascii / mermaid / md renderers across both gate
states. Snapshots are loose (substring/shape) so cosmetic tweaks don't churn,
but the load-bearing invariants are asserted: gate notes, mermaid validity +
escaping, and the no-network/no-JS guarantee (D4/F1)."""
import sys
from pathlib import Path

_LIB = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(_LIB))

from telemetry_render import render_md, render_ascii, render_mermaid  # noqa: E402


def _usage(gated):
    return {
        "lens": "usage_tokens", "days": 30,
        "total_invocations": 2 if gated else 12, "skills_used": 2,
        "catalog_size": 4, "never_used": ["telemetry"], "with_tokens": True,
        "gated": gated,
        "rows": [{"skill": "product-spec", "count": 8, "tokens": 450},
                 {"skill": "release", "count": 4, "tokens": 150},
                 {"skill": "telemetry", "count": 0, "tokens": 0}],
    }


def _health():
    return {"lens": "health", "approx": True, "total_runs": 9, "scripts": 2,
            "total_errors": 1, "gated": False,
            "rows": [{"script": "product-spec/scripts/validate.py", "runs": 8, "errors": 0,
                      "error_rate": 0, "avg_ms": 1000},
                     {"script": "release/scripts/release.py", "runs": 1, "errors": 1,
                      "error_rate": 100, "avg_ms": None}]}


def _reliability(gated):
    return {"lens": "reliability", "days": 30, "total": 2 if gated else 12, "gated": gated,
            "rows": [{"agent_type": "researcher", "total": 6, "success": 5, "api_error": 0,
                      "timeout": 1, "blocked": 0, "unknown": 0, "success_rate": 83}],
            "top_failure_modes": [("timeout", 1)]}


class TestAscii:
    def test_above_gate_has_status_lines(self):
        out = render_ascii([_usage(False), _health()])  # default lang = en
        assert "USAGE" in out and "HEALTH" in out
        assert "[OK]" in out  # health has a per-script ok line
        assert "[!]" in out   # release error line
        en = render_ascii([_usage(False), _health()], lang="en")
        assert "USAGE" in en and "HEALTH" in en

    def test_below_gate_shows_gated_usage(self):
        assert "[!] USAGE" in render_ascii([_usage(True)])          # en default
        assert "[!] USAGE" in render_ascii([_usage(True)], lang="en")  # gated → not-ok light

    def test_deterministic(self):
        a = render_ascii([_usage(False), _health()])
        b = render_ascii([_usage(False), _health()])
        assert a == b


class TestMermaid:
    def test_usage_pie_fenced_and_escaped(self):
        out = render_mermaid([_usage(False)])
        assert out.count("```mermaid") >= 1
        assert "pie showData" in out
        assert '"product-spec" : 8' in out

    def test_below_gate_note_not_chart(self):
        out = render_mermaid([_usage(True)])
        assert "```mermaid" not in out
        assert "insufficient data" in out

    def test_reliability_bar(self):
        out = render_mermaid([_reliability(False)])
        assert "xychart-beta" in out
        assert "researcher" in out

    def test_no_network_no_js_anywhere(self):
        out = render_mermaid([_usage(False), _health(), _reliability(False)])
        lo = out.lower()
        assert "http://" not in lo and "https://" not in lo
        assert "<script" not in lo and "javascript:" not in lo

    def test_tricky_skill_label_escaped(self):
        agg = _usage(False)
        agg["rows"][0]["skill"] = 'evil"; rm -rf\nx'
        out = render_mermaid([agg])
        # no raw double-quote inside the label, no embedded newline breaking syntax
        assert '"evil\'' in out or "evil'" in out
        assert "\nx\" :" not in out


class TestMd:
    def test_renders_each_lens_section(self):
        out = render_md([_usage(False), _health(), _reliability(False)])  # vi default
        assert "## Skill Usage" in out
        assert "## Sức khỏe script" in out
        assert "## Độ tin cậy subagent" in out
        en = render_md([_usage(False), _health(), _reliability(False)], lang="en")
        assert "## Skill Usage" in en
        assert "## Script Health" in en
        assert "## Subagent Reliability" in en

    def test_gate_note_in_md(self):
        assert "Chưa đủ dữ liệu" in render_md([_usage(True)])                  # vi default
        assert "Insufficient data" in render_md([_usage(True)], lang="en")

    def test_empty_list(self):
        assert "Không có lens" in render_md([])               # vi default
        assert "No lenses" in render_md([], lang="en")




class TestLensErrorIsolation:
    """A lens that raised becomes a visible error entry — render surfaces it,
    never silently drops it, and the healthy lenses still render."""
    def test_error_entry_surfaced_in_md(self):
        aggs = [_usage(False), {"lens": "workflow", "error": "FileNotFoundError: skill-chains.yaml"}]
        out = render_md(aggs)
        assert "## Skill Usage" in out                       # healthy lens still renders
        assert "workflow" in out and "FileNotFoundError" in out   # error not dropped

    def test_error_entry_surfaced_in_ascii(self):
        aggs = [{"lens": "health", "error": "ValueError: boom"}, _usage(False)]
        out = render_ascii(aggs)
        assert "[!]" in out and "ValueError: boom" in out
        assert "USAGE" in out

    def test_error_entry_surfaced_in_mermaid(self):
        # a chartable lens (health) erroring must still appear as a visible note —
        # never silently vanish from the chart surface.
        aggs = [{"lens": "health", "error": "ValueError: boom"}, _usage(False)]
        out = render_mermaid(aggs)
        assert "ValueError: boom" in out and "health" in out



    def test_unknown_lang_falls_back_to_en(self):
        out = render_md([_usage(False)], lang="zz")
        assert "## Skill Usage" in out  # graceful en fallback, never a KeyError
