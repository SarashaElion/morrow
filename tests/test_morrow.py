from datetime import datetime, timezone

from morrow import (
    Alternative,
    Assumption,
    Authority,
    Decision,
    Foreclosure,
    InheritancePacket,
    ReversibilityClass,
    assess_reversibility,
    validate_packet,
)


def test_unknown_stays_unknown():
    assessment = assess_reversibility(undoable=None)
    assert assessment.classification is ReversibilityClass.UNKNOWN


def test_irreversible_is_explicit():
    assessment = assess_reversibility(undoable=False)
    assert assessment.classification is ReversibilityClass.IRREVERSIBLE


def test_time_limited_precedes_cost_classification():
    deadline = datetime(2026, 10, 15, 18, 0, tzinfo=timezone.utc)
    assessment = assess_reversibility(
        undoable=True,
        meaningful_recovery_cost=True,
        reversible_until=deadline,
        recovery_path="rollback release before migration finalization",
    )
    assert assessment.classification is ReversibilityClass.TIME_LIMITED
    assert assessment.reversible_until == "2026-10-15T18:00:00Z"


def test_packet_serializes_and_validates():
    packet = InheritancePacket(
        decision=Decision(
            action="deploy_release_v4",
            summary="Deploy release v4 to production.",
            target="production",
        ),
        reversibility=assess_reversibility(
            undoable=True,
            meaningful_recovery_cost=True,
            recovery_path="rollback to v3",
        ),
        authority=Authority(
            source="human_operator",
            scope="production_deployment",
        ),
        alternatives=[
            Alternative(
                action="deploy_canary",
                status="available",
                note="Rejected for schedule pressure, not technical infeasibility.",
            )
        ],
        foreclosures=[
            Foreclosure(
                possibility="preserve_v3_database_schema",
                severity="high",
                recoverable=True,
                recovery_path="restore snapshot before destructive migration",
            )
        ],
        assumptions=[
            Assumption(
                id="telemetry_complete",
                statement="Production telemetry is representative.",
                confidence=0.72,
            )
        ],
        reopen_if=[
            "error_rate > 0.02",
            "assumption.telemetry_complete == false",
        ],
        inheritance_notes=[
            "A successor should distinguish schedule pressure from technical necessity."
        ],
    )

    data = packet.to_dict()

    assert data["reversibility"]["class"] == "costly"
    assert validate_packet(data) == []


def test_validator_rejects_false_confidence():
    packet = InheritancePacket(
        decision=Decision(action="example"),
        reversibility=assess_reversibility(undoable=None),
        authority=Authority(source="test"),
        assumptions=[
            Assumption(
                id="bad",
                statement="Confidence cannot exceed one.",
                confidence=1.2,
            )
        ],
    ).to_dict()

    errors = validate_packet(packet)
    assert "assumptions[0].confidence must be between 0 and 1" in errors
