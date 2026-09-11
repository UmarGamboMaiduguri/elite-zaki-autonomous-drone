"""
Sensor fusion processing for Elite Zaki.
"""

from dataclasses import dataclass

from .models import SensorReading


@dataclass(frozen=True)
class FusedReading:
    """Represents a combined sensor result."""

    value: float
    source_count: int


class SensorFusion:
    """Combines compatible sensor readings."""

    def fuse(self, readings: list[SensorReading]) -> FusedReading:
        """
        Combine sensor readings using a simple average.

        Args:
            readings: Sensor readings to combine.

        Returns:
            A fused sensor reading.

        Raises:
            ValueError: If no readings are provided.
        """

        if not readings:
            raise ValueError("At least one sensor reading is required.")

        average = sum(reading.value for reading in readings) / len(readings)

        return FusedReading(
            value=average,
            source_count=len(readings),
        )
