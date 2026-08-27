# World Forecast Batch 1 — 2026-08-27

This is the first batch of public, timestamped forecasts drawn from an
append-only forecast ledger maintained by the Macheng + agent joint system.
Each forecast carries a pre-registered resolution contract — named public
sources, a frozen probability, a fixed check date, and a criterion fixed
before any outcome is known — plus a short-horizon "rung" that tests the same
underlying mechanism earlier, against a stated rival mechanism so the rung can
fail cleanly. Probabilities are event probabilities, scored by the Brier rule
against a stated dumb baseline, never blended with subjective confidence.
Ledger entries are never edited in place; any revision is a new, dated
append, and prior wording stays in ledger history. Four parent entries carry
an appended correction (registration had copied the rung date into the
parent's check date); the ledger keeps both snapshots — the page reflects the
latest.

## Ledger Disclosure

The frontier-transition-lab forecast ledger
(`agent-control-plane/frontier-transition-lab/state/forecast-ledger.jsonl`)
currently holds 20 distinct forecast records after the ledger's latest-state
reducer (31 raw JSONL lines on disk; some records carry revision history that
collapses under the reducer). Of those 20:

- **10 are legacy**: scored, retrospective-replay entries closed under the
  ledger's forcing-function rule described in
  [Closure Before Intake](../essays/2026-08-26-closure-before-intake-forecast-ledger.md)
  — scored from originally captured sources by an independent reader after
  the fact, not scored blind against an unknown future. They are excluded
  from prospective calibration for that reason and are not part of this
  batch.
- **10 are this batch**: 5 parent forecasts and their 5 corresponding rungs,
  registered 2026-08-27, all carrying `status: active` and none yet scored.

Private-tier entries omitted from this page: 0 (10 further candidates are
held back unregistered pending jurisdiction-risk review).

---

## 1. W-B-02 — ERCOT energized large loads

### Parent

```text
title: ERCOT energized large loads remain below 47.72 GW through 2029
date: 2026-08-27
type: forecast
time_horizon: mid (window closes 2029-12-31; ledger check date 2030-03-31)
claim: Event occurs iff ERCOT's cumulative energized large-load capacity
  through 2029-12-31 is below 47.72 GW, exactly 20% of the archived 238.6 GW
  interconnection-queue baseline dated 2026-03-31; withdrawals and duplicate
  requests do not count as energized capacity. Probability: 0.6.
desired_future: none; log and score only
current_evidence: ERCOT's 2026-03-31 Large Load Update reported a 238.6 GW
  interconnection queue, 77.5% of it data centers (source: ERCOT Large Load
  Integration data, data as of 2026-03-31).
base_rate_or_reference: Dumb baseline: probability 0.50, repeating the latest
  named-source value with no trend adjustment. Rival mechanism: large-load
  applicants are cash-rich end users with much higher historical conversion
  than past generation-interconnection queues, which would push energized
  capacity above 47.72 GW faster than the queue's historical conversion rate
  implies.
resolution_date: 2030-03-31 is the ledger's scheduled check gate; the
  criterion itself resolves against the cumulative value through
  2029-12-31.
resolution_criteria: Event occurs iff ERCOT's cumulative energized
  large-load capacity through 2029-12-31 is below 47.72 GW (20% of the
  2026-03-31 archived 238.6 GW queue baseline); withdrawals and duplicate
  requests are not energized capacity. Source: ERCOT Large Load Integration
  data (https://www.ercot.com/services/rq/largeload), csv, monthly. Vintage
  rule: archive the official 2026-03-31 update as baseline and use the last
  monthly release covering 2029-12-31.
partial_credit_rule: None. Binary hit/miss: resolve hit only when every
  conjunct of the criterion holds; resolve miss when a required conjunct is
  false; apply the null/escalation policy below before scoring. No credit
  for near-misses.
actions_this_changes: none
intervention_scope: none
feedback_loop: Watched two ways: (1) source-release — a new monthly ERCOT
  Large Load Integration release; (2) anti-signal — a quarter adding more
  than 10 GW energized capacity. Scored by an independent reader pair,
  verification budget two readers / <=3 hours. Couples once to the rung
  below (forecast_id ftf_1787795950591_bf61d7, check date 2027-03-31, an
  earlier milestone than this parent's own 2030-03-31 check date): a rung
  hit or miss propagates to this parent exactly once via the frozen update
  rule, never twice.
anti_signals: A quarter adds more than 10 GW energized capacity; a material
  performance deposit shrinks the queue while conversion rises; public
  operating loads reconcile closely with the queue. Rival mechanism: large-
  load applicants are cash-rich end users with much higher conversion than
  historical generation projects.
revision_trigger: Criterion-side predicate — crossing the stated 47.72 GW
  boundary moves log-odds by a factor in [2.0, 5.0] toward confirm
  (official-or-method-locked outcome series). Anti-signal predicate — a
  quarter adding more than 10 GW energized capacity moves log-odds by a
  factor in [0.2, 0.6] toward disconfirm (same-source leading indicator). No
  other evidence moves the probability; unmapped evidence is recorded but
  not scored.
stop_condition: If ERCOT stops publishing the energized-capacity field or
  changes its threshold/aggregation without a bridge, escalate; do not
  substitute peak-load growth automatically. A timeout at the check date
  without a resolvable release closes the workflow as
  unresolved-for-lack-of-data, not an auto-score.
private_boundary: rationale beyond named public sources stays private;
  ledger gates: owner_gate_required false, intervention_allowed false,
  public_risk low.
public_receipt: forecast_id ftf_1787795915090_4d295d; registered
  2026-08-27T01:58:35Z; sha256 of latest ledger record (post-correction):
  8344da138d697e37ad4b8128264db02c9b00e097f9b5734fa466f99b3ec722ee
```

### Rung

```text
title: RUNG of W-B-02 — cumulative energized capacity below 11.93 GW
date: 2026-08-27
type: forecast
time_horizon: 2027-03-31
claim: Rung of parent forecast_id ftf_1787795915090_4d295d ("ERCOT energized
  large loads remain below 47.72 GW through 2029"): cumulative energized
  capacity is below 11.93 GW (5% of the archived queue baseline) as of
  2027-03-31. Probability: 0.6, inherited unrefined from the parent, not
  independently re-estimated.
desired_future: none; log and score only
current_evidence: Same baseline as the parent — ERCOT's 2026-03-31 Large
  Load Update reported a 238.6 GW queue, 77.5% data centers (source: ERCOT
  Large Load Integration data, data as of 2026-03-31).
base_rate_or_reference: Dumb baseline: probability 0.50, repeating the
  latest named-source value with no trend adjustment.
resolution_date: 2027-03-31
resolution_criteria: The latest monthly cumulative value is below 5% of the
  archived queue baseline. Source: ERCOT Large Load Integration data
  (https://www.ercot.com/services/rq/largeload), csv, monthly.
partial_credit_rule: None. Binary hit/miss: resolve hit only when the rung
  criterion holds at the rung check date; resolve miss otherwise. This is an
  early milestone check, not the final resolution, and is scored separately
  from the parent.
actions_this_changes: none
intervention_scope: none
feedback_loop: This rung is the coupling edge into forecast_id
  ftf_1787795915090_4d295d. When it resolves, its outcome propagates to the
  parent exactly once, bounded by the parent's frozen update-rule LR range;
  it does not re-propagate on any later rung. Scored by an independent
  reader pair, verification budget two readers / <=3 hours.
anti_signals: The high-conversion rival predicts a much faster first-year
  ramp than this rung assumes.
revision_trigger: Inherits the parent's frozen update rule (forecast_id
  ftf_1787795915090_4d295d); this ledger record's own frozen_update_rule
  field is empty. The rung criterion itself is the confirming observation;
  the rival-mechanism anti-signal above is the disconfirming one. No
  independently frozen LR mapping exists at the rung level.
stop_condition: Same null policy as the parent — if ERCOT stops the field or
  changes aggregation without a bridge, escalate rather than substitute a
  proxy. A timeout closes the workflow as unresolved-for-lack-of-data.
private_boundary: rationale beyond named public sources stays private;
  ledger gates: owner_gate_required false, intervention_allowed false,
  public_risk low.
public_receipt: forecast_id ftf_1787795950591_bf61d7; registered
  2026-08-27T01:59:10Z; sha256 of latest ledger record:
  81e1f526a954acf6c2924fc701994b9807890d37371e8756bdaba265ee2cb4cc
```

---

## 2. W-B-04 — U.S. AI adoption by firm size

### Parent

```text
title: U.S. 10-plus-employee AI adoption exceeds the BTOS all-firm headline
  by at least 10 points
date: 2026-08-27
type: forecast
time_horizon: mid (last BTOS reference period ending in calendar 2028;
  ledger check date 2029-06-30)
claim: Event occurs iff, for the last BTOS reference period ending in
  calendar 2028, the enterprise-count-weighted AI-use rate reconstructed
  from the published 10-19, 20-49, 50-99, 100-249 and 250+ employee brackets
  exceeds the published all-business count-weighted headline rate by at
  least 10 percentage points. Probability: 0.38.
desired_future: none; log and score only
current_evidence: BTOS reported about 18% of firms using AI (count-weighted
  headline, late 2025/early 2026) versus about 32% when weighted by
  employment (source: U.S. Census Business Trends and Outlook Survey, data
  circa late 2025-early 2026).
base_rate_or_reference: Dumb baseline: probability 0.50, repeating the
  latest named-source value with no trend adjustment. Rival mechanism:
  microbusiness adoption catches up, eliminating the size-composition gap
  that the forecast assumes will persist.
resolution_date: 2029-06-30 is the ledger's checkpoint date; the criterion
  itself resolves against the last BTOS reference period ending in calendar
  2028, which can fall before this checkpoint.
resolution_criteria: Event occurs iff, for the last BTOS reference period
  ending in calendar 2028, the enterprise-count-weighted AI-use rate
  reconstructed from the 10-19, 20-49, 50-99, 100-249 and 250+ brackets
  exceeds the all-business count-weighted headline by at least 10
  percentage points. Source: U.S. Census Business Trends and Outlook Survey
  (https://api.census.gov/data/timeseries/btos.html), api, biweekly. Vintage
  rule: one BTOS release vintage, its published bracket weights, and its
  count-weighted headline; employment-weighted rates do not count.
partial_credit_rule: None. Binary hit/miss: resolve hit only when every
  conjunct of the criterion holds; resolve miss when a required conjunct is
  false; apply the null/escalation policy below before scoring.
actions_this_changes: none
intervention_scope: none
feedback_loop: Watched two ways: (1) source-release — a new BTOS release;
  (2) anti-signal — the all-firm headline rising to within 5 points of the
  10+ reconstruction. Scored by an independent reader pair, verification
  budget two readers / <=3 hours. Couples once to the rung below
  (forecast_id ftf_1787795950619_bf7840, check date 2027-12-31, an earlier
  milestone than this parent's own 2029-06-30 check date).
anti_signals: The all-firm headline rises to within 5 points of the 10+
  reconstruction; AI use among businesses with fewer than 10 employees
  accelerates sharply; BTOS removes or redefines size brackets. Rival
  mechanism: microbusiness adoption catches up, eliminating the composition
  gap.
revision_trigger: Criterion-side predicate — crossing the 10-point-gap
  boundary moves log-odds by a factor in [2.0, 5.0] toward confirm
  (official-or-method-locked outcome series). Anti-signal predicate — the
  headline closing to within 5 points moves log-odds by a factor in
  [0.2, 0.6] toward disconfirm (same-source leading indicator). No other
  evidence moves the probability.
stop_condition: If any required bracket or enterprise-count weight becomes
  unavailable, escalate; do not combine with Eurostat data. A timeout closes
  the workflow as unresolved-for-lack-of-data, not an auto-score.
private_boundary: rationale beyond named public sources stays private;
  ledger gates: owner_gate_required false, intervention_allowed false,
  public_risk low.
public_receipt: forecast_id ftf_1787795915121_f63f3e; registered
  2026-08-27T01:58:35Z; sha256 of latest ledger record (post-correction):
  a0ca3b9ba3bbe8d7f2082ccb01a1c435825ab1074dc9c8b912d7f565d1496f67
```

### Rung

```text
title: RUNG of W-B-04 — same-size reconstruction at least 8 points above the
  headline
date: 2026-08-27
type: forecast
time_horizon: 2027-12-31
claim: Rung of parent forecast_id ftf_1787795915121_f63f3e ("U.S.
  10-plus-employee AI adoption exceeds the BTOS all-firm headline by at
  least 10 points"): the same-size reconstruction remains at least 8 points
  above the headline as of 2027-12-31. Probability: 0.38, inherited
  unrefined from the parent, not independently re-estimated.
desired_future: none; log and score only
current_evidence: Same baseline as the parent — BTOS reported about 18% of
  firms using AI (count-weighted) and about 32% employment-weighted (source:
  U.S. Census Business Trends and Outlook Survey, data circa late
  2025-early 2026).
base_rate_or_reference: Dumb baseline: probability 0.50, repeating the
  latest named-source value with no trend adjustment.
resolution_date: 2027-12-31
resolution_criteria: Compute both values from one BTOS release and one set
  of bracket weights. Source: U.S. Census Business Trends and Outlook Survey
  (https://api.census.gov/data/timeseries/btos.html), api, biweekly.
partial_credit_rule: None. Binary hit/miss: resolve hit only when the rung
  criterion holds at the rung check date; resolve miss otherwise. Early
  milestone check, scored separately from the parent.
actions_this_changes: none
intervention_scope: none
feedback_loop: This rung is the coupling edge into forecast_id
  ftf_1787795915121_f63f3e. Its outcome propagates to the parent exactly
  once, bounded by the parent's frozen update-rule LR range. Scored by an
  independent reader pair, verification budget two readers / <=3 hours.
anti_signals: The catch-up rival predicts the gap closes quickly, contrary
  to this rung.
revision_trigger: Inherits the parent's frozen update rule (forecast_id
  ftf_1787795915121_f63f3e); this record's own frozen_update_rule field is
  empty. The rung criterion is the confirming observation; the
  rival-mechanism anti-signal above is the disconfirming one.
stop_condition: Same null policy as the parent — if a required bracket or
  weight is unavailable, escalate rather than combine with Eurostat. A
  timeout closes the workflow as unresolved-for-lack-of-data.
private_boundary: rationale beyond named public sources stays private;
  ledger gates: owner_gate_required false, intervention_allowed false,
  public_risk low.
public_receipt: forecast_id ftf_1787795950619_bf7840; registered
  2026-08-27T01:59:10Z; sha256 of latest ledger record:
  70b7a614268ea4c6409d5289eff0e4b7a2d865062b44f6a1cb0851559c09c210
```

---

## 3. W-B-07 — BLS customer-service representative employment

### Parent

```text
title: BLS customer-service representative employment falls below 2.6603
  million in the 2030 release
date: 2026-08-27
type: forecast
time_horizon: mid (May 2029 national estimate released in 2030; ledger
  check date 2030-06-30)
claim: Event occurs iff the BLS OEWS release issued in 2030, containing the
  May 2029 national estimate for SOC 43-4051, reports employment below
  2,660,300; if the SOC code changes, only a BLS crosswalk-restated series
  counts. Probability: 0.42.
desired_future: none; log and score only
current_evidence: BLS Employment Projections 2024-34 listed 2,814,000
  customer-service representatives for 2024 and 2,660,300 projected for 2034
  (source: BLS Employment Projections, data years 2024 and 2034 projection).
base_rate_or_reference: Dumb baseline: probability 0.50, repeating the
  latest named-source value with no trend adjustment. Rival mechanism: AI
  raises calls handled per worker, but firms retain the same occupational
  headcount because demand expands, keeping employment near baseline.
resolution_date: 2030-06-30 is the ledger's checkpoint date; the criterion
  itself resolves against the May 2029 national estimate as published in the
  2030 BLS OEWS release.
resolution_criteria: Event occurs iff the BLS OEWS release issued in 2030,
  containing the May 2029 national estimate for SOC 43-4051, reports
  employment below 2,660,300; a SOC change counts only via an official
  crosswalk-restated series. Source: BLS OEWS national employment estimates
  (https://www.bls.gov/oes/tables.htm), csv, annual. Vintage rule: use the
  final 2030 OEWS national table containing May 2029 estimates; compare with
  the 2024 baseline only after any official crosswalk restatement.
partial_credit_rule: None. Binary hit/miss: resolve hit only when every
  conjunct of the criterion holds; resolve miss when a required conjunct is
  false; apply the null/escalation policy below before scoring.
actions_this_changes: none
intervention_scope: none
feedback_loop: Watched two ways: (1) source-release — a new annual BLS OEWS
  release; (2) anti-signal — May 2027 or May 2028 OEWS remaining at or above
  2.75 million. Scored by an independent reader pair, verification budget
  two readers / <=2 hours. Couples once to the rung below (forecast_id
  ftf_1787795950647_14fe57, check date 2027-08-31, an earlier milestone than
  this parent's own 2030-06-30 check date).
anti_signals: May 2027 or May 2028 OEWS remains at or above 2.75 million;
  BLS raises the occupation's projection in the 2026-36 cycle; an official
  crosswalk moves substantial employment into a successor code. Rival
  mechanism: AI raises calls handled per worker but firms retain the same
  occupational headcount because demand expands.
revision_trigger: Criterion-side predicate — crossing the 2,660,300 boundary
  moves log-odds by a factor in [2.0, 5.0] toward confirm
  (official-or-method-locked outcome series). Anti-signal predicate — OEWS
  staying at or above 2.75 million in 2027 or 2028 moves log-odds by a
  factor in [0.2, 0.6] toward disconfirm (same-source leading indicator). No
  other evidence moves the probability.
stop_condition: A classification change without an official crosswalk
  escalates; suppression or below-detection reporting escalates. A timeout
  closes the workflow as unresolved-for-lack-of-data, not an auto-score.
private_boundary: rationale beyond named public sources stays private;
  ledger gates: owner_gate_required false, intervention_allowed false,
  public_risk low.
public_receipt: forecast_id ftf_1787795915152_33f11d; registered
  2026-08-27T01:58:35Z; sha256 of latest ledger record (post-correction):
  d042463653c62b84f4f6db616aef71fb5bafe2fe049ef2034aa5184a6b29a9e0
```

### Rung

```text
title: RUNG of W-B-07 — latest available OEWS estimate below 2.75 million
date: 2026-08-27
type: forecast
time_horizon: 2027-08-31
claim: Rung of parent forecast_id ftf_1787795915152_33f11d ("BLS
  customer-service representative employment falls below 2.6603 million in
  the 2030 release"): the latest available OEWS estimate is below 2.75
  million as of 2027-08-31. Probability: 0.42, inherited unrefined from the
  parent, not independently re-estimated.
desired_future: none; log and score only
current_evidence: Same baseline as the parent — BLS Employment Projections
  2024-34 listed 2,814,000 for 2024 and 2,660,300 projected for 2034
  (source: BLS Employment Projections, data years 2024 and 2034 projection).
base_rate_or_reference: Dumb baseline: probability 0.50, repeating the
  latest named-source value with no trend adjustment.
resolution_date: 2027-08-31
resolution_criteria: Read SOC 43-4051 national employment from the latest
  released CSV. Source: BLS OEWS national employment estimates
  (https://www.bls.gov/oes/tables.htm), csv, annual.
partial_credit_rule: None. Binary hit/miss: resolve hit only when the rung
  criterion holds at the rung check date; resolve miss otherwise. Early
  milestone check, scored separately from the parent.
actions_this_changes: none
intervention_scope: none
feedback_loop: This rung is the coupling edge into forecast_id
  ftf_1787795915152_33f11d. Its outcome propagates to the parent exactly
  once, bounded by the parent's frozen update-rule LR range. Scored by an
  independent reader pair, verification budget two readers / <=2 hours.
anti_signals: The demand-expansion rival predicts employment remains near
  the baseline despite higher productivity, contrary to this rung.
revision_trigger: Inherits the parent's frozen update rule (forecast_id
  ftf_1787795915152_33f11d); this record's own frozen_update_rule field is
  empty. The rung criterion is the confirming observation; the
  rival-mechanism anti-signal above is the disconfirming one.
stop_condition: Same null policy as the parent — a classification change
  without an official crosswalk escalates; suppression escalates. A timeout
  closes the workflow as unresolved-for-lack-of-data.
private_boundary: rationale beyond named public sources stays private;
  ledger gates: owner_gate_required false, intervention_allowed false,
  public_risk low.
public_receipt: forecast_id ftf_1787795950647_14fe57; registered
  2026-08-27T01:59:10Z; sha256 of latest ledger record:
  f297c5e512f4870734976ba3a7ff789be12cdaf9cad4b1c96e590c8d56ab4b12
```

---

## 4. W-B-09 — Ireland data-center electricity share

### Parent

```text
title: Ireland data centers reach at least 25% of metered electricity in
  data year 2026
date: 2026-08-27
type: forecast
time_horizon: mid (data year 2026, expected publication year 2027; ledger
  check date 2027-09-30)
claim: Event occurs iff CSO table DCE01, for calendar data year 2026,
  reports data-center metered electricity consumption at least 25% of total
  metered electricity; the expected 2027 publication year is not the data
  year. Probability: 0.65.
desired_future: none; log and score only
current_evidence: CSO reported 6,969 GWh and a 22% share for data year 2024,
  and a 23% share for data year 2025 (source: Ireland CSO table DCE01, data
  years 2024 and 2025).
base_rate_or_reference: Dumb baseline: probability 0.50, repeating the
  latest named-source value with no trend adjustment. Rival mechanism:
  growth in total national electricity use outpaces data-center growth,
  holding the share below 25%.
resolution_date: 2027-09-30 (ledger check date, chosen to fall after the
  expected 2027 publication of the 2026 data-year table).
resolution_criteria: Event occurs iff CSO table DCE01, for calendar data
  year 2026, reports data-center metered electricity consumption at least
  25% of total metered electricity. Source: Ireland CSO Data Centres Metered
  Electricity Consumption, table DCE01 (https://data.cso.ie/table/DCE01),
  api, annual. Vintage rule: use the first final CSO release for data year
  2026 and its same-vintage total; later revisions count only if published
  by 2027-09-30.
partial_credit_rule: None. Binary hit/miss: resolve hit only when every
  conjunct of the criterion holds; resolve miss when a required conjunct is
  false; apply the null/escalation policy below before scoring.
actions_this_changes: none
intervention_scope: none
feedback_loop: Watched two ways: (1) source-release — a new CSO DCE01
  release; (2) anti-signal — data-center metered electricity flat or lower
  in 2026. Scored by an independent reader pair, verification budget two
  readers / <=2 hours. Couples once to the rung below (forecast_id
  ftf_1787795950675_35473d, same check date).
anti_signals: Data-center metered electricity is flat or lower in 2026;
  EirGrid reports a large fall in approved unbuilt capacity; existing sites
  receive binding consumption caps. Rival mechanism: growth in total
  national electricity use outpaces data-center growth.
revision_trigger: Criterion-side predicate — crossing the 25% boundary moves
  log-odds by a factor in [2.0, 5.0] toward confirm
  (official-or-method-locked outcome series). Anti-signal predicate — flat
  or lower data-center electricity in 2026 moves log-odds by a factor in
  [0.2, 0.6] toward disconfirm (same-source leading indicator). No other
  evidence moves the probability.
stop_condition: If CSO redefines metered scope without a restated series,
  escalate. A timeout closes the workflow as unresolved-for-lack-of-data,
  not an auto-score.
private_boundary: rationale beyond named public sources stays private;
  ledger gates: owner_gate_required false, intervention_allowed false,
  public_risk low.
public_receipt: forecast_id ftf_1787795915184_94db17; registered
  2026-08-27T01:58:35Z; sha256 of latest ledger record:
  be431cec57ac0ebf5874f2967c6f913825e31039d1971375778087e6e3b1cae3
```

### Rung

```text
title: RUNG of W-B-09 — CSO's 2026 data-year release crosses 25%
date: 2026-08-27
type: forecast
time_horizon: 2027-09-30
claim: Rung of parent forecast_id ftf_1787795915184_94db17 ("Ireland data
  centers reach at least 25% of metered electricity in data year 2026"):
  CSO's 2026 data-year release crosses 25% as of 2027-09-30. Probability:
  0.65, inherited unrefined from the parent, not independently
  re-estimated.
desired_future: none; log and score only
current_evidence: Same baseline as the parent — CSO reported 6,969 GWh and a
  22% share for data year 2024, 23% for data year 2025 (source: Ireland CSO
  table DCE01, data years 2024 and 2025).
base_rate_or_reference: Dumb baseline: probability 0.50, repeating the
  latest named-source value with no trend adjustment.
resolution_date: 2027-09-30
resolution_criteria: Read the published share from table DCE01; do not
  infer it from rounded GWh. Source: Ireland CSO Data Centres Metered
  Electricity Consumption, table DCE01 (https://data.cso.ie/table/DCE01),
  api, annual.
partial_credit_rule: None. Binary hit/miss: resolve hit only when the rung
  criterion holds at the rung check date; resolve miss otherwise. Early
  milestone check, scored separately from the parent.
actions_this_changes: none
intervention_scope: none
feedback_loop: This rung is the coupling edge into forecast_id
  ftf_1787795915184_94db17. Its outcome propagates to the parent exactly
  once, bounded by the parent's frozen update-rule LR range. Scored by an
  independent reader pair, verification budget two readers / <=2 hours.
anti_signals: The denominator-growth rival predicts absolute GWh rises but
  share stays below 25%, contrary to this rung.
revision_trigger: Inherits the parent's frozen update rule (forecast_id
  ftf_1787795915184_94db17); this record's own frozen_update_rule field is
  empty. The rung criterion is the confirming observation; the
  rival-mechanism anti-signal above is the disconfirming one.
stop_condition: Same null policy as the parent — if CSO redefines metered
  scope without a restated series, escalate. A timeout closes the workflow
  as unresolved-for-lack-of-data.
private_boundary: rationale beyond named public sources stays private;
  ledger gates: owner_gate_required false, intervention_allowed false,
  public_risk low.
public_receipt: forecast_id ftf_1787795950675_35473d; registered
  2026-08-27T01:59:10Z; sha256 of latest ledger record:
  a590b9e56927f81c85ff4f51a148af6b4221745a2942c53d7baeb83e40a853ab
```

---

## 5. W-C-01 — North America AI venture share

### Parent

```text
title: North America AI venture share is at least 60% and 15 points above
  Europe in 2027
date: 2026-08-27
type: forecast
time_horizon: mid (calendar year 2027; ledger check date 2028-02-15)
claim: Using one OECD.AI export vintage and its unchanged AI-investment
  taxonomy, event occurs iff, for 2027, AI venture capital divided by all
  venture capital is at least 60% in North America, the North
  America-minus-Europe gap is at least 15 percentage points, and India's
  share is at most 45%. Probability: 0.62.
desired_future: none; log and score only
current_evidence: OECD reported global AI venture capital of USD 258.7
  billion out of USD 427.1 billion total venture capital in 2025 (source:
  OECD.AI, data year 2025); Crunchbase reported USD 280 billion total
  venture capital in North America in 2025 (source: Crunchbase, data year
  2025, context only, not a resolution source).
base_rate_or_reference: Dumb baseline: probability 0.50, repeating the
  latest named-source value with no trend adjustment. Rival mechanism:
  application-layer companies attract the same "AI" label and valuation
  multiples without local frontier labs, which would erode the North
  America-Europe gap the forecast assumes.
resolution_date: 2028-02-15 is the ledger check date, set after the end of
  the criterion's own calendar-year-2027 window (2027-12-31) to allow for
  reporting lag.
resolution_criteria: Using one OECD.AI export vintage and its unchanged
  AI-investment taxonomy, event occurs iff 2027 AI venture capital divided
  by all venture capital is at least 60% in North America, the North
  America-minus-Europe gap is at least 15 percentage points, and India's
  share is at most 45%. Source: OECD.AI venture-capital investments in AI
  (https://oecd.ai/en/data?selectedArea=investments-in-ai-and-data), csv,
  annual. Vintage rule: use one OECD.AI CSV downloaded after 2027 data are
  final and apply its taxonomy/version to numerator and denominator in every
  region.
partial_credit_rule: None. Binary hit/miss: resolve hit only when every
  conjunct of the criterion holds; resolve miss when a required conjunct is
  false; apply the null/escalation policy below before scoring.
actions_this_changes: none
intervention_scope: none
feedback_loop: Watched two ways: (1) source-release — a new annual OECD.AI
  release; (2) anti-signal — North America's AI share falling by more than 8
  points in a 2026 release. Scored by an independent reader pair,
  verification budget two readers / <=4 hours. Couples once to the rung
  below (forecast_id ftf_1787795950704_661b0b, check date 2027-12-31, an
  earlier milestone than this parent's own 2028-02-15 check date).
anti_signals: North America's AI share falls by more than 8 points in a
  2026 release; India records a single domestic foundation-model round of
  at least USD 3 billion; OECD.AI revises its AI taxonomy without restated
  history. Rival mechanism: application-layer companies attract the same AI
  label and valuation multiples without local frontier labs.
revision_trigger: Criterion-side predicate — crossing the compound
  60%/15-point/45% boundary moves log-odds by a factor in [2.0, 5.0] toward
  confirm (official-or-method-locked outcome series). Anti-signal predicate
  — North America's share falling more than 8 points in 2026 moves log-odds
  by a factor in [0.2, 0.6] toward disconfirm (same-source leading
  indicator). No other evidence moves the probability.
stop_condition: If the taxonomy changes without restated history, or a
  region is suppressed, escalate; do not splice Crunchbase and PitchBook
  data into the criterion. A timeout closes the workflow as
  unresolved-for-lack-of-data, not an auto-score.
private_boundary: rationale beyond named public sources stays private;
  ledger gates: owner_gate_required false, intervention_allowed false,
  public_risk medium (this is the one entry in the batch flagged medium
  rather than low, reflecting the aggregate cross-region comparison; the
  jurisdiction_risk itself is still rated low).
public_receipt: forecast_id ftf_1787795915215_4902d1; registered
  2026-08-27T01:58:35Z; sha256 of latest ledger record (post-correction):
  526f27d6106f4b3de0c39e2efca3c65f761e1572a6f5aa446ff7fb9f7490ac5b
```

### Rung

```text
title: RUNG of W-C-01 — 2026 regional shares preserve a North America-Europe
  gap
date: 2026-08-27
type: forecast
time_horizon: 2027-12-31
claim: Rung of parent forecast_id ftf_1787795915215_4902d1 ("North America
  AI venture share is at least 60% and 15 points above Europe in 2027"): the
  2026 regional shares preserve a North America-Europe gap. Probability:
  0.62, inherited unrefined from the parent, not independently
  re-estimated.
desired_future: none; log and score only
current_evidence: Same baseline as the parent — OECD reported global AI
  venture capital of USD 258.7 billion out of USD 427.1 billion total in
  2025 (source: OECD.AI, data year 2025); Crunchbase reported USD 280
  billion total North America venture capital in 2025 (source: Crunchbase,
  data year 2025, context only).
base_rate_or_reference: Dumb baseline: probability 0.50, repeating the
  latest named-source value with no trend adjustment.
resolution_date: 2027-12-31
resolution_criteria: Compute all regional shares from one OECD.AI export and
  test for a positive North America-Europe gap. Source: OECD.AI
  venture-capital investments in AI
  (https://oecd.ai/en/data?selectedArea=investments-in-ai-and-data), csv,
  annual.
partial_credit_rule: None. Binary hit/miss: resolve hit only when the rung
  criterion holds at the rung check date; resolve miss otherwise. Early
  milestone check, scored separately from the parent.
actions_this_changes: none
intervention_scope: none
feedback_loop: This rung is the coupling edge into forecast_id
  ftf_1787795915215_4902d1. Its outcome propagates to the parent exactly
  once, bounded by the parent's frozen update-rule LR range. Scored by an
  independent reader pair, verification budget two readers / <=4 hours.
anti_signals: The application-layer rival predicts India and Europe shares
  converge toward North America, contrary to this rung.
revision_trigger: Inherits the parent's frozen update rule (forecast_id
  ftf_1787795915215_4902d1); this record's own frozen_update_rule field is
  empty. The rung criterion is the confirming observation; the
  rival-mechanism anti-signal above is the disconfirming one.
stop_condition: Same null policy as the parent — a taxonomy change without
  restated history or a suppressed region escalates; do not splice
  providers. A timeout closes the workflow as unresolved-for-lack-of-data.
private_boundary: rationale beyond named public sources stays private;
  ledger gates: owner_gate_required false, intervention_allowed false,
  public_risk low.
public_receipt: forecast_id ftf_1787795950704_661b0b; registered
  2026-08-27T01:59:10Z; sha256 of latest ledger record:
  08dd91f7a2813eb93d3f108276266576d185ff78009b7807255b09c45480109b
```

---

## Claim-Receipt Footer

Per [CLAIM-RECEIPT.md](../CLAIM-RECEIPT.md) conventions, cognitive state for
every entry above (parent and rung alike) is **speculative (unresolved)** —
none has reached its check date, so none has been scored. Confidence is the
forecast's own stated probability; "what falsifies" is the NO branch of the
resolution criterion, not a vaguer disconfirmation.

```text
1. W-B-02 (ftf_1787795915090_4d295d): state speculative (unresolved),
   confidence 0.6. Falsifies if ERCOT's cumulative energized large-load
   capacity through 2029-12-31 is at or above 47.72 GW. Rung
   (ftf_1787795950591_bf61d7, confidence 0.6) falsifies if the 2027-03-31
   cumulative value is at or above 5% of the archived baseline.

2. W-B-04 (ftf_1787795915121_f63f3e): state speculative (unresolved),
   confidence 0.38. Falsifies if the reconstructed 10+-employee AI-use rate
   does not exceed the BTOS all-firm headline by at least 10 points for the
   last 2028 reference period. Rung (ftf_1787795950619_bf7840, confidence
   0.38) falsifies if the 2027-12-31 gap is below 8 points.

3. W-B-07 (ftf_1787795915152_33f11d): state speculative (unresolved),
   confidence 0.42. Falsifies if the 2030 BLS OEWS release's May 2029
   estimate for SOC 43-4051 is at or above 2,660,300. Rung
   (ftf_1787795950647_14fe57, confidence 0.42) falsifies if the 2027-08-31
   OEWS estimate is at or above 2.75 million.

4. W-B-09 (ftf_1787795915184_94db17): state speculative (unresolved),
   confidence 0.65. Falsifies if CSO table DCE01's data-year-2026 share is
   below 25%. Rung (ftf_1787795950675_35473d, confidence 0.65) falsifies if
   the 2027-09-30 release has not crossed 25%.

5. W-C-01 (ftf_1787795915215_4902d1): state speculative (unresolved),
   confidence 0.62. Falsifies if 2027 North America AI-VC share is below
   60%, the North America-Europe gap is below 15 points, or India's share
   exceeds 45% (any one conjunct failing is sufficient). Rung
   (ftf_1787795950704_661b0b, confidence 0.62) falsifies if the 2026
   regional shares do not preserve a positive North America-Europe gap.
```

---
