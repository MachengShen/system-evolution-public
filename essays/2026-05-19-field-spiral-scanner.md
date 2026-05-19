# Field Spiral Scanner

Date: 2026-05-19

Public index: [Theory Mainline](../THEORY.md)

If scientific fields behave like public memory systems, their literature should
show more than monotonic growth. It should sometimes show recurrent phases:
expansion, conflict, consolidation, reactivation of older ideas, and renewed
expansion under a changed substrate.

Field Spiral Scanner is the first scouting instrument for that hypothesis.

## Thesis

Scientific literature can be treated as a dynamic memory graph. Papers,
citations, concepts, reviews, benchmarks, venues, and research groups form a
field-level substrate. If the General Learning Machine / sleep-consolidation
line is right, scientific fields should sometimes exhibit wake / sleep /
reawakening structure at the literature level.

## Operational Signals

The first scanner turns a field query into yearly metrics:

- **expansion**: paper volume growth, new concept ratio, concept diversity;
- **consolidation**: review/survey ratio, citation centralization, repeated
  concept reuse, top-term concentration;
- **reactivation**: older terms that disappear for a dormancy window and later
  return;
- **spiral score**: a rough composite that finds years worth historical
  inspection.

The score is not proof. It is a detector for places where human historical
reading should focus.

## First Anti-Signal

The first useful result was not a clean cycle. It was a boundary error.

Single search strings are not field definitions. For example:

- broad "deep learning" searches quickly mix method papers with medicine,
  biology, remote sensing, and other application literatures;
- "predictive coding" mixes neuroscience with genetics and coding-theory
  senses of "coding";
- adding terms like "brain" narrows the field, but does not remove all
  contamination.

This means the real object is a **query recipe**, not a single query.

The practical loop is:

```text
scan
  -> inspect top terms and reactivated terms
  -> identify ambiguity / contamination
  -> refine query recipe
  -> rescan
  -> historical reading around high-score years
```

The scanner itself therefore follows the theory: it needs prediction errors,
recipe updates, and consolidation.

## Why This Matters

If the spiral hypothesis becomes measurable, it can support three uses:

1. **Retrodiction**
   Test whether known scientific histories show replay, consolidation, and
   reactivation patterns.

2. **Navigation**
   Identify fields that may be near reawakening, where old ideas become newly
   powerful because the substrate changed.

3. **Intervention**
   Choose when to publish, cite, experiment, or organize collaborators so a
   latent reactivation becomes visible and useful.

## Next Iterations

The next scanner needs:

- include/exclude term filters for homonyms;
- multi-query recipes that union and intersect related scans;
- OpenAlex concept/topic filters once field identifiers are selected;
- old-paper reactivation, not only term reactivation;
- review/survey burst detection;
- embedding or topic drift;
- and comparison against a simple paper-count baseline.

## Source

The first version uses the OpenAlex Works API:

- https://docs.openalex.org/
- https://docs.openalex.org/api-entities/works
- https://docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication
