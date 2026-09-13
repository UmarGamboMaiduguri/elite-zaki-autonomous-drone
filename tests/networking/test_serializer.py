"""
Tests for Elite Zaki telemetry serialization.
"""

from datetime import datetime, timezone

import pytest

from elite_zaki.networking.serializer import (
    deserialize_telemetry,
    serialize_telemetry,
)
from elite_zaki.networking.telemetry import TelemetryPacket


def test_serialize_telemetry() -> None:
    """A telemetry packet should serialize to JSON."""

    timestamp = datetime.now(timezone.utc)

    packet = TelemetryPacket(
        source="elite_zaki_simulation",
        timestamp=timestamp,
        latitude=11.8333,
        longitude=13.1500,
        altitude=100.0,
        battery_level=85.0,
    )

    data = serialize_telemetry(packet)

    assert isinstance(data, str)
    assert "elite_zaki_simulation" in data
    assert "85.0" in data


def test_deserialize_telemetry() -> None:
    """Serialized telemetry should be reconstructed correctly."""

    timestamp = datetime.now(timezone.utc)

    packet = TelemetryPacket(
        source="elite_zaki_simulation",
        timestamp=timestamp,
        latitude=11.8333,
        longitude=13.1500,
        altitude=100.0,
        battery_level=85.0,
    )

    data = serialize_telemetry(packet)
    restored = deserialize_telemetry(data)

    assert restored.source == packet.source
    assert restored.timestamp == packet.timestamp
    assert restored.latitude == packet.latitude
    assert restored.longitude == packet.longitude
    assert restored.altitude == packet.altitude
    assert restored.battery_level == packet.battery_level


def test_deserialize_rejects_invalid_data() -> None:
    """Invalid telemetry JSON should raise an error."""

    with pytest.raises(ValueError):
        deserialize_telemetry(
            '{"invalid": "telemetry"}'
        )
