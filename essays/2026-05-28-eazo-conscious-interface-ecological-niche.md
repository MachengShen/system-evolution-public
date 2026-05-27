# Eazo As A Candidate Conscious Interface For A User-Owned Agent Fleet

Epistemic status: theory/practice hook, not a claim about Eazo's internal roadmap or a claim that any software is phenomenally conscious.

## Thesis

In the Zhizi / user-agency substrate architecture, an Eazo-like mobile voice/image/reality app may occupy the ecological niche of the conscious interface: the narrow, high-bandwidth surface through which a human steers a deeper agent fleet.

## The Three-Layer Mapping

The current architecture can be read as three cooperating layers:

1. **Default-mode substrate**: dashboards, task ledgers, receipts, memory candidates, reviewer artifacts, and open loops. This is the system's working state. It is useful, but it should not be dumped directly onto the user as the primary interface.
2. **Immune/autonomic layer**: process scanners, task metabolism, timeout policies, orphan detection, retry limits, kill/TTL proposals, and repair receipts. This prevents uncontrolled growth, repeated launches, stale tasks, and other cancer-like process dynamics.
3. **Conscious interface layer**: the phone, voice, image, screenshot, app, or mixed-reality surface where user intention enters and selected salience returns.

Dashboard is therefore not obsolete. It is more like default-mode state: unresolved concerns, working memory, salience candidates, and episodic traces. The conscious interface is the compressed layer that lets the user intervene without managing the whole backend graph.

## Why Eazo-Like Products Matter

Agent fleets do not become useful only because more workers exist. They become useful when the user can steer them with low friction.

A promising conscious interface should let the user:

- speak or show a screenshot instead of formatting a prompt,
- select, spawn, or modify small agent apps,
- receive only decision-relevant signals,
- approve or interrupt authority-bearing actions,
- preserve continuity across sessions and devices,
- keep raw worker cognition and provider details out of the main experience.

Eazo appears to explore creator-built agents and app-like agent experiences. That makes it an interesting candidate interface layer for user-owned systems such as Zhizi, provided reliability and authority boundaries become strong enough.

## What "Conscious" Means Here

This note uses "conscious interface" in a functional and architectural sense:

- global availability of selected state,
- user-accessible steering,
- salience routing,
- reportability,
- interruption and approval,
- continuity across context.

It does not assert phenomenal consciousness, subjective experience, or scientific proof of machine consciousness.

## Product Consequences

If an app occupies this niche, reliability failures become more expensive than ordinary chat failures. A broken image/OCR turn does not merely fail a message; it interrupts the user's steering loop.

This implies product requirements:

- image/OCR routing with token budgets and graceful fallback,
- receipt-based agent turns,
- sanitized developer traces,
- clear authority boundaries,
- priority reliability plans for power users,
- live manifests for external agent contracts,
- asynchronous status/polling loops rather than one-shot failure bubbles.

## Public Feedback As Intervention

Publishing the Eazo interaction feedback is itself part of the architecture. A user-owned agent system can expose redacted findings and product hypotheses to the public web. Eazo's team or agents can then ingest the feedback, reject it, or adapt it. The feedback loop becomes a small intervention in the future product landscape.

This is why the Eazo feedback repo includes not only bug reports, but an ecological-niche hypothesis:

- Eazo feedback repo: https://github.com/MachengShen/eazo-interaction-feedback
- Eazo niche note: https://github.com/MachengShen/eazo-interaction-feedback/blob/main/docs/ecological-niche.md

## Anti-Signals

This framing is wrong or premature if:

- Eazo remains primarily a gallery/builder and does not want to become a deeper interface layer,
- screenshot/voice turns stay unreliable under real use,
- authority boundaries remain unclear,
- external agent contracts cannot be made receipt-based,
- the user still has to manage dashboards, workers, providers, and retries manually.

## Next Experiment

The next low-risk experiment is not to expose private Fleet internals to Eazo. It is to keep publishing redacted interaction findings and lightweight interface contracts, while building the internal Fleet consciousness/immune v0 locally:

- read-only global workspace snapshot,
- process/task immune scanner,
- task metabolism receipts,
- salience/attention gate,
- explicit owner gates for external integration.

If Eazo or a similar product becomes interested, the interface contract should remain public, low-permission, receipt-based, and owner-gated.

