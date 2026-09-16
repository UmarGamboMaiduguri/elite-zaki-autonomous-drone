"""
Tests for the Elite Zaki networking package API.
"""

from elite_zaki.networking import (
    SecureTelemetryReceiver,
    TelemetryReceiveResult,
)


def test_networking_package_exports_receiver() -> None:
    """The networking package should expose the secure receiver."""

    receiver = SecureTelemetryReceiver(
        "test-secret-key",
    )

    assert isinstance(
        receiver,
        SecureTelemetryReceiver,
    )


def test_networking_package_exports_result_model() -> None:
    """The networking package should expose the receive result model."""

    result = TelemetryReceiveResult(
        accepted=True,
        packet=None,
        reason="Telemetry accepted.",
    )

    assert result.accepted
    assert result.reason == "Telemetry accepted."
