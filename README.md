# LLM Personalization Papers

An open, community-maintained index of research on personalized large language models, covering user modeling, memory, personalized alignment, generation, agents, and evaluation.

**New to the field?** Start with the [reading guide](docs/reading-guide.md).
**Looking for papers?** Browse the [paper index](#paper-index).
**Adding or updating a paper?** Read the [contribution guide](CONTRIBUTING.md).

## Contribute

Missing a relevant paper? Open a pull request or a paper-suggestion issue. Authors are welcome to submit their own work.

We welcome preprints and published papers. We review submissions for relevance, accurate metadata, working source links, and duplicates. In-scope entries that meet the contribution guidelines are welcome regardless of venue or code availability.

Inclusion does not imply endorsement of a paper's findings or a claim that its results have been independently reproduced.

## Scope

This index covers research where user preferences, history, profiles, feedback, personal context, or user-specific goals affect an LLM's behavior, outputs, interactions, or decisions. It includes methods, datasets, benchmarks, applications, and work on privacy, safety, bias, and user control. General RAG, generic agents, role-playing, and traditional recommendation papers are not included unless the paper explicitly studies user-specific adaptation.

See [CONTRIBUTING.md](CONTRIBUTING.md) for the full inclusion rules and entry format.

<a id="paper-index"></a>
## Paper Index

<!-- PAPERS:START -->

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

- **[User Profiling for Specification-Sensitive Recommendations with Large Language Model Prompting](https://aclanthology.org/2026.lrec-1.43/)**
  - ID: `url:https://aclanthology.org/2026.lrec-1.43/`
  - First public: `2026`
  - Publication: LREC 2026
  - Summary: Uses prompting to derive user and item profiles from reviews and specifications for recommendations that must respect fine-grained product attributes.
  - Tags: `user-profile` `recommendation` `prompting`

- **[Guided Profile Generation Improves Personalization with Large Language Models](https://aclanthology.org/2024.findings-emnlp.231/)**
  - ID: `url:https://aclanthology.org/2024.findings-emnlp.231/`
  - First public: `2024-11`
  - Publication: Findings of EMNLP 2024
  - Summary: Generates concise natural-language profiles from sparse personal context before asking an LLM to produce a personalized output.
  - Tags: `user-profile` `prompting` `user-history`

- **[User Embedding Model for Personalized Language Prompting](https://aclanthology.org/2024.personalize-1.12/)**
  - ID: `url:https://aclanthology.org/2024.personalize-1.12/`
  - First public: `2024-03`
  - Publication: PERSONALIZE 2024
  - Summary: Compresses long free-form user histories into embeddings that act as soft prompts for language models handling preference-sensitive tasks.
  - Tags: `user-history` `prompting` `user-profile`

<a id="memory-retrieval"></a>
### Memory & Retrieval

- **[Evoking User Memory: Personalizing LLM via Recollection-Familiarity Adaptive Retrieval](https://arxiv.org/abs/2603.09250)**
  - ID: `arxiv:2603.09250`
  - First public: `2026-03`
  - Publication: Preprint
  - Summary: Uses uncertainty-guided familiarity and recollection paths to retrieve user memories adaptively instead of relying on one-shot similarity search.
  - Tags: `memory` `retrieval` `user-history`

- **[PRIME: Large Language Model Personalization with Cognitive Dual-Memory and Personalized Thought Process](https://aclanthology.org/2025.emnlp-main.1711/)**
  - ID: `url:https://aclanthology.org/2025.emnlp-main.1711/`
  - First public: `2025-11`
  - Publication: EMNLP 2025
  - Summary: Separates episodic interaction memory from semantic user beliefs and adds a personalized thinking process to a unified personalization framework.
  - Tags: `memory` `personalized-alignment` `user-history`

- **[Personalized Large Language Model Assistant with Evolving Conditional Memory](https://aclanthology.org/2025.coling-main.254/)**
  - ID: `url:https://aclanthology.org/2025.coling-main.254/`
  - First public: `2025-01`
  - Publication: COLING 2025
  - Summary: Stores dialogue-derived records in a memory bank, retrieves relevant records, and evaluates personalized assistants on dialogue continuation, knowledge, and feedback tasks.
  - Tags: `memory` `retrieval` `agent`

- **[On the Way to LLM Personalization: Learning to Remember User Conversations](https://arxiv.org/abs/2411.13405)**
  - ID: `arxiv:2411.13405`
  - First public: `2024-11`
  - Publication: L2M2 2025 workshop
  - Summary: Introduces a parameter-efficient pipeline that turns sequential prior conversations into training pairs for remembering user-specific information.
  - Tags: `memory` `user-history` `fine-tuning`

- **[MemoryBank: Enhancing Large Language Models with Long-Term Memory](https://arxiv.org/abs/2305.10250)**
  - ID: `arxiv:2305.10250`
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

- **[Drift: Decoding-time Personalized Alignments with Implicit User Preferences](https://aclanthology.org/2025.findings-emnlp.324/)**
  - ID: `arxiv:2502.14289`
  - First public: `2025-02`
  - Publication: Findings of EMNLP 2025
  - Summary: Steers a frozen LLM at decoding time by representing implicit user preferences as interpretable attributes inferred from a small number of examples.
  - Tags: `decoding` `steering` `preference-elicitation`

- **[RAGs to Style: Personalizing LLMs with Style Embeddings](https://aclanthology.org/2024.personalize-1.11/)**
  - ID: `url:https://aclanthology.org/2024.personalize-1.11/`
  - First public: `2024-03`
  - Publication: PERSONALIZE 2024
  - Summary: Uses style embeddings in retrieval-augmented prompting to represent authorial characteristics for personalized generation on the LaMP benchmark.
  - Tags: `retrieval` `prompting` `user-profile`

<a id="training-alignment"></a>
### Fine-tuning & Personalized Alignment

- **[FaST: Feature-aware Sampling and Tuning for Personalized Preference Alignment with Limited Data](https://aclanthology.org/2025.emnlp-main.475/)**
  - ID: `url:https://aclanthology.org/2025.emnlp-main.475/`
  - First public: `2025-11`
  - Publication: EMNLP 2025
  - Summary: Studies personalized preference alignment with small per-user questionnaires and proposes feature-aware sampling and parameter-efficient tuning.
  - Tags: `personalized-alignment` `fine-tuning` `peft`

- **[Personalize Your LLM: Fake it then Align it](https://aclanthology.org/2025.findings-naacl.407/)**
  - ID: `url:https://aclanthology.org/2025.findings-naacl.407/`
  - First public: `2025-04`
  - Publication: Findings of NAACL 2025
  - Summary: Generates synthetic personal preference data and uses representation editing to adapt instruction-tuned models without a separate full fine-tuning run per user.
  - Tags: `personalized-alignment` `fine-tuning` `user-profile`

- **[Aligning LLMs with Individual Preferences via Interaction](https://aclanthology.org/2025.coling-main.511/)**
  - ID: `url:https://aclanthology.org/2025.coling-main.511/`
  - First public: `2025-01`
  - Publication: COLING 2025
  - Summary: Trains models to infer unspoken preferences through multi-turn interaction and introduces a customized-alignment benchmark for conversational evaluation.
  - Tags: `personalized-alignment` `preference-elicitation` `benchmark`

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

- **[Personalized Language Modeling from Personalized Human Feedback](https://arxiv.org/abs/2402.05133)**
  - ID: `arxiv:2402.05133`
  - First public: `2024-02`
  - Publication: Preprint
  - Summary: Jointly learns a lightweight user model and a personalized language model from feedback to represent explicit and implicit individual preferences.
  - Tags: `personalized-alignment` `reward-modeling` `preference-elicitation`

<a id="agents-applications"></a>
### Personalized Agents & Applications

- **[Language Models Don’t Know What You Want: Evaluating Personalization in Deep Research Needs Real Users](https://aclanthology.org/2026.acl-long.723/)**
  - ID: `url:https://aclanthology.org/2026.acl-long.723/`
  - First public: `2026`
  - Publication: ACL 2026
  - Summary: Introduces MyScholarQA, a personalized deep-research setting that profiles real users, proposes actions, and produces reports after user-approved planning.
  - Tags: `agent` `search` `evaluation`

- **[Personal Large Language Model Agents: A Case Study on Tailored Travel Planning](https://aclanthology.org/2024.emnlp-industry.37/)**
  - ID: `url:https://aclanthology.org/2024.emnlp-industry.37/`
  - First public: `2024-11`
  - Publication: EMNLP 2024 Industry Track
  - Summary: Adapts TravelPlanner into a personalized travel-planning benchmark and studies baselines for agents that incorporate individual preferences.
  - Tags: `agent` `recommendation` `benchmark`

- **[Crafting Personalized Agents through Retrieval-Augmented Generation on Editable Memory Graphs](https://aclanthology.org/2024.emnlp-main.281/)**
  - ID: `url:https://aclanthology.org/2024.emnlp-main.281/`
  - First public: `2024-11`
  - Publication: EMNLP 2024
  - Summary: Builds personalized agents from editable graphs of smartphone memories and evaluates transfer to a real assistant application.
  - Tags: `agent` `memory` `retrieval`

<a id="benchmarks-evaluation"></a>
### Benchmarks & Evaluation

- **[Personalized Benchmarking: Evaluating LLMs by Individual Preferences](https://arxiv.org/abs/2604.18943)**
  - ID: `arxiv:2604.18943`
  - First public: `2026-04`
  - Publication: Preprint
  - Summary: Computes user-specific model rankings from Chatbot Arena preferences and analyzes how topics and writing style relate to ranking differences.
  - Tags: `benchmark` `evaluation` `user-profile`

- **[MPTA: MultiTask Personalization Assessment](https://aclanthology.org/2025.findings-emnlp.640/)**
  - ID: `url:https://aclanthology.org/2025.findings-emnlp.640/`
  - First public: `2025-11`
  - Publication: Findings of EMNLP 2025
  - Summary: Uses large-scale survey responses to build detailed personas and tests personalized behavior across alignment tasks and subgroup-sensitive outcomes.
  - Tags: `benchmark` `evaluation` `personalized-alignment`

- **[Benchmarking and Improving LLM Robustness for Personalized Generation](https://aclanthology.org/2025.findings-emnlp.870/)**
  - ID: `url:https://aclanthology.org/2025.findings-emnlp.870/`
  - First public: `2025-11`
  - Publication: Findings of EMNLP 2025
  - Summary: Defines robust personalized generation as preserving factuality while following user preferences and introduces the PERG evaluation framework and dataset.
  - Tags: `benchmark` `evaluation` `user-history`

- **[LaMP: When Large Language Models Meet Personalization](https://aclanthology.org/2024.acl-long.399/)**
  - ID: `arxiv:2304.11406`
  - First public: `2023-04`
  - Publication: ACL 2024
  - Summary: Introduces seven personalized language tasks and retrieval augmentation methods for selecting relevant items from individual user profiles.
  - Tags: `benchmark` `retrieval` `evaluation`
  - Resources: [Code](https://github.com/LaMP-Benchmark/LaMP)

<a id="privacy-safety-control"></a>
### Privacy, Safety & User Control

- **[BenchPreS: A Benchmark for Context-Aware Personalized Preference Selectivity of Persistent-Memory LLMs](https://arxiv.org/abs/2603.16557)**
  - ID: `arxiv:2603.16557`
  - First public: `2026-03`
  - Publication: Preprint
  - Summary: Measures whether persistent user preferences are applied or suppressed appropriately across communication contexts using misapplication and appropriate-application rates.
  - Tags: `privacy` `user-control` `benchmark`

- **[When Personalization Meets Reality: A Multi-Faceted Analysis of Personalized Preference Learning](https://aclanthology.org/2025.findings-emnlp.916/)**
  - ID: `url:https://aclanthology.org/2025.findings-emnlp.916/`
  - First public: `2025-11`
  - Publication: Findings of EMNLP 2025
  - Summary: Evaluates personalized preference learning across performance, fairness, unintended effects, adaptability, and safety under differing user preferences.
  - Tags: `personalized-alignment` `safety` `evaluation`

<!-- PAPERS:END -->

## Contributors & Acknowledgments

Thank you to everyone who contributes paper suggestions, metadata corrections, source links, reading-guide improvements, and maintenance work. This first version does not list contributors until real contributions have been made.

## License

The original text, scripts, and templates in this repository are released under the [MIT License](LICENSE). Linked papers, code, datasets, and other external materials remain under their own licenses and terms; this repository license does not relicense them.

## Suggested GitHub Topics

`llm-personalization` `personalized-llm` `large-language-models` `paper-list` `user-modeling`
