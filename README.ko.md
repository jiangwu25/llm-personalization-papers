<div align="center">

# 🧠 Awesome LLM 개인화 논문 모음

**사람에게 맞춰지는 언어 모델을 위한, 근거 중심의 엄선된 읽기 목록입니다.**

사용자 모델링 · 메모리 · 검색 · 선호 정렬 · 개인화 에이전트 · 평가

[![Validate index](https://github.com/jiangwu25/llm-personalization-papers/actions/workflows/validate.yml/badge.svg?branch=main)](https://github.com/jiangwu25/llm-personalization-papers/actions/workflows/validate.yml)
[![Papers](https://img.shields.io/badge/papers-50-5B8FF9?style=flat-square)](#paper-index)
[![License](https://img.shields.io/badge/license-MIT-22A06B?style=flat-square)](LICENSE)

<br>

<a href="README.md">🇺🇸 English</a> · <a href="README.zh-CN.md">🇨🇳 简体中文</a> · <a href="README.ko.md"><b>🇰🇷 한국어</b></a>

</div>

<p align="center">
  <img src="assets/personalization-banner.png" alt="사용자 프로필, 메모리, 맞춤형 응답에 연결된 개인화 언어 모델의 추상 일러스트" width="900">
</p>

<p align="center">
  <a href="#foundations">🧱 기반 연구</a> ·
  <a href="#surveys">🔭 서베이</a> ·
  <a href="#memory-retrieval">🧠 메모리</a> ·
  <a href="#training-alignment">🎯 정렬</a> ·
  <a href="#agents-applications">🤖 에이전트</a> ·
  <a href="#benchmarks-evaluation">📊 평가</a> ·
  <a href="#privacy-safety">🛡️ 프라이버시</a>
</p>

## ✨ 컬렉션 둘러보기

**처음 시작하시나요?** [읽기 가이드](docs/reading-guide.md)를 따라간 뒤 [서베이](#surveys)로 전체 연구 지형을 살펴보세요.

**시스템을 만들고 있나요?** [메모리와 검색](#memory-retrieval), [개인화 정렬](#training-alignment), [에이전트와 응용](#agents-applications)으로 바로 이동해 보세요.

**방법론을 비교하고 싶나요?** [기반 연구](#foundations)와 [벤치마크 및 평가](#benchmarks-evaluation)부터 시작하는 것을 권합니다.

<details>
<summary><b>🎯 범위와 선정 기준</b></summary>

이 목록은 사용자의 선호, 기록, 프로필, 피드백, 개인적 맥락 또는 사용자별 목표가 언어 모델의 행동, 출력, 상호작용이나 의사결정에 영향을 주는 연구를 다룹니다. 방법론, 데이터셋, 벤치마크, 응용뿐 아니라 개인정보 보호, 안전, 편향, 사용자 제어에 관한 연구도 포함합니다.

기반 연구 섹션에는 LLM 이전의 개인화 대화 연구도 의도적으로 포함했습니다. 이 연구들은 이후 LLM 개인화가 이어받은 페르소나 조건화, 대규모 페르소나 데이터, 암묵적 사용자 프로필의 토대를 마련했습니다.

학회 논문, 워크숍, Findings, 데이터셋, 벤치마크, arXiv 프리프린트를 포함해 출판 단계와 관계없이 관련 연구의 제안을 환영합니다. 저자 본인의 연구도 적극 환영하며, 관련성과 발표 상태를 확인할 수 있는 정식 출처와 충분한 맥락을 함께 제공해 주세요.

제출 형식과 검토 기준은 [기여 가이드](CONTRIBUTING.md)를 확인해 주세요.

</details>

## 🌱 기여하기

관련 논문, 벤치마크, 데이터셋, 끊어진 링크 또는 메타데이터 수정 사항이 있나요? 모든 관련 제안을 환영합니다. [Pull Request](CONTRIBUTING.md#pull-request-checklist)를 열거나 [논문 제안 양식](https://github.com/jiangwu25/llm-personalization-papers/issues/new?template=paper-suggestion.yml)을 사용해 주세요. 모든 항목은 관련성, 출처 품질, 중복, 정확한 메타데이터, 중립적 표현을 확인합니다.

<a id="paper-index"></a>
## 📚 논문 목록

각 논문은 한 줄로 표시됩니다. **제목 링크** 뒤에 간결한 `학회 연도` 라벨이 붙습니다.

첫 번째 분류는 역사적 기반 연구, 정식 학회 발표 논문, arXiv/프리프린트 벤치마크의 세 층으로 구성됩니다.

<!-- PAPERS:START -->

<a id="foundations"></a>
### 🧱 기반 연구와 대표 벤치마크

#### 📚 역사적 기반

- **[Learning Implicit User Profiles for Personalized Retrieval-Based Chatbot](https://arxiv.org/abs/2108.07935)**  `CIKM 2021`
- **[One Chatbot Per Person: Creating Personalized Chatbots based on Implicit User Profiles](https://arxiv.org/abs/2108.09355)**  `SIGIR 2021`
- **[Training Millions of Personalized Dialogue Agents](https://aclanthology.org/D18-1298/)**  `EMNLP 2018`
- **[Personalizing Dialogue Agents: I have a dog, do you have pets too?](https://aclanthology.org/P18-1205/)**  `ACL 2018`

#### 🏛️ 학회 및 정식 발표

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
- **[PerLTQA: A Personal Long-Term Memory Dataset for Memory Classification, Retrieval, and Fusion in Question Answering](https://aclanthology.org/2024.sighan-1.18/)**  `SIGHAN Workshop 2024`

#### 🧪 arXiv 및 프리프린트

- **[LUNAR: Benchmarking Personalized Large Language Models on UNiversal User BehAvioR Logs](https://arxiv.org/abs/2608.05246)**  `arXiv 2026-08`
- **[SovereignPA-Bench: Evaluating User-Owned Personal Agents under Evolving Intent, Platform Mediation, and Consent Constraints](https://arxiv.org/abs/2607.05363)**  `arXiv 2026-07`
- **[LUCid: Redefining Relevance For Lifelong Personalization](https://arxiv.org/abs/2604.26996)**  `arXiv 2026-04`
- **[AlpsBench: An LLM Personalization Benchmark for Real-Dialogue Memorization and Preference Alignment](https://arxiv.org/abs/2603.26680)**  `arXiv 2026-03`
- **[Long Context, Less Focus: A Scaling Gap in LLMs Revealed through Privacy and Personalization](https://arxiv.org/abs/2602.15028)**  `arXiv 2026-02`
- **[A Personalized Conversational Benchmark: Towards Simulating Personalized Conversations](https://arxiv.org/abs/2505.14106)**  `arXiv 2025-05`
- **[LongLaMP: A Benchmark for Personalized Long-form Text Generation](https://arxiv.org/abs/2407.11016)**  `arXiv 2024-07`

<a id="surveys"></a>
### 🔭 서베이와 관점

- **[A Survey on Personalized and Pluralistic Preference Alignment in Large Language Models](https://arxiv.org/abs/2504.07070)**  `Survey · 2025-04`
- **[A Survey of Personalized Large Language Models: Progress and Future Directions](https://arxiv.org/abs/2502.11528)**  `Survey · 2025-02`
- **[Personalization of Large Language Models: A Survey](https://arxiv.org/abs/2411.00027)**  `Survey · 2024-10`
- **[Two Tales of Persona in LLMs: A Survey of Role-Playing and Personalization](https://aclanthology.org/2024.findings-emnlp.969/)**  `Survey · Findings EMNLP 2024`

<a id="user-modeling"></a>
### 👤 사용자 모델링과 선호 파악

- **[Decisive: Guiding User Decisions with Optimal Preference Elicitation from Unstructured Documents](https://aclanthology.org/2026.acl-long.1465/)**  `ACL 2026`
- **[Optimizing User Profiles via Contextual Bandits for Retrieval-Augmented LLM Personalization](https://aclanthology.org/2026.acl-long.1467/)**  `ACL 2026`
- **[Value Profiles for Encoding Human Variation](https://aclanthology.org/2025.emnlp-main.106/)**  `EMNLP 2025`

<a id="memory-retrieval"></a>
### 🧠 메모리와 검색

- **[In Prospect and Retrospect: Reflective Memory Management for Long-term Personalized Dialogue Agents](https://aclanthology.org/2025.acl-long.413/)**  `ACL 2025`
- **[PRIME: Large Language Model Personalization with Cognitive Dual-Memory and Personalized Thought Process](https://aclanthology.org/2025.emnlp-main.1711/)**  `EMNLP 2025`
- **[Optimization Methods for Personalizing Large Language Models through Retrieval Augmentation](https://arxiv.org/abs/2404.05970)**  `SIGIR 2024`
- **[MemoryBank: Enhancing Large Language Models with Long-Term Memory](https://ojs.aaai.org/index.php/AAAI/article/view/29946)**  `AAAI 2024`

<a id="inference-time"></a>
### 🎛️ 프롬프팅, 조향과 디코딩

- **[Do Implicit Personalization and Explicit Styles Conflict? PsPLUG: A Lightweight Plug-in for Balancing Personalization and Style in Customized LLMs](https://arxiv.org/abs/2601.06362)**  `EMNLP 2026`
- **[Personalized Text Generation with Contrastive Activation Steering](https://aclanthology.org/2025.acl-long.353/)**  `ACL 2025`
- **[Personalized LLM Decoding via Contrasting Personal Preference](https://aclanthology.org/2025.emnlp-main.1723/)**  `EMNLP 2025`

<a id="training-alignment"></a>
### 🎯 파인튜닝과 개인화 정렬

- **[CARD: Cluster-level Adaptation with Reward-guided Decoding for Personalized Text Generation](https://arxiv.org/abs/2601.06352)**  `EMNLP 2026`
- **[FaST: Feature-aware Sampling and Tuning for Personalized Preference Alignment with Limited Data](https://aclanthology.org/2025.emnlp-main.475/)**  `EMNLP 2025`
- **[MiCRo: Mixture Modeling and Context-aware Routing for Personalized Preference Learning](https://aclanthology.org/2025.emnlp-main.882/)**  `EMNLP 2025`
- **[Personalized Pieces: Efficient Personalized Large Language Models through Collaborative Efforts](https://aclanthology.org/2024.emnlp-main.371/)**  `EMNLP 2024`
- **[Democratizing Large Language Models via Personalized Parameter-Efficient Fine-tuning](https://aclanthology.org/2024.emnlp-main.372/)**  `EMNLP 2024`

<a id="agents-applications"></a>
### 🤖 개인화 에이전트와 응용

- **[Language Models Don’t Know What You Want: Evaluating Personalization in Deep Research Needs Real Users](https://aclanthology.org/2026.acl-long.723/)**  `ACL 2026`
- **[Orion: Steering Personalized Web Agents via Global-Micro Profiling and Adaptive Intent Tracking](https://ojs.aaai.org/index.php/AAAI/article/view/40188)**  `AAAI 2026`
- **[Crafting Personalized Agents through Retrieval-Augmented Generation on Editable Memory Graphs](https://aclanthology.org/2024.emnlp-main.281/)**  `EMNLP 2024`

<a id="benchmarks-evaluation"></a>
### 📊 벤치마크와 평가

- **[PersonaMem-v2: Towards Personalized Intelligence via Learning Implicit User Personas and Agentic Memory](https://arxiv.org/abs/2512.06688)**  `arXiv 2025-12`
- **[LaMP-QA: A Benchmark for Personalized Long-form Question Answering](https://aclanthology.org/2025.emnlp-main.60/)**  `EMNLP 2025`
- **[LaMP: When Large Language Models Meet Personalization](https://aclanthology.org/2024.acl-long.399/)**  `ACL 2024`
- **[Evaluating Very Long-Term Conversational Memory of LLM Agents](https://aclanthology.org/2024.acl-long.747/)**  `ACL 2024`

<a id="privacy-safety"></a>
### 🛡️ 프라이버시, 안전과 사용자 제어

- **[PRISP: Privacy-Safe Few-Shot Personalization via Lightweight Adaptation](https://aclanthology.org/2026.acl-long.1146/)**  `ACL 2026`
- **[Personalized Language Models via Privacy-Preserving Evolutionary Model Merging](https://aclanthology.org/2025.emnlp-main.1747/)**  `EMNLP 2025`

<!-- PAPERS:END -->

## 🙌 커뮤니티

논문 제안, 메타데이터 수정, 출처 링크, 읽기 가이드 개선에 기여해 주신 모든 분께 감사드립니다. 목록 등재는 선정 기준을 충족한다는 뜻이며, 논문의 결론을 지지한다는 의미는 아닙니다.

## 📄 라이선스

저장소의 글, 스크립트와 템플릿은 [MIT License](LICENSE)로 배포됩니다. 링크된 논문, 코드, 데이터셋 등 외부 자료에는 각각의 라이선스가 적용됩니다.

<p align="center">
  <sub>사람 중심의 언어 모델을 탐구하는 연구자와 개발자를 위해 만들었습니다.</sub>
</p>
