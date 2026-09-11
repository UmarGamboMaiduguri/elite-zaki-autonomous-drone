"""
Central configuration for Elite Zaki.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class SystemConfig:
    """Basic Elite Zaki system configuration."""

    project_name: str = "Elite Zaki"
    version: str = "0.1.0"
    mode: str = "simulation"
    confidence_threshold: float = 0.50


DEFAULT_CONFIG = SystemConfig()
