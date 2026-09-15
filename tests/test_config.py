"""
Tests for Elite Zaki system configuration.
"""

from elite_zaki.config import DEFAULT_CONFIG, SystemConfig


def test_default_config() -> None:
    """The default configuration should contain valid project values."""

    assert DEFAULT_CONFIG.project_name == "Elite Zaki"
    assert DEFAULT_CONFIG.version == "0.1.0"
    assert DEFAULT_CONFIG.mode == "simulation"
    assert DEFAULT_CONFIG.confidence_threshold == 0.50


def test_custom_config() -> None:
    """A custom system configuration should be created correctly."""

    config = SystemConfig(
        project_name="Test System",
        version="1.0.0",
        mode="testing",
        confidence_threshold=0.75,
    )

    assert config.project_name == "Test System"
    assert config.version == "1.0.0"
    assert config.mode == "testing"
    assert config.confidence_threshold == 0.75
