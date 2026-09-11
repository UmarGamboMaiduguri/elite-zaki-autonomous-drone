"""
Tests for the Elite Zaki AI vision pipeline.
"""

import numpy as np

from elite_zaki.ai_engine.detector import BaseDetector, Detection
from elite_zaki.ai_engine.pipeline import VisionPipeline


class TestDetector(BaseDetector):
    """Simple detector used for pipeline testing."""

    def detect(self, image: np.ndarray) -> list[Detection]:
        """Return a simulated detection."""

        return [
            Detection(
                label="person",
                confidence=0.95,
                bounding_box=(50, 60, 150, 250),
            )
        ]


def test_vision_pipeline_processes_image() -> None:
    """The pipeline should resize the image and return detections."""

    image = np.zeros((240, 320, 3), dtype=np.uint8)

    pipeline = VisionPipeline(
        detector=TestDetector(),
        width=640,
        height=480,
    )

    result = pipeline.process(image)

    assert result.image.shape == (480, 640, 3)
    assert len(result.detections) == 1
    assert result.detections[0].label == "person"


def test_vision_pipeline_uses_custom_dimensions() -> None:
    """The pipeline should support custom output dimensions."""

    image = np.zeros((100, 200, 3), dtype=np.uint8)

    pipeline = VisionPipeline(
        detector=TestDetector(),
        width=320,
        height=240,
    )

    result = pipeline.process(image)

    assert result.image.shape == (240, 320, 3)
