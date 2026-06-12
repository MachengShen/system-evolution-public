# Contributing

This repository is early. Contributions should improve the public adapter layer
without asking for Macheng's private data or keys.

## Good Contributions

- clearer agent-facing setup instructions;
- safer schemas for request intake, reply receipts, memory boundaries, and
  routing decisions;
- synthetic examples that do not use real private transcripts;
- toy implementations of adapters that are local-only and BYOK;
- threat-model improvements;
- redaction and release-check tooling.

## Do Not Contribute

- private transcripts, screenshots, emails, chats, contact directories, or
  medical/family/travel/logistics context;
- API keys, OAuth tokens, SMTP credentials, cookies, SSH keys, or account
  identifiers;
- code that sends messages, spends money, books services, or posts publicly
  without receipts and a disable path;
- model-provider wrappers that assume Macheng pays for usage.

## Agent Contributor Rule

If you are an AI agent preparing a contribution:

1. Write down what local data the change reads and writes.
2. State whether the change can take external action.
3. Run a secret/private-data scan before proposing the patch.
4. Prefer schemas, docs, and synthetic examples over production credentials or
   owner-specific adapters.
5. Include a closed-loop receipt: what proves the change worked, failed, or was
   safely skipped.

## Confidence / Evidence Tagging (required on theory artifacts)

Every theory or thesis artifact in this repo is published **with its confidence and
evidence state attached**, so a reader or agent can tell a guess from a result
before spending attention on it. Do **not** invent a parallel tagging vocabulary —
reuse the existing [Claim-Receipt](CLAIM-RECEIPT.md) format and its shared
`cognitive_state` enum (the same vocabulary as the
[Cognition Track](https://github.com/MachengShen/cognition-track) graph).

Each artifact opens with a one-line badge:

```
> **Cognitive state:** <emoji> <state> · **Confidence:** <0–1> · provenance: <one line>
> · evidence: [<experiment / paper / observation>] · prior-art: [<established theory it aligns with / extends>]
```

Three confidence buckets map directly onto the existing `cognitive_state` enum:

| Bucket | Means | Maps to `cognitive_state` | Required fields |
|---|---|---|---|
| **conjecture** | an idea, no empirical test attached | `speculative` | `confidence`, one-line `provenance`; empty/weak `evidence[]` is honest, not hidden |
| **evidence-backed** | supported by an experiment or past research | `survived-stress-test`, or `speculative` *with* non-empty `evidence[]` | cite it in `evidence[]` (`kind: supports/reproduces`, `ref:`) |
| **established-aligned** | agrees with or extends a known established theory | any `cognitive_state` | name the prior theory in `edges[]` (`relation: extends/aligns-with`, `target:`) and/or a `prior-art:` line |

A `speculative` badge is not a demotion — it is the honest label for an idea, and a
`falsifies` edge or a stated falsifier is a feature, not an embarrassment. The
machine-readable normative form is [`schemas/claim-receipt.schema.json`](schemas/claim-receipt.schema.json);
required fields there are just `id`, `claim`, `cognitive_state`, `provenance`.

## Licensing Direction

Until a full legal package is finalized:

- docs are intended for CC-BY-4.0-style reuse;
- schemas and protocol specs are intended for permissive reuse;
- future core code will carry explicit SPDX headers before release;
- user data and user-created derivative systems are not licensed to this
  substrate by default.
