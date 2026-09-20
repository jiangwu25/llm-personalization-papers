#!/usr/bin/env python3
"""Validate the hand-maintained paper index without network access."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date
from pathlib import Path
import re
import sys
from urllib.parse import urlsplit, urlunsplit


PAPER_START = "<!-- PAPERS:START -->"
PAPER_END = "<!-- PAPERS:END -->"
TAGS_START = "<!-- TAGS:START -->"
TAGS_END = "<!-- TAGS:END -->"
CATEGORY_ORDER = (
    "Foundations & Canonical Benchmarks",
    "Surveys & Perspectives",
    "User Modeling & Preference Elicitation",
    "Memory & Retrieval",
    "Prompting, Steering & Decoding",
    "Fine-tuning & Personalized Alignment",
    "Personalized Agents & Applications",
    "Benchmarks & Evaluation",
    "Privacy, Safety & User Control",
)
FIELD_NAMES = {"ID", "First public", "Publication", "Summary", "Tags", "Resources"}
DATE_RE = re.compile(r"^(?P<year>\d{4})(?:-(?P<month>\d{2}))?$")
URL_RE = re.compile(r"https?://[^\s)]+", re.IGNORECASE)
LINK_RE = re.compile(r"\[[^\]]+\]\((https?://[^)]+)\)", re.IGNORECASE)
ENTRY_RE = re.compile(r"^- \*\*\[(?P<title>.+?)\]\((?P<url>https?://[^)]+)\)\*\*\s*$")
COMPACT_ENTRY_RE = re.compile(
    r"^- \*\*\[(?P<title>.+?)\]\((?P<url>https?://[^)]+)\)\*\*\s+—\s+(?P<publication>.+?)\s*$"
)
FIELD_RE = re.compile(r"^\s+-\s+(?P<field>ID|First public|Publication|Summary|Tags|Resources):\s*(?P<value>.*)$")
COMPACT_DATE_RE = re.compile(r"(?P<year>\d{4})(?:-(?P<month>\d{2}))?$")


@dataclass
class PaperEntry:
    title: str
    url: str
    line: int
    category: str = ""
    paper_id: str = ""
    first_public: str = ""
    publication: str = ""
    summary: str = ""
    tags: tuple[str, ...] = ()
    resources: tuple[str, ...] = ()
    fields: dict[str, int] = field(default_factory=dict)
    compact: bool = False


@dataclass
class ValidationReport:
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    entry_count: int = 0
    category_counts: dict[str, int] = field(default_factory=dict)


def parse_marked_block(text: str, start_marker: str, end_marker: str) -> tuple[str, int]:
    """Return the text between exactly one ordered marker pair and its line offset."""
    lines = text.splitlines()
    starts = [index for index, line in enumerate(lines) if line.strip() == start_marker]
    ends = [index for index, line in enumerate(lines) if line.strip() == end_marker]
    if len(starts) != 1 or len(ends) != 1 or starts[0] >= ends[0]:
        raise ValueError(f"invalid or missing marker pair: {start_marker} / {end_marker}")
    return "\n".join(lines[starts[0] + 1 : ends[0]]), starts[0] + 2


def parse_tags(text: str) -> set[str]:
    block, _ = parse_marked_block(text, TAGS_START, TAGS_END)
    tags = re.findall(r"`([^`]+)`", block)
    if len(tags) != len(set(tags)):
        raise ValueError("controlled tag block contains repeated tags")
    return set(tags)


def _parse_entries(block: str, first_line: int) -> tuple[list[PaperEntry], list[str], list[str]]:
    lines = block.splitlines()
    entries: list[PaperEntry] = []
    categories: list[str] = []
    parse_errors: list[str] = []
    current: PaperEntry | None = None
    last_field = ""

    for offset, raw_line in enumerate(lines):
        line_number = first_line + offset
        line = raw_line.rstrip()
        heading = re.match(r"^###\s+(.+?)\s*$", line)
        if heading:
            current = None
            last_field = ""
            categories.append(heading.group(1))
            continue
        if line.startswith("<a ") or not line.strip():
            continue
        compact_match = COMPACT_ENTRY_RE.match(line)
        if compact_match:
            publication = compact_match.group("publication")
            date_match = COMPACT_DATE_RE.search(publication)
            first_public = date_match.group(0) if date_match else ""
            current = PaperEntry(
                title=compact_match.group("title"),
                url=compact_match.group("url"),
                line=line_number,
                category=categories[-1] if categories else "",
                paper_id=f"url:{compact_match.group('url')}",
                first_public=first_public,
                publication=publication,
                compact=True,
            )
            entries.append(current)
            last_field = ""
            continue
        entry_match = ENTRY_RE.match(line)
        if entry_match:
            current = PaperEntry(
                title=entry_match.group("title"),
                url=entry_match.group("url"),
                line=line_number,
                category=categories[-1] if categories else "",
            )
            entries.append(current)
            last_field = ""
            continue
        if current is None:
            if line.strip():
                parse_errors.append(f"README.md:{line_number}: unrecognized index content")
            continue
        field_match = FIELD_RE.match(line)
        if field_match:
            field_name = field_match.group("field")
            if field_name in current.fields:
                parse_errors.append(f"README.md:{line_number}: duplicate {field_name} field")
            current.fields[field_name] = line_number
            value = field_match.group("value").strip()
            if field_name == "ID":
                current.paper_id = value.strip("`")
            elif field_name == "First public":
                current.first_public = value.strip("`")
            elif field_name == "Publication":
                current.publication = value
            elif field_name == "Summary":
                current.summary = value
            elif field_name == "Tags":
                current.tags = tuple(re.findall(r"`([^`]+)`", value))
            elif field_name == "Resources":
                current.resources = tuple(LINK_RE.findall(value))
            last_field = field_name
            continue
        if len(line) - len(line.lstrip()) >= 4 and last_field in {"Summary", "Resources"}:
            continuation = line.strip()
            if last_field == "Summary":
                current.summary = f"{current.summary} {continuation}".strip()
            else:
                current.resources = current.resources + tuple(LINK_RE.findall(continuation))
            continue
        if line.strip():
            parse_errors.append(f"README.md:{line_number}: unrecognized entry content")
    return entries, categories, parse_errors


def parse_papers(text: str) -> list[PaperEntry]:
    """Parse only entries inside the README paper markers."""
    block, first_line = parse_marked_block(text, PAPER_START, PAPER_END)
    entries, _, parse_errors = _parse_entries(block, first_line)
    if parse_errors:
        raise ValueError("; ".join(parse_errors))
    return entries


def normalize_paper_url(url: str) -> str:
    """Normalize only stable URL details needed for duplicate detection."""
    parsed = urlsplit(url.strip())
    host = parsed.netloc.lower()
    scheme = parsed.scheme.lower()
    path = parsed.path
    if host in {"arxiv.org", "www.arxiv.org"}:
        match = re.search(r"/(?:abs|pdf)/(\d{4}\.\d{4,5})(?:v\d+)?(?:\.pdf)?/?$", path, re.IGNORECASE)
        if match:
            return f"https://arxiv.org/abs/{match.group(1)}"
    return urlunsplit((scheme, host, path.rstrip("/"), parsed.query, parsed.fragment))


def _id_is_valid(paper_id: str) -> bool:
    return bool(
        re.fullmatch(r"arxiv:(?:\d{4}\.\d{4,5}|\d{7})", paper_id)
        or re.fullmatch(r"doi:10\.\S+", paper_id)
        or re.fullmatch(r"url:https?://\S+", paper_id, re.IGNORECASE)
    )


def _date_value(value: str) -> tuple[int, bool, int] | None:
    match = DATE_RE.fullmatch(value)
    if not match:
        return None
    month = int(match.group("month")) if match.group("month") else 0
    if month and not 1 <= month <= 12:
        return None
    return int(match.group("year")), bool(month), month


def _sort_key(entry: PaperEntry) -> tuple[int, int, int, str]:
    parsed = _date_value(entry.first_public) or (0, False, 0)
    year, known_month, month = parsed
    return (-year, 0 if known_month else 1, -month, entry.paper_id.lower())


def _placeholder(url: str) -> bool:
    parsed = urlsplit(url)
    host = parsed.netloc.lower().split(":", 1)[0]
    return host in {"example.com", "example.org", "example.net", "localhost"} or "example.com" in url.lower()


def validate_index(readme_text: str, contributing_text: str, today: date) -> ValidationReport:
    report = ValidationReport()
    try:
        paper_block, first_line = parse_marked_block(readme_text, PAPER_START, PAPER_END)
    except ValueError as exc:
        report.errors.append(f"README.md: {exc}")
        return report
    try:
        allowed_tags = parse_tags(contributing_text)
    except ValueError as exc:
        report.errors.append(f"CONTRIBUTING.md: {exc}")
        allowed_tags = set()

    entries, categories, parse_errors = _parse_entries(paper_block, first_line)
    report.errors.extend(parse_errors)
    report.entry_count = len(entries)
    report.category_counts = {category: 0 for category in CATEGORY_ORDER}

    seen_categories: list[str] = []
    for category in categories:
        if category not in CATEGORY_ORDER:
            report.errors.append(f"README.md: unknown category '{category}'")
        elif category not in seen_categories:
            seen_categories.append(category)
    expected_categories = [category for category in CATEGORY_ORDER if category in seen_categories]
    if seen_categories != expected_categories:
        report.errors.append("README.md: categories are not in the required order")

    seen_ids: dict[str, int] = {}
    seen_urls: dict[str, int] = {}
    by_category: dict[str, list[PaperEntry]] = {}
    for entry in entries:
        report.category_counts[entry.category] = report.category_counts.get(entry.category, 0) + 1
        by_category.setdefault(entry.category, []).append(entry)
        prefix = f"README.md:{entry.line}"
        required = {"Publication": entry.publication, "First public": entry.first_public}
        if not entry.compact:
            required.update({"ID": entry.paper_id, "Summary": entry.summary, "Tags": entry.tags})
        for field_name, value in required.items():
            if not value:
                report.errors.append(f"{prefix}: missing required {field_name} field")
        if not entry.category:
            report.errors.append(f"{prefix}: entry is outside a known category")
        elif entry.category not in CATEGORY_ORDER:
            report.errors.append(f"{prefix}: unknown category '{entry.category}'")
        if not entry.compact and not _id_is_valid(entry.paper_id):
            report.errors.append(f"{prefix}: invalid stable ID '{entry.paper_id}'")
        normalized_id = entry.paper_id.lower()
        if normalized_id in seen_ids:
            report.errors.append(f"{prefix}: duplicate stable ID; first seen at line {seen_ids[normalized_id]}")
        else:
            seen_ids[normalized_id] = entry.line
        if not re.fullmatch(r"https?://\S+", entry.url, re.IGNORECASE):
            report.errors.append(f"{prefix}: paper URL must be a complete HTTP(S) URL")
        if _placeholder(entry.url):
            report.errors.append(f"{prefix}: placeholder URL is not allowed")
        normalized_url = normalize_paper_url(entry.url)
        if normalized_url in seen_urls:
            report.errors.append(f"{prefix}: duplicate normalized paper URL; first seen at line {seen_urls[normalized_url]}")
        else:
            seen_urls[normalized_url] = entry.line
        parsed_date = _date_value(entry.first_public)
        if parsed_date is None:
            report.errors.append(f"{prefix}: invalid first-public date or month '{entry.first_public}'")
        else:
            year, known_month, month = parsed_date
            if year > today.year or (year == today.year and known_month and month > today.month):
                report.errors.append(f"{prefix}: first-public date cannot be in the future")
        if not entry.compact:
            if not 1 <= len(entry.tags) <= 3:
                report.errors.append(f"{prefix}: Tags must contain 1–3 tags")
            if len(entry.tags) != len(set(entry.tags)):
                report.errors.append(f"{prefix}: repeated tag")
            for tag in entry.tags:
                if tag not in allowed_tags:
                    report.errors.append(f"{prefix}: unknown tag '{tag}'")
        for resource in entry.resources:
            if not re.fullmatch(r"https?://\S+", resource, re.IGNORECASE):
                report.errors.append(f"{prefix}: resource URL must be a complete HTTP(S) URL")
            if _placeholder(resource):
                report.errors.append(f"{prefix}: placeholder URL is not allowed")
        if not entry.compact and len(entry.summary.split()) == 0:
            report.errors.append(f"{prefix}: Summary cannot be empty")

    for category, category_entries in by_category.items():
        if category_entries != sorted(category_entries, key=_sort_key):
            report.errors.append(f"README.md: entries in '{category}' are not sorted by date and ID")
    if report.entry_count == 0:
        report.warnings.append("README.md: paper index is empty; structure is valid but content is not yet delivered")
    return report


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    readme_path = root / "README.md"
    contributing_path = root / "CONTRIBUTING.md"
    report = validate_index(readme_path.read_text(encoding="utf-8"), contributing_path.read_text(encoding="utf-8"), date.today())
    if report.errors:
        for error in report.errors:
            print(f"ERROR: {error}")
        return 1
    counts = ", ".join(f"{category}: {count}" for category, count in report.category_counts.items() if count)
    print(f"Validated {report.entry_count} paper entries.")
    print(f"Categories: {counts or 'none'}")
    for warning in report.warnings:
        print(f"WARNING: {warning}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
