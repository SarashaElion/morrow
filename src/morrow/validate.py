from __future__ import annotations

from datetime import datetime
from typing import Any


_REVERSIBILITY = {"reversible", "costly", "time_limited", "irreversible", "unknown"}
_ALT_STATUS = {"available", "costly", "foreclosed", "unknown"}
_SEVERITY = {"low", "medium", "high", "critical", "unknown"}


def _datetime_like(value: str) -> bool:
    try:
        datetime.fromisoformat(value.replace("Z", "+00:00"))
        return True
    except (TypeError, ValueError):
        return False


def validate_packet(packet: dict[str, Any]) -> list[str]:
    """Return validation errors. An empty list means v0.1 structural conformance.

    This lightweight validator keeps the reference implementation dependency-free.
    The JSON Schema in the schemas directory remains the normative machine-readable shape.
    """

    errors: list[str] = []

    required = ("morrow_version", "packet_id", "created_at", "decision", "reversibility", "authority")
    for key in required:
        if key not in packet:
            errors.append(f"missing required field: {key}")

    if errors:
        return errors

    if packet["morrow_version"] != "0.1":
        errors.append("morrow_version must be '0.1'")

    if not isinstance(packet["packet_id"], str) or not packet["packet_id"].strip():
        errors.append("packet_id must be a non-empty string")

    if not isinstance(packet["created_at"], str) or not _datetime_like(packet["created_at"]):
        errors.append("created_at must be an ISO-8601 datetime")

    decision = packet.get("decision")
    if not isinstance(decision, dict) or not isinstance(decision.get("action"), str) or not decision.get("action", "").strip():
        errors.append("decision.action must be a non-empty string")

    reversibility = packet.get("reversibility")
    if not isinstance(reversibility, dict) or reversibility.get("class") not in _REVERSIBILITY:
        errors.append("reversibility.class is invalid")

    authority = packet.get("authority")
    if not isinstance(authority, dict) or not isinstance(authority.get("source"), str) or not authority.get("source", "").strip():
        errors.append("authority.source must be a non-empty string")

    for index, item in enumerate(packet.get("alternatives", [])):
        if item.get("status") not in _ALT_STATUS:
            errors.append(f"alternatives[{index}].status is invalid")

    for index, item in enumerate(packet.get("foreclosures", [])):
        if item.get("severity") not in _SEVERITY:
            errors.append(f"foreclosures[{index}].severity is invalid")

    for index, item in enumerate(packet.get("assumptions", [])):
        confidence = item.get("confidence")
        if confidence is not None and (
            not isinstance(confidence, (int, float)) or isinstance(confidence, bool) or not 0 <= confidence <= 1
        ):
            errors.append(f"assumptions[{index}].confidence must be between 0 and 1")

    return errors
