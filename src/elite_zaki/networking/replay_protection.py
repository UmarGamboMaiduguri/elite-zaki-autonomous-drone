"""
Replay protection utilities for Elite Zaki telemetry.
"""

from dataclasses import dataclass
from datetime import datetime, timedelta, timezone


@dataclass
class ReplayProtection:
    """Tracks recently received telemetry messages."""

    max_age_seconds: int = 30

    def is_fresh(self, timestamp: datetime) -> bool:
        """
        Check whether a telemetry timestamp is recent.

        Args:
            timestamp: Timestamp associated with the message.

        Returns:
            True if the timestamp is within the allowed age.
        """

        if timestamp.tzinfo is None:
            timestamp = timestamp.replace(tzinfo=timezone.utc)

        now = datetime.now(timezone.utc)
        age = now - timestamp

        return timedelta(seconds=0) <= age <= timedelta(
            seconds=self.max_age_seconds
        )
