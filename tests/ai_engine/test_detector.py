"""
Tests for the Elite Zaki object detection interface.
"""

import numpy as np
import pytest

from elite_zaki.ai_engine.detector import Detection


def test_detection_creation() -> None:
    """A valid detection should be created successfully."""

    detection = Detection(
        label="person",
        confidence=0.95,
        bounding_box=(10, 20, 100, 200),
    )

    assert detection.label == "person"
    assert detection.confidence == 0.95
    assert detection.bounding_box == (10, 20, 100, 200)


def test_detection_rejects_invalid_confidence() -> None:
    """Confidence outside the valid range should raise an error."""

    with pytest.raises(ValueError):
        Detection(
            label="person",
            confidence=1.5,
            bounding_box=(10, 20, 100, 200),
        )


def test_detection_rejects_empty_label() -> None:
    """An empty detection label should raise an error."""

    with pytest.raises(ValueError):
        Detection(
            label="",
            confidence=0.90,
            bounding_box=(10, 20, 100, 200),
        )


def test_detection_accepts_numpy_workflow() -> None:
    """Detection data should work alongside NumPy image data."""

    image = np.zeros((480, 640, 3), dtype=np.uint8)

    detection = Detection(
        label="vehicle",
        confidence=0.88,
        bounding_box=(50, 60, 200, 180),
    )

    assert image.shape == (480, 640, 3)
    assert detection.label == "vehicle"
