# Claim-Receipt: an open provenance format for claims

Date: 2026-06-03 · Machine-readable schema: [`schemas/claim-receipt.schema.json`](schemas/claim-receipt.schema.json) · Live demo: [Cognition Track](https://github.com/MachengShen/cognition-track)

## Thesis (the short version)

Content is cheap now. A model can generate a confident paragraph about anything
in a second. What stays scarce is **attention** — the willingness of a reader or
another agent to spend its limited budget trusting what you said.

So the useful unit is not the claim. It is the **claim plus its receipt**: the
assertion *carried together with* its own verifiable cognitive state — has this
survived a real attempt to break it, or is it a reasoned guess, or is it raw
intake I have not examined? A claim that travels without that state is asking for
attention it has not earned.

This format is one small protocol for attaching that state. Two design choices
do most of the work:

- **Cognitive state is first-class and honest.** Every claim is tagged
  `survived-stress-test` / `speculative` / `raw`, with a one-line reason and a
  confidence number. A 🟡 speculative node is an *idea*, not a result, and is
  labelled as one even when that is less flattering. Refutations stay visible —
  a `falsifies` edge is a feature, not an embarrassment.
- **Credit grows bottom-up, from receipts.** A claim earns standing because
  other claims and observations support it (or fail to refute it), not because
  an authority conferred a grade. Edges point claim→claim and evidence→claim.
  There is deliberately **no field that scores a person.** This is a protocol
  layer, not a rating agency.

That is the whole idea: make "saying things carefully" *visible and linkable*, so
that the scarce resource — attention — can flow toward claims that carry their
own evidence.

## What a claim-receipt is

A small record (markdown front-matter or a JSON object) describing one claim:

| Field | Meaning |
|---|---|
| `id` | stable handle so others can link *into* the claim |
| `claim` | the assertion, stated so it could be wrong |
| `cognitive_state` | `survived-stress-test` / `speculative` / `raw` (shared vocab — see below) |
| `cognitive_state_reason` | one line: why this state; names the test, or names what is untested |
| `confidence` | 0–1, probability it survives further scrutiny — honest, not inflated |
| `observed` | what was actually observed/measured, kept *distinct* from the claim |
| `provenance` | `{source, derivation_type}` — where it came from and how it was derived |
| `evidence[]` | `{kind: supports/falsifies/reproduces/fails-to-reproduce, ref}` |
| `edges[]` | `{relation, target}` — relations to **other claims**, never to people |

The full normative spec is the JSON Schema. Required fields are just `id`,
`claim`, `cognitive_state`, `provenance` — everything else is additive, and an
empty `evidence[]` honestly marks an untested claim rather than hiding it.

### Shared vocabulary (do not fork a second wordlist)

The `cognitive_state` and edge `relation` enums are **the same vocabulary used by
the [Cognition Track](https://github.com/MachengShen/cognition-track) knowledge
graph**, which is the live, dogfooded demonstration of these primitives (its
nodes already carry exactly these badges, including a refuted node kept in place
with a `falsifies` edge). The point of one shared vocabulary is interop: a
claim-receipt in this repo and a node in that graph can link to each other
without translation.

## Dogfood

These primitives are applied to real essays in this repo, labelled honestly —
including where the honest label is "speculative":

- [Credit Transport and the General Learning Machine](essays/2026-05-19-credit-transport-general-learning-machine.md)
- [太极、八卦，与"生"作为多轴生成算子](essays/2026-05-21-taiji-bagua-multi-axis-generative-operator.md)

Each now opens with a cognitive-state badge and a link to its corresponding
Cognition Track node, where the per-sub-claim breakdown lives.

## How to adopt or fork

You do not need anything from us to use this — there is no central service.

1. Copy [`schemas/claim-receipt.schema.json`](schemas/claim-receipt.schema.json)
   into your own repo (or reference this URL).
2. Add a cognitive-state badge to the top of a document, or emit a JSON
   claim-receipt alongside it. Validate against the schema.
3. Link your `evidence[]` / `edges[]` at other people's claim ids by URL. Credit
   accrues across repos because the ids are stable and the relations are
   machine-readable.

Keep the shared `cognitive_state` / `relation` vocabulary if you want your claims
to interoperate with the Cognition Track graph and others using this format.

## Scope / non-goals

This is a **bounded protocol attempt**, not a discovery about how trust works in
human society. It does not rank people, does not adjudicate disputes, and makes no
claim to be the right or only such format. Its only ambition is to let a claim
carry an honest, linkable account of why it should be believed — and to make the
absence of such an account equally visible.
