"""
Data models for Elite Zaki sensor fusion.
"""

from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class SensorReading:
    """Represents a single sensor measurement."""

    sensor_name: str
    value: float
    unit: str
    timestamp: datetime

    def __post_init__(self) -> None:
        """Validate sensor reading values."""

        if not self.sensor_name:
            raise ValueError("Sensor name cannot be empty.")

        if not self.unit:
            raise ValueError("Sensor unit cannot be empty.")
