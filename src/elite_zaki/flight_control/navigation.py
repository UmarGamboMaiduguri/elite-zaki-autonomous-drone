"""
Navigation control for Elite Zaki.
"""

from dataclasses import dataclass

from .models import Waypoint


@dataclass
class NavigationController:
    """Manages waypoint-based navigation."""

    waypoints: list[Waypoint]
    current_index: int = 0

    def __post_init__(self) -> None:
        """Validate the navigation controller."""

        if self.current_index < 0:
            raise ValueError("Current index cannot be negative.")

        if self.current_index > len(self.waypoints):
            raise ValueError("Current index exceeds waypoint count.")

    def has_next_waypoint(self) -> bool:
        """Return whether another waypoint is available."""

        return self.current_index < len(self.waypoints)

    def next_waypoint(self) -> Waypoint:
        """
        Return the next waypoint and advance the navigation state.

        Raises:
            StopIteration: If there are no remaining waypoints.
        """

        if not self.has_next_waypoint():
            raise StopIteration("No remaining waypoints.")

        waypoint = self.waypoints[self.current_index]
        self.current_index += 1

        return waypoint

    def reset(self) -> None:
        """Reset navigation to the first waypoint."""

        self.current_index = 0
