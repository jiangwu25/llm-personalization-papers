import importlib.util
import sys
import textwrap
import unittest
from datetime import date
from pathlib import Path


MODULE_PATH = Path(__file__).parents[1] / "scripts" / "validate_index.py"
SPEC = importlib.util.spec_from_file_location("validate_index", MODULE_PATH)
validate_index = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
sys.modules[SPEC.name] = validate_index
SPEC.loader.exec_module(validate_index)


TAGS = """<!-- TAGS:START -->
`survey` `user-profile` `preference-elicitation` `user-history`
`memory` `retrieval` `prompting` `steering` `decoding`
`fine-tuning` `peft` `personalized-alignment` `reward-modeling`
`agent` `writing` `recommendation` `search`
`benchmark` `dataset` `evaluation`
`privacy` `safety` `user-control`
<!-- TAGS:END -->"""


def entry(
    *,
    title="A Verified Paper",
    paper_id="arxiv:2501.00001",
    first_public="2025-01",
    tags="`memory` `retrieval`",
    summary="A factual summary of the user-specific method.",
    url="https://arxiv.org/abs/2501.00001",
    resources="",
):
    resource_line = f"\n  - Resources: {resources}" if resources else ""
    return textwrap.dedent(
        f"""
        - **[{title}]({url})**
          - ID: `{paper_id}`
          - First public: `{first_public}`
          - Publication: Preprint
          - Summary: {summary}
          - Tags: {tags}{resource_line}
        """
    ).strip()


def compact_entry(
    *,
    title="A Compact Paper",
    publication="ACL 2025",
    url="https://arxiv.org/abs/2501.00001",
):
    return f"- **[{title}]({url})** — {publication}"


def readme(*entries, category="Memory & Retrieval", extra=""):
    lines = [
        "# Example",
        "Outside example: - **[Not an entry](https://example.com)**",
        '<a id="paper-index"></a>',
        "## Paper Index",
        "<!-- PAPERS:START -->",
        '<a id="memory-retrieval"></a>',
        f"### {category}",
        "",
    ]
    for item in entries:
        lines.extend(item.splitlines())
        lines.append("")
    if extra:
        lines.extend(extra.strip("\n").splitlines())
    lines.append("<!-- PAPERS:END -->")
    return "\n".join(lines) + "\n"


class ValidatorTests(unittest.TestCase):
    def assert_valid(self, readme_text):
        report = validate_index.validate_index(readme_text, TAGS, date(2026, 9, 20))
        self.assertEqual([], report.errors)
        return report

    def test_legal_entry_passes(self):
        report = self.assert_valid(readme(entry()))
        self.assertEqual(1, report.entry_count)

    def test_compact_entry_passes(self):
        report = self.assert_valid(readme(compact_entry()))
        self.assertEqual(1, report.entry_count)

    def test_compact_entry_requires_year(self):
        report = validate_index.validate_index(readme(compact_entry(publication="ACL")), TAGS, date(2026, 9, 20))
        self.assertTrue(any("First public" in error for error in report.errors))

    def test_compact_entries_sort_by_publication_year(self):
        newer = compact_entry(title="Newer", publication="EMNLP 2025", url="https://arxiv.org/abs/2501.00002")
        older = compact_entry(title="Older", publication="ACL 2024", url="https://arxiv.org/abs/2401.00001")
        self.assert_valid(readme(newer, older))
        report = validate_index.validate_index(readme(older, newer), TAGS, date(2026, 9, 20))
        self.assertTrue(any("sort" in error.lower() for error in report.errors))

    def test_missing_required_field_fails(self):
        invalid = readme(entry()).replace("  - Summary: A factual summary of the user-specific method.\n", "")
        report = validate_index.validate_index(invalid, TAGS, date(2026, 9, 20))
        self.assertTrue(any("Summary" in error for error in report.errors))

    def test_duplicate_id_fails(self):
        report = validate_index.validate_index(readme(entry(), entry(title="Another Paper")), TAGS, date(2026, 9, 20))
        self.assertTrue(any("duplicate" in error.lower() for error in report.errors))

    def test_arxiv_url_versions_normalize_to_duplicate(self):
        first = entry(url="https://arxiv.org/abs/2501.00001v1")
        second = entry(title="Versioned Paper", paper_id="url:https://arxiv.org/pdf/2501.00001v2.pdf", url="https://arxiv.org/pdf/2501.00001v2.pdf")
        report = validate_index.validate_index(readme(first, second), TAGS, date(2026, 9, 20))
        self.assertTrue(any("duplicate" in error.lower() for error in report.errors))

    def test_unknown_and_repeated_tags_fail(self):
        invalid = readme(entry(tags="`memory` `memory` `not-a-tag`"))
        report = validate_index.validate_index(invalid, TAGS, date(2026, 9, 20))
        self.assertTrue(any("unknown tag" in error.lower() for error in report.errors))
        self.assertTrue(any("repeated tag" in error.lower() for error in report.errors))

    def test_invalid_month_fails(self):
        report = validate_index.validate_index(readme(entry(first_public="2025-13")), TAGS, date(2026, 9, 20))
        self.assertTrue(any("month" in error.lower() for error in report.errors))

    def test_year_only_dates_sort_after_known_month(self):
        newer_known = entry(title="Known Month", paper_id="arxiv:2501.00002", first_public="2025-02", url="https://arxiv.org/abs/2501.00002")
        older_year_only = entry(title="Year Only", paper_id="arxiv:2501.00001", first_public="2025", url="https://arxiv.org/abs/2501.00001")
        self.assert_valid(readme(newer_known, older_year_only))
        invalid_order = readme(older_year_only, newer_known)
        report = validate_index.validate_index(invalid_order, TAGS, date(2026, 9, 20))
        self.assertTrue(any("sort" in error.lower() for error in report.errors))

    def test_same_date_ids_sort_ascending(self):
        first = entry(title="B", paper_id="arxiv:2501.00002", url="https://arxiv.org/abs/2501.00002")
        second = entry(title="A", paper_id="arxiv:2501.00001", url="https://arxiv.org/abs/2501.00001")
        report = validate_index.validate_index(readme(first, second), TAGS, date(2026, 9, 20))
        self.assertTrue(any("sort" in error.lower() for error in report.errors))

    def test_entry_without_resources_passes(self):
        report = self.assert_valid(readme(entry(resources="")))
        self.assertEqual(1, report.entry_count)

    def test_multiline_summary_passes(self):
        multiline = entry(summary="First factual sentence.").replace(
            "  - Tags:", "    Second factual clause.\n  - Tags:"
        )
        report = self.assert_valid(readme(multiline))
        self.assertEqual(1, report.entry_count)

    def test_out_of_range_sample_is_not_counted(self):
        report = self.assert_valid(readme(entry()))
        self.assertEqual(1, report.entry_count)

    def test_missing_or_duplicate_markers_fail(self):
        missing = "# Paper Index\n"
        report = validate_index.validate_index(missing, TAGS, date(2026, 9, 20))
        self.assertTrue(any("marker" in error.lower() for error in report.errors))
        duplicated = readme(entry()).replace("<!-- PAPERS:START -->", "<!-- PAPERS:START -->\n<!-- PAPERS:START -->")
        report = validate_index.validate_index(duplicated, TAGS, date(2026, 9, 20))
        self.assertTrue(any("marker" in error.lower() for error in report.errors))

    def test_empty_index_warns_but_is_structurally_valid(self):
        empty = readme("")
        report = self.assert_valid(empty)
        self.assertTrue(any("empty" in warning.lower() for warning in report.warnings))

    def test_placeholder_url_fails(self):
        invalid = readme(entry(url="https://example.com/paper"))
        report = validate_index.validate_index(invalid, TAGS, date(2026, 9, 20))
        self.assertTrue(any("placeholder" in error.lower() for error in report.errors))


if __name__ == "__main__":
    unittest.main()
