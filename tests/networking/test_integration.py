"""
Integration tests for Elite Zaki secure telemetry.
"""

from datetime import datetime, timezone

from elite_zaki.networking.replay_protection import ReplayProtection
from elite_zaki.networking.secure_message import (
    create_secure_message,
    verify_secure_message,
)
from elite_zaki.networking.telemetry import TelemetryPacket


def test_secure_telemetry_flow() -> None:
    """Telemetry should be created, signed, and successfully verified."""

    packet = TelemetryPacket(
        source="elite_zaki_simulation",
        timestamp=datetime.now(timezone.utc),
        latitude=11.8333,
        longitude=13.1500,
        altitude=100.0,
        battery_level=85.0,
    )

    secret_key = "test-secret-key"

    message = create_secure_message(
        packet,
        secret_key,
    )

    assert message.payload
    assert message.signature

    assert verify_secure_message(
        message,
        secret_key,
    )

    protection = ReplayProtection(
        max_age_seconds=30,
    )

    assert protection.is_fresh(
        packet.timestamp,
    )


def test_secure_telemetry_rejects_wrong_key() -> None:
    """Secure telemetry should reject an incorrect secret key."""

    packet = TelemetryPacket(
        source="elite_zaki_simulation",
        timestamp=datetime.now(timezone.utc),
        latitude=11.8333,
        longitude=13.1500,
        altitude=100.0,
        battery_level=85.0,
    )

    message = create_secure_message(
        packet,
        "test-secret-key",
    )

    assert not verify_secure_message(
        message,
        "wrong-secret-key",
    )
