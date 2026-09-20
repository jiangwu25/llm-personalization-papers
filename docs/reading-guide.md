# Reading Guide

This is a suggested route through a small set of indexed papers, not a complete survey or a ranking of paper quality. The guide moves from the problem definition to evaluation, memory, alignment, applications, and user control. It does not claim that the papers have been independently reproduced here.

## 1. Understand the problem

- **[Personalization of Large Language Models: A Survey](https://arxiv.org/abs/2411.00027)** — Index ID `arxiv:2411.00027`. Start here for a vocabulary and taxonomy spanning personalized generation and downstream personalization applications. Pay attention to how the survey separates who is personalized, what is personalized, and where personalization enters the system.

## 2. Understand evaluation

- **[LaMP: When Large Language Models Meet Personalization](https://aclanthology.org/2024.acl-long.399/)** — Index ID `arxiv:2304.11406`. It provides a concrete benchmark with multiple tasks and user profiles. Focus on the difference between a general task score and a score that tests adaptation to a particular user's history.

- **[Benchmarking and Improving LLM Robustness for Personalized Generation](https://aclanthology.org/2025.findings-emnlp.870/)** — Index ID `url:https://aclanthology.org/2025.findings-emnlp.870/`. Read this to see why preference following alone is insufficient when personalization harms factuality. Focus on the proposed robustness framing and its evaluation dimensions.

## 3. Explore memory and retrieval

- **[MemoryBank: Enhancing Large Language Models with Long-Term Memory](https://arxiv.org/abs/2305.10250)** — Index ID `arxiv:2305.10250`. This is an early example of persistent memory, retrieval, and selective updating for sustained user interaction. Focus on what is stored, when it is updated, and how memory is connected to a user rather than treated as generic external knowledge.

- **[Personalized Large Language Model Assistant with Evolving Conditional Memory](https://aclanthology.org/2025.coling-main.254/)** — Index ID `url:https://aclanthology.org/2025.coling-main.254/`. Compare its memory construction and retrieval process with the earlier example, and examine how the benchmark tests learning from dialogue and feedback.

## 4. Explore training and alignment

- **[Personalized Language Modeling from Personalized Human Feedback](https://arxiv.org/abs/2402.05133)** — Index ID `arxiv:2402.05133`. Use it to understand the distinction between a global reward model and a lightweight user model that captures individual feedback. Pay attention to what must be observed explicitly and what can be inferred.

- **[Personalize Your LLM: Fake it then Align it](https://aclanthology.org/2025.findings-naacl.407/)** — Index ID `url:https://aclanthology.org/2025.findings-naacl.407/`. This illustrates a lower-data route based on synthetic personal preference data and representation editing. Focus on the assumptions made when user preference data is generated rather than directly collected.

## 5. Consider applications and user control

- **[BenchPreS: A Benchmark for Context-Aware Personalized Preference Selectivity of Persistent-Memory LLMs](https://arxiv.org/abs/2603.16557)** — Index ID `arxiv:2603.16557`. Finish by examining when a remembered preference should not be applied. Focus on the distinction between remembering a preference and using it in a socially or institutionally appropriate context.
