"""
Decision control logic for Elite Zaki.
"""

from .models import Decision


class DecisionController:
    """Generates high-level decisions from system observations."""

    def decide(
        self,
        observation: str,
        confidence: float,
    ) -> Decision:
        """
        Create a decision from an observation.

        Args:
            observation: Description of the observed situation.
            confidence: Confidence in the observation.

        Returns:
            A structured system decision.
        """

        if not observation:
            raise ValueError("Observation cannot be empty.")

        if not 0.0 <= confidence <= 1.0:
            raise ValueError(
                "Confidence must be between 0.0 and 1.0."
            )

        return Decision(
            action="monitor",
            confidence=confidence,
            reason=observation,
        )
