# Contributing to MORROW

MORROW is intentionally small at v0.1. Contributions should strengthen interoperability without prematurely turning the protocol into a complete theory of agency.

## What belongs here

Good public contributions include:

- specification clarifications;
- schema improvements;
- conformance tests;
- reference adapters;
- examples across agent frameworks;
- privacy-preserving patterns;
- evidence that a field is unnecessary, underspecified, or harmful;
- adversarial cases that reveal where inheritance breaks.

## What may not belong here

This repository is not automatically the home for every implementation built around MORROW.

Before contributing advanced work such as learned consequence models, proprietary evaluation data, enterprise orchestration, predictive foreclosure estimators, or commercial observability, consider whether it belongs in a separate implementation layer.

The protocol should remain usable without requiring access to a private system.

## Design constraints

Contributions SHOULD preserve these commitments:

1. **No chain-of-thought requirement.** Decision-relevant artifacts are enough.
2. **Unknown stays unknown.** Do not fabricate alternatives, authority, confidence, or reversibility.
3. **Successors retain judgment.** Inheritance is evidence, not permanent command.
4. **Irreversibility raises the burden.** More consequential foreclosure should produce richer inheritance.
5. **Minimal sufficient record.** Preserve what a successor needs without indiscriminate surveillance.

## Proposing protocol changes

Open an issue describing:

- the failure mode;
- a concrete agent scenario;
- the proposed change;
- backward-compatibility implications;
- privacy implications;
- how the proposal can be tested.

Protocol changes should include conformance tests whenever practical.

## License

By contributing, you agree that your contributions will be licensed under Apache License 2.0.
