"""
Tests for Elite Zaki sensor data models.
"""

from datetime import datetime, timezone

import pytest

from elite_zaki.sensor_fusion.models import SensorReading


def test_sensor_reading_creation() -> None:
    """A valid sensor reading should be created successfully."""

    timestamp = datetime.now(timezone.utc)

    reading = SensorReading(
        sensor_name="temperature",
        value=25.5,
        unit="C",
        timestamp=timestamp,
    )

    assert reading.sensor_name == "temperature"
    assert reading.value == 25.5
    assert reading.unit == "C"
    assert reading.timestamp == timestamp


def test_sensor_reading_rejects_empty_sensor_name() -> None:
    """An empty sensor name should raise an error."""

    timestamp = datetime.now(timezone.utc)

    with pytest.raises(ValueError):
        SensorReading(
            sensor_name="",
            value=25.5,
            unit="C",
            timestamp=timestamp,
        )


def test_sensor_reading_rejects_empty_unit() -> None:
    """An empty unit should raise an error."""

    timestamp = datetime.now(timezone.utc)

    with pytest.raises(ValueError):
        SensorReading(
            sensor_name="temperature",
            value=25.5,
            unit="",
            timestamp=timestamp,
        )
