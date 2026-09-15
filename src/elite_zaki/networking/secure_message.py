"""
Secure telemetry message handling for Elite Zaki.
"""

from dataclasses import dataclass

from .integrity import create_signature, verify_signature
from .serializer import serialize_telemetry
from .telemetry import TelemetryPacket


@dataclass(frozen=True)
class SecureTelemetryMessage:
    """Represents a signed telemetry message."""

    payload: str
    signature: str


def create_secure_message(
    packet: TelemetryPacket,
    secret_key: str,
) -> SecureTelemetryMessage:
    """
    Serialize and sign a telemetry packet.

    Args:
        packet: Telemetry packet to protect.
        secret_key: Shared secret used for integrity protection.

    Returns:
        A secure telemetry message containing payload and signature.
    """

    payload = serialize_telemetry(packet)

    signature = create_signature(
        payload,
        secret_key,
    )

    return SecureTelemetryMessage(
        payload=payload,
        signature=signature,
    )


def verify_secure_message(
    message: SecureTelemetryMessage,
    secret_key: str,
) -> bool:
    """
    Verify the integrity of a secure telemetry message.

    Args:
        message: Secure telemetry message to verify.
        secret_key: Shared secret used for verification.

    Returns:
        True if the message is valid, otherwise False.
    """

    return verify_signature(
        message.payload,
        message.signature,
        secret_key,
    )
