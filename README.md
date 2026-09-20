<div align="center">

# LLM Personalization Papers

**A curated, evidence-first reading list for making language models useful to one person.**

User modeling · memory · retrieval · preference alignment · personalized agents · evaluation

[![Validate index](https://github.com/jiangwu25/llm-personalization-papers/actions/workflows/validate.yml/badge.svg?branch=main)](https://github.com/jiangwu25/llm-personalization-papers/actions/workflows/validate.yml)
[![Papers](https://img.shields.io/badge/papers-17-5B8FF9)](#paper-index)
[![License](https://img.shields.io/badge/license-MIT-22A06B)](LICENSE)

</div>

<p align="center">
  <img src="assets/personalization-banner.png" alt="Abstract illustration of a personalized language model connected to a user profile, memory, and tailored response" width="100%">
</p>

## 🚀 Start here

| If you want to… | Start with |
| --- | --- |
| Build the vocabulary | [Reading guide](docs/reading-guide.md) → [surveys](#surveys) |
| Understand the historical roots | [Foundations & canonical benchmarks](#foundations) |
| Compare evaluation setups | [Benchmarks & evaluation](#benchmarks-evaluation) |
| Study memory and retrieval | [Memory & retrieval](#memory-retrieval) |
| Add or correct a paper | [Contribution guide](CONTRIBUTING.md) |

## 🧭 Field map

| Track | What it covers | Papers |
| --- | --- | :---: |
| [Foundations & canonical benchmarks](#foundations) | Persona conditioning, implicit profiles, and early personalization tasks | 4 |
| [Surveys & perspectives](#surveys) | Taxonomies, problem definitions, and open questions | 3 |
| [User modeling & preference elicitation](#user-modeling) | Profiles, histories, preferences, and user representations | 1 |
| [Memory & retrieval](#memory-retrieval) | Long-term memory, profile construction, and history selection | 2 |
| [Prompting, steering & decoding](#inference-time) | Inference-time adaptation without full model retraining | 1 |
| [Fine-tuning & personalized alignment](#training-alignment) | PEFT, feedback, reward modeling, and parameter updates | 3 |
| [Personalized agents & applications](#agents-applications) | Agents, planning, writing, recommendation, and search | 2 |
| [Benchmarks & evaluation](#benchmarks-evaluation) | Tasks, datasets, and user-specific evaluation | 1 |

## 🎯 Scope and curation

This index covers research where user preferences, history, profiles, feedback, personal context, or user-specific goals affect a language model’s behavior, outputs, interactions, or decisions. It includes methods, datasets, benchmarks, applications, and work on privacy, safety, bias, and user control.

The first section intentionally includes pre-LLM personalized-dialogue work: these papers established persona conditioning, large-scale persona data, and implicit user profiles that later LLM-personalization work builds on. The remaining sections emphasize the LLM era and current research directions.

For the main index, non-survey papers must be formally published in a selected top/main venue: ACL, EMNLP, NAACL, AAAI, SIGIR, or CIKM. Surveys are the only exception. Workshop papers, Findings volumes, industry tracks, LREC papers, and preprint-only work are intentionally excluded from the main index. General RAG, generic agents, role-playing, and traditional recommendation papers are also out unless the paper explicitly studies user-specific adaptation.

See [CONTRIBUTING.md](CONTRIBUTING.md) for the full inclusion rules and entry format.

## 🤝 Contribute

Found a missing paper, a broken link, or a misleading label? The fastest route is a focused [pull request](CONTRIBUTING.md#pull-request-checklist). If you do not want to edit Markdown, use the [paper-suggestion issue form](https://github.com/jiangwu25/llm-personalization-papers/issues/new?template=paper-suggestion.yml).

Authors are welcome to submit their own work. We check relevance, source quality, metadata, duplicates, venue, neutral wording, and ordering. Inclusion does not imply endorsement of a paper’s findings.

<a id="paper-index"></a>
## 📚 Paper Index

One line per paper: title, canonical link, and venue/year.

<!-- PAPERS:START -->

<a id="foundations"></a>
### Foundations & Canonical Benchmarks

- **[Learning Implicit User Profiles for Personalized Retrieval-Based Chatbot](https://arxiv.org/abs/2108.07935)** — CIKM 2021
- **[One Chatbot Per Person: Creating Personalized Chatbots based on Implicit User Profiles](https://arxiv.org/abs/2108.09355)** — SIGIR 2021
- **[Training Millions of Personalized Dialogue Agents](https://aclanthology.org/D18-1298/)** — EMNLP 2018
- **[Personalizing Dialogue Agents: I have a dog, do you have pets too?](https://aclanthology.org/P18-1205/)** — ACL 2018

<a id="surveys"></a>
### Surveys & Perspectives

- **[A Survey on Personalized and Pluralistic Preference Alignment in Large Language Models](https://arxiv.org/abs/2504.07070)** — Survey · 2025-04
- **[A Survey of Personalized Large Language Models: Progress and Future Directions](https://arxiv.org/abs/2502.11528)** — Survey · 2025-02
- **[Personalization of Large Language Models: A Survey](https://arxiv.org/abs/2411.00027)** — Survey · 2024-10

<a id="user-modeling"></a>
### User Modeling & Preference Elicitation

- **[Optimizing User Profiles via Contextual Bandits for Retrieval-Augmented LLM Personalization](https://aclanthology.org/2026.acl-long.1467/)** — ACL 2026

<a id="memory-retrieval"></a>
### Memory & Retrieval

- **[PRIME: Large Language Model Personalization with Cognitive Dual-Memory and Personalized Thought Process](https://aclanthology.org/2025.emnlp-main.1711/)** — EMNLP 2025
- **[MemoryBank: Enhancing Large Language Models with Long-Term Memory](https://ojs.aaai.org/index.php/AAAI/article/view/29946)** — AAAI 2024

<a id="inference-time"></a>
### Prompting, Steering & Decoding

- **[Personalized LLM Decoding via Contrasting Personal Preference](https://aclanthology.org/2025.emnlp-main.1723/)** — EMNLP 2025

<a id="training-alignment"></a>
### Fine-tuning & Personalized Alignment

- **[FaST: Feature-aware Sampling and Tuning for Personalized Preference Alignment with Limited Data](https://aclanthology.org/2025.emnlp-main.475/)** — EMNLP 2025
- **[Personalized Pieces: Efficient Personalized Large Language Models through Collaborative Efforts](https://aclanthology.org/2024.emnlp-main.371/)** — EMNLP 2024
- **[Democratizing Large Language Models via Personalized Parameter-Efficient Fine-tuning](https://aclanthology.org/2024.emnlp-main.372/)** — EMNLP 2024

<a id="agents-applications"></a>
### Personalized Agents & Applications

- **[Language Models Don’t Know What You Want: Evaluating Personalization in Deep Research Needs Real Users](https://aclanthology.org/2026.acl-long.723/)** — ACL 2026
- **[Crafting Personalized Agents through Retrieval-Augmented Generation on Editable Memory Graphs](https://aclanthology.org/2024.emnlp-main.281/)** — EMNLP 2024

<a id="benchmarks-evaluation"></a>
### Benchmarks & Evaluation

- **[LaMP: When Large Language Models Meet Personalization](https://aclanthology.org/2024.acl-long.399/)** — ACL 2024

<!-- PAPERS:END -->

## 🙌 Contributors & Acknowledgments

Thank you to everyone who contributes paper suggestions, metadata corrections, source links, reading-guide improvements, and maintenance work. Contributors will be listed here as the project grows.

## 📄 License

The original text, scripts, and templates in this repository are released under the [MIT License](LICENSE). Linked papers, code, datasets, and other external materials remain under their own licenses and terms; this repository license does not relicense them.

## 🏷️ Suggested GitHub Topics

`llm-personalization` `personalized-llm` `large-language-models` `paper-list` `user-modeling`
