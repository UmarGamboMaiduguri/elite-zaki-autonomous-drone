"""
Tests for Elite Zaki secure telemetry messages.
"""

from datetime import datetime, timezone

from elite_zaki.networking.secure_message import (
    create_secure_message,
    verify_secure_message,
)
from elite_zaki.networking.telemetry import TelemetryPacket


def create_test_packet() -> TelemetryPacket:
    """Create a telemetry packet for testing."""

    return TelemetryPacket(
        source="elite_zaki_simulation",
        timestamp=datetime.now(timezone.utc),
        latitude=11.8333,
        longitude=13.1500,
        altitude=100.0,
        battery_level=85.0,
    )


def test_create_secure_message() -> None:
    """A telemetry packet should become a signed message."""

    packet = create_test_packet()

    message = create_secure_message(
        packet,
        "test-secret-key",
    )

    assert message.payload
    assert message.signature
    assert len(message.signature) == 64


def test_verify_secure_message() -> None:
    """A valid secure message should pass verification."""

    packet = create_test_packet()

    message = create_secure_message(
        packet,
        "test-secret-key",
    )

    assert verify_secure_message(
        message,
        "test-secret-key",
    )


def test_verify_secure_message_rejects_modified_payload() -> None:
    """A modified payload should fail verification."""

    packet = create_test_packet()

    message = create_secure_message(
        packet,
        "test-secret-key",
    )

    modified_message = type(message)(
        payload=message.payload.replace(
            '"altitude": 100.0',
            '"altitude": 500.0',
        ),
        signature=message.signature,
    )

    assert not verify_secure_message(
        modified_message,
        "test-secret-key",
    )


def test_verify_secure_message_rejects_wrong_key() -> None:
    """A wrong secret key should fail verification."""

    packet = create_test_packet()

    message = create_secure_message(
        packet,
        "test-secret-key",
    )

    assert not verify_secure_message(
        message,
        "wrong-secret-key",
    )
