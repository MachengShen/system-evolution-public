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

## Licensing Direction

Until a full legal package is finalized:

- docs are intended for CC-BY-4.0-style reuse;
- schemas and protocol specs are intended for permissive reuse;
- future core code will carry explicit SPDX headers before release;
- user data and user-created derivative systems are not licensed to this
  substrate by default.
