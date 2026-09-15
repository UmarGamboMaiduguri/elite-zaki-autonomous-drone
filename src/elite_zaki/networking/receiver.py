"""
Secure telemetry receive and validation pipeline for Elite Zaki.
"""

from dataclasses import dataclass

from .replay_protection import ReplayProtection
from .secure_message import (
    SecureTelemetryMessage,
    verify_secure_message,
)
from .serializer import deserialize_telemetry
from .telemetry import TelemetryPacket


@dataclass(frozen=True)
class TelemetryReceiveResult:
    """Result of secure telemetry validation."""

    accepted: bool
    packet: TelemetryPacket | None
    reason: str


class SecureTelemetryReceiver:
    """Validates incoming Elite Zaki telemetry messages."""

    def __init__(
        self,
        secret_key: str,
        max_age_seconds: int = 30,
    ) -> None:
        """Initialize the secure telemetry receiver."""

        if not secret_key:
            raise ValueError("Secret key cannot be empty.")

        self._secret_key = secret_key
        self._replay_protection = ReplayProtection(
            max_age_seconds=max_age_seconds,
        )

    def receive(
        self,
        message: SecureTelemetryMessage,
    ) -> TelemetryReceiveResult:
        """
        Validate and deserialize a secure telemetry message.

        Validation order:

        1. Verify message signature.
        2. Deserialize telemetry payload.
        3. Check timestamp freshness.
        4. Accept or reject the message.
        """

        if not verify_secure_message(
            message,
            self._secret_key,
        ):
            return TelemetryReceiveResult(
                accepted=False,
                packet=None,
                reason="Invalid telemetry signature.",
            )

        try:
            packet = deserialize_telemetry(
                message.payload,
            )
        except ValueError:
            return TelemetryReceiveResult(
                accepted=False,
                packet=None,
                reason="Invalid telemetry payload.",
            )

        if not self._replay_protection.is_fresh(
            packet.timestamp,
        ):
            return TelemetryReceiveResult(
                accepted=False,
                packet=None,
                reason="Telemetry timestamp is not fresh.",
            )

        return TelemetryReceiveResult(
            accepted=True,
            packet=packet,
            reason="Telemetry accepted.",
        )
