# Reading Guide

This is a focused route through the index, not a ranking of paper quality. Surveys are included as orientation; the remaining entries are restricted to the selected top/main conference venues listed in [CONTRIBUTING.md](../CONTRIBUTING.md#venue-filter).

## 🗺️ A compact route

| Stage | Question | Start with |
| --- | --- | --- |
| 1. Foundations | What does it mean for a dialogue system to model a person? | [Personalizing Dialogue Agents](https://aclanthology.org/P18-1205/) |
| 2. Implicit profiles | Can history reveal a user’s style and preferences? | [Learning Implicit User Profiles](https://arxiv.org/abs/2108.07935) |
| 3. LLM benchmark | How do we measure personalization across tasks and users? | [LaMP](https://aclanthology.org/2024.acl-long.399/) |
| 4. Memory | What should be stored, retrieved, updated, or forgotten? | [MemoryBank](https://ojs.aaai.org/index.php/AAAI/article/view/29946) |
| 5. Alignment | How can a model learn an individual’s preferences efficiently? | [Personalized Pieces](https://aclanthology.org/2024.emnlp-main.371/) |
| 6. Agents | How does a user model change planning and tool use? | [Language Models Don’t Know What You Want](https://aclanthology.org/2026.acl-long.723/) |

## 1. 🧱 Start with the historical roots

- **[Personalizing Dialogue Agents: I have a dog, do you have pets too?](https://aclanthology.org/P18-1205/)** — Index ID `doi:10.18653/v1/P18-1205`. Read this for persona-conditioned dialogue and the original Persona-Chat framing. Ask: what information is given explicitly, and what must the agent learn from interaction?

- **[Training Millions of Personalized Dialogue Agents](https://aclanthology.org/D18-1298/)** — Index ID `doi:10.18653/v1/D18-1298`. Read this for the scale question: does persona conditioning still help when the number of personas and conversations grows dramatically?

- **[Learning Implicit User Profiles for Personalized Retrieval-Based Chatbot](https://arxiv.org/abs/2108.07935)** — Index ID `arxiv:2108.07935`. Compare explicit profile text with implicit style and preference signals extracted from history.

- **[One Chatbot Per Person: Creating Personalized Chatbots based on Implicit User Profiles](https://arxiv.org/abs/2108.09355)** — Index ID `arxiv:2108.09355`. Focus on the separation between a general user profile, a query-dependent profile, and a personalized decoder.

## 2. 📏 Learn the LLM-era benchmark

- **[Personalization of Large Language Models: A Survey](https://arxiv.org/abs/2411.00027)** — Index ID `arxiv:2411.00027`. Start here for the vocabulary: who is personalized, what is personalized, and where personalization enters the system.

- **[LaMP: When Large Language Models Meet Personalization](https://aclanthology.org/2024.acl-long.399/)** — Index ID `arxiv:2304.11406`. It provides seven personalized tasks across classification and generation, plus retrieval-augmentation baselines. Keep separate a general task score from a score that depends on a particular user’s history.

## 3. 🧠 Study memory and retrieval

- **[MemoryBank: Enhancing Large Language Models with Long-Term Memory](https://ojs.aaai.org/index.php/AAAI/article/view/29946)** — Index ID `doi:10.1609/aaai.v38i17.29946`. Study its memory storage, retrieval, and forgetting-inspired update mechanism for sustained user interaction.

- **[PRIME: Large Language Model Personalization with Cognitive Dual-Memory and Personalized Thought Process](https://aclanthology.org/2025.emnlp-main.1711/)** — Index ID `url:https://aclanthology.org/2025.emnlp-main.1711/`. Compare episodic interaction memory with semantic user beliefs, and ask what each memory type contributes.

## 4. 🎛️ Study fine-tuning and alignment

- **[FaST: Feature-aware Sampling and Tuning for Personalized Preference Alignment with Limited Data](https://aclanthology.org/2025.emnlp-main.475/)** — Index ID `url:https://aclanthology.org/2025.emnlp-main.475/`. Focus on the limited-data setting and the way feature-aware sampling changes personalized preference alignment.

- **[Personalized Pieces: Efficient Personalized Large Language Models through Collaborative Efforts](https://aclanthology.org/2024.emnlp-main.371/)** — Index ID `url:https://aclanthology.org/2024.emnlp-main.371/`. Focus on the systems trade-off between sharing reusable PEFT pieces and preserving user-specific behavior.

- **[Democratizing Large Language Models via Personalized Parameter-Efficient Fine-tuning](https://aclanthology.org/2024.emnlp-main.372/)** — Index ID `url:https://aclanthology.org/2024.emnlp-main.372/`. Compare per-user PEFT ownership with retrieval and profile-based personalization.

## 5. 🤖 Finish with personalized agents

- **[Language Models Don’t Know What You Want: Evaluating Personalization in Deep Research Needs Real Users](https://aclanthology.org/2026.acl-long.723/)** — Index ID `url:https://aclanthology.org/2026.acl-long.723/`. Examine why real-user profiles and approval-aware planning matter in personalized deep research.

- **[Crafting Personalized Agents through Retrieval-Augmented Generation on Editable Memory Graphs](https://aclanthology.org/2024.emnlp-main.281/)** — Index ID `url:https://aclanthology.org/2024.emnlp-main.281/`. Study how editable memory graphs connect user history to an assistant application.
