from __future__ import annotations

from datetime import datetime

from .models import Reversibility, ReversibilityClass


def assess_reversibility(
    *,
    undoable: bool | None,
    meaningful_recovery_cost: bool = False,
    reversible_until: datetime | None = None,
    recovery_path: str | None = None,
) -> Reversibility:
    """Classify an action without pretending to know what the caller does not know.

    MORROW deliberately requires explicit signals. It does not infer irreversibility
    from action names or silently invent a recovery path.
    """

    if undoable is None:
        classification = ReversibilityClass.UNKNOWN
    elif undoable is False:
        classification = ReversibilityClass.IRREVERSIBLE
    elif reversible_until is not None:
        classification = ReversibilityClass.TIME_LIMITED
    elif meaningful_recovery_cost:
        classification = ReversibilityClass.COSTLY
    else:
        classification = ReversibilityClass.REVERSIBLE

    deadline = None
    if reversible_until is not None:
        deadline = reversible_until.isoformat()
        if deadline.endswith("+00:00"):
            deadline = deadline[:-6] + "Z"

    return Reversibility(
        classification=classification,
        reversible_until=deadline,
        recovery_path=recovery_path,
    )
