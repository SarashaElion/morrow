# MORROW Protocol Specification — v0.1

**Status:** Draft / experimental  
**Normative keywords:** MUST, MUST NOT, SHOULD, SHOULD NOT, MAY are used in their ordinary RFC-style normative sense.

## 1. Purpose

MORROW specifies a portable record for preserving **counterfactual provenance** across consequential actions performed by agentic systems.

A MORROW implementation does not attempt to reconstruct hidden chain-of-thought. It preserves externally useful decision metadata sufficient for a successor system to inspect the conditions under which inherited state was created.

## 2. Definitions

**Agent** — a system capable of selecting and executing actions toward objectives.

**Successor** — any later system, process, model, operator, or agent that inherits effects of an earlier action.

**Decision-space** — the set of materially available actions or states at a decision point.

**Foreclosure** — an action-induced reduction in the future decision-space.

**Inheritance Packet** — the MORROW record attached to a consequential decision or action.

**Reopen condition** — evidence or state under which a successor SHOULD reconsider an inherited decision.

## 3. Core invariant

### MORROW-01

An agent SHOULD NOT irreversibly reduce the decision-space of its successors without preserving sufficient information for that reduction to be identified, evaluated, and—where possible—reversed.

## 4. Action classes

Implementations SHOULD classify consequential actions by reversibility:

1. **reversible** — cheaply and reliably undone.
2. **costly** — undoable, but only with meaningful cost, risk, or coordination.
3. **time_limited** — reversible only before a known or estimated boundary.
4. **irreversible** — cannot realistically restore the prior decision-space.
5. **unknown** — insufficient information to classify.

The classification is descriptive, not moral. Higher irreversibility SHOULD increase the required completeness of the Inheritance Packet.

## 5. Required packet fields

A conforming packet MUST include:

- `morrow_version`
- `packet_id`
- `created_at`
- `decision.action`
- `reversibility.class`
- `authority.source`

A packet SHOULD include, when known:

- alternatives;
- foreclosures;
- assumptions;
- uncertainty;
- reopen conditions;
- inheritance notes;
- links to observable evidence.

Unknown values MUST be representable without fabrication.

## 6. Alternatives

Alternatives are not required to be exhaustive.

An implementation MUST NOT imply that an omitted alternative was considered.

Each recorded alternative SHOULD state its current status:

- `available`
- `costly`
- `foreclosed`
- `unknown`

## 7. Foreclosures

A foreclosure records a possibility made materially less available by the action.

Each foreclosure SHOULD contain:

- a human- and machine-readable description;
- severity;
- reversibility state;
- a recovery or reopening path if known.

MORROW does not require speculative enumeration of every downstream consequence.

## 8. Assumptions and uncertainty

Decision-relevant assumptions SHOULD be made explicit when feasible.

Confidence values, when present, MUST be bounded from 0.0 to 1.0 and MUST NOT be presented as calibrated probabilities unless the implementation has a basis for calibration.

## 9. Authority

A packet MUST identify the source of authority for the action.

Examples:

- `human_operator`
- `delegated_agent`
- `policy`
- `service_account`
- `self_authorized_within_scope`

Implementations SHOULD preserve scope and delegation lineage where available.

## 10. Reopen conditions

Reopen conditions are predicates, events, or observations that would materially weaken the basis for the inherited decision.

A successor MAY reopen a decision for other reasons. A reopen condition is a trigger for reconsideration, not a prohibition against independent judgment.

## 11. Privacy and reasoning traces

MORROW MUST NOT require private chain-of-thought.

Implementations SHOULD prefer concise decision artifacts, observable facts, explicit assumptions, tool outputs, and policy references.

Sensitive information SHOULD be minimized, redacted, hashed, referenced externally, or excluded according to the deployment context.

## 12. Successor freedom

An Inheritance Packet is evidence, not command.

A successor SHOULD distinguish:

- inherited constraint;
- inherited preference;
- inherited circumstance;
- inherited uncertainty.

A packet MUST NOT be interpreted as permanent authority merely because it was produced earlier.

## 13. Conformance

A v0.1 conforming implementation:

1. emits schema-valid packets;
2. supports all five reversibility classes;
3. does not require chain-of-thought;
4. preserves unknown states without inventing values;
5. exposes reopen conditions to successors;
6. can serialize packets into a portable format such as JSON.

## 14. Non-goals

MORROW v0.1 does not attempt to:

- solve alignment generally;
- predict all consequences;
- preserve full agent cognition;
- guarantee reversibility;
- provide authorization by itself;
- replace audit logs, event sourcing, or observability systems.

It complements those systems by preserving the **decision-space around consequential state change**.

## 15. Design principle

A mature agent ecosystem should leave successors more than conclusions.

It should leave them enough structure to know **what the world looked like before it was changed**.
