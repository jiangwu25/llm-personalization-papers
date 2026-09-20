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
| [Benchmarks & evaluation](#benchmarks-evaluation) | Tasks, datasets, robustness, and user-specific evaluation | 1 |

## 🎯 Scope and curation

This index covers research where user preferences, history, profiles, feedback, personal context, or user-specific goals affect a language model’s behavior, outputs, interactions, or decisions. It includes methods, datasets, benchmarks, applications, and work on privacy, safety, bias, and user control.

The first section intentionally includes pre-LLM personalized-dialogue work: these papers established persona conditioning, large-scale persona data, and implicit user profiles that later LLM-personalization work builds on. The remaining sections emphasize the LLM era and current research directions.

For the main index, non-survey papers must be formally published in a selected top/main venue: ACL, EMNLP, NAACL, AAAI, SIGIR, or CIKM. Surveys are the only exception. Workshop papers, Findings volumes, industry tracks, LREC papers, and preprint-only work are intentionally excluded from the main index. General RAG, generic agents, role-playing, and traditional recommendation papers are also out unless the paper explicitly studies user-specific adaptation.

See [CONTRIBUTING.md](CONTRIBUTING.md) for the full inclusion rules and entry format.

## 🤝 Contribute

Found a missing paper, a broken link, or a misleading summary? The fastest route is a focused [pull request](CONTRIBUTING.md#pull-request-checklist). If you do not want to edit Markdown, use the [paper-suggestion issue form](https://github.com/jiangwu25/llm-personalization-papers/issues/new?template=paper-suggestion.yml).

Authors are welcome to submit their own work. We check relevance, source quality, metadata, duplicates, neutral wording, and ordering. Inclusion does not imply endorsement of a paper’s findings.

<a id="paper-index"></a>
## 📚 Paper Index

<!-- PAPERS:START -->

<a id="foundations"></a>
### Foundations & Canonical Benchmarks

- **[Learning Implicit User Profiles for Personalized Retrieval-Based Chatbot](https://arxiv.org/abs/2108.07935)**
  - ID: `arxiv:2108.07935`
  - First public: `2021-08`
  - Publication: CIKM 2021
  - Summary: Separates a user’s language style from context-dependent preferences and uses both signals to rank responses for a personalized retrieval-based chatbot.
  - Tags: `foundations` `user-profile` `retrieval`

- **[One Chatbot Per Person: Creating Personalized Chatbots based on Implicit User Profiles](https://arxiv.org/abs/2108.09355)**
  - ID: `arxiv:2108.09355`
  - First public: `2021-08`
  - Publication: SIGIR 2021
  - Summary: Learns implicit user profiles from dialogue history, combines general and post-aware memory, and decodes responses using user-specific vocabulary.
  - Tags: `foundations` `user-profile` `memory`

- **[Training Millions of Personalized Dialogue Agents](https://aclanthology.org/D18-1298/)**
  - ID: `doi:10.18653/v1/D18-1298`
  - First public: `2018-10`
  - Publication: EMNLP 2018
  - Summary: Scales persona-based dialogue training to millions of personas and hundreds of millions of persona-grounded conversations.
  - Tags: `foundations` `dataset` `user-profile`

- **[Personalizing Dialogue Agents: I have a dog, do you have pets too?](https://aclanthology.org/P18-1205/)**
  - ID: `doi:10.18653/v1/P18-1205`
  - First public: `2018-07`
  - Publication: ACL 2018
  - Summary: Introduces persona-conditioned dialogue modeling and the Persona-Chat task, including conditioning on the agent’s profile and learning about the conversation partner.
  - Tags: `foundations` `user-profile` `preference-elicitation`

<a id="surveys"></a>
### Surveys & Perspectives

- **[A Survey on Personalized and Pluralistic Preference Alignment in Large Language Models](https://arxiv.org/abs/2504.07070)**
  - ID: `arxiv:2504.07070`
  - First public: `2025-04`
  - Publication: Preprint
  - Summary: Surveys personalized preference alignment and organizes methods by training-time, inference-time, and user-modeling approaches while discussing evaluation and open problems.
  - Tags: `survey` `personalized-alignment` `evaluation`

- **[A Survey of Personalized Large Language Models: Progress and Future Directions](https://arxiv.org/abs/2502.11528)**
  - ID: `arxiv:2502.11528`
  - First public: `2025-02`
  - Publication: Preprint
  - Summary: Reviews personalized LLM methods through prompting, personalized adapters, and preference alignment, and summarizes applications, limitations, and future research directions.
  - Tags: `survey` `user-profile` `personalized-alignment`

- **[Personalization of Large Language Models: A Survey](https://arxiv.org/abs/2411.00027)**
  - ID: `arxiv:2411.00027`
  - First public: `2024-10`
  - Publication: Preprint
  - Summary: Unifies personalized text generation and LLM-based personalization applications with taxonomies for personalization granularity, techniques, datasets, evaluation, and use cases.
  - Tags: `survey` `evaluation` `user-profile`

<a id="user-modeling"></a>
### User Modeling & Preference Elicitation

- **[Optimizing User Profiles via Contextual Bandits for Retrieval-Augmented LLM Personalization](https://aclanthology.org/2026.acl-long.1467/)**
  - ID: `url:https://aclanthology.org/2026.acl-long.1467/`
  - First public: `2026-07`
  - Publication: ACL 2026
  - Summary: Treats profile construction as an order-sensitive contextual-bandit problem instead of selecting history records by semantic relevance alone.
  - Tags: `user-profile` `retrieval` `agent`

<a id="memory-retrieval"></a>
### Memory & Retrieval

- **[PRIME: Large Language Model Personalization with Cognitive Dual-Memory and Personalized Thought Process](https://aclanthology.org/2025.emnlp-main.1711/)**
  - ID: `url:https://aclanthology.org/2025.emnlp-main.1711/`
  - First public: `2025-11`
  - Publication: EMNLP 2025
  - Summary: Separates episodic interaction memory from semantic user beliefs and adds a personalized thinking process to a unified personalization framework.
  - Tags: `memory` `personalized-alignment` `user-history`

- **[MemoryBank: Enhancing Large Language Models with Long-Term Memory](https://ojs.aaai.org/index.php/AAAI/article/view/29946)**
  - ID: `doi:10.1609/aaai.v38i17.29946`
  - First public: `2023-05`
  - Publication: AAAI 2024
  - Summary: Adds evolving long-term memory with retrieval and forgetting-inspired updates to support sustained interaction and adaptation to a user's personality.
  - Tags: `memory` `retrieval` `user-history`

<a id="inference-time"></a>
### Prompting, Steering & Decoding

- **[Personalized LLM Decoding via Contrasting Personal Preference](https://aclanthology.org/2025.emnlp-main.1723/)**
  - ID: `url:https://aclanthology.org/2025.emnlp-main.1723/`
  - First public: `2025-11`
  - Publication: EMNLP 2025
  - Summary: Applies reward-guided contrasting at decoding time after user-specific PEFT to amplify an implicit personal preference signal without another training stage.
  - Tags: `decoding` `personalized-alignment` `peft`

<a id="training-alignment"></a>
### Fine-tuning & Personalized Alignment

- **[FaST: Feature-aware Sampling and Tuning for Personalized Preference Alignment with Limited Data](https://aclanthology.org/2025.emnlp-main.475/)**
  - ID: `url:https://aclanthology.org/2025.emnlp-main.475/`
  - First public: `2025-11`
  - Publication: EMNLP 2025
  - Summary: Studies personalized preference alignment with small per-user questionnaires and proposes feature-aware sampling and parameter-efficient tuning.
  - Tags: `personalized-alignment` `fine-tuning` `peft`

- **[Personalized Pieces: Efficient Personalized Large Language Models through Collaborative Efforts](https://aclanthology.org/2024.emnlp-main.371/)**
  - ID: `url:https://aclanthology.org/2024.emnlp-main.371/`
  - First public: `2024-11`
  - Publication: EMNLP 2024
  - Summary: Breaks personalized PEFT modules into shareable pieces and learns gates that assemble useful pieces for a target user while reducing per-user cost.
  - Tags: `peft` `personalized-alignment` `privacy`

- **[Democratizing Large Language Models via Personalized Parameter-Efficient Fine-tuning](https://aclanthology.org/2024.emnlp-main.372/)**
  - ID: `url:https://aclanthology.org/2024.emnlp-main.372/`
  - First public: `2024-11`
  - Publication: EMNLP 2024
  - Summary: Stores user-specific behavior patterns and preferences in one PEFT module per user to support model ownership and local personalization.
  - Tags: `peft` `fine-tuning` `user-history`

<a id="agents-applications"></a>
### Personalized Agents & Applications

- **[Language Models Don’t Know What You Want: Evaluating Personalization in Deep Research Needs Real Users](https://aclanthology.org/2026.acl-long.723/)**
  - ID: `url:https://aclanthology.org/2026.acl-long.723/`
  - First public: `2026`
  - Publication: ACL 2026
  - Summary: Introduces MyScholarQA, a personalized deep-research setting that profiles real users, proposes actions, and produces reports after user-approved planning.
  - Tags: `agent` `search` `evaluation`

- **[Crafting Personalized Agents through Retrieval-Augmented Generation on Editable Memory Graphs](https://aclanthology.org/2024.emnlp-main.281/)**
  - ID: `url:https://aclanthology.org/2024.emnlp-main.281/`
  - First public: `2024-11`
  - Publication: EMNLP 2024
  - Summary: Builds personalized agents from editable graphs of smartphone memories and evaluates transfer to a real assistant application.
  - Tags: `agent` `memory` `retrieval`

<a id="benchmarks-evaluation"></a>
### Benchmarks & Evaluation

- **[LaMP: When Large Language Models Meet Personalization](https://aclanthology.org/2024.acl-long.399/)**
  - ID: `arxiv:2304.11406`
  - First public: `2023-04`
  - Publication: ACL 2024
  - Summary: Introduces seven personalized language tasks and retrieval augmentation methods for selecting relevant items from individual user profiles.
  - Tags: `benchmark` `retrieval` `evaluation`
  - Resources: [Code](https://github.com/LaMP-Benchmark/LaMP)

<!-- PAPERS:END -->

## 🙌 Contributors & Acknowledgments

Thank you to everyone who contributes paper suggestions, metadata corrections, source links, reading-guide improvements, and maintenance work. Contributors will be listed here as the project grows.

## 📄 License

The original text, scripts, and templates in this repository are released under the [MIT License](LICENSE). Linked papers, code, datasets, and other external materials remain under their own licenses and terms; this repository license does not relicense them.

## 🏷️ Suggested GitHub Topics

`llm-personalization` `personalized-llm` `large-language-models` `paper-list` `user-modeling`
