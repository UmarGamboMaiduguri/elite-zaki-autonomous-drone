"""
Tests for Elite Zaki telemetry replay protection.
"""

from datetime import datetime, timedelta, timezone

from elite_zaki.networking.replay_protection import ReplayProtection


def test_fresh_timestamp_is_accepted() -> None:
    """A recent timestamp should be accepted."""

    protection = ReplayProtection(max_age_seconds=30)

    timestamp = datetime.now(timezone.utc)

    assert protection.is_fresh(timestamp)


def test_old_timestamp_is_rejected() -> None:
    """A stale timestamp should be rejected."""

    protection = ReplayProtection(max_age_seconds=30)

    timestamp = datetime.now(timezone.utc) - timedelta(
        seconds=60
    )

    assert not protection.is_fresh(timestamp)


def test_future_timestamp_is_rejected() -> None:
    """A future timestamp should be rejected."""

    protection = ReplayProtection(max_age_seconds=30)

    timestamp = datetime.now(timezone.utc) + timedelta(
        seconds=10
    )

    assert not protection.is_fresh(timestamp)


def test_naive_timestamp_is_supported() -> None:
    """A timestamp without timezone information should be handled."""

    protection = ReplayProtection(max_age_seconds=30)

    timestamp = datetime.now()

    assert protection.is_fresh(timestamp)


def test_custom_max_age() -> None:
    """A custom freshness window should be respected."""

    protection = ReplayProtection(max_age_seconds=120)

    timestamp = datetime.now(timezone.utc) - timedelta(
        seconds=60
    )

    assert protection.is_fresh(timestamp)
