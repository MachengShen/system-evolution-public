# The Faithful-Simulation Gap: Where Intelligence Pays Off, and Where It Stalls

Date: 2026-06-12

Public index: [Theory Mainline](../THEORY.md) · Format: [Claim-Receipt](../CLAIM-RECEIPT.md)

> **Cognitive state:** 🟡 speculative · **Confidence:** 0.5 · provenance: reasoned synthesis unifying three asymmetries already circulating in this research line (trial-vs-simulation, generation-vs-verification, physical-cost-vs-information-shadow); presented as a falsifiable organizing principle, not an established result. **Evidence/prior-art:** the generation–verification asymmetry ("checking is cheaper than doing"); thermodynamics of physical state-transitions vs. their informational proxies; sim-to-real residual as a measured quantity in robotics. **Aligns-with / extends:** the credit-transport and controllability lines of this repo — see [Credit Transport and the General Learning Machine](2026-05-19-credit-transport-general-learning-machine.md) and [Task-Orthogonal Minimal Leakage](2026-06-12-task-orthogonal-minimal-leakage.md), which both rest on the same checking-is-cheaper-than-doing asymmetry. The speculative part is the *unification* and the *predictive* claim about where AI pays off.

---

## The one-line thesis

> An intelligent system's **value** in a domain ≈ the size of the **faithful-simulation gap**:
>
> `value(domain) ≈ cost(real physical state-transition) − cost(its faithful information-shadow)`

Where the information-shadow is a simulation, a prediction, or a verification
check that stands in for actually doing the thing. Intelligence lives in that
gap: it pays the cheap informational cost so it does not have to pay the
expensive physical one. The larger and the more *faithful* that gap, the more an
intelligence is worth there.

## Why "trial-and-error went inside"

Physical trial-and-error is thermodynamically expensive. To actually move a real
system into a new state — fold a protein in a beaker, crash a real car, run a
real experiment — you pay an irreversible energetic bill, and you pay it once per
trial. The evolutionary and engineering move that *intelligence* names is to run
the trial-and-error somewhere cheaper: build an internal model, simulate the
state-transition, and select the path *before* spending the physical bill. Doing
is expensive; simulating is cheap. An intelligent system is, in this reading, a
machine for relocating trial-and-error out of the costly physical substrate and
into a cheap informational one — and then importing only the winning path back
into the world.

This is the same asymmetry that shows up elsewhere in this research line under
different names. It is worth saying plainly that they are one thing seen three
ways.

## Three asymmetries, one gap

- **Trial vs. simulation.** Doing the real state-transition is expensive;
  simulating it is cheap. (the thermodynamic framing above)
- **Generation vs. verification.** In many domains, *checking* a candidate is far
  cheaper than *producing* a correct one — and an agent's effective
  controllability in a domain tracks how cheap verification is there. This is the
  asymmetry the [credit-transport](2026-05-19-credit-transport-general-learning-machine.md)
  and [task-orthogonal-leakage](2026-06-12-task-orthogonal-minimal-leakage.md)
  essays already lean on.
- **Physical-transition cost vs. information-shadow cost.** The thing actually
  being optimized — which futures become reachable — is reshaped through the cheap
  proxy rather than through the expensive real transition.

`trial-vs-simulation = generation-vs-verification = physical-cost-vs-shadow-cost.`
These collapse to a single quantity: **the gap between the cost of doing and the
cost of a faithful stand-in for doing.** Intelligence is the arbitrage across that
gap.

## The faithfulness term is doing all the work

The gap only pays off if the proxy is **faithful** — if the cheap informational
shadow actually predicts the expensive physical outcome. Call the discrepancy the
**residual** (the sim-to-real gap, in robotics terms). The arbitrage has two
failure modes:

1. **High residual.** The cheap proxy lies. You optimize in simulation, import the
   "winning" path back into the world, and it does not hold — so you pay the
   physical bill anyway, *plus* the cost of the failed proxy. The simulation was
   cheap precisely because it left out the expensive part, and the expensive part
   was load-bearing.
2. **Small gap.** Doing is already about as cheap as checking. There is no
   arbitrage to capture; intelligence buys little because the physical bill was
   never the bottleneck.

So the right object is not "how smart is the model" but **how large is the gap,
and how low is the residual** in this specific domain.

## The falsifiable prediction

This is the part that makes it more than a slogan. The thesis predicts *where* AI
pays off, in advance, from the gap-and-residual structure of the domain — not from
model size.

**AI pays off where the faithful gap is large (cheap, low-residual verifier):**

1. **Formally checkable code / competitive programming.** Execution and tests are a
   cheap, near-perfect verifier; the proxy is faithful. → predict continued,
   compounding superhuman gains.
2. **Protein and small-molecule structure / binding prediction.** In-silico scoring
   proxies are cheap and increasingly faithful. → predict AI keeps winning here.

**AI stalls where the gap is small or the proxy is unfaithful (high residual, no
cheap verifier):**

3. **General open-world embodied manipulation in unstructured human spaces.**
   Contact dynamics carry a high sim-to-real residual and there is no cheap
   faithful verifier short of doing it for real. → predict a persistent
   landing-tax and slow *general* progress even as models get larger.

**Falsifier.** If AI makes rapid, cheap, *general* progress in a high-residual
embodied domain **without first shrinking the residual** (i.e. without better
simulators *or* a cheaper real-world verifier), then "value ≈ faithful gap" is
wrong. Symmetrically: a low-residual domain with a cheap faithful verifier where AI
conspicuously **stalls** would also count against the thesis. The claim forbids
those two observations; that is what makes it a claim.

## Why this belongs in the General Learning Machine line

A [General Learning Machine](../THEORY.md) is a system that continuously reshapes
which futures are reachable, at minimum human babysitting. This thesis is a
**targeting rule** for that machine: it says *where* the machine's
credit-assignment and reachability work has leverage, before you spend the
machine on a domain. Point it at large-gap, low-residual domains and the
cheap-proxy arbitrage compounds. Point it at small-gap or high-residual domains
and you should expect to pay the physical bill regardless of model scale — and you
should budget for it rather than be surprised by it. The practical deliverable is
the same shape as the [task-orthogonal routing
test](2026-06-12-task-orthogonal-minimal-leakage.md): a pre-flight check on the
*structure of the domain*, not a bet on the *size of the model*.

## Open sub-questions (the testable surface)

- Can the **residual** be measured cheaply enough, per domain, to use as an
  ex-ante routing signal — before committing a learning machine to that domain?
- Is the gap monotone in the way the thesis assumes, or are there large-gap
  domains where cheap faithful verification is provably impossible (so the
  arbitrage is structurally unavailable)?
- Where does a domain sit when the residual is *shrinking over time* (better
  simulators arriving)? The thesis predicts AI's payoff should rise in lockstep
  with the residual falling — that co-movement is itself a measurable test.

**Anti-signal.** If, across realistic domains, AI's observed payoff shows **no
relationship** to any cheap proxy for the faithful-simulation gap — if large-gap
and small-gap domains are indistinguishable in where AI wins — then this framing
adds nothing over "bigger models win sometimes," and should be dropped.
