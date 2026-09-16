"""
Elite Zaki Networking Engine.

Provides the foundation for secure telemetry,
authentication, and communication research.
"""

from .receiver import SecureTelemetryReceiver, TelemetryReceiveResult

__version__ = "0.1.0"

__all__ = [
    "SecureTelemetryReceiver",
    "TelemetryReceiveResult",
]
