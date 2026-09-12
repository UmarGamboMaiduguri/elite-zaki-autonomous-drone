"""
Data models for Elite Zaki decision making.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Decision:
    """Represents a high-level system decision."""

    action: str
    confidence: float
    reason: str

    def __post_init__(self) -> None:
        """Validate decision values."""

        if not self.action:
            raise ValueError("Decision action cannot be empty.")

        if not 0.0 <= self.confidence <= 1.0:
            raise ValueError(
                "Decision confidence must be between 0.0 and 1.0."
            )

        if not self.reason:
            raise ValueError("Decision reason cannot be empty.")
