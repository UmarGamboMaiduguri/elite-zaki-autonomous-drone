"""
Telemetry data models for Elite Zaki.
"""

from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class TelemetryPacket:
    """Represents a telemetry message."""

    source: str
    timestamp: datetime
    latitude: float
    longitude: float
    altitude: float
    battery_level: float

    def __post_init__(self) -> None:
        """Validate telemetry values."""

        if not self.source:
            raise ValueError("Telemetry source cannot be empty.")

        if not -90.0 <= self.latitude <= 90.0:
            raise ValueError("Latitude must be between -90 and 90.")

        if not -180.0 <= self.longitude <= 180.0:
            raise ValueError("Longitude must be between -180 and 180.")

        if self.altitude < 0.0:
            raise ValueError("Altitude cannot be negative.")

        if not 0.0 <= self.battery_level <= 100.0:
            raise ValueError(
                "Battery level must be between 0 and 100."
            )
