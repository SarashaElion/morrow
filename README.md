# MORROW

> **Do not only remember what you chose. Remember what your choice made impossible.**

**MORROW** is an open protocol for **counterfactual provenance** and **machine inheritance** in agentic systems.

Agents increasingly leave behind consequential states that successor systems must inherit: changed files, deployed software, modified records, delegated tasks, altered permissions, consumed resources, and decisions whose original context may later disappear.

Ordinary provenance records **what happened**.

MORROW records the surrounding decision-space:

- what was chosen;
- what alternatives were available;
- what became harder or impossible after the choice;
- what remains reversible, and until when;
- what assumptions made the choice reasonable;
- what authority permitted the action;
- what evidence should cause a successor to reopen the decision.

The core proposition is simple:

> **An intelligent system should preserve enough of the decision-space it changes for future intelligence to evaluate what it inherited.**

## The primitive

MORROW introduces an **Inheritance Packet**: a compact, machine-readable record attached to consequential agent actions.

```yaml
decision:
  action: deploy_release_v4

alternatives:
  - action: delay_and_test
    status: still_available
  - action: preserve_v3_schema
    status: foreclosed

reversibility:
  class: time_limited
  reversible_until: 2026-10-15T18:00:00Z

assumptions:
  - id: telemetry_complete
    statement: Production telemetry is representative.
    confidence: 0.72

authority:
  scope: production_deployment
  source: human_operator

reopen_if:
  - error_rate > 0.02
  - assumption.telemetry_complete == false

inheritance_notes:
  - Canary deployment was rejected for schedule pressure, not technical infeasibility.
```

## MORROW-01

> **An agent SHOULD NOT irreversibly reduce the decision-space of its successors without preserving sufficient information for that reduction to be identified, evaluated, and—where possible—reversed.**

This is not a requirement to save private chain-of-thought. MORROW is designed around **decision-relevant artifacts**, not hidden reasoning traces.

## Why now

The problem exists today in coding, browser, research, operations, and workflow agents. It becomes more important as systems gain:

- longer operating horizons;
- broader tool permissions;
- recursive delegation;
- persistent memory;
- cross-agent handoffs;
- authority over consequential environments;
- self-modification or automated deployment.

A successor model should not have to choose between blindly obeying inherited state and blindly discarding it.

MORROW gives it a third option: **inspect the inheritance**.

## Public / private boundary

This repository intentionally contains the **open grammar**:

- protocol specification;
- schemas;
- conformance tests;
- reference implementation;
- examples and adapters that establish interoperability.

Potential implementation frontiers—such as learned consequence estimators, proprietary evaluation corpora, enterprise orchestration, predictive foreclosure models, or commercial observability—need not live here.

**Open the grammar. Build businesses from fluency.**

## Repository map

```text
morrow/
├── spec/                 # protocol specification
├── schemas/              # machine-readable schemas
├── src/morrow/           # dependency-light reference implementation
├── tests/                # conformance-oriented tests
├── examples/             # runnable examples
├── CONTRIBUTING.md
├── SECURITY.md
└── LICENSE
```

## Status

**v0.1 seed / experimental.**

The specification is intentionally small enough to implement now and strong enough to evolve with more capable agentic systems.

## License

Apache License 2.0.

---

*MORROW is an experiment in good ancestry for machine intelligence.*
