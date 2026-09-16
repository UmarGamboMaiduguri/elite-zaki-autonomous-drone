"""
Replay protection utilities for Elite Zaki telemetry.
"""

from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone


@dataclass
class ReplayProtection:
    """Tracks recently received telemetry messages."""

    max_age_seconds: int = 30
    _seen_messages: set[str] = field(
        default_factory=set,
        init=False,
    )

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

    def is_replayed(self, message_id: str) -> bool:
        """
        Check whether a message has already been received.

        Args:
            message_id: Unique identifier for the message.

        Returns:
            True if the message was previously recorded.
        """

        if not message_id:
            raise ValueError("Message ID cannot be empty.")

        if message_id in self._seen_messages:
            return True

        self._seen_messages.add(message_id)
        return False
