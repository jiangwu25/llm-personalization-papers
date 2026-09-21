<div align="center">

# 🧠 Awesome LLM Personalization Papers

**A curated, evidence-first reading list for language models that adapt to people.**

User modeling · Memory · Retrieval · Preference alignment · Personalized agents · Evaluation

[![Validate index](https://github.com/jiangwu25/llm-personalization-papers/actions/workflows/validate.yml/badge.svg?branch=main)](https://github.com/jiangwu25/llm-personalization-papers/actions/workflows/validate.yml)
[![Papers](https://img.shields.io/badge/papers-44-5B8FF9?style=flat-square)](#paper-index)
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
  <a href="#privacy-safety">🛡️ Privacy</a> ·
  <a href="#root-classics">🌳 Root</a>
</p>

## ✨ Explore the collection

**New to the field?** Follow the [reading guide](docs/reading-guide.md), then use the [surveys](#surveys) to build a map of the area.

**Building a system?** Jump to [memory and retrieval](#memory-retrieval), [personalized alignment](#training-alignment), or [agents and applications](#agents-applications).

**Comparing methods?** Start with [foundational work](#foundations) and [benchmarks and evaluation](#benchmarks-evaluation).

<details>
<summary><b>🎯 Scope and curation policy</b></summary>

This index covers research where user preferences, history, profiles, feedback, personal context, or user-specific goals affect a language model’s behavior, outputs, interactions, or decisions. It includes methods, datasets, benchmarks, applications, and work on privacy, safety, bias, and user control.

The foundations section intentionally includes pre-LLM personalized-dialogue work. These papers established persona conditioning, large-scale persona data, and implicit user profiles that later LLM-personalization research builds on.

Submissions are welcome, including conference papers, workshop papers, Findings papers, datasets, benchmarks, and preprints. The active list emphasizes the latest work from 2026 onward. It also includes selected papers from 2025. New paper submissions should be from 2026 onward. Genuinely foundational pre-2025 papers and canonical benchmarks are retained at the end under Root & Classics. Authors are especially encouraged to submit their own work with a canonical source and enough context for readers to verify relevance and publication status.

See the [contribution guide](CONTRIBUTING.md) for the submission format and review checks.

</details>

## 🌱 Contribute

Have a relevant paper, benchmark, dataset, broken link, or metadata correction? All submissions are welcome—open a [pull request](CONTRIBUTING.md#pull-request-checklist) or use the [paper-suggestion form](https://github.com/jiangwu25/llm-personalization-papers/issues/new?template=paper-suggestion.yml). Every entry is checked for relevance, source quality, duplicates, accurate metadata, and neutral wording.

<a id="paper-index"></a>
## 📚 Paper Index

Each paper stays on one line: **title link** followed by a compact `venue year` label.

The active sections lead with the latest 2026+ work. Selected 2025 papers are also included. Canonical pre-2025 roots are grouped at the end.

<!-- PAPERS:START -->

<a id="foundations"></a>
### 🧱 Foundations & Canonical Benchmarks

#### 🏛️ Conference & Proceedings

- **[When Personalization Misleads: Understanding and Mitigating Hallucinations in Personalized LLMs](https://aclanthology.org/2026.findings-acl.395/)**  `Findings ACL 2026`
- **[PersonalAlign: Hierarchical Implicit Intent Alignment for Personalized GUI Agent with Long-Term User-Centric Records](https://arxiv.org/abs/2601.09636)**  `ACL 2026 Main`
- **[PrefDisco: Benchmarking Proactive Personalized Reasoning](https://proceedings.iclr.cc/paper_files/paper/2026/hash/82d50077a0e140b524a18f380c95d55a-Abstract-Conference.html)**  `ICLR 2026`
- **[Evaluating Personalized Tool-Augmented LLMs from the Perspectives of Personalization and Proactivity](https://aclanthology.org/2025.acl-long.1064/)**  `ACL 2025`
- **[PersonaBench: Evaluating AI Models on Understanding Personal Information through Accessing (Synthetic) Private User Data](https://aclanthology.org/2025.findings-acl.49/)**  `Findings ACL 2025`
- **[PersonaLens: A Benchmark for Personalization Evaluation in Conversational AI Assistants](https://aclanthology.org/2025.findings-acl.927/)**  `Findings ACL 2025`
- **[LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory](https://arxiv.org/abs/2410.10813)**  `ICLR 2025`
- **[Know Me, Respond to Me: Benchmarking LLMs for Dynamic User Profiling and Personalized Responses at Scale](https://arxiv.org/abs/2504.14225)**  `COLM 2025`
- **[Do LLMs Recognize Your Preferences? Evaluating Personalized Preference Following in LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/hash/28a46044775d97a4efcbcf14e7f13209-Abstract-Conference.html)**  `ICLR 2025`
- **[PersonalLLM: Tailoring LLMs to Individual Preferences](https://proceedings.iclr.cc/paper_files/paper/2025/hash/a730abbcd6cf4a371ca9545db5922442-Abstract-Conference.html)**  `ICLR 2025`

#### 🧪 arXiv & Preprints

- **[LUNAR: Benchmarking Personalized Large Language Models on UNiversal User BehAvioR Logs](https://arxiv.org/abs/2608.05246)**  `arXiv 2026-08`
- **[SovereignPA-Bench: Evaluating User-Owned Personal Agents under Evolving Intent, Platform Mediation, and Consent Constraints](https://arxiv.org/abs/2607.05363)**  `arXiv 2026-07`
- **[LUCid: Redefining Relevance For Lifelong Personalization](https://arxiv.org/abs/2604.26996)**  `arXiv 2026-04`
- **[AlpsBench: An LLM Personalization Benchmark for Real-Dialogue Memorization and Preference Alignment](https://arxiv.org/abs/2603.26680)**  `arXiv 2026-03`
- **[Long Context, Less Focus: A Scaling Gap in LLMs Revealed through Privacy and Personalization](https://arxiv.org/abs/2602.15028)**  `arXiv 2026-02`
- **[A Personalized Conversational Benchmark: Towards Simulating Personalized Conversations](https://arxiv.org/abs/2505.14106)**  `arXiv 2025-05`

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

<a id="agents-applications"></a>
### 🤖 Personalized Agents & Applications

- **[Language Models Don’t Know What You Want: Evaluating Personalization in Deep Research Needs Real Users](https://aclanthology.org/2026.acl-long.723/)**  `ACL 2026`
- **[Orion: Steering Personalized Web Agents via Global-Micro Profiling and Adaptive Intent Tracking](https://ojs.aaai.org/index.php/AAAI/article/view/40188)**  `AAAI 2026`

<a id="benchmarks-evaluation"></a>
### 📊 Benchmarks & Evaluation

- **[PersonaMem-v2: Towards Personalized Intelligence via Learning Implicit User Personas and Agentic Memory](https://arxiv.org/abs/2512.06688)**  `arXiv 2025-12`
- **[LaMP-QA: A Benchmark for Personalized Long-form Question Answering](https://aclanthology.org/2025.emnlp-main.60/)**  `EMNLP 2025`

<a id="privacy-safety"></a>
### 🛡️ Privacy, Safety & User Control

- **[PRISP: Privacy-Safe Few-Shot Personalization via Lightweight Adaptation](https://aclanthology.org/2026.acl-long.1146/)**  `ACL 2026`
- **[Personalized Language Models via Privacy-Preserving Evolutionary Model Merging](https://aclanthology.org/2025.emnlp-main.1747/)**  `EMNLP 2025`

<a id="root-classics"></a>
### 🌳 Root & Classics

#### 📚 Canonical Pre-2025 References

- **[LaMP: When Large Language Models Meet Personalization](https://aclanthology.org/2024.acl-long.399/)**  `ACL 2024`
- **[Evaluating Very Long-Term Conversational Memory of LLM Agents](https://aclanthology.org/2024.acl-long.747/)**  `ACL 2024`
- **[MemoryBank: Enhancing Large Language Models with Long-Term Memory](https://ojs.aaai.org/index.php/AAAI/article/view/29946)**  `AAAI 2024`
- **[Learning Implicit User Profiles for Personalized Retrieval-Based Chatbot](https://arxiv.org/abs/2108.07935)**  `CIKM 2021`
- **[One Chatbot Per Person: Creating Personalized Chatbots based on Implicit User Profiles](https://arxiv.org/abs/2108.09355)**  `SIGIR 2021`
- **[Training Millions of Personalized Dialogue Agents](https://aclanthology.org/D18-1298/)**  `EMNLP 2018`
- **[Personalizing Dialogue Agents: I have a dog, do you have pets too?](https://aclanthology.org/P18-1205/)**  `ACL 2018`

<!-- PAPERS:END -->

## 🙌 Community

Thanks to everyone who contributes paper suggestions, metadata corrections, source links, and reading-guide improvements. Inclusion means a paper matches the collection policy. It does not imply endorsement of its findings.

## 📄 License

Repository text, scripts, and templates are released under the [MIT License](LICENSE). Linked papers, code, datasets, and other external materials retain their own licenses.

<p align="center">
  <sub>Built for researchers and builders exploring human-centered language models.</sub>
</p>
