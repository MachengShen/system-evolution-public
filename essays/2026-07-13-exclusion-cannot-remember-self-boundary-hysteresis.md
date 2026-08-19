# Exclusion Cannot Remember — why a Φ-argmax self-boundary needs a state→coupling term, and how to kill the idea

Date: 2026-07-13 (published 2026-08-19, with a 2026-08-19 addendum)

Public index: [Theory Mainline](../THEORY.md) · Format: [Claim-Receipt](../CLAIM-RECEIPT.md)

> **Cognitive state:** 🟡 speculative (step 4, the bet) on top of 🟢 steps 1–3 · **Confidence:** 0.55 for "self-boundary theories need a state→coupling (self-seal) term"; the weaker causal reading κ=κ(s) only — no self-model implied · provenance: reasoned note; four pillar references in hand; **the in-silico gain-g demo was later run (mu-boundary D2, 2026-07-28) and the specificity control removed half the story — see addendum** · **evidence:** Friedman et al. 2010 PLoS One (neural inertia survives pharmacokinetic control); Kim, Moon, Mashour, Lee 2018 PLoS Comput Biol ("adaptive feedback" hysteresis); mu-boundary D2 (hysteresis emerges from a precision gate with a=0, but an identically gated disturbance channel shows identical hysteresis) · **prior-art:** Tononi & Koch 2015 Phil Trans R Soc B (boundary bifurcation at critical coupling — *not* claimed here as new); Rosas et al. 2020 causal blankets; IIT exclusion postulate. **Known counterexample to step 4 (recorded 2026-07-13):** ordinary multistability under *fixed* coupling can also yield range-hysteresis because Φ depends on state, so self-seal is sufficient-not-necessary unless the loop-width is shown to scale with the feedback gain g and vanish at g=0.

Cross-domain mappings are tagged **[已证] / [推断] / [韵脚]**. Anything I could not verify is marked **未核实** and is not used as evidence.

---

## 1. The claim

One claim, four steps:

1. **IIT's exclusion postulate defines the self-boundary as an argmax of Φ over candidate subsets.**
2. **argmax is a memoryless function. Exclusion therefore contributes zero memory: on its own it can produce a bifurcation of the boundary, but it cannot produce hysteresis.**
3. **Consciousness-state transitions empirically *do* show hysteresis, and the pharmacokinetic explanation has been experimentally excluded** (neural inertia; Friedman et al. 2010).
4. **Therefore any theory of the self-boundary must add a term that IIT does not have: the system's own state feeding back onto its coupling, κ = κ(s). That term is self-sealing.**

Step 4 is the bet. Steps 1–3 I take to be secure. The purpose of this note is to state the bet precisely enough that it can be killed, and to say exactly what would kill it (§6).

**What this note is not claiming.** Not that the boundary bifurcates at a critical coupling — Tononi & Koch published that in 2015, verbatim (§7). Not that hysteresis in consciousness is news — anesthesiology has called it neural inertia for fifteen years. The only claim is the *joint*: that the argmax criterion and the hysteresis are formally incompatible, that nobody appears to have noticed, and that the repair has a measurable signature.

---

## 2. Scope discipline: two boundaries, and this note is about only one

Almost every discussion of "the boundary of the self" slides between two objects. They dissociate, so they must be kept apart.

- **(I) The causal / constitutive boundary.** Which physical stuff actually composes one causally integrated system. This is IIT's *complex*; it is what anesthesia moves; it is what a coupled cell collective has.
- **(II) The represented boundary.** The line the system's *own model* draws around "me". This is the body schema, the self-model, the μ of the projection-consistency notes.

**This note is about (I), throughout.** The dissociation is clean in both directions: somatoparaphrenia moves (II) while (I) is untouched (the disowned hand is still causally attached); general anesthesia moves (I) with no interesting story about (II). The rubber-hand illusion (Botvinick & Cohen 1998, *Nature* 391:756) and tool incorporation into the body schema (Iriki, Tanaka & Iwamura 1996, *NeuroReport* 7:2325–2330) are (II)-only and are **not evidence for or against anything below.** I will not use them.

I will also **not** use LSD ego dissolution as support — on the record, not in a footnote, because the temptation is strong and the direction is wrong: ego dissolution correlates with *increased* global functional connectivity (Tagliazucchi et al. 2016, *Current Biology* 26(8):1043–1050). "The self dissolves" there means *more* integration, not a shrinking complex. It rhymes with boundary collapse and it is not boundary collapse. **[韵脚 — rejected]**

Why the split matters to the claim: self-sealing has a **weak (causal) reading** — the integrated system's state controls its own coupling, κ = κ(s), no self-model required — and a **strong (representational) reading** — the self-*model* μ controls the coupling. §5 shows the hysteresis argument licenses **only the weak reading**.

---

## 3. The argmax argument

Set it up minimally. Let *U* be a substrate of units, *s* its micro-state, and *T* its transition mechanism (the TPM). Let κ be a coupling parameter set from outside — callosal efficacy, anesthetic effect-site concentration, gap-junction conductance — so that *T* = *T*(κ).

IIT's exclusion postulate (Oizumi, Albantakis & Tononi 2014, *PLoS Comput Biol* 10(5):e1003588; restated in IIT 4.0, Albantakis et al. 2023, *PLoS Comput Biol* 19(10):e1011465) says: of all overlapping candidate subsets, exactly one exists as a subject — the one of maximal irreducibility. So the boundary is

> **B = X\*(s, κ) := argmax over Z ⊆ U of φ<sub>s</sub>(Z ; s, T(κ))**

**X\* is a function.** It takes (s, κ) and returns a subset. It has no internal state, no tape, no dependence on how (s, κ) was reached. This is not a criticism of IIT's execution; it is what the postulate *says*. Exclusion is a **selection rule**, not a **dynamical law**. **[已证 — this is definitional, not an inference]**

Now define hysteresis properly. Run κ quasi-statically down and back up: κ<sub>hi</sub> → κ<sub>lo</sub> → κ<sub>hi</sub>. There is boundary hysteresis iff, at some κ visited on both legs, the boundary differs between the legs.

**Lemma.** Under exclusion, boundary hysteresis at κ requires state hysteresis at κ: *s*<sub>down</sub>(κ) ≠ *s*<sub>up</sub>(κ), *and* those two states must have different argmax subsets.

**Corollary — the load-bearing one.** *Exclusion imports all of its memory and manufactures none.* Whatever path-dependence the boundary shows is inherited wholesale from the substrate's dynamics d*s*/d*t*, about which **IIT says nothing**. IIT specifies *X\**; it does not specify d*s*/d*t*. Tononi & Koch's own phrasing gives this away — the complex "may expand, shrink and even move within a given brain **depending on various conditions**" (2015). The conditions are exogenous. There is no term in the theory by which the complex acts on the conditions of its own complex-hood.

So there is a **structurally empty slot in IIT: the dynamics of the boundary.** Not an unfinished calculation — an absent law. And the empirical hysteresis is a constraint on precisely that absent law.

Two further things fall out of the same observation and are worth one line each:

- Under the standard reading — κ exogenous, and the fast dynamics at fixed κ settling to a unique attractor *a*(κ) — we get B = X\*(*a*(κ), κ), a **function of κ**. Bifurcation: available. Hysteresis: **impossible**. This is the pure-exclusion prediction, and it is falsified (§4).
- Exactly at the critical coupling, φ values of competing candidate subsets converge — that is what "critical" means here. But argmax is ill-defined under ties, and Hanson & Walker 2023 (*Neuroscience of Consciousness* 2023(1):niad014) have already shown that published Φ values are "selected arbitrarily from a multitude of equally valid alternatives." **The theory is least well-defined exactly in the regime where its most interesting prediction lives.** I flag this and move on; it is a separate wound.

---

## 4. The hysteresis is real, and it is not pharmacokinetics

The empirical fact is called **neural inertia**: emergence from anesthesia occurs at a *lower* drug concentration than the one at which induction occurred. Same drug, same concentration, two stable states, depending on which way you came.

The obvious deflationary explanation is pharmacokinetic — the drug is still in the tissue on the way out, so the "same concentration" isn't the same concentration. **This has been ruled out.** Friedman, Sun, Moore, Hung, Meng, Perera, Joiner, Thomas, Eckenhoff, Sehgal & Kelz 2010 (*PLoS One* 5(7):e11903) showed that **single-gene mutations affecting sleep–wake regulation narrow or widen the hysteresis loop while leaving anesthetic uptake, distribution and metabolism unchanged.** A loop width that is under genetic control of the arousal system, and not under control of the drug's kinetics, is a property of the *neural* dynamics. The effect is conserved from *Drosophila* through mouse. **[已证]**

Apply the four-part test for genuine hysteresis (coercivity / bistability at fixed field / path-dependent loop / remanence). Neural inertia passes all four: sub-threshold concentration changes don't flip the state; the same concentration supports either state; the in-path differs from the out-path; and the anesthetized state persists as the drug falls below its own induction threshold. This is a **latch**, in the strict sense: a multistable system with a switching threshold and memory. Linear systems cannot do this.

**Guard, stated explicitly:** the fact that anesthesia satisfies the same formal criteria as any other latch does **not** license transporting the mechanism to other latches (habit, 习气, magnetization). Same abstraction, different substrate; ferromagnetism is a *sibling* of this phenomenon, not its source. Any such transport here would be **[韵脚]** and I am not making it.

Kim, Moon, Mashour & Lee 2018 (*PLoS Comput Biol* 14(8):e1006424) went after the mechanism and found two things I need:

1. Their proposed mechanism is an **"adaptive feedback process"** in the network — i.e. **the network's state modulating its own effective coupling.** They wrote down the term. They did not connect it to the question of *what the subject is*, because nobody has asked exclusion to explain hysteresis.
2. **The hysteresis shows up in the connectivity pattern, not in EEG power.** This matters enormously for §6, and it is the single most encouraging fact I have: the memory is **structural**, not merely intensive.

---

## 5. What must be added: κ = κ(s)

Take the substrate law seriously. The standard reading is:

> d*s*/d*t* = F(*s* ; κ),  κ exogenous.

The repair is one term:

> d*s*/d*t* = F(*s* ; κ),  **κ = κ<sub>ext</sub> + g · h(*s*)**

The system's own state sets a part of its own coupling, with **gain g**. The attractor condition then becomes a self-consistency equation,

> *a* = A( *a* ; κ<sub>ext</sub> + g·h(*a*) )

which generically has **multiple solutions at the same κ<sub>ext</sub>**, and whose solution branches trace a loop under a quasi-static sweep. This is the same fixed-point structure as μ = F(μ) in the projection-consistency line, now with the boundary's own coupling as the fixed-point variable rather than the projection.

**This is what self-sealing *is*, stated as a term rather than as a metaphor:** the boundary state acts on the coupling that constitutes the boundary. In cancer that action is literal and physical — closing gap junctions, downregulating MHC-I — and no self-model is needed for it **[推断]**. In anesthesia the candidate physical carrier is the arousal/neuromodulatory circuitry, which both *is part of* the integrated system and *sets* that system's effective coupling **[推断 — the biological identification of κ's controller is an assumption, not a finding]**.

The payoff of writing it this way is that **self-sealing acquires a number**: the gain **g**. And the term makes a monotone prediction the alternatives do not:

> **Loop width is a monotonically increasing function of g, and vanishes at g = 0.**

That is not a rhyme. That is a curve someone can measure. Everything below is about whether it is the *right* curve.

**Honest downgrade, and this is the important one:** the hysteresis licenses the **weak (causal) reading** of self-sealing — κ = κ(s) — and *nothing more*. It does **not** license the strong reading in which a self-*model* μ steers the boundary. Neural inertia in a fly is not evidence of a fly self-model. The strong reading needs its own evidence and does not get to ride on this.

---

## 6. What would kill this

The claim has two joints, and the first one is *thin*. I am putting it in the body, not in a footnote, because the note is worth more as an honest fork than as a defended thesis.

### 6.1 The thin joint: level vs. extent

Every scalar in this literature measures the **level of integration**, not the **extent of the boundary**. PCI (Casali et al. 2013, *Sci Transl Med* 5(198):198ra105) is a scalar; it separates conscious from unconscious states beautifully and it does not tell you *which regions are in the complex*. φ is a scalar. Neural inertia, as measured, is hysteresis **in a scalar**.

But the claim needs hysteresis **in an argmax — in a set.**

So the competing explanation, stated at full strength: **ordinary neural multistability produces hysteresis in the level of integration, while the *extent* of the complex continues to track current coupling memorylessly.** On that story, exclusion survives completely intact, there is no need for any κ = κ(s) term, and this note is about nothing. Nobody has ever measured the extent of a complex in a brain — the exact-Φ ceiling is on the order of 8–12 binary units, so it is not merely unmeasured but currently unmeasurable head-on. **There is at present zero direct evidence of hysteresis in boundary extent.**

Kim 2018's finding that the hysteresis lives in *connectivity pattern* and not in *power* is the right direction — extent is a structural property, and a structural memory is the kind of memory that could be a memory of extent. It is not sufficient. Connectivity pattern is not complex membership.

**The decisive test, and it can be run on data that already exists:**

> **Test E (matched-level extent test).** In induction/emergence recordings, find pairs of time points — one on the induction leg, one on the emergence leg — matched on **(i)** effect-site drug concentration *and* **(ii)** global integration level (PCI, or a Φ-surrogate). Matching on (ii) is the whole trick: it subtracts out the level hysteresis and isolates extent. Now ask whether the **membership** of the maximally-integrated core differs between the legs. Use a computable surrogate for membership — the ΦID synergistic-core methodology is the obvious candidate (Luppi, Mediano, Rosas et al. 2022, *Nature Neuroscience* 25(6):771–782).
>
> - **Core membership differs at matched concentration and matched level → extent-hysteresis is real → premise 3 holds at the level the argument needs.**
> - **Core membership is identical whenever level is matched → the entire hysteresis lives in level, the boundary is a memoryless function of current coupling, exclusion is untouched, and this note is dead.**

I want to be very clear that I expect this test to be the one that decides it, and that I do not know which way it goes.

### 6.2 The second joint: feedback vs. plain multistability

Suppose Test E comes back positive: extent really does remember. There is *still* a null hypothesis that does not need self-sealing. A recurrent network with **fixed** coupling can be multistable, and two attractors at the same fixed κ can in principle have different argmax subsets. That gives extent-hysteresis with **no state→coupling feedback at all.**

Friedman 2010 does **not** discriminate here, and I want to say so plainly because it is tempting to claim that it does. Their sleep-mutant genes could be changing the *depth of the intrinsic attractor wells* (the null) just as easily as the *gain of a coupling-control pathway* (the claim). Friedman kills pharmacokinetics. It does not kill plain multistability.

> **Test F (open-loop coupling clamp).** Drive the candidate coupling-controller open-loop — clamp the neuromodulatory arousal drive so that it *cannot* respond to cortical state — while sweeping the anesthetic through a full up-down cycle. Then sweep g by graded clamping.
>
> - **Loop width collapses toward zero as the loop is opened, and is monotone in g → self-sealing.**
> - **Loop width survives the clamp → plain multistability; the κ = κ(s) term is unnecessary; the second half of the claim dies.**
>
> The in-silico version is cheap and should be done first: a network model with an explicit gain g from mean state onto coupling, exact-Φ small enough for PyPhi, sweeping κ<sub>ext</sub> up and down, reporting **loop width in the argmax *set* as a function of g.** This simultaneously tests both joints and costs a weekend of CPU. *(Not run. This note contains no computation.)*

### 6.3 Third kill, the cheapest of all

If anyone reproduces the empirical hysteresis loop in a model with a **fixed TPM, exogenous κ, and pure argmax** — no added feedback term — the claim is dead on the spot, no experiment required.

### 6.4 Summary of what survives each kill

| Killed by | What dies | What survives |
|---|---|---|
| Test E negative (extent memoryless) | Everything in this note | — |
| Test F negative (clamp doesn't collapse loop) | Self-sealing as the *required* term | §3: exclusion is memoryless, IIT still owes a boundary dynamics |
| §6.3 (pure-argmax model reproduces the loop) | Everything | — |

Note the asymmetry: **§3 is much harder to kill than §5.** The observation that exclusion is a memoryless selection rule and therefore cannot be a theory of boundary *motion* stands regardless of what fills the slot. If I had to defend one sentence, it would be that one.

---

## 7. Relation to existing work — including what is not mine

**The bifurcation half is Tononi & Koch's, and it is theirs verbatim.** Tononi & Koch 2015, *Phil Trans R Soc B* 370(1668):20140167:

> *"if the efficacy of the 200 million callosal fibres through which the two cerebral hemispheres communicate with each other were reduced progressively, there would be a moment at which, for a minimal change in the traffic of neural impulses across the callosum, there would be an all-or-none change in consciousness: experience would go from being a single one to suddenly splitting into two separate experiencing minds."*

and

> *"IIT also predicts that the NCC is not necessarily fixed, but may expand, shrink and even move within a given brain depending on various conditions."*

That is a boundary, moving, all-or-none, at a critical coupling, published in 2015. **I am adding nothing to it and I claim nothing about it.** **[已证]** (Two honest riders: no one appears to have ever *numerically demonstrated* this — the assertion exists, the parameter sweep does not; and its flagship empirical case is now contested, since Pinto et al. 2017, *Brain* 140(5):1231–1237, report above-chance cross-field performance in complete callosotomy patients — "divided perception but undivided consciousness." So do not lean on split-brain.)

**The feedback term is Kim et al.'s.** They named the mechanism "adaptive feedback" in 2018. What they did not do — because nobody asked exclusion to account for hysteresis — is connect it to the question of *what the subject is*. **That interface is what this note supplies, and it is the only thing it supplies.**

**The formalism for history-dependent boundaries already exists.** Rosas, Mediano, Biehl, Chandaria & Polani 2020, "Causal blankets: Theory and algorithmic framework" (arXiv:2008.12568) show that real coupled systems do *not* satisfy instantaneous conditional independence, and that the correct blanket must be conditioned on **sensorimotor history**. A boundary defined on history is, definitionally, a boundary with memory. So: **exclusion (memoryless argmax) and causal blankets (history-dependent) sit on opposite sides of exactly the question this note is about**, and one of them has to give. **[已证 as a statement about their theorem; 推断 that causal blankets are the right home for the repair]**

Why exclusion deserves this much attention at all: it is the only boundary criterion on offer that is *derived* from the system's own dynamics rather than *stipulated* by a modeler. Friston-style Markov blankets are stipulated (Bruineberg, Dołęga, Dewhurst & Baltieri 2022, *Behavioral and Brain Sciences* 45:e183). Krakauer et al. 2020 ("The Information Theory of Individuality", *Theory in Biosciences*; volume/pages **未核实**) offer a different derived functional, but one predicting *graded* individuality rather than an all-or-none boundary, with no application to any real system that I could find. **Exclusion is the strongest available answer to "what sets the boundary" — which is precisely why its inability to answer "how does the boundary move" is worth a paper.**

---

## 8. The one-sentence version

> **IIT tells you where the subject *is*. It has no term that tells you how the subject *sticks*. Anesthesia proves the subject sticks. The missing term is the subject's grip on its own coupling — and its width is measurable.**

---

## Appendix: honesty ledger

**Unverified / not used as evidence:** Krakauer et al. 2020 volume and pages; the first-report literature on somatoparaphrenia (mentioned in §2 only for the dissociation, not as support); early Tononi split-brain Φ numerics (widely quoted, original source not located).

**Explicitly refused rhymes:** ego dissolution as boundary collapse (direction reversed — connectivity *increases*); 习气 / magnetization as sharing a mechanism with neural inertia (they share an abstraction — bistability + threshold + memory — and nothing else); the WITNESS/INSTRUMENT two-layer distinction (both (I) and (II) live inside the instrument layer; that split is unrelated and is not being merged in).

**Biggest self-doubt:** §6.1. Everything the argument needs turns on hysteresis being in the *extent* of the boundary, and every measurement in existence is of the *level* of integration. Kim 2018's connectivity-pattern result points the right way and does not close it. **If Test E comes back negative, the note is worth nothing and should be discarded rather than defended.**

**Zero computation was performed for this note.** All four load-bearing results are already in the literature. The contribution is the join, the fork, and the kill conditions.

---

## Addendum 2026-08-19 — what happened when we tried to kill it

- **§6.2 demo was run** as `mu-boundary` D2 (MuJoCo 3R arm, precision gate, no hand-built cubic term): rate-independent hysteresis **does emerge** (A₀ = +0.19…+0.28 = 24–35× the protocol resolution floor; frozen-gate control falls back to the floor). **But** the specificity control — the same gate on the wind-driven disturbance ball with loop gain flattened to match — produces **bit-identical hysteresis**. Hysteresis is a generic property of a gated slow variable; self-specificity enters only through the measured Δπ difference, which is small enough (1–3 % relative precision) to require fine-tuning. The §5.7 time-constant asymmetry prediction was **falsified** (τ_off/τ_on = 1.008; 0.794 in the opposite direction when the gate multiplies the whole drive). Full numbers: [RESULTS-D1-D2](2026-08-19-mu-boundary/RESULTS-D1-D2.md).
- **Human-data anchor did not stand up either**: rubber-hand-illusion order effect (OSF `bsfwu`, Tsuji & Imaizumi Exp2, N=185) is on the **adaptation** side (d = −0.76), opposite to hysteresis, and measures expectancy rather than lived ownership; trial-level synchrony-judgment sequential dependence is robust but task-dependent in sign and dies by lag-3 (short tail, not a latch). [RESULTS-bsfwu-order](2026-08-19-mu-boundary/human-reanalysis/RESULTS-bsfwu-order.md) · [RESULTS-sync-dryrun](2026-08-19-mu-boundary/human-reanalysis/RESULTS-sync-dryrun.md). The only hard human anchor remains anesthetic neural inertia.
- **Consequence for the bet:** first-order hysteresis cannot carry the self-specific claim. The line has moved to a *second-order* signature — active defense/repair of the boundary definition — pre-registered in [Boundary-Defense pre-registration](2026-08-19-boundary-defense-preregistration.md) (running as of 2026-08-19).
