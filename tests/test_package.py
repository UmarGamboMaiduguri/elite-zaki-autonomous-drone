"""
Tests for the Elite Zaki Python package.
"""

import elite_zaki


def test_package_version() -> None:
    """The package should expose the expected version."""

    assert elite_zaki.__version__ == "0.1.0"


def test_package_author() -> None:
    """The package should expose the project author."""

    assert elite_zaki.__author__ == "Umar Gambo"
