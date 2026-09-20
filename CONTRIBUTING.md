# Contributing

Authors are welcome to submit their own papers. You do not need prior permission to open a pull request. If you prefer not to edit Markdown, open a paper-suggestion issue instead.

Contributions may add a relevant paper, correct metadata, update publication status, add a verified resource link, improve a tag or category, or suggest a reading-guide change.

## Scope and review

The paper's core research question should use user preferences, history, profiles, feedback, personal context, or user-specific goals to adapt an LLM's behavior, output, interaction, or decision. Preprints, published papers, surveys, benchmarks, datasets, analysis studies, applications, and negative results are welcome.

Ordinary RAG, general-purpose agents, generic RLHF/DPO, generic memory systems, fictional role-playing, and traditional recommendation papers are not automatically in scope. Explain the direct personalization connection for a boundary case.

Maintainers manually check relevance, source links, metadata, duplicates, and neutral wording. Venue, citation count, and code availability are not entry requirements. Small formatting issues can be fixed during review. For unclear boundary cases, maintainers may request a short relevance explanation. Rejections should give a concrete reason, such as out of scope, duplicate, unreliable source, or obvious spam. Matching entries are normally mergeable after review, but nothing is auto-merged and no fixed review time is promised.

## Entry format

Add each paper to one primary category in the marked Paper Index section of `README.md`. Keep entries ordered by first-public date from newest to oldest within each category; use the normalized ID as the tie-breaker. Update an existing entry when a work receives a stable publication version instead of adding a duplicate.

```markdown
- **[Exact paper title](https://canonical-paper-url)**
  - ID: `arxiv:XXXX.XXXXX`
  - First public: `YYYY-MM`
  - Publication: Preprint
  - Summary: One factual sentence describing the problem and the main approach or contribution.
  - Tags: `user-history` `retrieval`
  - Resources: [Code](https://official-code-url)
```

This is a format template, not a real paper entry. Use a DOI or canonical URL ID when no arXiv ID is available. Summaries should be neutral and supported by the paper; do not claim best performance, reproduction, or field-wide solutions. Omit Resources when no relevant verified link exists, and label third-party implementations as `Unofficial code`.

## Controlled tags

Use one to three tags from this vocabulary. Add a new tag only through a PR that updates this list and explains the need.

<!-- TAGS:START -->
`survey` `user-profile` `preference-elicitation` `user-history`
`memory` `retrieval` `prompting` `steering` `decoding`
`fine-tuning` `peft` `personalized-alignment` `reward-modeling`
`agent` `writing` `recommendation` `search`
`benchmark` `dataset` `evaluation`
`privacy` `safety` `user-control`
<!-- TAGS:END -->

## Submission steps

1. Check whether the work is already indexed under another URL or version.
2. Add or update the entry in one primary category using the format above.
3. Use existing tags and preserve the category/date/ID ordering.
4. Run the local checks below, or open an issue if you cannot run them.
5. Open a focused pull request, usually one paper per PR; a small related batch is also fine.
6. Respond to review questions about sources, relevance, and metadata.

```bash
python3 scripts/validate_index.py
python3 -m unittest discover -s tests -v
```

## Source verification

Use the paper's abstract or full text, official proceedings or journal page, author project page, or an author-associated code repository. Verify the title, canonical link, stable ID, first-public date, publication status, relevance, summary, and optional resources. Do not upload paper PDFs, copy full abstracts, or reuse another list's original descriptions.

## Contributors and paper authors

Submitting a paper does not make you a paper author and does not grant authorship on any future survey. Authors may voluntarily disclose their relationship to a submission, but unrelated personal information is not required. Entries do not carry submitter profile cards.
