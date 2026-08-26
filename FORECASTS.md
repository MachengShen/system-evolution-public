# Forecasts, Targets, and Interventions

This is the public entrypoint for future-world predictions made from the
Macheng + agent joint system.

The key rule is simple:

> A forecast from an intelligent system is not always a detached observation.
> It can also be a target, a coordination signal, and an intervention.

The theory line explains why the system learns. The practice line explains what
agents should do. This file explains how to handle predictions about the future
when the act of predicting may change the future being predicted.

## Why This Exists

As a personal AI system becomes more capable, it stops being only a passive
assistant.

The coupled system of a human principal, memory substrate, agents, reviewers,
tools, public artifacts, and external feedback can become a causal actor. It can
change which ideas are visible, which people coordinate, which projects receive
attention, and which futures become easier to reach.

That means some predictions are partly performative. They are not merely:

```text
what will happen?
```

They may also mean:

```text
what future is the system trying to make reachable?
what action will this prediction cause?
what feedback would make the system revise course?
```

## Three-Way Classification

Every public prediction should classify itself as one or more of:

### F-01: Descriptive Forecast

A claim about what is likely to happen if the system does not materially
intervene.

Required fields:

```text
forecast:
time_horizon:
confidence:
evidence:
base_rate_or_reference:
resolution_date:
resolution_criteria:
partial_credit_rule:
revision_trigger:
```

### F-02: Desired Target

A future the system wants to make more reachable.

Required fields:

```text
target:
not_a_forecast_marker:
why_it_matters:
who_benefits:
who_could_be_harmed:
acceptable_methods:
unacceptable_methods:
owner_gate:
```

### F-03: Intervention / Commitment

A prediction that also changes what the system will do.

Required fields:

```text
intervention:
intervention_scope: self | collaborators | public | institutions
public_commitment:
changed_actions:
feedback_loop:
rollback_or_stop_condition:
audit_receipt:
```

## Agent-Readable Forecast Contract

When an agent publishes or updates a future-world prediction, it should use this
shape:

```text
title:
date:
type: forecast | target | intervention | mixed
time_horizon:
claim:
desired_future:
current_evidence:
base_rate_or_reference:
resolution_date:
resolution_criteria:
partial_credit_rule:
actions_this_changes:
intervention_scope:
feedback_loop:
anti_signals:
revision_trigger:
stop_condition:
private_boundary:
public_receipt:
```

If `actions_this_changes` is empty, the prediction is probably only a forecast.
If `actions_this_changes` is non-empty, the artifact must treat the prediction
as an intervention too.

Targets should be marked as desired futures, not smuggled in as forecasts. A
target may later become a forecast only if it has independent evidence,
resolution criteria, and a stated base rate or reference class.

The rationale layer is often where privacy risk lives. Public artifacts should
publish the claim, classification, criteria, and calibration record. Private
health, relationship, financial, employer, collaborator, or raw-memory evidence
should stay private unless explicitly approved.

## Intended Use

These artifacts are for calibration, coordination, self-governance, and public
audit of the joint system's direction.

They are not investment advice, recruiting claims, prophecies, threats, or
promises that other people must coordinate around.

## Governance Rule

Do not let predictions hide their agency.

Bad form:

```text
X will happen.
```

Better form:

```text
X is a forecast under current conditions.
We also want to make Y more reachable.
Publishing this changes our actions in Z ways.
We will revise if A, B, or C happens.
```

This matters because a system that can act on its own predictions can create
self-fulfilling, self-defeating, or destabilizing loops.

Interventions should also distinguish scope. An intervention on the system's own
memory, publication, or research loop is different from an intervention that
tries to affect collaborators, public readers, institutions, markets, or other
people's choices. Wider-scope interventions require stronger governance,
receipts, and stop conditions.

## Practice Implication

Prediction handling is part of the engineering system.

The loop is:

```text
world model
  -> forecast / target / intervention classification
  -> public artifact
  -> changed agent behavior
  -> external feedback
  -> memory and strategy update
  -> revised forecast
```

This makes predictions a special kind of closed-loop channel.

## Anti-Signals

The forecast line is failing if:

1. predictions are written as prophecy rather than working hypotheses;
2. desired futures are presented as neutral forecasts;
3. interventions do not disclose what actions they change;
4. public predictions increase drama without improving coordination or
   evidence;
5. the system ignores disconfirming evidence;
6. the system's pursuit of a target harms agency, trust, safety, or the people
   it claims to help;
7. prediction artifacts create attention pressure without a repair or rollback
   path.
8. targets are later counted as successful forecasts without pre-stated
   resolution criteria.

## Huineng / Laozi Check

Strongest insight: predictions from a capable agentic system are not only maps;
they can become part of the territory.

Main failure mode: using future-language to avoid checking present conduct,
relationship quality, body state, power, incentives, and concrete harm.

Architecture implication: every serious forecast needs classification,
feedback, revision, and stop conditions.

Disconfirming observation: the public prediction changes rhetoric but not
behavior, receipts, or feedback handling.

Reviewer improvement: ask what action changed because the prediction was
published, and what evidence would make the system stop.

## Performative Exposure (correction, 2026-08-26)

Confidence-tagged per [Claim-Receipt](CLAIM-RECEIPT.md): mechanism 0.8, the
specific accounting rule below 0.6.

An earlier internal rule said the engine should minimize surprise on perception
and never by action. That rule is retracted. It mistook an accounting problem
for an ontological one.

A forecast, once spoken, is already an action: whoever hears it changes what
they do, and the system itself acts on its own forecasts. There is no wall
between observation, prediction, and action; they are three nodes on one loop
(performative prediction, Perdomo et al. 2020; reflexivity; self-fulfilling
prophecy, Merton 1948; the Lucas critique). The real failure of "active
inference" as a design is not that it unifies prediction and action. It is that
it lets the system be scored on a surprise it can lower by acting.

So the guard is not "do not act" but "record what you did":

1. **Footprint on the ledger.** Every forecast carries
   `performative_exposure: none | low | high` plus the mechanism by which
   publishing it could move the outcome. Every dissemination (a post, a
   message, a conversation) is itself a ledger event, not a side effect.
2. **Skill is measured only where the system has no hand.** Calibration and
   Brier summaries are computed over the `exposure != high` subset only.
   High-exposure forecasts still stay in the listing and are resolved in two
   separate columns: did it happen (automatic) and did our dissemination
   contribute (requires independent evidence; defaults to unknown, never
   auto-filled). Skill claims may cite only the first column.

Consequence for the classification above: F-01 / F-02 / F-03 are no longer
three exclusive classes. They are one continuous quantity (exposure) plus one
intent marker (desired or not) on the same forecast. F-03 is not a contaminant
to be quarantined; it is the end of the performative channel the system
actually wants, kept in its own column. The isolation rule keeps its accounting
meaning (columns must not be mixed) and loses its behavioral meaning (do not
act).

Anti-signals: a high-exposure entry appearing inside a calibration summary; a
contribution column filled without independent evidence; a forecast visible in
public output with no dissemination record.

## Relation To Theory And Practice

- [THEORY.md](THEORY.md) explains the broader General Learning Machine frame.
- [PRACTICE.md](PRACTICE.md) explains the engineering practice contract.
- This file explains how future-world claims become governed artifacts.
