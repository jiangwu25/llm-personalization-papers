# Reading Guide

This is a route through the index, not a ranking of paper quality. The order is intentional: first learn where personalization came from, then study how modern systems represent, retrieve, train, and evaluate user-specific information.

> [!IMPORTANT]
> “Canonical” means historically influential or structurally foundational. It does not mean that a paper is the newest, best-performing, or universally accepted.

## A compact route

| Stage | Question | Start with |
| --- | --- | --- |
| 1. Foundations | What does it mean for a dialogue system to model a person? | [Personalizing Dialogue Agents](https://aclanthology.org/P18-1205/) |
| 2. Implicit profiles | Can history reveal a user’s style and preferences without a hand-written profile? | [Learning Implicit User Profiles](https://arxiv.org/abs/2108.07935) |
| 3. LLM benchmark | How do we measure personalization across tasks and users? | [LaMP](https://aclanthology.org/2024.acl-long.399/) |
| 4. Memory | What should be stored, retrieved, updated, or forgotten? | [MemoryBank](https://arxiv.org/abs/2305.10250) |
| 5. Alignment | How can a model learn an individual’s preferences from limited feedback? | [Personalized Language Modeling from Personalized Human Feedback](https://arxiv.org/abs/2402.05133) |
| 6. User control | When should a remembered preference *not* be applied? | [BenchPreS](https://arxiv.org/abs/2603.16557) |

## 1. Start with the historical roots

- **[Personalizing Dialogue Agents: I have a dog, do you have pets too?](https://aclanthology.org/P18-1205/)** — Index ID `doi:10.18653/v1/P18-1205`. Read this for persona-conditioned dialogue and the original Persona-Chat framing. Ask: what information is given explicitly, and what must the agent learn from interaction?

- **[Training Millions of Personalized Dialogue Agents](https://aclanthology.org/D18-1298/)** — Index ID `doi:10.18653/v1/D18-1298`. Read this for the scale question: does persona conditioning still help when the number of personas and conversations grows dramatically?

- **[Learning Implicit User Profiles for Personalized Retrieval-Based Chatbot](https://arxiv.org/abs/2108.07935)** — Index ID `arxiv:2108.07935`. Compare explicit profile text with implicit style and preference signals extracted from history.

- **[One Chatbot Per Person: Creating Personalized Chatbots based on Implicit User Profiles](https://arxiv.org/abs/2108.09355)** — Index ID `arxiv:2108.09355`. Focus on the separation between a general user profile, a query-dependent profile, and a personalized decoder.

## 2. Learn the LLM-era benchmark

- **[LaMP: When Large Language Models Meet Personalization](https://aclanthology.org/2024.acl-long.399/)** — Index ID `arxiv:2304.11406`. It provides seven personalized tasks across classification and generation, plus retrieval-augmentation baselines. Keep separate the score on a general task and the score that depends on a particular user’s history.

- **[Benchmarking and Improving LLM Robustness for Personalized Generation](https://aclanthology.org/2025.findings-emnlp.870/)** — Index ID `url:https://aclanthology.org/2025.findings-emnlp.870/`. Read this to see why preference following is not enough when personalization damages factuality or reliability.

## 3. Study memory and retrieval

- **[MemoryBank: Enhancing Large Language Models with Long-Term Memory](https://arxiv.org/abs/2305.10250)** — Index ID `arxiv:2305.10250`. This is an early LLM-era example of persistent memory, retrieval, and selective updating for sustained interaction.

- **[Personalized Large Language Model Assistant with Evolving Conditional Memory](https://aclanthology.org/2025.coling-main.254/)** — Index ID `url:https://aclanthology.org/2025.coling-main.254/`. Compare its memory construction and retrieval process with MemoryBank, especially how the evaluation tests learning from dialogue and feedback.

## 4. Study training and alignment

- **[Personalized Language Modeling from Personalized Human Feedback](https://arxiv.org/abs/2402.05133)** — Index ID `arxiv:2402.05133`. Use it to distinguish a global reward model from a lightweight user model that captures individual feedback.

- **[Personalized Pieces: Efficient Personalized Large Language Models through Collaborative Efforts](https://aclanthology.org/2024.emnlp-main.371/)** — Index ID `url:https://aclanthology.org/2024.emnlp-main.371/`. Focus on the systems trade-off between sharing reusable PEFT pieces and preserving user-specific behavior.

- **[Personalize Your LLM: Fake it then Align it](https://aclanthology.org/2025.findings-naacl.407/)** — Index ID `url:https://aclanthology.org/2025.findings-naacl.407/`. Examine the assumptions introduced when personal preference data is generated synthetically rather than collected directly.

## 5. Finish with user control and open problems

- **[BenchPreS: A Benchmark for Context-Aware Personalized Preference Selectivity of Persistent-Memory LLMs](https://arxiv.org/abs/2603.16557)** — Index ID `arxiv:2603.16557`. Study the difference between remembering a preference and applying it in the right context.

- **[When Personalization Meets Reality: A Multi-Faceted Analysis of Personalized Preference Learning](https://aclanthology.org/2025.findings-emnlp.916/)** — Index ID `url:https://aclanthology.org/2025.findings-emnlp.916/`. Use it as a checklist for performance, fairness, unintended effects, adaptability, and safety.
