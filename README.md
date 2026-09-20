<div align="center">

# 🧠 Awesome LLM Personalization Papers

**A curated, evidence-first reading list for language models that adapt to people.**

User modeling · Memory · Retrieval · Preference alignment · Personalized agents · Evaluation

[![Validate index](https://github.com/jiangwu25/llm-personalization-papers/actions/workflows/validate.yml/badge.svg?branch=main)](https://github.com/jiangwu25/llm-personalization-papers/actions/workflows/validate.yml)
[![Papers](https://img.shields.io/badge/papers-32-5B8FF9?style=flat-square)](#paper-index)
[![License](https://img.shields.io/badge/license-MIT-22A06B?style=flat-square)](LICENSE)

<br>

<a href="README.md"><b>🇺🇸 English</b></a> · <a href="README.zh-CN.md">🇨🇳 简体中文</a> · <a href="README.ko.md">🇰🇷 한국어</a>

</div>

<p align="center">
  <img src="assets/personalization-banner.png" alt="Abstract illustration of a personalized language model connected to a user profile, memory, and tailored response" width="900">
</p>

<p align="center">
  <a href="#foundations">🧱 Foundations</a> ·
  <a href="#surveys">🔭 Surveys</a> ·
  <a href="#memory-retrieval">🧠 Memory</a> ·
  <a href="#training-alignment">🎯 Alignment</a> ·
  <a href="#agents-applications">🤖 Agents</a> ·
  <a href="#benchmarks-evaluation">📊 Evaluation</a> ·
  <a href="#privacy-safety">🛡️ Privacy</a>
</p>

## ✨ Explore the collection

**New to the field?** Follow the [reading guide](docs/reading-guide.md), then use the [surveys](#surveys) to build a map of the area.

**Building a system?** Jump to [memory and retrieval](#memory-retrieval), [personalized alignment](#training-alignment), or [agents and applications](#agents-applications).

**Comparing methods?** Start with [foundational work](#foundations) and [benchmarks and evaluation](#benchmarks-evaluation).

<details>
<summary><b>🎯 Scope and curation policy</b></summary>

This index covers research where user preferences, history, profiles, feedback, personal context, or user-specific goals affect a language model’s behavior, outputs, interactions, or decisions. It includes methods, datasets, benchmarks, applications, and work on privacy, safety, bias, and user control.

The foundations section intentionally includes pre-LLM personalized-dialogue work. These papers established persona conditioning, large-scale persona data, and implicit user profiles that later LLM-personalization research builds on.

For the main index, non-survey papers must be formally published in a selected top/main venue: **ACL, EMNLP, NAACL, AAAI, SIGIR, or CIKM**. Surveys are the general exception. One explicitly approved benchmark preprint, PersonaMem-v2, is listed through the [inclusion-exception ledger](docs/inclusion-exceptions.json); this does not open the index to other preprint-only work. CARD and PsPLUG display EMNLP 2026 based on author-confirmed venue information recorded in the [provenance ledger](docs/paper-provenance.json); no track or proceedings URL is inferred.

Workshop papers, Findings volumes, industry tracks, LREC papers, and other preprint-only work remain excluded. General RAG, generic agents, role-playing, and traditional recommendation papers are also out unless they explicitly study user-specific adaptation.

See the [contribution guide](CONTRIBUTING.md) for the complete inclusion rules.

</details>

## 🌱 Contribute

Found a missing paper, broken link, or incorrect venue? Open a focused [pull request](CONTRIBUTING.md#pull-request-checklist) or use the [paper-suggestion form](https://github.com/jiangwu25/llm-personalization-papers/issues/new?template=paper-suggestion.yml). Authors are welcome to submit their own work; every entry is checked for relevance, source quality, duplicates, venue, and neutral wording.

<a id="paper-index"></a>
## 📚 Paper Index

Each paper stays on one line: **title link** followed by a compact `venue year` label.

<!-- PAPERS:START -->

<a id="foundations"></a>
### 🧱 Foundations & Canonical Benchmarks

- **[Learning Implicit User Profiles for Personalized Retrieval-Based Chatbot](https://arxiv.org/abs/2108.07935)**  `CIKM 2021`
- **[One Chatbot Per Person: Creating Personalized Chatbots based on Implicit User Profiles](https://arxiv.org/abs/2108.09355)**  `SIGIR 2021`
- **[Training Millions of Personalized Dialogue Agents](https://aclanthology.org/D18-1298/)**  `EMNLP 2018`
- **[Personalizing Dialogue Agents: I have a dog, do you have pets too?](https://aclanthology.org/P18-1205/)**  `ACL 2018`

<a id="surveys"></a>
### 🔭 Surveys & Perspectives

- **[A Survey on Personalized and Pluralistic Preference Alignment in Large Language Models](https://arxiv.org/abs/2504.07070)**  `Survey · 2025-04`
- **[A Survey of Personalized Large Language Models: Progress and Future Directions](https://arxiv.org/abs/2502.11528)**  `Survey · 2025-02`
- **[Personalization of Large Language Models: A Survey](https://arxiv.org/abs/2411.00027)**  `Survey · 2024-10`
- **[Two Tales of Persona in LLMs: A Survey of Role-Playing and Personalization](https://aclanthology.org/2024.findings-emnlp.969/)**  `Survey · Findings EMNLP 2024`

<a id="user-modeling"></a>
### 👤 User Modeling & Preference Elicitation

- **[Decisive: Guiding User Decisions with Optimal Preference Elicitation from Unstructured Documents](https://aclanthology.org/2026.acl-long.1465/)**  `ACL 2026`
- **[Optimizing User Profiles via Contextual Bandits for Retrieval-Augmented LLM Personalization](https://aclanthology.org/2026.acl-long.1467/)**  `ACL 2026`
- **[Value Profiles for Encoding Human Variation](https://aclanthology.org/2025.emnlp-main.106/)**  `EMNLP 2025`

<a id="memory-retrieval"></a>
### 🧠 Memory & Retrieval

- **[In Prospect and Retrospect: Reflective Memory Management for Long-term Personalized Dialogue Agents](https://aclanthology.org/2025.acl-long.413/)**  `ACL 2025`
- **[PRIME: Large Language Model Personalization with Cognitive Dual-Memory and Personalized Thought Process](https://aclanthology.org/2025.emnlp-main.1711/)**  `EMNLP 2025`
- **[Optimization Methods for Personalizing Large Language Models through Retrieval Augmentation](https://arxiv.org/abs/2404.05970)**  `SIGIR 2024`
- **[MemoryBank: Enhancing Large Language Models with Long-Term Memory](https://ojs.aaai.org/index.php/AAAI/article/view/29946)**  `AAAI 2024`

<a id="inference-time"></a>
### 🎛️ Prompting, Steering & Decoding

- **[Do Implicit Personalization and Explicit Styles Conflict? PsPLUG: A Lightweight Plug-in for Balancing Personalization and Style in Customized LLMs](https://arxiv.org/abs/2601.06362)**  `EMNLP 2026`
- **[Personalized Text Generation with Contrastive Activation Steering](https://aclanthology.org/2025.acl-long.353/)**  `ACL 2025`
- **[Personalized LLM Decoding via Contrasting Personal Preference](https://aclanthology.org/2025.emnlp-main.1723/)**  `EMNLP 2025`

<a id="training-alignment"></a>
### 🎯 Fine-tuning & Personalized Alignment

- **[CARD: Cluster-level Adaptation with Reward-guided Decoding for Personalized Text Generation](https://arxiv.org/abs/2601.06352)**  `EMNLP 2026`
- **[FaST: Feature-aware Sampling and Tuning for Personalized Preference Alignment with Limited Data](https://aclanthology.org/2025.emnlp-main.475/)**  `EMNLP 2025`
- **[MiCRo: Mixture Modeling and Context-aware Routing for Personalized Preference Learning](https://aclanthology.org/2025.emnlp-main.882/)**  `EMNLP 2025`
- **[Personalized Pieces: Efficient Personalized Large Language Models through Collaborative Efforts](https://aclanthology.org/2024.emnlp-main.371/)**  `EMNLP 2024`
- **[Democratizing Large Language Models via Personalized Parameter-Efficient Fine-tuning](https://aclanthology.org/2024.emnlp-main.372/)**  `EMNLP 2024`

<a id="agents-applications"></a>
### 🤖 Personalized Agents & Applications

- **[Language Models Don’t Know What You Want: Evaluating Personalization in Deep Research Needs Real Users](https://aclanthology.org/2026.acl-long.723/)**  `ACL 2026`
- **[Orion: Steering Personalized Web Agents via Global-Micro Profiling and Adaptive Intent Tracking](https://ojs.aaai.org/index.php/AAAI/article/view/40188)**  `AAAI 2026`
- **[Crafting Personalized Agents through Retrieval-Augmented Generation on Editable Memory Graphs](https://aclanthology.org/2024.emnlp-main.281/)**  `EMNLP 2024`

<a id="benchmarks-evaluation"></a>
### 📊 Benchmarks & Evaluation

- **[PersonaMem-v2: Towards Personalized Intelligence via Learning Implicit User Personas and Agentic Memory](https://arxiv.org/abs/2512.06688)**  `arXiv 2025-12`
- **[LaMP-QA: A Benchmark for Personalized Long-form Question Answering](https://aclanthology.org/2025.emnlp-main.60/)**  `EMNLP 2025`
- **[LaMP: When Large Language Models Meet Personalization](https://aclanthology.org/2024.acl-long.399/)**  `ACL 2024`
- **[Evaluating Very Long-Term Conversational Memory of LLM Agents](https://aclanthology.org/2024.acl-long.747/)**  `ACL 2024`

<a id="privacy-safety"></a>
### 🛡️ Privacy, Safety & User Control

- **[PRISP: Privacy-Safe Few-Shot Personalization via Lightweight Adaptation](https://aclanthology.org/2026.acl-long.1146/)**  `ACL 2026`
- **[Personalized Language Models via Privacy-Preserving Evolutionary Model Merging](https://aclanthology.org/2025.emnlp-main.1747/)**  `EMNLP 2025`

<!-- PAPERS:END -->

## 🙌 Community

Thanks to everyone who contributes paper suggestions, metadata corrections, source links, and reading-guide improvements. Inclusion means a paper matches the collection policy; it does not imply endorsement of its findings.

## 📄 License

Repository text, scripts, and templates are released under the [MIT License](LICENSE). Linked papers, code, datasets, and other external materials retain their own licenses.

<p align="center">
  <sub>Built for researchers and builders exploring human-centered language models.</sub>
</p>
