"""
Tests for Elite Zaki navigation control.
"""

import pytest

from elite_zaki.flight_control.models import Waypoint
from elite_zaki.flight_control.navigation import NavigationController


def test_navigation_returns_waypoints_in_order() -> None:
    """Waypoints should be returned in their defined order."""

    waypoints = [
        Waypoint(11.8333, 13.1500, 100.0),
        Waypoint(11.8400, 13.1600, 120.0),
    ]

    controller = NavigationController(waypoints)

    assert controller.next_waypoint() == waypoints[0]
    assert controller.next_waypoint() == waypoints[1]
    assert not controller.has_next_waypoint()


def test_navigation_raises_when_finished() -> None:
    """Navigation should stop when no waypoints remain."""

    waypoint = Waypoint(11.8333, 13.1500, 100.0)
    controller = NavigationController([waypoint])

    controller.next_waypoint()

    with pytest.raises(StopIteration):
        controller.next_waypoint()


def test_navigation_reset() -> None:
    """Reset should return navigation to the first waypoint."""

    waypoints = [
        Waypoint(11.8333, 13.1500, 100.0),
        Waypoint(11.8400, 13.1600, 120.0),
    ]

    controller = NavigationController(waypoints)

    controller.next_waypoint()
    controller.reset()

    assert controller.next_waypoint() == waypoints[0]


def test_navigation_rejects_invalid_index() -> None:
    """An invalid starting index should raise an error."""

    waypoint = Waypoint(11.8333, 13.1500, 100.0)

    with pytest.raises(ValueError):
        NavigationController(
            [waypoint],
            current_index=2,
  )
