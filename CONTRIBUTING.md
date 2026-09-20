<div align="center">

# Contributing

Help keep this list useful, verifiable, and easy to read.

[Add or correct a paper](https://github.com/jiangwu25/llm-personalization-papers/compare) · [Suggest a paper](https://github.com/jiangwu25/llm-personalization-papers/issues/new?template=paper-suggestion.yml) · [Read the index](README.md)

</div>

> [!TIP]
> The best contribution is small and source-backed: one paper, one correction, or one clearly scoped documentation improvement.

## Choose a contribution path

| You want to… | Use | Include |
| --- | --- | --- |
| Add or correct an entry | [Pull request](https://github.com/jiangwu25/llm-personalization-papers/compare) | Canonical URL, relevance note, metadata sources, and a clean validator run |
| Suggest a paper without editing Markdown | [Paper suggestion](https://github.com/jiangwu25/llm-personalization-papers/issues/new?template=paper-suggestion.yml) | Complete title, stable link, and why it directly studies personalization |
| Fix a broken link or typo | Pull request | The smallest possible change and the replacement source |
| Improve the reading route or docs | Pull request | The learner problem it solves and any links it adds |

## What belongs here

The paper’s core research question should use user preferences, history, profiles, feedback, personal context, or user-specific goals to adapt a language model’s behavior, output, interaction, or decision.

We welcome:

- foundational persona and user-modeling work;
- preprints, published papers, surveys, benchmarks, datasets, applications, and negative results;
- methods based on prompting, retrieval, memory, fine-tuning, preference learning, decoding, or agents;
- work on privacy, safety, fairness, leakage, and user control in personalization.

Usually out of scope unless the paper makes the personalization connection explicit:

- ordinary RAG or generic memory systems;
- general-purpose agents and generic RLHF/DPO;
- fictional role-playing without user-specific adaptation;
- traditional recommendation systems without a language-model personalization component.

For a boundary case, explain the direct connection in one or two sentences.

## Entry format

Add each paper to one primary category inside the marked Paper Index section of `README.md`. Keep entries newest-first by first-public date; use the normalized ID as the tie-breaker.

```markdown
- **[Exact paper title](https://canonical-paper-url)**
  - ID: `arxiv:XXXX.XXXXX`
  - First public: `YYYY-MM`
  - Publication: Preprint
  - Summary: One factual sentence describing the problem and the main approach or contribution.
  - Tags: `user-history` `retrieval`
  - Resources: [Code](https://official-code-url)
```

Use a DOI or canonical URL ID when no arXiv ID is available. Summaries should be neutral and supported by the paper; do not claim best performance, reproduction, or field-wide solutions. Omit `Resources` when no relevant verified link exists. Label third-party implementations as `Unofficial code`.

## Five-minute checklist

- [ ] The work is not already indexed under another URL or version.
- [ ] The paper has a stable abstract, proceedings, journal, or arXiv link.
- [ ] The relevance to user-specific adaptation is explicit.
- [ ] Title, date, publication status, and summary are source-backed.
- [ ] The entry uses one primary category and one to three existing tags.
- [ ] The entry is in date/ID order and has no placeholder links.
- [ ] I ran the validator and unit tests.

## Controlled tags

Use one to three tags from this vocabulary. Add a new tag only through a PR that updates this list and explains the need.

<!-- TAGS:START -->
`foundations` `survey` `user-profile` `preference-elicitation` `user-history`
`memory` `retrieval` `prompting` `steering` `decoding`
`fine-tuning` `peft` `personalized-alignment` `reward-modeling`
`agent` `writing` `recommendation` `search`
`benchmark` `dataset` `evaluation`
`privacy` `safety` `user-control`
<!-- TAGS:END -->

## Pull request checklist

Open a focused PR, usually one paper per PR; a small related batch is fine. The repository’s PR template will ask you to provide the paper URL, category, relevance, and metadata sources.

Run these commands from the repository root:

```bash
python3 scripts/validate_index.py
python3 -m unittest discover -s tests -v
```

Keep unrelated formatting changes out of the same PR. Nothing is auto-merged: maintainers manually check relevance, source links, metadata, duplicates, neutral wording, and ordering.

## Source verification

Prefer this source order:

1. official proceedings, journal, or publisher page;
2. the paper’s arXiv or other stable preprint page;
3. an author or lab project page;
4. an author-associated code or data repository.

Verify the title, canonical link, stable ID, first-public date, publication status, relevance, summary, and optional resources. Do not upload PDFs, copy full abstracts, or reuse another list’s original descriptions.

## Review and authorship

For unclear boundary cases, maintainers may request a short relevance explanation. Rejections should give a concrete reason, such as out of scope, duplicate, unreliable source, or obvious spam. No fixed review time is promised.

Submitting a paper does not make you a paper author and does not grant authorship on any future survey. Authors may voluntarily disclose their relationship to a submission; unrelated personal information is not required.
