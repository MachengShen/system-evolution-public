# Locality as Protocol: A Framework for Rule-System Competition and Co-Evolution

**Version**: v0 (2026-04-29, pre-calibration)  
**Repository**: `MachengShen/system-evolution-public`  
**Status**: Published for critique and engagement. External calibration pending.

---

## Overview

This document articulates a framework for thinking about the long-arc evolution of governance: what happens when the organizing principle of "where rules apply" decouples from the nation-state as the fundamental unit, and rule-systems themselves become the substrate that individuals, capital, and attention select among.

The argument is not a prediction that this transition is inevitable, nor a manifesto that it is desirable. It is an attempt to trace the internal logic of a partially-visible evolutionary pressure — one already visible in charter cities, crypto networks, digital residency programs, and pop-up city experiments — and to articulate both its coherent endpoint and its unresolved design problems honestly.

This is an early-stage articulation. The design problems identified in Part 3 are genuinely open; the counter-mechanism candidates are research directions, not solutions.

---

## Part 1 — Four Principles

### Principle A: Rule-as-substrate, not organism-as-substrate

The conventional framing of government is as an organism — a territorial human institution that holds a claim to the monopoly on legitimate coercion within a geographic boundary. This is the Weberian framing: the state is defined by its exclusive claim on legitimate force.

An alternative framing starts from what government *functionally provides*: a set of rules whose violation is costly. The state's core product is not its bureaucracy, its officials, or even its territory — it is a rule-system in which non-compliance carries sufficient cost that most actors comply. What makes a legal norm effective is not that an enforcement agency exists, but that circumventing the norm is sufficiently expensive that widespread cooperation is a stable equilibrium.

If "rules with high violation costs" are the actual product, then the question becomes: does this product require delivery via a human-staffed territorial organism? Increasingly, some kinds of rules do not. Smart contracts auto-execute without a bailiff. Protocol-level rules governing asset transfer or identity verification do not require a court to enforce them; the violation cost is architectural, not institutional.

This is the first principle: governance systems can evolve from organism-substrate toward rule-substrate — from "a human institution that enforces rules" toward "a designed protocol that makes rule-violation architecturally costly." The two are not fully substitutable today. Organism-enforcement is still required for physical-world enforcement: property, bodily security, emergency services, cross-border disputes. But the frontier is shifting, and the conceptual frame matters for design decisions about where to invest coordination resources.

### Principle B: Locality-bound, not nation-bound

The nation-state bundles two things that are conceptually separable: a *rule-set* and a *geographic perimeter of exclusive jurisdiction*. The rule-set is what governance actually provides — the services and constraints that make collective action possible. The geographic perimeter is the delivery mechanism: historically necessary when physical force was the primary enforcement tool, because force requires territory.

Locality-as-protocol separates these. Each locality has a local rule-set, but the relevant boundary is not a nation-state border. It is the softer boundary of: who has engaged with this rule-system? The answer is those who have voluntarily participated — by residing, registering, transacting, or obtaining credentials within it.

This is not a claim that territorial governance vanishes; it does not, as long as physical enforcement is required, and physical enforcement is tied to geography. It is a claim that the *primary unit of selection* can shift from the nation-state toward the local rule-set, which might be a charter city, a digital community, an e-residency system, a pop-up physical experiment, or a protocol-governed network. The relevant question becomes "which rule-set governs this interaction?" not exclusively "which country's jurisdiction applies?"

Estonia's e-residency program (launched 2014) is an early partial example: legal and commercial governance partially decoupled from territorial residency. Próspera (Honduras Roatán, operational from ~2017) is a physical experiment at small scale. Zuzalu and subsequent pop-up city experiments test whether aligned-values communities at short time horizons produce discernibly different governance outcomes. Scale and time horizon vary; the structural logic is consistent.

### Principle C: Global resource flow as the evolutionary signal

In the nation-state model, the primary feedback mechanism is electoral: periodic voting aggregates preferences, with geographic and majority-rule constraints. The classical exit-option literature identified that mobility across jurisdictions provides a second feedback mechanism. When individuals can move, the credible threat of exit disciplines local rule-sets (Tiebout, 1956; Hirschman, 1970).

The extended claim here is that as rule-systems partially decouple from territorial boundaries, the feedback mechanism becomes *global resource flow* — the aggregate decisions of all individuals globally about where to deploy attention, capital, talent, and time. A rule-system that attracts more of these resources is, in an evolutionary sense, fitter; one that loses them declines and must adapt or collapse.

"Voting with your feet" (Tiebout) upgrades to "voting with your capital, time, talent, and public endorsement," and the relevant population is global rather than local. This is already partially true: Gitcoin grants aggregate global funding for public goods projects across territorial lines. Optimism's Retroactive Public Goods Funding retroactively rewards demonstrated impact. These are early experiments in a selection mechanism that operates across territorial boundaries.

The mechanism is not new; what has changed are the friction costs. Digital finance, remote work, fast travel, and global communication have reduced the friction of participation across jurisdictions from prohibitive to manageable for increasing fractions of the global population.

### Principle D: Coupled co-evolution

The fourth principle concerns the dynamics, not the statics. Individuals selecting among rule-systems *changes* both parties over time: individuals adapt to the rule-systems they select, and rule-systems evolve in response to aggregate selection pressure. This is a reflexive system — there is no stable equilibrium, only ongoing optimization.

Paul Romer's charter city argument (2009-) is partly about rule-sets as a design problem: deliberately design better rules, import them into a territory via a new institutional charter, and create value. The coupled co-evolution extension is that this design process is never terminal — rule-systems that attract global resource flow have the resources to iterate; those that do not, do not.

The mechanism design work of Buterin, Weyl, and collaborators (quadratic funding, retroactive public goods funding) is partly about designing the selection mechanism itself: how do you aggregate individual resource-allocation decisions into collective outcomes in ways that resist concentration effects and preserve diversity of rule-systems? These are design questions that operate at the layer above any individual rule-set — questions about what properties the *selection mechanism* itself should have.

---

## Part 2 — Academic and Practical Lineage

This framework is not original. It extends a well-developed intellectual tradition:

**Charles Tiebout (1956)** — "A Pure Theory of Local Expenditures." The foundational model: individuals choose among local jurisdictions by moving, creating competitive pressure on local governments to provide efficient bundles of public services and taxation. Tiebout's model required strong mobility assumptions that did not hold empirically in the 1950s; the digital-era reduction of mobility friction makes the core logic more applicable, though the assumptions remain imperfect.

**Albert Hirschman (1970)** — *Exit, Voice, and Loyalty.* The canonical framing of exit (leaving) versus voice (reforming from within) as responses to deterioration in firms, organizations, or nations. The key insight relevant here: the availability of a credible exit option changes the equilibrium use of voice. When exit is easy, defection disciplines governance; when exit is blocked, voice becomes the primary mechanism and its quality determines governance outcomes.

**Paul Romer (2009-)** — Charter cities. The argument that rule-sets are the key input to development outcomes, that importing better rules is possible, and that this requires a new governance experiment — a new city with a new charter operating under agreed external oversight. Próspera (Roatán, Honduras) is the most developed live physical experiment, operating with special economic zone status from ~2017.

**Vitalik Buterin + Glen Weyl** — Quadratic funding (2019-), retroactive public goods funding (Optimism, 2021-). Mechanism design contributions for aggregating global preferences in public goods funding in ways that give more weight to broad-based support than to concentrated capital. Gitcoin Grants and Optimism RPGF are live at small scale.

**Balaji Srinivasan (2022)** — *The Network State.* The cloud-community-to-physical-territory pathway: start as a digital community with aligned values, develop social trust and shared norms, eventually obtain physical territory for collective habitation. The startup-society framing of governance as a design problem with intentional founding values.

**Estonia e-residency (2014-)** — Governance-as-service, partially unbundled from territorial residence. Offers legal personhood and digital services to global participants who have never resided in Estonia. Currently limited to commercial and legal scope, not full civic or social services membership.

**Zuzalu / Cabin / Edge City (2022-)** — Pop-up and semi-permanent co-living experiments that combine physical presence with explicit community governance design. Short time horizons, but testing whether values-aligned communities at small scale produce discernibly different governance outcomes from default municipal governance.

The push beyond this lineage: fully decoupling "where you are physically located" from "who funds the rules you live under and benefit from," and making global resource flow — not just local electoral politics or local migration — the primary evolutionary selection signal for rule-systems.

---

## Part 3 — Five Unresolved Design Problems

Honest articulation requires confronting five design problems. These are not solved; they are the genuine open questions that any serious implementation must address.

### Problem 1: Race-to-bottom selection equilibrium

If rule-systems evolve primarily in response to capital-flow signals, the historically dominant competitive strategy is *removing protections to attract capital*. The Cayman Islands, British Virgin Islands, and Delaware's corporate law regime are winners of this game: they attract incorporation and registration by offering reduced liability, reduced disclosure requirements, and favorable treatment for capital holders. This competitive dynamic drove toward these outcomes — not toward better protections for workers, non-mobile residents, or ecosystems.

A locality-as-protocol framework without counter-mechanisms likely reproduces this dynamic at larger scale: rule-systems compete by reducing friction for mobile capital, while less-mobile parties bear the externalities. The endpoint would resemble a global extension of current offshore financial center dynamics.

Counter-mechanism candidates that remain in the open design space:

- **Reputation and track record layers** — making historical rule-system behavior legible across time, so resource allocators can price governance quality, not just governance convenience
- **Multi-dimensional flow signals** — weighting person-endorsement, quadratic-intensity contributions, and long-duration engagement differently from pure capital deployment, reducing the overweighting of capital concentration
- **Minimum standards floors enforced by coalition** — localities binding themselves to shared standards as a collective reputation hedge against race-to-bottom dynamics

None of these is implemented at scale with demonstrated effectiveness. The "minimum standards floor" problem is recursive: who enforces the floor is itself an organism-state-class problem — requiring exactly the kind of centralized enforcement authority that this framework is trying to evolve beyond.

### Problem 2: Capital-weighted selection ≠ person-weighted selection

The global resource flow signal is structurally capital-weighted. The top decile of global wealth holders control the majority of mobile capital. Rule-systems that optimize for this signal will disproportionately reflect their preferences — not the preferences of the broader global population. This is not the same as democratic person-weighted voting, where each person's ballot counts equally regardless of wealth.

This is not necessarily a reason to reject resource flow as a selection mechanism. Revealed preference through actual resource deployment may capture preference intensity better than ballot casting. A person who relocates, invests, or dedicates years of work to a rule-system has demonstrated stronger preference than a periodic vote. But the normative implications are different from democratic theory, and this difference should be acknowledged explicitly rather than obscured.

The structural self-check for anyone advocating capital-weighted selection mechanisms: high-net-worth, geographically mobile, high-skill individuals are the structural net beneficiaries of such selection rules. This does not invalidate the argument, but it is a known bias that should be disclosed and actively counterweighted in mechanism design.

Partial counter-mechanisms exist: quadratic funding weights by number-of-contributors rather than size-of-contribution; retroactive public goods funding attempts to reward demonstrated broad impact over concentrated patronage. These are design directions, not proven solutions at scale.

### Problem 3: Physical-boundary enforcement gap

Smart contracts auto-execute for on-chain assets. The physical world — property ownership, bodily security, cross-border medical care, involuntary contract enforcement for physical goods and services — still requires organism-state enforcement at territorial boundaries. A purely protocol-native rule-system governs only the digital layer; the moment physical assets or physical persons are involved, organism-state enforcement capacity re-enters as a necessary dependency.

Full decoupling of physical governance from organism-states requires either: (a) sufficiently high physical tokenization that most physical assets have on-chain representations enforceable without organism-state intervention; or (b) sufficient densification of physical rule-system experiments that new organism-states form around successful rule-sets. Option (a) is a multi-decade technological horizon. Option (b) is what charter city projects attempt, and the uncertain legal status of existing experiments illustrates the difficulty of achieving genuine legal independence from surrounding nation-states.

The framework applies more immediately to digital-native activities — software, data services, remote work, digital assets — than to physical-world governance. Scope should be stated honestly.

### Problem 4: Free-rider problem during transition

The framework implies that individuals and organizations should select rule-systems based on governance quality, exiting poor rule-systems for better ones. But during any realistic transition period, individuals continue to consume services from the rule-systems they are nominally exiting: court systems for dispute resolution, emergency services, property registries, physical security guarantees against violence. Pure exit advocacy combined with continued consumption of organism-state services is structurally a free-rider position.

Honest articulation requires acknowledging the transition-period dual obligation: those building toward exit should also comply with and contribute to current governance frameworks during the transition. This is not a contradiction; it is a temporal structure. The endpoint aspiration and the transition-period obligation coexist. The transition-period obligation is not merely strategic (avoiding backlash) but substantive: the current system, for all its inefficiencies, provides services that are being consumed and that deserve contribution.

### Problem 5: Cross-cutting public goods

National defense, pandemic response, climate mitigation, basic research, and fundamental physical infrastructure are characterized by strong free-rider dynamics — the individual incentive to defect from collective provision while continuing to benefit from it. This is precisely why organism-states with coercive taxation emerged historically: as coordination mechanisms for public goods provision at scale that cannot be solved through voluntary participation alone.

Competing local rule-systems have historically been less robust on these cross-cutting verticals. This is not accidental; the competitive dynamic creates race-to-bottom pressures for costs and externalities while making collective commitment to cross-cutting goods harder to sustain. The network state and charter city literature tends to select verticals where local governance works well (housing regulation, commercial law, local services) while leaving the hardest cross-cutting cases underspecified.

Partial answers exist and deserve serious investment: quadratic funding for public goods, retroactive public goods funding, protocol-level coordination for shared digital infrastructure, and coalition-level commitments among rule-systems for cross-cutting goods. But the full mechanism design for cross-cutting public goods under locality-as-protocol conditions remains the central unsolved problem of this framework. Any credible proposal for locality-as-protocol governance must address this directly.

---

## Part 4 — Connection to Software-Layer Governance

The locality-as-protocol logic maps onto software-layer governance in a compressed form. An open-source software project with a permissive license, an active fork community, and a reputational layer around governance decisions is a miniature rule-system competing for contributors, users, and funding. The selection mechanism — who forks, who funds, who contributes — is the global resource flow signal in microcosm.

Governance documents (license, charter, governance commitments), fork-welcome clauses, and user-owned-derivative policies constitute the rule-set. Developer and user engagement constitutes the resource flow. The evolution of the project is coupled co-evolution between the rule-set and its community.

This is not a metaphor; it is the same structural logic operating at smaller scale and faster iteration speed. The design problems are structurally analogous:

- **Race-to-bottom** parallels in software: copyleft minimization to attract commercial adoption, governance centralization to reduce coordination costs
- **Capital-weighted selection**: venture-backed forks with larger deployment budgets outcompeting community forks with better governance commitments
- **Enforcement gap**: license compliance in software is technically easier than physical-world enforcement but still requires occasional organism-state legal action for serious violations
- **Free-rider during transition**: users benefiting from open-source infrastructure without contributing to its maintenance or governance
- **Cross-cutting goods**: security research, accessibility tooling, foundational protocol development — undersupplied by competitive dynamics even in healthy open-source ecosystems

Software governance has produced some partial answers: copyleft licensing for enforcement, quadratic-funding experiments for public goods allocation, retroactive grants for historical contributions. These are not fully transferable to physical governance, but they are design experiments at smaller scale that iterate faster than physical-world institutions. The learning generated at software-layer scale is relevant to the harder physical-layer design problems.

---

## Versioning

This is v0. The argument is incomplete; the design problems are genuinely hard. The purpose of publishing at this stage is to invite engagement: critique, alternative framings, evidence from existing experiments, and proposals for counter-mechanisms.

External calibration via cross-model review is pending. Feedback will be incorporated in v0.1.

---

## Closing

I am articulating this vision for what comes after the nation-state model — specifically, the evolutionary pressures and structural logic that are already partially visible. The artifact is the ask. Critique, fork the vision, build instances, silence, or nothing — is yours to choose.

---

*See also: [VISION.md](VISION.md) — the user-agency substrate as one software-layer instance of this broader framing.*
