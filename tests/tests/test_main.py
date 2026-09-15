"""
Tests for the Elite Zaki application entry point.
"""

from elite_zaki.main import main


def test_main_initializes_system(capsys) -> None:
    """The main application should initialize successfully."""

    main()

    captured = capsys.readouterr()

    assert "Elite Zaki v0.1.0" in captured.out
    assert "Operating mode: simulation" in captured.out
    assert "System initialized successfully." in captured.out
