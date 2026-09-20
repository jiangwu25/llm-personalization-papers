# LLM Personalization Papers Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a trustworthy local GitHub-ready index of LLM personalization papers with contribution workflows and an offline validator.

**Architecture:** Keep README as the only manually maintained index, with fixed category and entry markers. Use a standard-library Python parser/validator with pure functions tested through `unittest`; keep community files and CI declarative and read-only.

**Tech Stack:** Markdown, YAML, Python 3.11+ standard library, `unittest`, GitHub Actions.

**Spec:** `docs/superpowers/specs/2026-09-20-llm-personalization-papers-design.md`

## Global Constraints

- Public repository content is English; execution report is Chinese.
- Preserve existing files; never reset or overwrite unrelated user work.
- Do not invent papers, metadata, source links, authors, publication status, tests, or maintenance data.
- No network access from the validator, tests, or CI checks.
- No remote repository creation, push, external issue/PR, website, crawler, database, or LLM API.
- README is the only hand-maintained paper metadata source.

---

### Task 1: Repository skeleton and community documents

**Files:**
- Create: `README.md`, `CONTRIBUTING.md`, `LICENSE`, `.gitignore`
- Create: `docs/reading-guide.md`
- Create: `.github/pull_request_template.md`
- Create: `.github/ISSUE_TEMPLATE/paper-suggestion.yml`
- Create: `.github/ISSUE_TEMPLATE/correction.yml`
- Create: `.github/ISSUE_TEMPLATE/config.yml`

**Steps:**
- [ ] Create the required directories without adding application dependencies.
- [ ] Write the English README structure, fixed category anchors, contribution policy, external-resource rights note, and empty-index-safe paper markers.
- [ ] Write the controlled tag vocabulary once in `CONTRIBUTING.md` and document the exact entry template.
- [ ] Write the reading-guide structure so every eventual recommendation must point to a README ID.
- [ ] Add the supplied PR template and valid GitHub Issue Forms with only the requested fields.
- [ ] Add a standard MIT license for `LLM Personalization Papers contributors` dated 2026.
- [ ] Run YAML parsing/shape checks available locally before adding entries.

**Verification:** Confirm no `TODO`, `OWNER/REPO`, `example.com`, fake paper, or empty resource link appears in public files; inspect all required paths.

### Task 2: Validator tests first

**Files:**
- Create: `tests/test_validate_index.py`
- Test target: `scripts/validate_index.py`

**Steps:**
- [ ] Write `unittest` fixtures for a legal marked index and tag block.
- [ ] Add tests for missing fields, duplicate IDs, normalized arXiv URL/version duplicates, unknown and repeated tags, invalid months, `YYYY` sorting, same-date ID sorting, no resources, multiline summaries, out-of-range examples, missing/invalid markers, empty indexes, and placeholder URLs.
- [ ] Run `python3 -m unittest discover -s tests -v` and confirm the new tests fail because the validator is not implemented yet.

**Verification:** Capture the expected failure mode and ensure failures are assertion failures or import errors caused by the missing implementation, not malformed test fixtures.

### Task 3: Minimal offline validator implementation

**Files:**
- Create: `scripts/validate_index.py`
- Modify: `tests/test_validate_index.py` only if a test fixture exposes a test defect

**Interfaces:**
- `parse_marked_block(text: str, start_marker: str, end_marker: str) -> tuple[str, int]`
- `parse_tags(text: str) -> set[str]`
- `parse_papers(text: str) -> list[PaperEntry]`
- `normalize_paper_url(url: str) -> str`
- `validate_index(readme_text: str, contributing_text: str, today: date) -> ValidationReport`
- `main() -> int`

**Steps:**
- [ ] Define small dataclasses or equivalent typed records for parsed entries and validation errors.
- [ ] Locate markers relative to their owning file, reject missing/duplicate/out-of-order markers, and preserve line numbers.
- [ ] Parse only category headings and bullet entries inside README markers; support indented continuation lines for summaries and resources.
- [ ] Parse stable IDs and normalize arXiv `abs`, `pdf`, and versioned forms to the base identifier.
- [ ] Validate fields, dates, category order, descending date order with year-only dates after month-known dates, ID tie-breakers, tags, URL forms, and placeholder hosts/paths.
- [ ] Emit actionable filename/line errors, real entry/category counts on success, and a visible warning for an empty index.
- [ ] Keep all network, subprocess, and third-party imports out of the validator.
- [ ] Run the full unittest suite and fix only production defects exposed by failing tests.

**Verification:** `python3 -m unittest discover -s tests -v` exits 0 with all cases passing.

### Task 4: Verified paper content and reading route

**Files:**
- Modify: `README.md`
- Modify: `docs/reading-guide.md`

**Steps:**
- [ ] Search primary sources for candidates across the eight categories.
- [ ] For every candidate, record title, canonical URL, stable ID, first-public date, publication status, relevance, summary, tags, and verified official resources.
- [ ] Exclude candidates whose personalization relevance or metadata cannot be supported; do not infer missing dates or venues.
- [ ] Sort each category exactly as specified and keep one principal category per paper.
- [ ] Select 5–8 verified entries for a staged reading path and refer to their exact IDs.
- [ ] Re-read the README as a user and remove unsupported claims about completeness, quality, popularity, reproduction, or coverage.

**Verification:** Run the validator, count entries by category, and manually trace every reading-guide ID to exactly one README entry.

### Task 5: CI, local checks, and final audit

**Files:**
- Create: `.github/workflows/validate.yml`
- Modify: `.gitignore` if needed after running tests

**Steps:**
- [ ] Verify current official checkout/setup-python action references from primary GitHub sources; if SHA verification is unavailable, use a clearly documented limitation rather than inventing a SHA.
- [ ] Configure `pull_request` and `push` to `main`, `contents: read`, credential persistence disabled, a five-minute timeout, and the two local commands.
- [ ] Run the validator from the repository root and from `/tmp` or another unrelated directory.
- [ ] Run the full test suite from the repository root.
- [ ] Inspect `git diff --check`, `git status`, tracked file list, links/anchors, placeholder strings, secrets, caches, and the final file structure.
- [ ] Report local verification separately from GitHub-hosted CI; do not claim the workflow ran unless it actually did.

**Verification:** Save the exact command outputs and compare the final tree against the execution document's acceptance checklist before reporting completion.
