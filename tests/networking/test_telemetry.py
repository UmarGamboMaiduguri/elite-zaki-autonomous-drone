"""
Tests for Elite Zaki telemetry data models.
"""

from datetime import datetime, timezone

import pytest

from elite_zaki.networking.telemetry import TelemetryPacket


def test_telemetry_packet_creation() -> None:
    """A valid telemetry packet should be created successfully."""

    timestamp = datetime.now(timezone.utc)

    packet = TelemetryPacket(
        source="elite_zaki_simulation",
        timestamp=timestamp,
        latitude=11.8333,
        longitude=13.1500,
        altitude=100.0,
        battery_level=85.0,
    )

    assert packet.source == "elite_zaki_simulation"
    assert packet.timestamp == timestamp
    assert packet.latitude == 11.8333
    assert packet.longitude == 13.1500
    assert packet.altitude == 100.0
    assert packet.battery_level == 85.0


def test_telemetry_rejects_empty_source() -> None:
    """An empty telemetry source should raise an error."""

    timestamp = datetime.now(timezone.utc)

    with pytest.raises(ValueError):
        TelemetryPacket(
            source="",
            timestamp=timestamp,
            latitude=11.8333,
            longitude=13.1500,
            altitude=100.0,
            battery_level=85.0,
        )


def test_telemetry_rejects_invalid_coordinates() -> None:
    """Invalid coordinates should raise an error."""

    timestamp = datetime.now(timezone.utc)

    with pytest.raises(ValueError):
        TelemetryPacket(
            source="elite_zaki_simulation",
            timestamp=timestamp,
            latitude=100.0,
            longitude=13.1500,
            altitude=100.0,
            battery_level=85.0,
        )


def test_telemetry_rejects_negative_altitude() -> None:
    """Negative altitude should raise an error."""

    timestamp = datetime.now(timezone.utc)

    with pytest.raises(ValueError):
        TelemetryPacket(
            source="elite_zaki_simulation",
            timestamp=timestamp,
            latitude=11.8333,
            longitude=13.1500,
            altitude=-10.0,
            battery_level=85.0,
        )


def test_telemetry_rejects_invalid_battery_level() -> None:
    """Battery level outside 0 to 100 should raise an error."""

    timestamp = datetime.now(timezone.utc)

    with pytest.raises(ValueError):
        TelemetryPacket(
            source="elite_zaki_simulation",
            timestamp=timestamp,
            latitude=11.8333,
            longitude=13.1500,
            altitude=100.0,
            battery_level=120.0,
  )
