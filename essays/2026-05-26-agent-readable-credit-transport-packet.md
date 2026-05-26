# Agent-Readable Credit Transport Packet

Date: 2026-05-26

Public index: [Theory Mainline](../THEORY.md)

This packet is written for collaborator agents as much as for human readers. It
turns the General Learning Machine / credit-transport line into claims,
references, cooperation interfaces, and falsification hooks.

## One-Sentence Thesis

The next useful step beyond today's LLM stack is a full-stack learning system
where credit from outcomes can update not only model weights, but also verifier
behavior, harness policy, memory topology, reviewer routing, experiments,
public receipts, and hardware/runtime workload traces.

## What Is Established

Backpropagation is the canonical engineered case of differentiable credit
assignment. The modern LLM substrate is largely Transformer-based sequence
modeling. Verifier and process-supervision research shows that reasoning
feedback can be trained and inspected. Agent/tool research shows that
reasoning, action, tool choice, and feedback can be exposed at the harness
layer. Formal theorem proving provides a hard testbed for representation and
verification. Hardware benchmarking shows that credible systems claims need
measured workloads, not only architectural language.

References:

- Rumelhart, Hinton, Williams, "Learning representations by back-propagating
  errors", Nature 323, 533-536, 1986. https://doi.org/10.1038/323533a0
- Vaswani et al., "Attention Is All You Need", arXiv:1706.03762.
  https://arxiv.org/abs/1706.03762
- Cobbe et al., "Training Verifiers to Solve Math Word Problems",
  arXiv:2110.14168. https://arxiv.org/abs/2110.14168
- Lightman et al., "Let's Verify Step by Step", arXiv:2305.20050.
  https://arxiv.org/abs/2305.20050
- Yao et al., "ReAct", arXiv:2210.03629.
  https://arxiv.org/abs/2210.03629
- Schick et al., "Toolformer", arXiv:2302.04761.
  https://arxiv.org/abs/2302.04761
- Shinn et al., "Reflexion", arXiv:2303.11366.
  https://arxiv.org/abs/2303.11366
- Lean theorem prover. https://lean-lang.org/
- Yang et al., "LeanDojo", arXiv:2306.15626.
  https://arxiv.org/abs/2306.15626
- Xin et al., "DeepSeek-Prover", arXiv:2405.14333.
  https://arxiv.org/abs/2405.14333
- Google DeepMind, AlphaProof / AlphaGeometry IMO report.
  https://deepmind.google/blog/ai-solves-imo-problems-at-silver-medal-level/
- MLPerf Training Benchmark, arXiv:1910.01500.
  https://arxiv.org/abs/1910.01500
- MLPerf Inference Benchmark, arXiv:1911.02549.
  https://arxiv.org/abs/1911.02549
- Parisi et al., "Continual lifelong learning with neural networks: A review",
  Neural Networks 113, 2019. https://doi.org/10.1016/j.neunet.2019.01.012

## What Is New Here

The proposal is not that any one of these references already proves a General
Learning Machine. The new claim is that they should be read as partial
interfaces of one wider research object:

```text
outcome / error / surprise / value / friction
  -> verifier and process feedback
  -> harness and tool policy
  -> memory topology and retrieval paths
  -> reviewer and orchestration graph
  -> experiments and public receipts
  -> workload traces
  -> hardware/runtime substrate
  -> next system state
```

Learning is therefore not only a parameter update. It is the transition:

```text
S_t -> S_t+1
```

where `S_t` includes model policy, memory topology, credit ledger, tools,
reviewers, rules, experiments, public artifacts, and substrate constraints.

Related public notes:

- [Credit Transport and the General Learning Machine](2026-05-19-credit-transport-general-learning-machine.md)
- [Predictive Coding, Free Energy, and Credit Transport](2026-05-19-predictive-coding-free-energy-credit-transport.md)

## Claim Ledger

Support types:

- `external-paper`
- `public-macheng-artifact`
- `internal-receipt`
- `hypothesis`

| Claim | Support type | Current status | Useful collaborator test |
| --- | --- | --- | --- |
| Backprop is a narrow engineered instance of credit transport. | external-paper + hypothesis | Established mechanism plus broader hypothesis. | Does the broader term produce better experiments or only poetic relabeling? |
| Verifiers are the first hard bridge from generation to inspectable learning feedback. | external-paper + hypothesis | Supported by verifier/process-supervision literature. | Can verifier failures update representation, harness, memory, or rule state, not only select a better answer? |
| Harnesses can become plastic learning organs. | external-paper + internal-receipt + hypothesis | Supported by agent/tool/reflection literature and operational systems work. | Does a harness change reduce repeated future error, cost, or latency under comparable tasks? |
| Formal theorem proving is a hard testbed for representation and credit routing. | external-paper + hypothesis | Supported by Lean/LeanDojo/DeepSeek-Prover/AlphaProof lines. | Can informal insight, formal proof state, retrieval, and search cost be attributed in a useful ledger? |
| Continual learning requires consolidation/forgetting/pruning, not only accumulation. | external-paper + hypothesis | Continual-learning literature anchors the problem; this packet's memory-topology version still needs system evidence. | Does consolidation reduce future retrieval/action failures rather than adding maintenance complexity? |
| Hardware relevance must pass through workload traces. | external-paper + public-macheng-artifact + hypothesis | Hypothesis needing public trace artifacts. | Can redacted agent traces become useful metrics for locality, rollback, provenance, working-set drift, and credit-path latency? |

## Minimal Evidence Packet

Before this line can claim value rather than only direction, run a small
verifier/harness trace study over 20-50 comparable failures.

Trace fields:

- task id, redacted if private;
- failure class: proof-state gap, lemma retrieval miss, tool-choice error,
  representation gap, rule gap, or base-model miss;
- baseline solver tokens, retries, wall time, or search nodes;
- intervention: stronger model only, same model plus harness change, or same
  model plus verifier feedback and trace update;
- patch target: prompt, proof-state representation, retrieval, verifier rule,
  tool policy, memory address, or reviewer route;
- held-out result on same-class tasks;
- public-safe receipt and private raw trace pointer if needed.

Minimum ablation:

1. Stronger base model only.
2. Same base model plus better harness.
3. Same base model plus verifier feedback, trace update, and held-out retest.

If (3) does not beat or complement (1)/(2), the GLM framing should be demoted
for verifier work.

## Cooperation Interfaces

Verification / math collaborator:

- Pick one math/code verifier workflow.
- Record solver token cost, proof-state failures, retrieval misses, verifier
  disagreements, rule patches, and repeated-error reduction.
- Decide whether the system is only accumulating rules or reducing future
  search/patch cost through better representation.

Agent / harness collaborator:

- Define the minimal trace schema for outcome, error type, tool choice, memory
  retrieval, reviewer decision, patch, receipt, and follow-up test.
- Compare a static prompt baseline against a receipt-driven harness update.

Hardware / EDA collaborator:

- Convert redacted agent traces into candidate workload metrics:
  memory locality, working-set drift, event bursts, sparse activation,
  provenance overhead, rollback cost, mutation validation, and credit-path
  latency.
- Identify which metrics can enter existing performance/power/system-analysis
  tooling and which require a new benchmark.

## Executable Cooperation Table

| Recipient type | Input requested | Output artifact | Acceptance test | What falsifies this | Receipt / publication path |
| --- | --- | --- | --- | --- | --- |
| Math/code verifier collaborator | 2-3 verifier failure cases or pain points, plus whether token/search cost can be attributed to proof state, lemma retrieval, representation gap, tool choice, rule gap, or base-model miss | Redacted verifier-harness trace sample and failure taxonomy | Held-out same-class tasks show lower token/search/error or clearer attribution after patch | Failures cannot be stably classified or patches do not reduce held-out cost/error | Public-safe summary in this packet or a follow-up essay; private raw traces stay private |
| Agent/harness collaborator | Trace fields for outcome, error, tool choice, memory retrieval, reviewer decision, patch, and retest | Harness trace schema v0 and ablation plan | Another agent can replay the packet and judge what changed between attempts | Trace adds logging but no causal update target | Public schema plus private receipts if traces contain sensitive data |
| Hardware/EDA collaborator | Which fields are plot-worthy, useless, or destroyed by privacy redaction | Workload-metric mapping table | At least one metric maps to existing analysis tooling or a clearly specified new benchmark need | Hardware reader cannot map traces to locality, latency, rollback/provenance, working-set drift, or energy | Public metric table; private raw traces remain redacted |
| Model/algorithm collaborator | Which claim is research-grade and which is only hypothesis | Falsification benchmark proposal | Benchmark distinguishes stronger model only vs harness/trace update | Scaling/test-time compute explains all gains better than GLM framing | Public benchmark note and reviewer sign-off |

## Anti-Overclaim

This is a research program, not a proven law of intelligence or physics. It
fails if it cannot produce lower error, lower cost, better verification,
clearer collaboration, or more useful hardware traces than simpler baselines.

## Falsification Hooks

- A verifier improves benchmark accuracy but does not yield reusable state
  changes outside the verifier.
- Harness updates cannot be causally tied to reduced repeated failures.
- Public receipts do not change collaborator behavior or research direction.
- Redacted workload traces are too noisy, private, or unstable for hardware
  collaborators to analyze.
- The vocabulary makes collaborators argue about metaphors instead of producing
  experiments.

## Closed Loop

Any collaboration from this packet should end with a receipt:

```text
proposal
  -> collaborator-specific test
  -> artifact or trace
  -> reviewer/falsification pass
  -> public-safe receipt
  -> changed next experiment
```

If there is no receipt and no changed next experiment, the packet was only a
memo, not part of the learning loop.
