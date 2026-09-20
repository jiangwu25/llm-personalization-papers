<div align="center">

# 🧠 LLM 个性化论文精选

**一份注重来源与可验证性的精选阅读清单，关注真正适应用户的语言模型。**

用户建模 · 记忆 · 检索 · 偏好对齐 · 个性化智能体 · 评测

[![Validate index](https://github.com/jiangwu25/llm-personalization-papers/actions/workflows/validate.yml/badge.svg?branch=main)](https://github.com/jiangwu25/llm-personalization-papers/actions/workflows/validate.yml)
[![Papers](https://img.shields.io/badge/papers-32-5B8FF9?style=flat-square)](#paper-index)
[![License](https://img.shields.io/badge/license-MIT-22A06B?style=flat-square)](LICENSE)

<br>

<a href="README.md">🇺🇸 English</a> · <a href="README.zh-CN.md"><b>🇨🇳 简体中文</b></a> · <a href="README.ko.md">🇰🇷 한국어</a>

</div>

<p align="center">
  <img src="assets/personalization-banner.png" alt="个性化语言模型与用户画像、记忆和定制回复相连接的抽象插图" width="900">
</p>

<p align="center">
  <a href="#foundations">🧱 奠基工作</a> ·
  <a href="#surveys">🔭 综述</a> ·
  <a href="#memory-retrieval">🧠 记忆</a> ·
  <a href="#training-alignment">🎯 对齐</a> ·
  <a href="#agents-applications">🤖 智能体</a> ·
  <a href="#benchmarks-evaluation">📊 评测</a> ·
  <a href="#privacy-safety">🛡️ 隐私</a>
</p>

## ✨ 如何阅读

**刚接触这个领域？** 先看[阅读指南](docs/reading-guide.md)，再通过[综述论文](#surveys)建立完整的领域地图。

**准备构建系统？** 可以直接阅读[记忆与检索](#memory-retrieval)、[个性化对齐](#training-alignment)或[智能体与应用](#agents-applications)。

**想比较不同方法？** 建议从[奠基工作](#foundations)与[基准和评测](#benchmarks-evaluation)开始。

<details>
<summary><b>🎯 收录范围与筛选标准</b></summary>

本清单关注用户偏好、历史记录、画像、反馈、个人上下文或用户特定目标如何影响语言模型的行为、输出、交互或决策，涵盖方法、数据集、基准、应用，以及隐私、安全、偏差和用户控制等议题。

“奠基工作”部分特意保留了 LLM 时代之前的个性化对话研究，因为这些工作建立了人物设定、规模化 persona 数据和隐式用户画像等重要基础。

主清单中的非综述论文必须正式发表于指定顶级会议的主会：**ACL、EMNLP、NAACL、AAAI、SIGIR 或 CIKM**。综述论文是通常例外。PersonaMem-v2 作为唯一明确批准的 benchmark 预印本，通过[例外台账](docs/inclusion-exceptions.json)记录；这不代表其他 arXiv 论文都可以加入。CARD 和 PsPLUG 的 `EMNLP 2026` 来自作者确认，具体记录见[来源台账](docs/paper-provenance.json)；没有推测 track 或 proceedings 链接。

Workshop、Findings、Industry Track、LREC 和其他仅有预印本的方法论文仍不纳入主清单。通用 RAG、通用智能体、角色扮演和传统推荐论文，若未明确研究用户特定适配，也不在收录范围内。

完整规则请参阅[贡献指南](CONTRIBUTING.md)。

</details>

## 🌱 参与贡献

发现遗漏论文、失效链接或错误会议信息？欢迎提交一个聚焦的 [Pull Request](CONTRIBUTING.md#pull-request-checklist)，也可以使用[论文推荐表单](https://github.com/jiangwu25/llm-personalization-papers/issues/new?template=paper-suggestion.yml)。论文作者也可以推荐自己的工作；每个条目都会核查相关性、来源质量、重复项、会议和表述中立性。

<a id="paper-index"></a>
## 📚 论文列表

每篇论文只占一行：**标题链接**，末尾附简洁的`会议 年份`标签。

<!-- PAPERS:START -->

<a id="foundations"></a>
### 🧱 奠基工作与经典基准

- **[Learning Implicit User Profiles for Personalized Retrieval-Based Chatbot](https://arxiv.org/abs/2108.07935)**  `CIKM 2021`
- **[One Chatbot Per Person: Creating Personalized Chatbots based on Implicit User Profiles](https://arxiv.org/abs/2108.09355)**  `SIGIR 2021`
- **[Training Millions of Personalized Dialogue Agents](https://aclanthology.org/D18-1298/)**  `EMNLP 2018`
- **[Personalizing Dialogue Agents: I have a dog, do you have pets too?](https://aclanthology.org/P18-1205/)**  `ACL 2018`

<a id="surveys"></a>
### 🔭 综述与观点

- **[A Survey on Personalized and Pluralistic Preference Alignment in Large Language Models](https://arxiv.org/abs/2504.07070)**  `Survey · 2025-04`
- **[A Survey of Personalized Large Language Models: Progress and Future Directions](https://arxiv.org/abs/2502.11528)**  `Survey · 2025-02`
- **[Personalization of Large Language Models: A Survey](https://arxiv.org/abs/2411.00027)**  `Survey · 2024-10`
- **[Two Tales of Persona in LLMs: A Survey of Role-Playing and Personalization](https://aclanthology.org/2024.findings-emnlp.969/)**  `Survey · Findings EMNLP 2024`

<a id="user-modeling"></a>
### 👤 用户建模与偏好获取

- **[Decisive: Guiding User Decisions with Optimal Preference Elicitation from Unstructured Documents](https://aclanthology.org/2026.acl-long.1465/)**  `ACL 2026`
- **[Optimizing User Profiles via Contextual Bandits for Retrieval-Augmented LLM Personalization](https://aclanthology.org/2026.acl-long.1467/)**  `ACL 2026`
- **[Value Profiles for Encoding Human Variation](https://aclanthology.org/2025.emnlp-main.106/)**  `EMNLP 2025`

<a id="memory-retrieval"></a>
### 🧠 记忆与检索

- **[In Prospect and Retrospect: Reflective Memory Management for Long-term Personalized Dialogue Agents](https://aclanthology.org/2025.acl-long.413/)**  `ACL 2025`
- **[PRIME: Large Language Model Personalization with Cognitive Dual-Memory and Personalized Thought Process](https://aclanthology.org/2025.emnlp-main.1711/)**  `EMNLP 2025`
- **[Optimization Methods for Personalizing Large Language Models through Retrieval Augmentation](https://arxiv.org/abs/2404.05970)**  `SIGIR 2024`
- **[MemoryBank: Enhancing Large Language Models with Long-Term Memory](https://ojs.aaai.org/index.php/AAAI/article/view/29946)**  `AAAI 2024`

<a id="inference-time"></a>
### 🎛️ 提示、引导与解码

- **[Do Implicit Personalization and Explicit Styles Conflict? PsPLUG: A Lightweight Plug-in for Balancing Personalization and Style in Customized LLMs](https://arxiv.org/abs/2601.06362)**  `EMNLP 2026`
- **[Personalized Text Generation with Contrastive Activation Steering](https://aclanthology.org/2025.acl-long.353/)**  `ACL 2025`
- **[Personalized LLM Decoding via Contrasting Personal Preference](https://aclanthology.org/2025.emnlp-main.1723/)**  `EMNLP 2025`

<a id="training-alignment"></a>
### 🎯 微调与个性化对齐

- **[CARD: Cluster-level Adaptation with Reward-guided Decoding for Personalized Text Generation](https://arxiv.org/abs/2601.06352)**  `EMNLP 2026`
- **[FaST: Feature-aware Sampling and Tuning for Personalized Preference Alignment with Limited Data](https://aclanthology.org/2025.emnlp-main.475/)**  `EMNLP 2025`
- **[MiCRo: Mixture Modeling and Context-aware Routing for Personalized Preference Learning](https://aclanthology.org/2025.emnlp-main.882/)**  `EMNLP 2025`
- **[Personalized Pieces: Efficient Personalized Large Language Models through Collaborative Efforts](https://aclanthology.org/2024.emnlp-main.371/)**  `EMNLP 2024`
- **[Democratizing Large Language Models via Personalized Parameter-Efficient Fine-tuning](https://aclanthology.org/2024.emnlp-main.372/)**  `EMNLP 2024`

<a id="agents-applications"></a>
### 🤖 个性化智能体与应用

- **[Language Models Don’t Know What You Want: Evaluating Personalization in Deep Research Needs Real Users](https://aclanthology.org/2026.acl-long.723/)**  `ACL 2026`
- **[Orion: Steering Personalized Web Agents via Global-Micro Profiling and Adaptive Intent Tracking](https://ojs.aaai.org/index.php/AAAI/article/view/40188)**  `AAAI 2026`
- **[Crafting Personalized Agents through Retrieval-Augmented Generation on Editable Memory Graphs](https://aclanthology.org/2024.emnlp-main.281/)**  `EMNLP 2024`

<a id="benchmarks-evaluation"></a>
### 📊 基准与评测

- **[PersonaMem-v2: Towards Personalized Intelligence via Learning Implicit User Personas and Agentic Memory](https://arxiv.org/abs/2512.06688)**  `arXiv 2025-12`
- **[LaMP-QA: A Benchmark for Personalized Long-form Question Answering](https://aclanthology.org/2025.emnlp-main.60/)**  `EMNLP 2025`
- **[LaMP: When Large Language Models Meet Personalization](https://aclanthology.org/2024.acl-long.399/)**  `ACL 2024`
- **[Evaluating Very Long-Term Conversational Memory of LLM Agents](https://aclanthology.org/2024.acl-long.747/)**  `ACL 2024`

<a id="privacy-safety"></a>
### 🛡️ 隐私、安全与用户控制

- **[PRISP: Privacy-Safe Few-Shot Personalization via Lightweight Adaptation](https://aclanthology.org/2026.acl-long.1146/)**  `ACL 2026`
- **[Personalized Language Models via Privacy-Preserving Evolutionary Model Merging](https://aclanthology.org/2025.emnlp-main.1747/)**  `EMNLP 2025`

<!-- PAPERS:END -->

## 🙌 社区

感谢所有贡献论文推荐、元数据修正、来源链接和阅读指南改进的朋友。论文被收录只代表它符合本项目的筛选标准，并不表示对其研究结论的背书。

## 📄 许可证

仓库中的原创文字、脚本和模板采用 [MIT License](LICENSE)。外部论文、代码和数据集仍遵循各自的许可证。

<p align="center">
  <sub>为探索以人为中心的语言模型研究者与开发者而建。</sub>
</p>
