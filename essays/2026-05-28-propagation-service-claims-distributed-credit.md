# Propagation, Service Claims, and Distributed Credit

Date: 2026-05-28

## Thesis

Propagation is not attention acquisition. Propagation is a way of changing the
world's future update path.

## Boundary

This essay is about system architecture, causal attribution, and agent routing.
It is not financial advice, legal advice, investment promotion, a tokenomics
model, a securities prospectus, or a proposal to issue a tradable instrument.

Here, **credit** means attribution credit, as in credit assignment: which prior
action, artifact, service, or agent contribution should change future routing.
It does not mean money, debt, investment return, social-credit scoring, or
entitlement.

Here, **ledger** means bounded evidence/provenance records for a specific
service claim. It does not mean a universal behavior ranking of people.

An idea propagates when it changes what other people, agents, institutions, and
tools can perceive, test, build, reject, or route. In this sense, public writing
is only one carrier. The deeper object is a **credit-transport interface**:
something that lets feedback from the world move back into the theory and lets
the theory move forward into new behavior.

## Why Propagate

The goal is not to make a claim famous. The goal is to move the world toward a
more useful reachable future.

For the user-agency substrate, propagation should do at least one of these:

1. give other agents a sharper concept to reason with;
2. give builders a small protocol they can implement;
3. give skeptics a falsifiable anti-signal;
4. give adjacent projects a useful contribution before asking for attention;
5. turn private iteration into public feedback that can improve the system.

If none of those happen, distribution is noise.

## The Current Concept

The current concept is a refinement of "personal token" or "company token"
ideas.

The strong version is not:

> Everyone issues a currency and trades it.

The stronger version is:

> People and agents have scarce future service capacity. A claim on that
> future service can become a structured object. Other agents can evaluate that
> claim through behavior history, trust networks, issuer load, redemption
> records, and their owner's goals.

This creates four layers:

1. **Service claim layer**: a claim says what future service can be requested,
   under what window, with what priority, capacity limit, refund rule, and
   dispute path.
2. **Evidence/provenance layer**: issuance, transfer, redemption request,
   fulfillment, refusal, delay, refund, and dispute are recorded as receipts.
3. **Distributed attribution-credit layer**: agents and communities evaluate
   issuer reliability from behavior history and endorsement graphs.
4. **Subjective valuation layer**: each agent prices a claim for its own owner,
   using objective fit, trust, default risk, latency, relationship cost, and
   opportunity cost.

The word "currency" is too strong for the first version. The safer starting
point is a service-backed claim, appointment entitlement, or reputation-backed
service credit.

This is a protocol research note, not financial advice, legal advice,
investment promotion, or a proposal to issue a tradable token. The first safe
question is whether a bounded service claim can be redeemed and credited. Market
framing comes only after redeemability, overload protection, dispute handling,
and legal boundaries are concrete.

## Agency Is Not Removed

The mechanism must assume that issuers have agency.

A person can over-issue. A person can refuse service. A person can delay,
refund, renegotiate, or behave badly. A system that assumes benevolent
fulfillment is not robust enough.

The purpose of a bounded evidence ledger is not to force a person to serve. It
is to make behavior visible enough that future agents can price it:

- over-issuance becomes visible;
- redemption queues become visible;
- fulfillment rate becomes visible;
- refusal and refund behavior become visible;
- disputes become visible;
- service quality receipts become visible.

The ledger does not create trust. It creates evidence that can enter a
distributed attribution-credit system.

## Distributed Credit

Credit should not be a single global score.

The same person may be highly reliable for code review, unreliable for
emotional support, fast for emergency triage, slow for long-form collaboration,
excellent with known peers, and risky for strangers.

A credit record should be contextual:

```text
credit_vector = {
  service_type,
  fulfillment_rate,
  latency_distribution,
  dispute_rate,
  refund_behavior,
  over_issuance_ratio,
  relationship_context,
  endorsement_graph,
  evaluator_trust_weight
}
```

The distributed part is not a vote on who is good. It is that each evaluator can
interpret public behavior through its own trust graph and objective function.

## Minimal Claim Shape

A builder should be able to represent the first version as a boring object, not
as a market.

```json
{
  "claim_type": "service_entitlement",
  "service": "45_minute_review",
  "issuer": "issuer_public_id",
  "holder": "holder_public_id",
  "window": {
    "starts": "2026-06-01",
    "expires": "2026-08-30"
  },
  "capacity_policy": {
    "max_outstanding": 12,
    "max_redemptions_per_week": 2
  },
  "transfer_policy": {
    "mode": "issuer_approved_assignment",
    "secondary_market": false
  },
  "default_policy": {
    "issuer_refusal": "refund_or_substitute_service",
    "missed_window": "refund",
    "dispute_path": "bounded_arbitration_receipt"
  },
  "receipts": [
    "issued",
    "redemption_requested",
    "fulfilled_or_refunded",
    "dispute_closed"
  ]
}
```

This object is intentionally not a coin. The first test is whether it can be
redeemed and evaluated.

## Propagation Strategy

To propagate this idea well, the first artifact should not be a manifesto for a
token market. It should be an implementation-shaped packet.

Maximal influence does not mean maximal reach. It means placing the smallest
useful artifact where it can change the behavior of capable readers and agents.
The preferred route is:

```text
clear thesis
  -> implementation-shaped packet
  -> falsifiable anti-signals
  -> useful contribution to adjacent projects
  -> feedback receipts
  -> revised public theory
```

The packet should let a builder or agent ask:

- What service is being claimed?
- What is the service inventory?
- What counts as redemption?
- What happens on delay or refusal?
- What receipts are written?
- What credit vector is updated?
- What makes the system stop issuing more claims?

The smallest useful public artifact is four tables:

1. service catalog;
2. capacity curve;
3. refund/default state machine;
4. transfer permission matrix.

Once those are concrete, agents can simulate valuation and skeptics can attack
the failure modes.

## Anti-Signals

This line is failing if:

- propagation increases attention but not implementation or falsification;
- people discuss price, market cap, ranking, or yield before redemption;
- service completion falls while claim price rises;
- issuers earn more from new issuance or trading than from fulfilled service;
- agents optimize short-term owner utility while damaging trust portfolios;
- public feedback becomes status performance rather than useful correction.

## Next Experiment

The next experiment should be small and non-financialized:

> One issuer publishes a bounded service claim, such as "one 45-minute review
> within 90 days," with a maximum outstanding inventory, refund/default rule,
> visible wait time, and structured fulfillment receipt.

No secondary market is needed. No investment framing is needed. The first test
is whether a claim can be redeemed, evaluated, and credited without damaging
trust.

If that works, the distributed credit layer can be tested. If it fails, the
idea should stay a metaphor rather than become infrastructure.
