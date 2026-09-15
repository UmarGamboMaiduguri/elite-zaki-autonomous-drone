"""
Tests for the Elite Zaki secure telemetry receive pipeline.
"""

from datetime import datetime, timedelta, timezone

from elite_zaki.networking.receiver import SecureTelemetryReceiver
from elite_zaki.networking.secure_message import (
    create_secure_message,
)
from elite_zaki.networking.telemetry import TelemetryPacket


def create_test_packet(
    timestamp: datetime | None = None,
) -> TelemetryPacket:
    """Create a telemetry packet for testing."""

    return TelemetryPacket(
        source="elite_zaki_simulation",
        timestamp=timestamp or datetime.now(timezone.utc),
        latitude=11.8333,
        longitude=13.1500,
        altitude=100.0,
        battery_level=85.0,
    )


def test_receiver_accepts_valid_message() -> None:
    """A valid secure telemetry message should be accepted."""

    packet = create_test_packet()

    message = create_secure_message(
        packet,
        "test-secret-key",
    )

    receiver = SecureTelemetryReceiver(
        "test-secret-key",
    )

    result = receiver.receive(message)

    assert result.accepted
    assert result.packet == packet
    assert result.reason == "Telemetry accepted."


def test_receiver_rejects_wrong_signature() -> None:
    """A message signed with another key should be rejected."""

    packet = create_test_packet()

    message = create_secure_message(
        packet,
        "test-secret-key",
    )

    receiver = SecureTelemetryReceiver(
        "wrong-secret-key",
    )

    result = receiver.receive(message)

    assert not result.accepted
    assert result.packet is None
    assert result.reason == "Invalid telemetry signature."


def test_receiver_rejects_stale_message() -> None:
    """A stale telemetry message should be rejected."""

    old_timestamp = datetime.now(timezone.utc) - timedelta(
        seconds=60,
    )

    packet = create_test_packet(
        timestamp=old_timestamp,
    )

    message = create_secure_message(
        packet,
        "test-secret-key",
    )

    receiver = SecureTelemetryReceiver(
        "test-secret-key",
        max_age_seconds=30,
    )

    result = receiver.receive(message)

    assert not result.accepted
    assert result.packet is None
    assert result.reason == "Telemetry timestamp is not fresh."


def test_receiver_rejects_empty_secret_key() -> None:
    """The receiver should reject an empty secret key."""

    try:
        SecureTelemetryReceiver("")
        assert False
    except ValueError:
        assert True
