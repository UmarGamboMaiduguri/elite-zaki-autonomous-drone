"""
Tests for Elite Zaki decision control.
"""

import pytest

from elite_zaki.decision_engine.controller import DecisionController


def test_decision_controller_creates_decision() -> None:
    """A valid observation should produce a decision."""

    controller = DecisionController()

    decision = controller.decide(
        observation="Object detected in monitored area.",
        confidence=0.90,
    )

    assert decision.action == "monitor"
    assert decision.confidence == 0.90
    assert decision.reason == "Object detected in monitored area."


def test_decision_controller_rejects_empty_observation() -> None:
    """An empty observation should raise an error."""

    controller = DecisionController()

    with pytest.raises(ValueError):
        controller.decide(
            observation="",
            confidence=0.90,
        )


def test_decision_controller_rejects_invalid_confidence() -> None:
    """Confidence outside the valid range should raise an error."""

    controller = DecisionController()

    with pytest.raises(ValueError):
        controller.decide(
            observation="Object detected.",
            confidence=1.5,
        )
