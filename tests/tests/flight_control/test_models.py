"""
Tests for Elite Zaki flight control data models.
"""

import pytest

from elite_zaki.flight_control.models import Waypoint


def test_waypoint_creation() -> None:
    """A valid waypoint should be created successfully."""

    waypoint = Waypoint(
        latitude=11.8333,
        longitude=13.1500,
        altitude=100.0,
    )

    assert waypoint.latitude == 11.8333
    assert waypoint.longitude == 13.1500
    assert waypoint.altitude == 100.0


def test_waypoint_rejects_invalid_latitude() -> None:
    """Latitude outside the valid range should raise an error."""

    with pytest.raises(ValueError):
        Waypoint(
            latitude=100.0,
            longitude=13.1500,
            altitude=100.0,
        )


def test_waypoint_rejects_invalid_longitude() -> None:
    """Longitude outside the valid range should raise an error."""

    with pytest.raises(ValueError):
        Waypoint(
            latitude=11.8333,
            longitude=200.0,
            altitude=100.0,
        )


def test_waypoint_rejects_negative_altitude() -> None:
    """Negative altitude should raise an error."""

    with pytest.raises(ValueError):
        Waypoint(
            latitude=11.8333,
            longitude=13.1500,
            altitude=-10.0,
        )
