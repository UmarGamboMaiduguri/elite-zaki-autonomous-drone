"""
Telemetry serialization utilities for Elite Zaki.
"""

from dataclasses import asdict
from datetime import datetime
import json

from .telemetry import TelemetryPacket


def serialize_telemetry(packet: TelemetryPacket) -> str:
    """
    Convert a telemetry packet into a JSON string.

    Args:
        packet: Telemetry packet to serialize.

    Returns:
        JSON representation of the telemetry packet.
    """

    data = asdict(packet)
    data["timestamp"] = packet.timestamp.isoformat()

    return json.dumps(data, sort_keys=True)


def deserialize_telemetry(data: str) -> TelemetryPacket:
    """
    Convert a JSON string back into a telemetry packet.

    Args:
        data: JSON telemetry data.

    Returns:
        Reconstructed telemetry packet.

    Raises:
        ValueError: If the JSON data is invalid.
    """

    try:
        payload = json.loads(data)

        return TelemetryPacket(
            source=payload["source"],
            timestamp=datetime.fromisoformat(payload["timestamp"]),
            latitude=float(payload["latitude"]),
            longitude=float(payload["longitude"]),
            altitude=float(payload["altitude"]),
            battery_level=float(payload["battery_level"]),
        )

    except (KeyError, TypeError, ValueError, json.JSONDecodeError) as exc:
        raise ValueError(
            "Invalid telemetry data."
        ) from exc
