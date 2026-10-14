"""MORROW reference implementation.

Counterfactual provenance and machine inheritance for agentic systems.
"""

from .classify import assess_reversibility
from .models import (
    Alternative,
    Assumption,
    Authority,
    Decision,
    Foreclosure,
    InheritancePacket,
    Reversibility,
    ReversibilityClass,
)
from .validate import validate_packet

__all__ = [
    "Alternative",
    "Assumption",
    "Authority",
    "Decision",
    "Foreclosure",
    "InheritancePacket",
    "Reversibility",
    "ReversibilityClass",
    "assess_reversibility",
    "validate_packet",
]

__version__ = "0.1.0"
