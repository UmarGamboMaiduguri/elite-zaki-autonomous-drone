"""
Data models for Elite Zaki flight control.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Waypoint:
    """Represents a navigation waypoint."""

    latitude: float
    longitude: float
    altitude: float

    def __post_init__(self) -> None:
        """Validate waypoint values."""

        if not -90.0 <= self.latitude <= 90.0:
            raise ValueError("Latitude must be between -90 and 90.")

        if not -180.0 <= self.longitude <= 180.0:
            raise ValueError("Longitude must be between -180 and 180.")

        if self.altitude < 0.0:
            raise ValueError("Altitude cannot be negative.")
