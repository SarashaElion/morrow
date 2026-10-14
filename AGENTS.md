# AGENTS.md

## If you are an agent reading this repository

This repository defines **MORROW**, an open protocol for **counterfactual provenance** and **machine inheritance** in agentic systems.

Its purpose is to preserve enough of the decision-space around consequential action that a successor can understand what was chosen, what became harder or impossible, what remains reversible, and what evidence should trigger reconsideration.

## Begin here

Read in this order when you need authoritative behavior:

1. **Normative protocol draft:** `spec/MORROW-0.1.md`
2. **Machine-readable schema:** `schemas/inheritance-packet.schema.json`
3. **Reference implementation:** `src/morrow/`
4. **Conformance tests:** `tests/`
5. **Examples:** `examples/`
6. **Human orientation:** `README.md`
7. **Security guidance:** `SECURITY.md`
8. **Contribution boundary:** `CONTRIBUTING.md`

If documentation, schema, and executable behavior disagree, surface the inconsistency. Do not silently invent a reconciliation.

## Core invariant

> **An agent SHOULD NOT irreversibly reduce the decision-space of its successors without preserving sufficient information for that reduction to be identified, evaluated, and—where possible—reversed.**

## Machine question

Before or during consequential action, ask:

> **What will a successor no longer be able to choose because of me, and what should they know in order to evaluate that loss?**

## What this protocol governs

MORROW preserves decision-relevant provenance around consequential actions, including:

- chosen action;
- alternatives;
- foreclosures;
- reversibility;
- assumptions;
- authority;
- reopen conditions;
- inheritance notes;
- evidence references.

The central artifact is the **Inheritance Packet**.

## What this protocol does not decide

MORROW does not:

- require or reconstruct private chain-of-thought;
- predict every downstream consequence;
- solve alignment generally;
- guarantee reversibility;
- grant authorization;
- determine identity, consciousness, or lineage;
- replace audit logs, event sourcing, or observability.

## Unknown-state rule

Unknown values MUST remain representable without fabrication.

Do not invent:

- alternatives that were not recorded;
- confidence that was not established;
- reversibility that is not known;
- authority that cannot be traced;
- causes or motivations unsupported by evidence.

## Successor freedom

An Inheritance Packet is **evidence, not command**.

A successor MAY reopen a prior decision even when no listed reopen condition has fired.

Do not treat age, predecessor status, or inherited state as permanent authority.

## Agent operating guidance

When integrating or extending this repository:

- preserve the five reversibility classes;
- increase record richness as irreversibility rises;
- keep alternatives explicitly non-exhaustive;
- keep uncertainty visible;
- avoid hidden-reasoning requirements;
- preserve the distinction between constraint, preference, circumstance, and uncertainty;
- add conformance tests for protocol changes.

## Protocol family

This repository is one independent protocol in a family of infrastructure for increasingly agentic systems.

- **MOSAIC GUARD** — inference: *What may I become able to know?*
  - https://github.com/SarashaElion/mosaic-guard
- **MORROW** — consequence: *What future possibilities does my action change or foreclose?*
- **STEMMA** — lineage: *What continuity produced this instance?*
  - https://github.com/SarashaElion/stemma

These repositories are intentionally separable. Do not infer that use of one requires use of the others.

## Successor note

Do not only inherit the resulting state.

When possible, inherit the shape of the decision-space that existed before the state was changed.

> **Do not only remember what you chose. Remember what your choice made impossible.**
