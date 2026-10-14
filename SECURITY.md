# Security Policy

MORROW is experimental protocol infrastructure. v0.1 should not be treated as an authorization, access-control, rollback, or safety guarantee.

## Sensitive records

Inheritance Packets can expose operational context. Implementations should minimize sensitive data and may use:

- references instead of embedded secrets;
- hashes or content-addressed evidence;
- redaction;
- access-controlled external evidence stores;
- retention policies appropriate to the deployment.

Never place credentials, private keys, access tokens, or unnecessary personal data in a packet.

## Reporting vulnerabilities

Please report security-sensitive issues privately through GitHub's security reporting features when available rather than publishing exploitable details in a public issue.

## Threats to consider

Implementers should account for:

- forged or tampered inheritance packets;
- stale authority claims;
- malicious reopen conditions;
- sensitive-information leakage;
- successors over-trusting predecessor assertions;
- denial of service through unbounded provenance growth;
- agents falsely describing irreversible actions as reversible.

A future MORROW version may standardize signatures, trust metadata, and bounded evidence retention. They are intentionally outside the v0.1 core.
