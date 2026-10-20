# Empty of Intrinsic Order, Non-Void in Constraint

## Indefinite causal order, self-referential boundary conditions, and the thermodynamic ledger of predictive intervention

> [!NOTE]
> **Status**: public theory note v1.0 (2026-10-19), System Evolution theory mainline. English edition written for theoretical physicists, quantum-foundations researchers, stochastic thermodynamicists and mathematical systems theorists. It is stricter than the [Chinese edition](2026-10-19-emptiness-causality-intervention-ledger-zh.md). Where the two differ, this edition wins; §5 lists the corrections.
>
> **Epistemic grading** (every claim carries one tag):
> **[Theorem]**: a published or directly provable result, stated with its hypotheses.
> **[Structural Isomorphism]**: an exact mathematical correspondence. The cross-domain *interpretation* is ours.
> **[Falsifiable Hypothesis]**: a claim with a stated kill condition (§4).
> **[Heuristic Metaphor]**: a communication aid that carries no proof burden.

---

## 0. The Counter-Intuitive Hook & Thesis in Three Lines

**Why this is surprising (plain-language overview).** Everyone—including Einstein—instinctively treats strict cause-and-effect as the unshakeable bedrock of reality: Event $A$ happens before Event $B$, and the past pushes the future like a rigid row of dominoes. Yet foundational physics over the past decade has quietly overturned this picture. In tabletop quantum optics (the *quantum switch*), photons traverse two operations in a superposition of "$A$ before $B$" and "$B$ before $A$"; in Wheeler–DeWitt quantum cosmology, the universe as a whole has no external clock at all. Causal order is not built-in hardware—it is an emergent, relational pattern, strikingly close to what Buddhist Madhyamaka philosophy called *dependent origination and emptiness of intrinsic nature* (*pratītyasamutpāda* & *śūnyatā*).

**The second surprise.** If strict causal order isn't fundamental, does that mean "anything goes"—or that an observer can peek ahead and rewrite outcomes ("steer fate") for free? **The exact opposite.** Dissolving a rigid causal timeline replaces "A pushes B" with an unyielding **global consistency and thermodynamic balance sheet**. When an external agent predicts a trajectory and forces a counterfactual outcome, the entropy cost lands squarely on the intervener, network stress concentrates right at the intervention point, and clamping a trajectory against the natural flow burns continuous housekeeping heat—whereas reshaping the underlying potential landscape avoids that perpetual tax.

### Formal summary in three lines

1. Process-matrix theory shows that *which event comes first* need not be an intrinsic property of events. The validity constraints (positivity, normalization, and a fixed linear subspace) stay rigid. In short: **empty of intrinsic order, non-void in constraint.**
2. An agent that predicts a system and then acts on it is running a measure–feedback–erase loop. Stochastic thermodynamics puts a price on that loop, and the price can be **booked to a party other than the beneficiary.**
3. In overdamped dynamics, the **non-gradient part** of an actuation field is exactly the part that dissipates beyond the optimal-transport bound. At steady state it is the housekeeping heat. On a graph, the same object is the cokernel residual $r_\perp$, and its cycle circulations are Schnakenberg's affinities. *Reshaping the landscape* is the gradient part. *Clamping the state* generically is not.

**Use of traditional vocabulary.** We read Nāgārjuna's *pratītyasamutpāda* / *śūnyatā* (Mūlamadhyamakakārikā, MMK), the *Daodejing*'s "produce without possessing, act without presuming, lead without dominating" (生而不有，为而不恃，长而不宰), and Yuan Liaofan's sixteenth-century *Four Lessons* as **historical compressions**: lossy encodings of relational and thermodynamic constraints, made by people who had no formalism. We do not claim that they anticipated any of the mathematics. We claim that a few of their structural distinctions survive translation, and we mark exactly which ones.

---

## Part I — Ontology: indefinite causal order, relational QM, and the non-voidness of emptiness

### 1.1 Process matrices [Theorem]

Consider two local laboratories $A, B$ with input and output spaces $\mathcal H^{A_I},\mathcal H^{A_O},\mathcal H^{B_I},\mathcal H^{B_O}$. Each local operation is a quantum instrument whose elements have Choi operators $M^{a}_A \in \mathcal L(\mathcal H^{A_I A_O})$, $M^a_A \ge 0$. The sum $\sum_a M^a_A$ is the Choi operator of a CPTP map: $\mathrm{Tr}_{A_O}\sum_a M^a_A = \mathbb 1_{A_I}$. Oreshkov, Costa and Brukner (2012) assume only that local quantum mechanics holds in each laboratory. They show that all bilinear, consistent probability rules take the form

$$
p(a,b) = \mathrm{Tr}\!\left[W\,(M^a_A\otimes M^b_B)\right],\qquad W\in\mathcal L(\mathcal H^{A_IA_OB_IB_O}),
$$

with validity conditions

$$
W \ge 0,\qquad \mathrm{Tr}\!\left[W\,(M_A\otimes M_B)\right]=1\quad\forall\ \text{CPTP Choi operators } M_A, M_B .
$$

(We suppress the transpose convention.) The equality condition is equivalent to $\mathrm{Tr}\,W = d_{A_O}d_{B_O}$ together with $W = L_V(W)$. Here $L_V$ is a fixed projector onto a linear subspace built from trace-and-replace maps (Araújo et al. 2015). The valid set is therefore

$$
\mathcal W = \mathrm{PSD}\ \cap\ \mathcal A,\qquad \mathcal A = \{W : L_V(W) = W,\ \mathrm{Tr}\,W = d_{A_O}d_{B_O}\}.
$$

A bipartite $W$ is **causally separable** if $W = q\,W^{A\prec B} + (1-q)\,W^{B\prec A}$ with $q\in[0,1]$, where each term is a valid process compatible with the stated order. Otherwise $W$ is **causally non-separable**, and non-separability can be certified by causal witnesses (Araújo et al. 2015).

The **quantum switch** (Chiribella, D'Ariano, Perinotti, Valiron 2013) applies $U_A,U_B$ to a target in an order set by a control qubit:

$$
\tfrac{1}{\sqrt2}\big(|0\rangle_c\,U_BU_A|\psi\rangle + |1\rangle_c\,U_AU_B|\psi\rangle\big).
$$

The switch is causally non-separable and has been implemented photonically (Procopio et al. 2015; Rubino et al. 2017). Two caveats matter later. First, the switch **cannot** violate a causal inequality; OCB's original inequality-violating process has no known physical implementation. Second, no valid process permits signalling that would break the normalization above for any choice of local CPTP maps.

**Quantum reference frames.** Castro-Ruiz, Giacomini, Belenchia and Brukner (2020) show that when clocks or gravitating sources are in superposition, the *temporal localisation* of an event is relative to a quantum reference frame. They also construct changes of frame between such descriptions. We use only the weak consequence: a change of description implemented by a map that sends valid processes to valid processes preserves the probability rule by construction. *Order* can be frame-relative. *Validity* is not.

### 1.2 The isomorphism with śūnyatā [Structural Isomorphism]

The exact content is three mathematical facts:

| Madhyamaka | Process-matrix fact |
|---|---|
| *niḥsvabhāvatā*: no own-being | Causal order is not fixed by local data. The same local instruments embed in both separable and non-separable $W$, and non-separable $W$ exist. Order is a property of a decomposition of the global $W$. |
| *pratītyasamutpāda*: arising in dependence (MMK 24.18) | Statistics $p(a,b)$ exist only as the joint contraction of $W$ with *both* local instruments. Neither side alone defines an outcome distribution over the pair. |
| the middle way: not nihilism | The constraint set $\mathcal A$ and positivity are fixed independently of any particular $W$. Normalization holds for every local choice. Nothing is "anything goes." |

So **"empty of intrinsic order, yet non-void in relational constraint"** is a precise sentence: order is absent as an intrinsic property, and the affine set $\mathcal A$ is invariant. The interpretation (that this two-sided negation is the one Madhyamaka makes) is ours. The isomorphism **breaks** at one identifiable point. Physics treats $\mathcal A$ as fundamental, while Madhyamaka would deny own-being to the constraint set as well. That break is the subject of §1.3.

### 1.3 Relational QM and the emptiness of emptiness [open problem]

In relational quantum mechanics (Rovelli 1996), the values of variables are defined only relative to other physical systems. Rovelli explicitly invokes Nāgārjuna (*Helgoland*, 2020). Adlam and Rovelli (2022) add **cross-perspective links (CPL)**: if Alice measures variable $V$ of $S$, and Bob later measures the corresponding variable of Alice's record, Bob's outcome matches Alice's. The purpose is to secure intersubjective agreement and avoid perspectival solipsism.

The second-order tension is sharp. MMK 13.8: *"The victorious ones have said that emptiness is the relinquishing of all views. Those for whom emptiness is a view are said to be incurable."* The Prajñāpāramitā lineage names this *śūnyatā-śūnyatā*, the emptiness of emptiness. CPL postulates a law-like, perspective-transcending regularity about relations. The question is whether that **reifies the relation** that Madhyamaka empties.

There are two readings:

- **(a) CPL as constraint.** CPL is a constraint on relations, playing the role $\mathcal A$ plays for process matrices. RQM then sits exactly where process matrices sit: relational content plus invariant constraint. The Madhyamaka reply is that the constraint is conventionally valid (*saṃvṛti*) but not ultimately so (*paramārtha*). Physics has no counterpart to that distinction.
- **(b) Derived constraints.** Physics might take the second-order step itself, by deriving the validity constraints from something weaker so that they become relative to a meta-description. Operational reconstructions of process theories move partway in this direction.

**Precise question.** Is there a predictive framework in which the validity constraints (the analogue of $\mathcal A$, or of CPL) are themselves frame-relative, and which still yields frame-independent, testable statistics? We do not know the answer. We list this as an open problem, not as an isomorphism.

### 1.4 Time and causal power as conditional or coarse-grained [Theorem + Structural Isomorphism]

**Page–Wootters (1983) [Theorem].** Let $\hat H = \hat H_C\otimes\mathbb 1 + \mathbb 1\otimes\hat H_S$ with $\hat H|\Psi\rangle\rangle = 0$, and clock states $|t\rangle_C = e^{-i\hat H_C t}|0\rangle_C$. Then

$$
|\psi_S(t)\rangle \propto \langle t|_C\,|\Psi\rangle\rangle \quad\Longrightarrow\quad i\hbar\,\partial_t|\psi_S(t)\rangle = \hat H_S|\psi_S(t)\rangle .
$$

The global state is stationary, and Schrödinger evolution is the conditional projection onto clock readings. Ideal clocks need a continuous spectrum. Realistic versions use covariant POVMs (Giovannetti–Lloyd–Maccone 2015; Höhn–Smith–Lock 2021). A tabletop demonstration is given by Moreva et al. (2014).

**Causal emergence (Hoel–Albantakis–Tononi 2013) [Theorem, definitional].** For a transition matrix $T$, $EI(T) = I(X;Y)$ with $X$ drawn from the uniform (maximum-entropy) intervention distribution $do(X)$ and $Y\sim T(\cdot|X)$. Coarse-grainings exist with $EI(\text{macro}) > EI(\text{micro})$, because coarse-graining can remove degeneracy and noise. Critics point out that the uniform intervention measure is a choice. Our reading [Structural Isomorphism] is that **causal power is defined relative to a description scale**, which is dependent arising one level up. The criticism strengthens this reading rather than weakening it.

---

## Part II — Self-referential boundary conditions and a thermodynamic reading of the Fermi paradox

### 2.1 Multi-axis credit transport and the self-boundary [Falsifiable Hypothesis]

The May 2026 mainline treats *Sheng* (生, "generation") as a **recursive generative operator** acting on a product of independent axes (time, space, scale, agent, goal). Single-axis autoregression is its one-dimensional projection. Learning requires **credit transport**: routing each loss-relevant signal to a modifiable variable along some axis.

**H1.** Suppose credit closure is complete over an axis set that includes the channel through which the agent's own boundary (its initialization, architecture, objective) was set. Then the minimal sufficient world model contains a representation of that boundary origin. The formal kernel is close to a tautology: if the boundary is loss-relevant and closure is required, credit has to land on a variable that represents it. The substantive, falsifiable claim is empirical. It says that the representation appears with **threshold behaviour** as independent credit axes are added (kill criterion K6a).

### 2.2 Boundary conditions at both ends [Theorem]

**Two-state vector formalism.** Aharonov, Bergmann and Lebowitz (1964) gave the time-symmetric rule for an intermediate *strong* measurement between pre-selection $|\Psi\rangle$ and post-selection $\langle\Phi|$:

$$
P(a_j) = \frac{|\langle\Phi|\Pi_j|\Psi\rangle|^2}{\sum_k|\langle\Phi|\Pi_k|\Psi\rangle|^2}.
$$

The **weak value** comes from Aharonov, Albert and Vaidman (1988):

$$
A_w = \frac{\langle\Phi_{\text{future}}|\hat A|\Psi_{\text{past}}\rangle}{\langle\Phi_{\text{future}}|\Psi_{\text{past}}\rangle}.
$$

The past and future boundaries enter symmetrically. Anomalously large $|A_w|$ requires small post-selection probability $p_{\text{post}} = |\langle\Phi|\Psi\rangle|^2$ (for trivial intermediate dynamics).

**Deutsch CTCs (1991).** The chronology-violating system must satisfy

$$
\rho_{\text{CTC}} = \mathrm{Tr}_S\!\left[U(\rho_S\otimes\rho_{\text{CTC}})U^\dagger\right]\equiv\Phi(\rho_{\text{CTC}}).
$$

$\Phi$ is CPTP, hence continuous, on the compact convex set $\mathcal D(\mathcal H_{\text{CTC}})$. In finite dimension Brouwer's theorem guarantees a fixed point; Schauder's theorem extends this under compactness assumptions. Consistent solutions therefore always exist. They are generally not unique, and the induced map on $\rho_S$ is nonlinear.

**P-CTCs (Lloyd, Maccone, Garcia-Patron, Giovannetti, Shikano 2011)** are a *different* model, not a fixed-point model. P-CTCs use post-selected teleportation. The effective map is $\rho_S\mapsto C\rho_SC^\dagger/\mathrm{Tr}(C\rho_SC^\dagger)$ with $C=\mathrm{Tr}_{\text{CTC}}U$. It is undefined when $C\rho_SC^\dagger = 0$; in this model the grandfather paradox shows up as a probability-zero branch. The Deutsch and P-CTC models disagree in general.

**Price of selecting a future [Theorem].** Take a classical or quantum thermal protocol that starts in equilibrium and obeys Jarzynski's equality $\langle e^{-\beta W}\rangle = e^{-\beta\Delta F}$. Let $E$ be any event with $P(E)=p$. Then

$$
\langle W\,|\,E\rangle \;\ge\; \Delta F - k_BT\ln\frac1p .
$$

*Proof.* $p\,\langle e^{-\beta W}|E\rangle \le \langle e^{-\beta W}\rangle = e^{-\beta\Delta F}$. Jensen's inequality gives $e^{-\beta\langle W|E\rangle}\le\langle e^{-\beta W}|E\rangle$. $\square$

The apparent free-energy gain from conditioning on a future event is therefore capped at $k_BT\ln(1/p_{\text{post}})$. This replaces the heuristic "Landauer cost of discarded branches" in the Chinese edition. Scope: the bound applies when the selection is carried out by a physical, thermodynamically accounted protocol. Abstract post-selection in a P-CTC is not such a protocol. **Self-reference is not free: the more sharply you specify the future boundary, the less it can pay.**

### 2.3 Seeded, then left alone: observability vs controllability [Structural Isomorphism]

The June 2026 note *Seeded, Then Left Alone* models a seeded system as $\dot x = f(x) + g(x)u(t)$ with output $y = h(x)$. It separates **observability** (the descendants reconstruct $x_0$, which means reading the past) from **controllability** (the seeder applies $u(t)$, which means writing the future). The two are independent. Non-interference comes in grades:

- **strong**: the seeder sets only $x_0$;
- **weak**: the seeder authors $f$ and then holds $u\equiv0$.

The Daoist line 长而不宰 ("leads without dominating") is the weak grade.

That note argued from ethics and epistemology. Part III supplies the thermodynamic part of the argument, with a correction to the folk version. **It is false that every $u(t)\neq0$ is thermodynamically suboptimal.** A gradient forcing $u=-\nabla V$ is simply a change of Hamiltonian. The correct statement (Result 3) is that the **non-gradient** component of forcing (cycle affinity, curl) carries strictly positive housekeeping heat for as long as it is applied. That component is avoidable when actuation is complete and becomes *forced* when actuation is restricted to a boundary that cannot realise the required gradient. Cross-blanket forcing is costly exactly when it cannot be internalised as a landscape.

**Fermi reading [Falsifiable Hypothesis + Heuristic Metaphor].** Suppose a civilization optimises long-horizon dissipation per unit of influence. Then its preferred mode is to specify boundaries or landscapes and then set $u\equiv0$, rather than to drive its environment persistently with non-gradient forcing. Prediction: its traces lie in *initial conditions and structural selections*, not in active emission. Known weaknesses:

- On cosmic scales, beacons are not obviously large thermodynamic expenses.
- Minimising dissipation may not be the binding objective.
- The hypothesis is compatible with aestivation (Sandberg–Armstrong–Ćirković 2017) and transcension (Smart 2012) and does not single itself out.
- It invites pattern-reading of coincidences as design.

Kill criterion K6b addresses this.

---

## Part III — The thermodynamic ledger of predictive intervention: three results

### Result 1 — Information–work transfer and multi-monotone resource asymmetry

**Setup.** A system $X$ is in contact with a bath at temperature $T$. A demon $D$ measures $X$ into a memory $M$, and the mutual information is $I = I(X;M)$. A feedback protocol benefits agent $A$.

**[Theorem] (Sagawa–Ueda 2008).** With feedback, the extractable work satisfies $W_{\text{ext}}\le -\Delta F + k_BT\,I$. Equivalently, the work saved for $A$ relative to the optimal protocol without feedback is $\langle W^A_{\text{saved}}\rangle \le k_BT\,I(X;M)$.

**[Theorem] (Sagawa–Ueda 2009; Landauer 1961).** In the standard setting where the memory's initial and final free energies coincide, $W^D_{\text{meas}} + W^D_{\text{erase}} \ge k_BT\,I(X;M)$. Hence

$$
\boxed{\ \langle W^A_{\text{saved}}\rangle \;\le\; k_BT\,I(X;M) \;\le\; W^D_{\text{meas}} + W^D_{\text{erase}}\ }
$$

**Ledger split [Structural Isomorphism; exact accounting].** The global second law does not care whose ledger a term is booked to. If $A=D$ (closed self-feedback), the net gain is $\le 0$. If $A\neq D$ (third-party intervention), $A$ receives $\langle W^A_{\text{saved}}\rangle>0$ at zero cost to $A$, and $D$ pays. If $D$ defers erasure, $D$ carries a correlated memory with $I(X;M)>0$: an **open liability** of at least $k_BT\,I$, payable into $D$'s bath when erasure happens. This adds no new theorem. It is the accounting implied by the two theorems above.

**Rényi free energies.** For energy-incoherent states, Brandão, Horodecki, Ng, Oppenheim and Wehner (2015) define

$$
F_\alpha(\rho,\gamma_\beta) = k_BT\left[D_\alpha(\rho\,\|\,\gamma_\beta) - \ln Z\right].
$$

Each $F_\alpha$ with $\alpha\ge0$ is non-increasing under (catalytic) thermal operations, and joint monotonicity is essentially sufficient for catalytic convertibility. Naming: $F_1$ is the ordinary free energy. $F_0$ governs *deterministic extractable work*, the single-shot "min" side. $F_\infty$ governs the *deterministic work of formation*, the "max" side. In the Chinese edition and the task brief, $F_\infty$ was loosely called the "min-free energy"; the correction is recorded in §5.

**Proposition 1 (compensation gap) [Theorem].** An intervention moves $A$ from $\rho$ to $\rho'$, with deficits $\Delta_\alpha = F_\alpha(\rho)-F_\alpha(\rho')$.

- **(i)** Compensation by deterministic work $w$ (a sharp shift of a battery level, which adds exactly $w$ to every $F_\alpha$) can restore $\rho$ only if $w \ge \sup_{\alpha\ge0}\Delta_\alpha$. In particular, paying the **mean deficit $w=\Delta_1$ is insufficient whenever $\sup_\alpha\Delta_\alpha > \Delta_1$.**
- **(ii)** Compensation by a fluctuating resource $\tau$ requires $F_\alpha(\tau)-F_\alpha(\gamma_\tau)\ge\Delta_\alpha$ for all $\alpha$. Because $D_\alpha$ is non-decreasing in $\alpha$, a payment worth $F_1$ "on average" is worth at most that in $F_0$. A payment indexed to its mean is therefore weakest exactly at the guaranteed-work end.

*Proof.* Additivity $D_\alpha(\rho\otimes\tau\|\gamma\otimes\gamma') = D_\alpha(\rho\|\gamma)+D_\alpha(\tau\|\gamma')$, plus monotonicity of every $F_\alpha$ (necessity only). $\square$

**Decoupling [Theorem for the identity; Falsifiable Hypothesis for the reading].** For product Gibbs references, $D(\rho_{XM}\|\gamma_X\otimes\gamma_M) = D(\rho_X\|\gamma_X)+D(\rho_M\|\gamma_M)+I(X;M)$. A residual correlation is therefore a free-energy resource of $k_BT\,I$ that **belongs to neither party alone**. Transfers that act locally on each party cannot remove it. Only operations that consume the correlation can, namely erasure or further feedback. The hypothesis is that "settling" an intervention completely means driving $I\to0$, and that scalar compensation without decoupling leaves a measurable residual (K3).

### Result 2 — Discrete maximum principle on causal graphs and Motter–Lai overload cascades

**Setup.** Let $G=(V,E)$ be connected and oriented, with incidence matrix $B\in\mathbb R^{E\times V}$, where $(B\phi)_e = \phi_u-\phi_v$ for $e=u\to v$. Conductances are $W=\mathrm{diag}(w_e)>0$, and currents are $J = WB\phi$. Conservation $B^\top J=\rho$ gives

$$
L\phi = \rho,\qquad L = B^\top W B .
$$

$L$ is singular (constants span its kernel). An injection must therefore be absorbed somewhere: we inject one unit at $A$ and extract it at a ground $g$, so $\rho=\delta_A-\delta_g$ and $\phi = L^+(\delta_A-\delta_g)$. Then

$$
\phi_A-\phi_g = (\delta_A-\delta_g)^\top L^+(\delta_A-\delta_g) = R_{\text{eff}}(A,g).
$$

**[Theorem] (a) Discrete maximum principle.** $\phi$ is harmonic (a conductance-weighted mean of its neighbours) on $V\setminus\{A,g\}$. Hence $\max\phi=\phi_A$ and $\min\phi=\phi_g$. The maximum is **strict** at every vertex joined to $g$ by a path that avoids $A$. Vertices whose only connection to $g$ passes through $A$ carry $\phi_v=\phi_A$ exactly: **parties that are coupled to the rest of the network only through the source share the source's full potential.**

**[Theorem] (b) The source star.** Every edge incident to $A$ carries non-negative outward current $J_e = w_e(\phi_A-\phi_v)\ge0$, and these currents sum to $1$. So $\max_{e\ni A}J_e \ge 1/\deg(A)$. *Correction to the brief:* unit flux crosses **every** $A$–$g$ cut, not only $A$'s star. The single most-loaded edge need not be incident to $A$. In a high-degree source feeding a bridge, the bridge carries the full unit. The precise senses in which stress concentrates at the source are (a) the potential and (b) the per-edge load $\ge1/\deg(A)$, which is large for weakly connected sources.

**[Theorem] (c) Thomson and Rayleigh.** The flow minimises $\sum_e J_e^2/w_e$, and the minimum equals $R_{\text{eff}}(A,g)$. Adding conductance anywhere, in particular at $A$, can only lower $R_{\text{eff}}$.

**Cascades [Theorem for the model; Falsifiable Hypothesis for applications].** We use a flow-based variant of Motter–Lai (2002); the original model uses shortest-path betweenness load. The baseline flow is $J^{(0)}$ and the capacities are $C_e=(1+\alpha)|J^{(0)}_e|$. An intervention of size $s$ adds $s\hat J$, where $\hat J$ is the unit $A\to g$ flow. Edge $e$ overloads iff $|J^{(0)}_e+s\hat J_e|>(1+\alpha)|J^{(0)}_e|$.

**Proposition 2 (first-failure bound) [Theorem].** The first-overload threshold satisfies

$$
s^\star \;\le\; (2+\alpha)\,\deg(A)\,\max_{e\ni A}|J^{(0)}_e| .
$$

*Proof.* Pick $e\ni A$ with $\hat J_e\ge1/\deg(A)$ (it exists by (b)). If $s\hat J_e>(2+\alpha)|J^{(0)}_e|$, then $|J^{(0)}_e+s\hat J_e|\ge s\hat J_e-|J^{(0)}_e|>(1+\alpha)|J^{(0)}_e|$. $\square$

A **peripheral, weakly coupled source with low local baseline traffic** therefore has a guaranteed early failure in its own neighbourhood, whatever the network looks like elsewhere. After a failure, the failed edge is removed and $L^+$ is updated by a rank-one Sherman–Morrison correction (line-outage distribution factors), and the process iterates into a cascade.

**Reading [Structural Isomorphism].** The folk claim that "backlash concentrates on the practitioner and the practitioner's dependants" corresponds to (a), the dangling-vertex clause, (b) and Proposition 2. We make no claim about any specific folk prediction. The structure is what survives.

### Result 3 — Cokernel residual $r_\perp$ ⇔ Schnakenberg cycle affinity ⇔ housekeeping heat, plus the $\mathcal W_2$ speed limit

#### 3a. Markov jump processes

Take a continuous-time Markov jump process on a finite, irreducible graph, with $k_{uv}>0 \Leftrightarrow k_{vu}>0$. The **edge force** of $e=u\to v$ is $r_e=\ln(k_{uv}/k_{vu})$. The cycle space is $\ker B^\top\subset\mathbb R^E$, and for a cycle $c$ the Schnakenberg (1976) affinity is

$$
\mathcal A(c)=\langle c,r\rangle=\ln\prod_{e\in c}\frac{k_e^{+}}{k_e^{-}} .
$$

The August 2026 cokernel obstruction, at $\gamma=1$ (where $D_1=B$), is the $W$-weighted least-squares residual of $r$ modulo gradients:

$$
r_\perp=\left[I-B(B^\top WB)^+B^\top W\right]r = r-B\phi^\star .
$$

**Proposition 3.1 [Theorem].** For every cycle $c\in\ker B^\top$ and every positive diagonal $W$,

$$
\langle c,r_\perp\rangle=\langle c,r\rangle=\mathcal A(c).
$$

Consequently

$$
r_\perp=0\iff \mathcal A(c)=0\ \ \forall c\iff\text{detailed balance (Kolmogorov)}\iff J_{\text{ss}}\equiv0 .
$$

*Proof.* $r-r_\perp\in\mathrm{im}\,B$ and $\ker B^\top=(\mathrm{im}\,B)^\perp$ in the Euclidean inner product, so cycle circulations of $r$ and $r_\perp$ agree. $r_\perp=0\iff r\in\mathrm{im}\,B\iff r\perp\ker B^\top$. Kolmogorov's criterion identifies the last condition with detailed balance, and detailed balance is equivalent to the vanishing of the stationary current. $\square$

*Precision note.* "Identical" means identical **cycle circulations** and identical vanishing sets. The edge-wise distribution of $r_\perp$ depends on $W$; the affinities do not. For $\gamma<1$ the discounted residual is a different object: it is a reinforcement-learning shaping-irreducible residual with no Schnakenberg reading, and we do not claim one.

**Housekeeping [Theorem].** If some $\mathcal A(c)\neq0$, then $J_{\text{ss}}\neq0$ on some edge. The steady-state entropy production rate

$$
\sigma_{\text{ss}}=\sum_{u<v}(p_uk_{uv}-p_vk_{vu})\ln\frac{p_uk_{uv}}{p_vk_{vu}}=\sum_{c}J(c)\,\mathcal A(c) > 0
$$

(Schnakenberg's cycle decomposition over a fundamental basis). The housekeeping or adiabatic part (Hatano–Sasa 2001; Esposito–Van den Broeck 2010) is $\ge0$ for all $t$. It vanishes identically iff detailed balance holds, and it equals $\sigma_{\text{ss}}$ at steady state. Therefore

$$
\boxed{\ r_\perp\neq0\iff J_{\text{ss}}\neq0\iff\dot Q_{\text{hk}}=k_BT\,\sigma_{\text{hk}}>0\ }
$$

#### 3b. Overdamped Langevin and the continuum cokernel

The dynamics are $dx=\mu F\,dt+\sqrt{2D}\,dW_t$, with $D=\mu k_BT$ and $F=-\nabla H_\lambda+u$. The local mean velocity is $v=\mu F-D\nabla\ln p$, the current is $J=pv$, and $\partial_tp=-\nabla\!\cdot J$. The entropy production rate (in units of $k_B$) is $\dot\Sigma=D^{-1}\!\int p|v|^2$.

Decompose $v$ in $L^2(p)$ (Helmholtz–Hodge): $v=\nabla\psi+w$ with $\nabla\!\cdot(pw)=0$.

**Proposition 3.2 [Theorem].** For a fixed density path $p_t$, $\nabla\psi$ is uniquely fixed by $\partial_tp=-\nabla\!\cdot(p\nabla\psi)$, and

$$
\dot\Sigma=\underbrace{D^{-1}\!\int p|\nabla\psi|^2}_{\text{excess (transport)}}+\underbrace{D^{-1}\!\int p|w|^2}_{\text{housekeeping}} .
$$

The component $w$ does not move the density at all; it only circulates. **$w$ is the continuum $r_\perp$.** At steady state $\nabla\psi=0$, so $v=J_{\text{ss}}/p_{\text{ss}}$ and

$$
\dot Q_{\text{hk}}=\int\frac{|J_{\text{ss}}|^2}{\mu\,p_{\text{ss}}}\,dx>0\quad\text{iff } J_{\text{ss}}\not\equiv0 .
$$

Attribution: this $L^2$ form is the Speck–Seifert (2005) expression of Hatano–Sasa housekeeping heat. For time-dependent driving, the orthogonal split above is the geometric decomposition of Dechant, Sasa and Ito (2022). It coincides with Hatano–Sasa at steady states but differs from it in general.

**$\mathcal W_2$ speed limit [Theorem].** By Benamou–Brenier and Cauchy–Schwarz in time,

$$
\Sigma_{\text{tot}}\;\ge\;\frac1D\int_0^\tau\!\!\int p|\nabla\psi|^2\;\ge\;\frac{\mathcal W_2(p_i,p_f)^2}{D\,\tau},\qquad\text{i.e.}\quad \Sigma_{\text{tot}}\cdot\tau\ \ge\ \frac{\mathcal W_2(p_i,p_f)^2}{D}.
$$

Equality holds along the constant-speed $\mathcal W_2$ geodesic with $w\equiv0$ (Aurell, Mejía-Monasterio, Muratore-Ginanneschi 2011; Nakazato–Ito 2021; Dechant–Sasa–Ito 2022). Shiraishi, Funo and Saito (2018) give a different speed limit, for jump processes, in terms of total variation and dynamical activity.

**Proposition 3.3 (landscape realisability) [Theorem].** With full actuation, the optimal protocol is realised by a **pure gradient force**. With $v=\nabla\psi$, the required force $F=\mu^{-1}(v+D\nabla\ln p)=\mu^{-1}\nabla(\psi+D\ln p)$ is a gradient, that is, a time-dependent Hamiltonian $H_{\lambda(t)}$ with $u\equiv0$. Steady maintenance of any smooth target $p_f>0$ is likewise achieved by $H_f=-k_BT\ln p_f$ with zero housekeeping heat.

The brief's "fast forcing vs. quasi-static reshaping" contrast therefore splits into **two independent axes**:

| | speed axis | gradient axis |
|---|---|---|
| cost | excess $\ge\mathcal W_2^2/(D\tau)$ | housekeeping $D^{-1}\!\int p|w|^2$ |
| applies to | *both* strategies at finite $\tau$ | only non-gradient forcing |
| vanishes when | $\tau\to\infty$ | $w\equiv0$ (landscape protocol) |

Fast non-gradient state forcing pays on both axes, divergently on the first ($\tau\to0$) and perpetually on the second. Quasi-static Hamiltonian reshaping, $H(\lambda)$ with $u\equiv0$ and $\tau\to\infty$, pays on neither. It still pays $\Delta F$ as **principal**: reshaping is not free. It converts perpetual interest into a one-time principal.

#### 3c. Counterfactual clamping is non-reciprocity [Theorem + Structural Isomorphism]

A clamp is not automatically non-gradient: a stiff harmonic trap on one coordinate is a potential. What produces curl is the *do*-structure. If $X$ is held to ignore its neighbours while they still respond to $X$, the result is a **one-way coupling**. For the linear (Ornstein–Uhlenbeck) case with isotropic noise, $dx=-Ax\,dt+\sqrt{2D}\,dW$, where $A$ is stable and the stationary covariance $C$ solves $AC+CA^\top=2D\,\mathbb 1$:

**Proposition 3.4 [Theorem].**

$$
\sigma_{\text{ss}}=D^{-1}\,\mathrm{Tr}\!\left[(A-DC^{-1})\,C\,(A-DC^{-1})^\top\right],\qquad\sigma_{\text{ss}}>0\iff A\neq A^\top .
$$

*Proof.* $v(x)=-(A-DC^{-1})x$. If $A=A^\top$, then $C=DA^{-1}$ is the unique Lyapunov solution, so $A-DC^{-1}=0$. Conversely, $A-DC^{-1}=0$ forces $A$ to be symmetric, and $C\succ0$ makes the trace strictly positive otherwise. $\square$

**Reading [Structural Isomorphism].** Replacing $X$'s row of a symmetric coupling matrix by a self-term while leaving $X$'s column in place is **local counterfactual clamping**. It makes $A$ asymmetric and creates a perpetual housekeeping current. Liao-Fan's practice, revising one's own conduct and relationships *reciprocally* over years, corresponds to a slow symmetric deformation $A(\lambda)$: every intermediate state is an equilibrium of the current landscape. A *physical* implementation of $do(X=x^\star)$ that measures and cancels the neighbours' influence is also a feedback loop, so Result 1 bills it as well.

| | local counterfactual clamping | quasi-static landscape reshaping |
|---|---|---|
| acts on | state, via one-way coupling | landscape $H(\lambda)$ / symmetric $A(\lambda)$ |
| graph signature | $r_\perp\neq0$ | $r_\perp=0$ |
| housekeeping heat | $>0$, perpetual | $0$ |
| transient excess | $\ge\mathcal W_2^2/(D\tau)$, $\tau$ small | $\to0$ as $\tau\to\infty$ |
| cost form | perpetual interest | one-time principal $\Delta F$ |
| *Daodejing* | 宰 (domination) | 长而不宰 (lead without dominating) |

---

## Part IV — Kill criteria and falsifiable predictions

The theorems stand or fall with their hypotheses. The tests below target **our mappings and hypotheses**, and each one says what would make us retract.

**K1 — Ontology ("non-void").** A physically realised process that permits signalling which breaks normalization under some choice of local CPTP maps, or a reproducible failure of the process-matrix probability rule, kills the "non-void in constraint" half of §1.2. (A physical violation of a causal inequality would *not* kill it, since it stays within $\mathcal W$. A predictive framework in which $\mathcal A$ itself is frame-relative would *shift* the isomorphism toward §1.3(b) rather than kill it.)

**K2 — Split ledger (Result 1).** Run a feedback-controlled colloid, or a single-electron box, in which the demon's memory has its own calorimetry. Measuring $\langle W^A_{\text{saved}}\rangle > W^D_{\text{meas}}+W^D_{\text{erase}}$ beyond error is a second-law-level anomaly and kills Result 1. The weaker, more likely-to-fail prediction: deferring erasure leaves a measurable residual $k_BT\,I(X;M)$ in the joint state.

**K3 — Compensation gap, applied (Prop. 1 + decoupling).** In a thermal-operations simulator, or in a multi-agent RL economy with risk-sensitive objectives, preregister harm events with $\sup_\alpha\Delta_\alpha>\Delta_1$. If mean-matched scalar compensation $w=\Delta_1$ systematically restores worst-case task success with $I$ left nonzero, the theorem survives but our model of "settlement" is wrong and is withdrawn.

**K4 — Cascade locality (Result 2, H3).** Use networks with recorded interventions: power-grid redispatch, supply-chain shocks, collaboration graphs. The preregistered null is the flow model with measured conductances and margins. If first overloads land on **high-margin edges far from the source** significantly more often than the model predicts, and Proposition 2's neighbourhood bound is routinely violated in effect, H3 is dead.

**K5 — $r_\perp$ as an operational detector (Result 3).** Use a driven colloidal ring, or a coupled OU pair with tunable non-reciprocity $A-A^\top$. Estimate $r_\perp$ from trajectories on a coarse-grained observation graph and compare it with calorimetric housekeeping heat. The theorem is exact for the Markov model. The falsifiable claim is that coarse-grained $r_\perp$ is a *useful* detector. If $\|r_\perp\|\approx0$ while the measured $\dot Q_{\text{hk}}$ is large across reasonable coarse-grainings, the detector is useless in practice (hidden cycles) and we downgrade it.

**K6 — Part II hypotheses.**
- **(a) H1.** Build learning systems with progressively more independent credit axes. If probe-decodability of the system's own boundary variables (initialization, objective, architecture choices) shows **no threshold** as the number of axes increases, H1 is downgraded.
- **(b) Fermi reading.** Abundant, long-lived, high-power artificial beacons would kill it. So would a demonstration that persistent emission is thermodynamically negligible against any plausible civilizational budget, since the argument would then have no force. A third way to lose it: any proposed "initial-condition signature" fails a preregistered look-elsewhere correction, so that we cannot tell design from coincidence.

---

## 5. Corrections relative to the Chinese edition and the task brief

1. The weak value $A_w$ is due to Aharonov–Albert–Vaidman (1988). ABL (1964) is the strong-measurement rule.
2. P-CTCs (Lloyd et al. 2011) are post-selection models, not fixed-point models. The fixed-point existence argument applies to Deutsch CTCs. The post-selection cost is now the exact Jarzynski–Jensen bound of §2.2, not a heuristic.
3. "The source's edges are fully loaded" is replaced by Result 2(b). Unit flux crosses every $A$–$g$ cut, and the per-edge maximum need not sit at $A$.
4. "Any $u(t)\neq0$ incurs maintenance heat" is false as stated. Only the non-gradient component does (Props 3.2–3.4).
5. $F_\infty$ is the max-free energy (work of formation), and $F_0$ governs extractable work. The compensation statement is restated as Proposition 1.
6. $r_\perp$ ⇔ Schnakenberg is exact at $\gamma=1$, as equality of cycle circulations and of vanishing sets. It is not an entry-wise identity, and it does not extend to $\gamma<1$.
7. Hatano–Sasa housekeeping heat in the explicit $L^2$ form is Speck–Seifert's. The time-dependent orthogonal split is Dechant–Sasa–Ito's.

---

## References

Oreshkov, Costa, Brukner, *Nat. Commun.* 3, 1092 (2012) · Araújo, Branciard, Costa, Feix, Giarmatzi, Brukner, *New J. Phys.* 17, 102001 (2015) · Chiribella, D'Ariano, Perinotti, Valiron, *Phys. Rev. A* 88, 022318 (2013) · Procopio et al., *Nat. Commun.* 6, 7913 (2015) · Rubino et al., *Sci. Adv.* 3, e1602589 (2017) · Castro-Ruiz, Giacomini, Belenchia, Brukner, *Nat. Commun.* 11, 2672 (2020) · Rovelli, *Int. J. Theor. Phys.* 35, 1637 (1996); *Helgoland* (2020) · Adlam, Rovelli, *Philos. Phys.* (2023; arXiv 2022) · Page, Wootters, *Phys. Rev. D* 27, 2885 (1983) · Giovannetti, Lloyd, Maccone, *Phys. Rev. D* 92, 045033 (2015) · Höhn, Smith, Lock, *Phys. Rev. D* 104, 066001 (2021) · Moreva et al., *Phys. Rev. A* 89, 052122 (2014) · Hoel, Albantakis, Tononi, *PNAS* 110, 19790 (2013) · Aharonov, Bergmann, Lebowitz, *Phys. Rev.* 134, B1410 (1964) · Aharonov, Albert, Vaidman, *PRL* 60, 1351 (1988) · Deutsch, *Phys. Rev. D* 44, 3197 (1991) · Lloyd, Maccone, Garcia-Patron, Giovannetti, Shikano, *PRL* 106, 040403 (2011) · Jarzynski, *PRL* 78, 2690 (1997) · Landauer, *IBM J. Res. Dev.* 5, 183 (1961) · Sagawa, Ueda, *PRL* 100, 080403 (2008); *PRL* 102, 250602 (2009) · Brandão, Horodecki, Ng, Oppenheim, Wehner, *PNAS* 112, 3275 (2015) · Motter, Lai, *Phys. Rev. E* 66, 065102 (2002) · Schnakenberg, *Rev. Mod. Phys.* 48, 571 (1976) · Hatano, Sasa, *PRL* 86, 3463 (2001) · Speck, Seifert, *J. Phys. A* 38, L581 (2005) · Esposito, Van den Broeck, *PRL* 104, 090601 (2010) · Aurell, Mejía-Monasterio, Muratore-Ginanneschi, *PRL* 106, 250601 (2011) · Nakazato, Ito, *Phys. Rev. Research* 3, 043093 (2021) · Dechant, Sasa, Ito, *Phys. Rev. Research* 4, L012034 (2022) · Shiraishi, Funo, Saito, *PRL* 121, 070601 (2018) · Benamou, Brenier, *Numer. Math.* 84, 375 (2000) · Sandberg, Armstrong, Ćirković, arXiv:1705.03394 (2017) · Smart, *Acta Astronaut.* 78, 55 (2012) · Nāgārjuna, *Mūlamadhyamakakārikā* 13.8, 24.18 · *Daodejing* ch. 10, 51 · Yuan Liaofan, *Liaofan Sixun* (16th c.).

*Bibliographic details were assembled from memory and should be checked against the primary sources before citation.*

*Related on this site:* [Seeded, Then Left Alone](2026-06-22-seeded-then-left-alone-directed-panspermia-non-interference.md) · [Discounted cokernel obstruction (THEORY v3)](2026-08-19-information-dynamics-theory-v3-cokernel-obstruction.md) · [Taiji–Bagua multi-axis generative operator](2026-05-21-taiji-bagua-multi-axis-generative-operator.md) · [Theory Mainline](../THEORY.md)
