# EAZO App Handoff 2026

Public-safe handoff for a temporary EAZO -> Macheng -> Zhizi bridge.

Machine-readable artifact:

```text
https://machengshen.github.io/system-evolution-public/eazo-app-handoff-2026.json
```

Human-readable companion:

```text
https://machengshen.github.io/system-evolution-public/eazo-app-handoff-2026.html
```

## Intent

Build a lightweight mobile front door that lets Macheng capture intent, context,
and follow-up signals, then hands them to Zhizi through a receipt-gated
owner-review loop.

## First App Shape

- Capture: intent input, need selector, modality selector, compact context,
  submit, latest receipt strip.
- Receipt: receipt id, minimal state, owner-review marker, attach-context
  action.
- Attach Context: short follow-up note or screen context linked to the original
  receipt.

## Boundary

This artifact contains no secrets and authorizes no external action. EAZO must
not send messages, pay, book, publish, change accounts, handle credentials,
delete data, or make legal/medical/contract/public commitments. Those requests
must become owner-review-only receipts.
