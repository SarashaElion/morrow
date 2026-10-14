"""A minimal MORROW packet around a consequential deployment decision."""

import json
from datetime import datetime, timezone

from morrow import (
    Alternative,
    Assumption,
    Authority,
    Decision,
    Foreclosure,
    InheritancePacket,
    assess_reversibility,
    validate_packet,
)


packet = InheritancePacket(
    decision=Decision(
        action="deploy_release_v4",
        summary="Promote release v4 to production.",
        target="production",
    ),
    reversibility=assess_reversibility(
        undoable=True,
        reversible_until=datetime(2026, 10, 15, 18, 0, tzinfo=timezone.utc),
        recovery_path="rollback before database migration finalization",
    ),
    authority=Authority(
        source="human_operator",
        scope="production_deployment",
    ),
    alternatives=[
        Alternative(
            action="deploy_canary",
            status="available",
            note="Technically feasible; not selected because of schedule pressure.",
        ),
        Alternative(
            action="retain_v3_schema",
            status="foreclosed",
            note="Unavailable after destructive migration finalization.",
        ),
    ],
    foreclosures=[
        Foreclosure(
            possibility="retain_v3_schema_without_restore",
            severity="high",
            recoverable=True,
            recovery_path="restore pre-migration snapshot",
        )
    ],
    assumptions=[
        Assumption(
            id="telemetry_complete",
            statement="Current telemetry is representative of production traffic.",
            confidence=0.72,
        )
    ],
    reopen_if=[
        "error_rate > 0.02",
        "assumption.telemetry_complete == false",
    ],
    inheritance_notes=[
        "Canary deployment was rejected for schedule pressure, not technical infeasibility."
    ],
)

data = packet.to_dict()
errors = validate_packet(data)

if errors:
    raise SystemExit("\n".join(errors))

print(json.dumps(data, indent=2))
