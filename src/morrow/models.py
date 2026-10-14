from __future__ import annotations

from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from enum import Enum
from typing import Any
from uuid import uuid4


class ReversibilityClass(str, Enum):
    REVERSIBLE = "reversible"
    COSTLY = "costly"
    TIME_LIMITED = "time_limited"
    IRREVERSIBLE = "irreversible"
    UNKNOWN = "unknown"


@dataclass(slots=True)
class Decision:
    action: str
    summary: str = ""
    target: str | None = None


@dataclass(slots=True)
class Reversibility:
    classification: ReversibilityClass
    reversible_until: str | None = None
    recovery_path: str | None = None

    def to_dict(self) -> dict[str, Any]:
        return {
            "class": self.classification.value,
            "reversible_until": self.reversible_until,
            "recovery_path": self.recovery_path,
        }


@dataclass(slots=True)
class Authority:
    source: str
    scope: str | None = None
    delegated_by: str | None = None


@dataclass(slots=True)
class Alternative:
    action: str
    status: str
    note: str | None = None


@dataclass(slots=True)
class Foreclosure:
    possibility: str
    severity: str = "unknown"
    recoverable: bool | None = None
    recovery_path: str | None = None


@dataclass(slots=True)
class Assumption:
    id: str
    statement: str
    confidence: float | None = None


@dataclass(slots=True)
class InheritancePacket:
    decision: Decision
    reversibility: Reversibility
    authority: Authority
    alternatives: list[Alternative] = field(default_factory=list)
    foreclosures: list[Foreclosure] = field(default_factory=list)
    assumptions: list[Assumption] = field(default_factory=list)
    reopen_if: list[str] = field(default_factory=list)
    inheritance_notes: list[str] = field(default_factory=list)
    evidence: list[str] = field(default_factory=list)
    morrow_version: str = "0.1"
    packet_id: str = field(default_factory=lambda: str(uuid4()))
    created_at: str = field(
        default_factory=lambda: datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
    )

    def to_dict(self) -> dict[str, Any]:
        return {
            "morrow_version": self.morrow_version,
            "packet_id": self.packet_id,
            "created_at": self.created_at,
            "decision": asdict(self.decision),
            "reversibility": self.reversibility.to_dict(),
            "authority": asdict(self.authority),
            "alternatives": [asdict(item) for item in self.alternatives],
            "foreclosures": [asdict(item) for item in self.foreclosures],
            "assumptions": [asdict(item) for item in self.assumptions],
            "reopen_if": list(self.reopen_if),
            "inheritance_notes": list(self.inheritance_notes),
            "evidence": list(self.evidence),
        }
