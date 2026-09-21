<div align="center">

# Contributing

Help keep this list useful, verifiable, and easy to read.

[Add or correct a paper](https://github.com/jiangwu25/llm-personalization-papers/compare) · [Suggest a paper](https://github.com/jiangwu25/llm-personalization-papers/issues/new?template=paper-suggestion.yml) · [Read the index](README.md)

</div>

> [!TIP]
> The best contribution is small and source-backed: one paper, one correction, or one clearly scoped documentation improvement.

## 🧭 Choose a contribution path

| You want to… | Use | Include |
| --- | --- | --- |
| Add or correct an entry | [Pull request](https://github.com/jiangwu25/llm-personalization-papers/compare) | Canonical URL, relevance note, metadata sources, and a clean validator run |
| Suggest a paper without editing Markdown | [Paper suggestion](https://github.com/jiangwu25/llm-personalization-papers/issues/new?template=paper-suggestion.yml) | Complete title, stable link, and why it directly studies personalization |
| Fix a broken link or typo | Pull request | The smallest possible change and the replacement source |
| Improve the reading route or docs | Pull request | The learner problem it solves and any links it adds |

## 🎯 What belongs here

The paper’s core research question should use user preferences, history, profiles, feedback, personal context, or user-specific goals to adapt a language model’s behavior, output, interaction, or decision.

We welcome:

- foundational persona and user-modeling work.
- recent papers, benchmarks, datasets, applications, and negative results from 2025 onward.
- canonical benchmarks in Benchmarks & Evaluation and foundational pre-2025 papers in Root & Classics.
- methods based on prompting, retrieval, memory, fine-tuning, preference learning, decoding, or agents.
- work on privacy, safety, fairness, leakage, and user control in personalization.

Usually out of scope unless the paper makes the personalization connection explicit:

- ordinary RAG or generic memory systems.
- general-purpose agents and generic RLHF/DPO.
- fictional role-playing without user-specific adaptation.
- traditional recommendation systems without a language-model personalization component.

For a boundary case, explain the direct connection in one or two sentences.

### 📅 Recency policy

The active index emphasizes the latest work from 2026 onward. Selected papers from 2025 are also included. New paper submissions should be from 2026 onward. Pre-2025 work is retained only when it is a canonical benchmark in Benchmarks & Evaluation or a foundational reference in Root & Classics. Surveys remain available as orientation across publication years.

### Venue filter

For the main index, non-survey papers must be formally published at **ACL, EMNLP, ICLR, ICML, or NeurIPS**. Findings papers count as accepted publications. AAAI and COLM papers are considered only as exceptional classics with at least 1,000 citations documented by a stable bibliometric source. Surveys are the general exception and may remain preprints. The curated benchmark set is recorded in [benchmark-catalog.json](docs/benchmark-catalog.json) and appears in Benchmarks & Evaluation. Other pre-2025 canonical references are placed under Root & Classics. PersonaMem-v2 remains separately covered by the transparent [inclusion-exception ledger](docs/inclusion-exceptions.json). Do not treat these named records as a blanket admission rule for unrelated work.

For entries whose venue was supplied by an author but is not yet independently represented by a public proceedings page, see the [paper provenance ledger](docs/paper-provenance.json). Do not invent a track, DOI, page number, or proceedings URL.

## 🧩 Entry format

Add each paper to one primary category inside the marked Paper Index section of `README.md`. Keep the public list compact: one paper per line, with the venue and year at the end. Sort entries newest-first by year. Use the normalized URL as the tie-breaker.

Benchmark additions must also update [benchmark-catalog.json](docs/benchmark-catalog.json). Every catalog entry must remain in the unified Benchmarks & Evaluation section.

```markdown
- **[Exact paper title](https://canonical-paper-url)**  `ACL 2018`
```

Use the official proceedings or publisher URL when available. The one-line label should use the formal venue and publication year, for example `ACL 2018`, `ICLR 2026`, or `Survey · 2025`. A named benchmark exception must use its accurate preprint label, such as `arXiv 2025-12`. Keep summaries and implementation details in the paper itself or the reading guide rather than expanding the main index.

## ✅ Five-minute checklist

- [ ] The work is not already indexed under another URL or version.
- [ ] The paper has a stable abstract, proceedings, journal, or arXiv link.
- [ ] The relevance to user-specific adaptation is explicit.
- [ ] Title, date, publication status, and summary are source-backed.
- [ ] The entry uses one primary category and the compact one-line format.
- [ ] The entry is in year/URL order and has no placeholder links.
- [ ] I ran the validator and unit tests.

## 🏷️ Controlled tags

The compact README list does not display tags. This vocabulary is retained for future structured metadata and for maintainers who need consistent labels. Add a new tag only through a PR that updates this list and explains the need.

<!-- TAGS:START -->
`foundations` `survey` `user-profile` `preference-elicitation` `user-history`
`memory` `retrieval` `prompting` `steering` `decoding`
`fine-tuning` `peft` `personalized-alignment` `reward-modeling`
`agent` `writing` `recommendation` `search`
`benchmark` `dataset` `evaluation`
`privacy` `safety` `user-control`
<!-- TAGS:END -->

## 🔀 Pull request checklist

Open a focused PR, usually one paper per PR. A small related batch is fine. The repository’s PR template will ask you to provide the paper URL, category, relevance, and metadata sources.

Run these commands from the repository root:

```bash
python3 scripts/validate_index.py
python3 -m unittest discover -s tests -v
```

Keep unrelated formatting changes out of the same PR. Nothing is auto-merged: maintainers manually check relevance, source links, metadata, duplicates, neutral wording, and ordering.

## 🔍 Source verification

Prefer this source order:

1. official proceedings, journal, or publisher page.
2. the paper’s arXiv or other stable preprint page.
3. an author or lab project page.
4. an author-associated code or data repository.

Verify the title, canonical link, stable ID, first-public date, publication status, relevance, summary, and optional resources. Do not upload PDFs, copy full abstracts, or reuse another list’s original descriptions.

## 🤝 Review and authorship

For unclear boundary cases, maintainers may request a short relevance explanation. Rejections should give a concrete reason, such as out of scope, duplicate, unreliable source, or obvious spam. No fixed review time is promised.

Submitting a paper does not make you a paper author and does not grant authorship on any future survey. Authors may voluntarily disclose their relationship to a submission. Unrelated personal information is not required.
