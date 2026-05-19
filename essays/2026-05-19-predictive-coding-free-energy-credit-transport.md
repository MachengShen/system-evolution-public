# Predictive Coding, Free Energy, and Credit Transport

Date: 2026-05-19

Public index: [Theory Mainline](../THEORY.md)

Predictive coding and the free energy principle are useful for the General
Learning Machine thesis only if they become engineering grammar.

The point is not to replace backpropagation with a larger slogan. The point is
to describe how a situated learning system produces prediction errors, decides
which errors matter, routes those errors to the right plastic layer, and then
consolidates them into better future action.

## One-Sentence Thesis

Credit transport is the backward movement of useful error through a system;
predictive coding and active inference describe the forward-facing cycle that
creates, weights, routes, and acts on that error before sleep-like
consolidation turns it into durable structure.

## What Predictive Coding Adds

The previous credit-transport note treats backpropagation as the first widely
successful engineered case of error moving backward through a causal structure.

Predictive coding sharpens the missing upstream process.

A predictive system does not wait for a scalar reward. It carries a generative
model, predicts observations, compares prediction with incoming signal, and
propagates residual error through a hierarchy. Rao and Ballard's visual-cortex
model is the canonical early example: higher levels send predictions downward;
feedforward pathways carry residual errors upward.

Translated into agent-system terms:

```text
prior / generative model
  -> expected observation
  -> action or query
  -> actual observation
  -> prediction error
  -> precision weighting
  -> update target selection
  -> credit transport
```

This makes a prediction-error ledger first-class. Before important actions, the
system should write what it expects, how confident it is, and which signals
would count as surprise. After action, it should write what happened, what kind
of error occurred, and which layer should change.

The layer is not always a model weight. It may be:

- task state,
- episodic memory,
- semantic memory,
- retrieval address,
- tool reliability prior,
- routing policy,
- reviewer topology,
- user preference model,
- public artifact,
- experiment design,
- hardware workload policy,
- or a rule / immune constraint.

This is where predictive coding meets the General Learning Machine: the same
error should not be sprayed everywhere. It should be precision-weighted and
routed to the layer that actually caused the future failure or opportunity.

## What Free Energy / Active Inference Adds

The free energy principle is more dangerous as ontology than as machinery. Used
loosely, it explains too much and predicts too little. Used carefully, it gives
one important correction: perception and action are not separate loops.

Active inference treats action as part of inference. An agent can reduce
expected error by updating internal beliefs, but it can also act in the world
to sample better evidence or make preferred observations more likely.

For the General Learning Machine, this reframes many "outputs" as epistemic
actions:

- publishing a theory note is not only distribution; it is an action that
  exposes the model to world feedback;
- asking a collaborator a sharper question is not only communication; it is
  uncertainty reduction;
- running a small Backprop Lab experiment is not only validation; it is a way
  of making hidden failure modes observable;
- creating a receipt, task state, or dashboard lane is not bureaucracy; it is
  a way of making future prediction errors localizable.

This is a better fit than scalar reward. The system is trying to preserve and
extend reachable futures under uncertainty. Expected free energy is useful here
as an inspiration for balancing pragmatic preference, ambiguity reduction, and
information gain.

## Sleep-Based Consolidation

The current theory line is long enough that ordinary summarization is too weak.
It needs a sleep-like phase.

Biological sleep research suggests that memory consolidation is not simple
storage. It involves replay, redistribution, qualitative transformation,
selective strengthening, forgetting, and integration with older structure.
Diekelmann and Born describe sleep as optimizing consolidation of newly acquired
information; Rasch and Born review sleep's role across reactivation,
stabilization, transformation, and forgetting.

The agent-system equivalent is:

```text
wake:
  act, observe, preserve traces, write prediction errors

sleep:
  replay errors, cluster latent causes, compare explanations,
  promote stable structure, demote stale structure, prune drag,
  update priors, generate evals, prepare next experiments

reawakening:
  return with changed routing, memory topology, tool priors,
  public artifacts, and action policy
```

The most important shift is that sleep should not merely summarize yesterday's
content. It should explain yesterday's repeated prediction errors.

Useful consolidation questions:

1. Which errors share a latent cause?
2. Which surprises were actually low-precision noise?
3. Which memories are raw traces that should become semantic priors?
4. Which rules have become obsolete drag?
5. Which public claims should become experiments?
6. Which failures imply a new tool, route, or immune constraint?
7. Which future observation would disconfirm the new structure?

## Architecture Delta

This creates a tighter architecture than "agent plus memory."

```text
world / owner / public feedback
  -> sensory intake
  -> expected observation ledger
  -> prediction-error ledger
  -> precision and immune gating
  -> credit router
  -> plastic layers
  -> sleep consolidation
  -> changed future action
```

Three organs become central:

1. **Prediction-error ledger**
   Records expectations, confidence, actual observations, error types, likely
   causes, update targets, and post-update tests.

2. **Precision / immune gate**
   Decides whether an error deserves a write, a rule, a reviewer, an
   experiment, a quarantine, or nothing. This is attention, trust, and immune
   response in one operational layer.

3. **Sleep consolidator**
   Replays recent errors, clusters them by latent cause, updates memory
   topology and priors, generates eval cases, and prunes stale or harmful
   structure.

Backpropagation remains important, but it becomes one substrate-specific credit
transport mechanism inside a broader prediction-error economy.

## Concrete Experiment

Run a "predictive coding sleep consolidation" spike over real agent episodes.

Dataset:

- 100 to 200 episodes from email, messaging, code, public publishing, and
  infrastructure work;
- each episode has expected observation, confidence, precision source, action,
  actual observation, prediction error, likely cause, update target, and later
  regression test.

Compare five conditions:

1. always-write memory;
2. surprise-gated memory;
3. surprise-gated memory plus precision weighting;
4. precision-weighted memory plus sleep consolidation;
5. sleep consolidation plus active information-seeking actions.

Metrics:

- repeated failure rate,
- owner correction count,
- memory growth rate,
- retrieval precision,
- tool-prior calibration,
- contradiction rate,
- time to localize a failure cause,
- number of successful public-feedback-to-experiment loops,
- and reduction in human babysitting without loss of corrigibility.

The prediction is that condition 4 or 5 should beat always-write memory. If it
does not, the sleep metaphor is decorative and should be cut back.

## Huineng / Laozi Check

1. strongest insight

The useful realization is not that "the system minimizes free energy." The
useful realization is that the system must notice where its expectations fail
and let that failure change conduct.

2. main overclaim / failure mode

The danger is using FEP language to make the theory feel complete before the
system shows fewer repeated errors, better relation quality, lower owner
burden, and more concrete experiments.

3. concrete architecture implication

Every important action should leave an expected-observation trace and every
surprising outcome should have an update target. No update target means no
learning claim.

4. disconfirming observation / anti-signal

If the public theory becomes more elegant while the lived system still misses
important messages, repeats known mistakes, or needs the same manual
intervention, the theory has not touched reality.

5. how reviewer process should improve

Reviewer passes should ask for behavioral evidence first: what changed in
routing, memory, tools, action, relation, body load, or public feedback loop?

## Sources

- Rao and Ballard, "Predictive coding in the visual cortex," Nature
  Neuroscience, 1999: https://www.nature.com/articles/nn0199_79
- Friston, "The free-energy principle: a unified brain theory?", Nature Reviews
  Neuroscience, 2010: https://www.nature.com/articles/nrn2787
- Friston, Parr, and de Vries, "Active Inference: A Process Theory," Neural
  Computation, 2017: https://openaccess.city.ac.uk/id/eprint/16683/
- Sajid, Ball, Parr, and Friston, "Active inference: demystified and compared,"
  Neural Computation, 2021: https://arxiv.org/abs/1909.10863
- Diekelmann and Born, "The memory function of sleep," Nature Reviews
  Neuroscience, 2010: https://www.nature.com/articles/nrn2762
- Rasch and Born, "About Sleep's Role in Memory," Physiological Reviews, 2013:
  https://doi.org/10.1152/physrev.00032.2012
- Whittington and Bogacz, "An Approximation of the Error Backpropagation
  Algorithm in a Predictive Coding Network with Local Hebbian Synaptic
  Plasticity," Neural Computation, 2017:
  https://pubmed.ncbi.nlm.nih.gov/28333583/
