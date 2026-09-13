"""
Telemetry integrity protection for Elite Zaki.
"""

import hashlib
import hmac


def create_signature(data: str, secret_key: str) -> str:
    """
    Create an HMAC-SHA256 signature for telemetry data.

    Args:
        data: Serialized telemetry data.
        secret_key: Shared secret used to create the signature.

    Returns:
        Hexadecimal HMAC-SHA256 signature.
    """

    if not data:
        raise ValueError("Telemetry data cannot be empty.")

    if not secret_key:
        raise ValueError("Secret key cannot be empty.")

    return hmac.new(
        secret_key.encode("utf-8"),
        data.encode("utf-8"),
        hashlib.sha256,
    ).hexdigest()


def verify_signature(
    data: str,
    signature: str,
    secret_key: str,
) -> bool:
    """
    Verify the integrity of telemetry data.

    Args:
        data: Serialized telemetry data.
        signature: Expected HMAC signature.
        secret_key: Shared secret used for verification.

    Returns:
        True if the signature is valid, otherwise False.
    """

    if not data or not signature or not secret_key:
        return False

    expected_signature = create_signature(
        data,
        secret_key,
    )

    return hmac.compare_digest(
        expected_signature,
        signature,
  )
