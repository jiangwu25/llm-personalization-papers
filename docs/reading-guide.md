# Reading Guide

This is a focused route through the index, not a ranking of paper quality. The active index emphasizes the latest 2026+ work. Selected 2025 papers are also included. Genuinely foundational pre-2025 references are grouped at the end under Root & Classics, while surveys remain available as orientation. Source and venue details are recorded according to the policy in [CONTRIBUTING.md](../CONTRIBUTING.md).

## 🗺️ A compact route

| Stage | Question | Start with |
| --- | --- | --- |
| 1. Foundations | What does it mean for a dialogue system to model a person? | [Personalizing Dialogue Agents](https://aclanthology.org/P18-1205/) |
| 2. Implicit profiles | Can history reveal a user’s style and preferences? | [Learning Implicit User Profiles](https://arxiv.org/abs/2108.07935) |
| 3. LLM benchmark | How do we measure personalization across tasks and users? | [LaMP](https://aclanthology.org/2024.acl-long.399/) |
| 4. Memory | What should be stored, retrieved, updated, or forgotten? | [MemoryBank](https://ojs.aaai.org/index.php/AAAI/article/view/29946) |
| 5. Alignment | How can a model learn an individual’s preferences efficiently? | [FaST](https://aclanthology.org/2025.emnlp-main.475/) |
| 6. Agents | How does a user model change planning and tool use? | [Language Models Don’t Know What You Want](https://aclanthology.org/2026.acl-long.723/) |
| 7. Control and safety | How do style, privacy, and user control constrain personalization? | [PsPLUG](https://arxiv.org/abs/2601.06362) |

## 1. 🧱 Start with the historical roots

- **[Personalizing Dialogue Agents: I have a dog, do you have pets too?](https://aclanthology.org/P18-1205/)** — Index ID `doi:10.18653/v1/P18-1205`. Read this for persona-conditioned dialogue and the original Persona-Chat framing. Ask: what information is given explicitly, and what must the agent learn from interaction?

- **[Training Millions of Personalized Dialogue Agents](https://aclanthology.org/D18-1298/)** — Index ID `doi:10.18653/v1/D18-1298`. Read this for the scale question: does persona conditioning still help when the number of personas and conversations grows dramatically?

- **[Learning Implicit User Profiles for Personalized Retrieval-Based Chatbot](https://arxiv.org/abs/2108.07935)** — Index ID `arxiv:2108.07935`. Compare explicit profile text with implicit style and preference signals extracted from history.

- **[One Chatbot Per Person: Creating Personalized Chatbots based on Implicit User Profiles](https://arxiv.org/abs/2108.09355)** — Index ID `arxiv:2108.09355`. Focus on the separation between a general user profile, a query-dependent profile, and a personalized decoder.

## 2.5 👤 Model users and elicit preferences

- **[Decisive: Guiding User Decisions with Optimal Preference Elicitation from Unstructured Documents](https://aclanthology.org/2026.acl-long.1465/)** — Compare passive profile inference with actively eliciting preferences from unstructured documents. Keep the decision-support setting separate from general conversational personalization.

- **[Value Profiles for Encoding Human Variation](https://aclanthology.org/2025.emnlp-main.106/)** — Study interpretable value representations and ask how well individual rating behavior transfers to open-ended assistant preferences.

## 2. 📏 Learn the LLM-era benchmark

- **[Personalization of Large Language Models: A Survey](https://arxiv.org/abs/2411.00027)** — Index ID `arxiv:2411.00027`. Start here for the vocabulary: who is personalized, what is personalized, and where personalization enters the system.

- **[Two Tales of Persona in LLMs: A Survey of Role-Playing and Personalization](https://aclanthology.org/2024.findings-emnlp.969/)** — Use this to separate role-playing from user-centered personalization. It is retained as a survey despite its Findings venue.

- **[LaMP: When Large Language Models Meet Personalization](https://aclanthology.org/2024.acl-long.399/)** — Index ID `arxiv:2304.11406`. It provides seven personalized tasks across classification and generation, plus retrieval-augmentation baselines. Keep separate a general task score from a score that depends on a particular user’s history.

- **[LaMP-QA: A Benchmark for Personalized Long-form Question Answering](https://aclanthology.org/2025.emnlp-main.60/)** — Use this as a contrast to task-level LaMP: long-form answers create different attribution and user-history evaluation questions.

- **[PersonaMem-v2: Towards Personalized Intelligence via Learning Implicit User Personas and Agentic Memory](https://arxiv.org/abs/2512.06688)** — A named benchmark-preprint exception. Read the [code](https://github.com/bowen-upenn/PersonaMem-v2) and [dataset card](https://huggingface.co/datasets/bowen-upenn/PersonaMem-v2), but do not describe its simulated conversations as real user logs or imply that the code has been reproduced here.

## 3. 🧠 Study memory and retrieval

- **[MemoryBank: Enhancing Large Language Models with Long-Term Memory](https://ojs.aaai.org/index.php/AAAI/article/view/29946)** — Index ID `doi:10.1609/aaai.v38i17.29946`. Study its memory storage, retrieval, and forgetting-inspired update mechanism for sustained user interaction.

- **[PRIME: Large Language Model Personalization with Cognitive Dual-Memory and Personalized Thought Process](https://aclanthology.org/2025.emnlp-main.1711/)** — Index ID `url:https://aclanthology.org/2025.emnlp-main.1711/`. Compare episodic interaction memory with semantic user beliefs, and ask what each memory type contributes.

- **[In Prospect and Retrospect: Reflective Memory Management for Long-term Personalized Dialogue Agents](https://aclanthology.org/2025.acl-long.413/)** — Compare reflective memory construction with retrieval alone. The agent framing does not change its primary memory contribution.

## 4. 🎛️ Study fine-tuning and alignment

- **[FaST: Feature-aware Sampling and Tuning for Personalized Preference Alignment with Limited Data](https://aclanthology.org/2025.emnlp-main.475/)** — Index ID `url:https://aclanthology.org/2025.emnlp-main.475/`. Focus on the limited-data setting and the way feature-aware sampling changes personalized preference alignment.

- **[CARD: Cluster-level Adaptation with Reward-guided Decoding for Personalized Text Generation](https://arxiv.org/abs/2601.06352)** — Pair group-level LoRA sharing with user-specific preference learning. Read it alongside OPPU to compare shared adaptation, per-user adaptation, and inference-time correction. Do not call it training-free.

- **[MiCRo: Mixture Modeling and Context-aware Routing for Personalized Preference Learning](https://aclanthology.org/2025.emnlp-main.882/)** — Separate mixture-based preference modeling and context routing from claims about recovering every individual value.

## 5. 🤖 Finish with personalized agents

- **[Language Models Don’t Know What You Want: Evaluating Personalization in Deep Research Needs Real Users](https://aclanthology.org/2026.acl-long.723/)** — Index ID `url:https://aclanthology.org/2026.acl-long.723/`. Examine why real-user profiles and approval-aware planning matter in personalized deep research.

- **[Orion: Steering Personalized Web Agents via Global-Micro Profiling and Adaptive Intent Tracking](https://ojs.aaai.org/index.php/AAAI/article/view/40188)** — Use this as an action-oriented contrast: personalized planning and intent tracking matter when the system changes the web actions it takes, not only the text it writes.

## 6. 🎛️ Compare prompting, steering, and decoding

- **[Personalized Text Generation with Contrastive Activation Steering](https://aclanthology.org/2025.acl-long.353/)** — Compare activation-level control with prompt and retrieval-based personalization. Do not treat style control as a complete user model.

- **[PsPLUG: A Lightweight Plug-in for Balancing Personalization and Style in Customized LLMs](https://arxiv.org/abs/2601.06362)** — Study the conflict between explicit style instructions and implicit preferences, plus inference-time control of personalization strength. The plug-in is learned, so it is not fully training-free.

## 7. 🛡️ Read privacy and user-control boundaries

- **[PRISP: Privacy-Safe Few-Shot Personalization via Lightweight Adaptation](https://aclanthology.org/2026.acl-long.1146/)** — Treat “privacy-safe” as the paper’s stated scope, not as a universal zero-leakage guarantee across threat models.

- **[Personalized Language Models via Privacy-Preserving Evolutionary Model Merging](https://aclanthology.org/2025.emnlp-main.1747/)** — Compare privacy–utility trade-offs in model merging. Do not confuse PriME with the existing PRIME dual-memory paper.

- **[Evaluating Very Long-Term Conversational Memory of LLM Agents](https://aclanthology.org/2024.acl-long.747/)** — Use as a memory-capability boundary case. Generated and human-checked conversations are not the same as real long-term user logs.
