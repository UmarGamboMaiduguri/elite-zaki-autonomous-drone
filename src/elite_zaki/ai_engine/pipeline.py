"""
AI vision pipeline for Elite Zaki.
"""

from dataclasses import dataclass

import numpy as np

from .detector import BaseDetector, Detection
from .preprocessing import resize_image


@dataclass(frozen=True)
class PipelineResult:
    """Result produced by the AI vision pipeline."""

    image: np.ndarray
    detections: list[Detection]


class VisionPipeline:
    """Coordinates preprocessing and object detection."""

    def __init__(
        self,
        detector: BaseDetector,
        width: int = 640,
        height: int = 480,
    ) -> None:
        """Initialize the vision pipeline."""

        self.detector = detector
        self.width = width
        self.height = height

    def process(self, image: np.ndarray) -> PipelineResult:
        """
        Preprocess an image and run object detection.

        Args:
            image: Input image as a NumPy array.

        Returns:
            Processed image and detected objects.
        """

        if image is None:
            raise ValueError("Input image cannot be None.")

        if image.size == 0:
            raise ValueError("Input image cannot be empty.")

        processed_image = resize_image(
            image,
            width=self.width,
            height=self.height,
        )

        detections = self.detector.detect(processed_image)

        return PipelineResult(
            image=processed_image,
            detections=detections,
        )
