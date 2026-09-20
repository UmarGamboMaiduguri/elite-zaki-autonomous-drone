"""Secure telemetry receiver for Elite Zaki."""

from __future__ import annotations

import hashlib
import hmac
import json
import time
from dataclasses import dataclass
from typing import Any


@dataclass
class ReceiveResult:
    """Result returned after processing a telemetry payload."""

    accepted: bool
    reason: str
    data: dict[str, Any] | None = None


class TelemetryReceiver:
    """Verify and validate signed telemetry received from a drone node."""

    def __init__(
        self,
        secret: bytes,
        max_age_seconds: int = 30,
    ) -> None:
        self.secret = secret
        self.max_age_seconds = max_age_seconds

    def sign(self, payload: bytes) -> str:
        """Create an HMAC-SHA256 signature for a payload."""

        return hmac.new(
            self.secret,
            payload,
            hashlib.sha256,
        ).hexdigest()

    def receive(
        self,
        payload: bytes,
        signature: str,
        timestamp: float | None = None,
    ) -> ReceiveResult:
        """Verify a telemetry payload and return the validation result."""

        expected_signature = self.sign(payload)

        if not hmac.compare_digest(signature, expected_signature):
            return ReceiveResult(
                accepted=False,
                reason="invalid_signature",
            )

        if timestamp is not None:
            age = time.time() - timestamp

            if age < 0 or age > self.max_age_seconds:
                return ReceiveResult(
                    accepted=False,
                    reason="stale",
                )

        try:
            data = json.loads(payload.decode("utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError):
            return ReceiveResult(
                accepted=False,
                reason="invalid_payload",
            )

        if not isinstance(data, dict):
            return ReceiveResult(
                accepted=False,
                reason="invalid_payload",
            )

        return ReceiveResult(
            accepted=True,
            reason="valid",
            data=data,
        )
