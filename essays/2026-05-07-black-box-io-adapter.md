# The Black-Box I/O Adapter Principle

Closed-source tools do not have to be fully controllable to become useful parts of an agent system.

If a tool is a black box, wrap its input and output boundaries.

```
human intent + context
  -> input adapter
  -> black-box tool
  -> output adapter
  -> agent memory / action / user interface
```

The point is not to modify the closed-source tool internally. The point is to make its behavior composable, auditable, and replaceable from the outside.

## Why This Matters

Modern personal AI systems inevitably depend on closed or semi-closed tools: dictation apps, messaging apps, email clients, hotel and concierge systems, AR glasses, mobile operating systems, model-provider APIs, payment systems, and identity systems.

Waiting for every layer to become open and programmable is not realistic. But treating every closed tool as an untouchable endpoint is also too weak.

The practical move is to control the boundary.

## Dictation As A Concrete Example

An AI dictation tool can be useful because it turns speech into text everywhere.

But it can also be dangerous as a ground-truth layer because many dictation systems optimize for polished writing. They may remove uncertainty, rewrite terminology, or infer a cleaner intention than the speaker actually had.

The adapter solution is:

1. Keep a canonical terminology lexicon.
2. Preserve raw audio when possible.
3. Capture the tool's output.
4. Correct known terms and names.
5. Detect likely intent drift.
6. Send downstream agents both the corrected text and the uncertainty metadata.

This makes the dictation app a component, not the cognitive authority.

## Input Adapter

Before a black-box tool receives input, add the missing context and constraints where possible:

- current task mode,
- target app,
- domain terminology,
- user preference,
- permission boundary,
- allowed transformations,
- whether polishing is allowed.

If the tool does not accept prompts or custom settings, store the context beside the event so downstream systems can interpret the output correctly.

## Output Adapter

After the black-box tool emits output, do not trust it blindly:

- normalize terminology,
- preserve uncertainty,
- compare with raw input where possible,
- classify confidence,
- detect drift from the user's likely intent,
- log evidence for later audit,
- route only the actionable result forward.

## Boundary Control Is Cognitive Control

A personal AI system is not only a pile of tools. It is a cognitive boundary manager.

It decides what enters the user's attention, what stays in the background, what becomes memory, and what becomes action.

Closed-source software is just another information barrier. If we cannot see inside it, we can still decide what it receives, how its output is interpreted, when it is trusted, when it is bypassed, and how it can be replaced.

## Design Rule

For closed-source or unreliable tools:

> Do not treat the tool's output as truth. Treat it as a signal emitted by a black box, then wrap it with context, correction, memory, and verification.

This principle applies to dictation tools, chat apps, email, AR glasses, mobile OS integrations, and external services.

