# LLM Personalization Papers Design

## Goal

Create a small, publishable, community-maintained index of research on LLM personalization with trustworthy initial entries, a focused reading guide, contribution forms, and an offline validator.

## Scope

- Build the repository at `/Users/jiangwu/llm-personalization-papers`.
- Maintain paper metadata only in the marked Paper Index section of `README.md`.
- Verify initial papers against primary sources available during execution.
- Keep the repository static and dependency-free at runtime; no website, database, crawler, LLM API, or ranking system.
- Do not create or modify a remote repository, push commits, or open external issues or pull requests.

## Structure and data flow

`README.md` is the human-maintained source of truth. `CONTRIBUTING.md` owns the controlled tag vocabulary. `scripts/validate_index.py` locates the repository root from its own path, extracts only the marked sections, parses the agreed Markdown entry format, and reports blocking errors with file and line information. `tests/test_validate_index.py` exercises parser and validator behavior with in-memory fixtures. GitHub Actions runs the same two local commands with read-only permissions.

## Content policy

The index uses eight fixed categories and one category per paper. Entries include a stable ID, first-public date, publication status, neutral summary, controlled tags, and only verified resource links. The reading guide references 5–8 existing entries by ID and gives stage-specific reading reasons. Missing evidence is reported rather than inferred.

## Validation policy

The validator is standard-library-only and offline. It checks section markers, category order, required fields, allowed ID forms, normalized duplicate IDs and URLs, dates, category sorting, tag vocabulary/count/duplicates, HTTP(S) URLs, placeholder URLs, multiline summaries, and empty-index warnings. It does not claim to verify paper quality, publication truth, external link availability, or reproducibility.

## Verification

The final checks run `python3 scripts/validate_index.py` and `python3 -m unittest discover -s tests -v` from the repository root, repeat the validator from another directory, inspect the final diff, and separately report whether GitHub Actions has actually run. 
