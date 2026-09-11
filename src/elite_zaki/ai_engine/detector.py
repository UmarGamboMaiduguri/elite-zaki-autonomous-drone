"""
Object detection interfaces for Elite Zaki.
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass

import numpy as np


@dataclass(frozen=True)
class Detection:
    """Represents a single detected object."""

    label: str
    confidence: float
    bounding_box: tuple[int, int, int, int]

    def __post_init__(self) -> None:
        """Validate detection values."""

        if not self.label:
            raise ValueError("Detection label cannot be empty.")

        if not 0.0 <= self.confidence <= 1.0:
            raise ValueError(
                "Detection confidence must be between 0.0 and 1.0."
            )

        if len(self.bounding_box) != 4:
            raise ValueError(
                "Bounding box must contain four values."
            )


class BaseDetector(ABC):
    """Abstract interface for Elite Zaki object detectors."""

    @abstractmethod
    def detect(self, image: np.ndarray) -> list[Detection]:
        """
        Detect objects in an image.

        Args:
            image: Input image as a NumPy array.

        Returns:
            A list of detected objects.
        """

        raise NotImplementedError
