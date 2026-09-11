"""
Tests for Elite Zaki image preprocessing utilities.
"""

import numpy as np
import pytest

from elite_zaki.ai_engine.preprocessing import resize_image


def test_resize_image() -> None:
    """An image should be resized to the requested dimensions."""

    image = np.zeros((240, 320, 3), dtype=np.uint8)

    resized = resize_image(
        image,
        width=640,
        height=480,
    )

    assert resized.shape == (480, 640, 3)


def test_resize_image_rejects_invalid_width() -> None:
    """A non-positive width should raise an error."""

    image = np.zeros((240, 320, 3), dtype=np.uint8)

    with pytest.raises(ValueError):
        resize_image(
            image,
            width=0,
            height=480,
        )


def test_resize_image_rejects_invalid_height() -> None:
    """A non-positive height should raise an error."""

    image = np.zeros((240, 320, 3), dtype=np.uint8)

    with pytest.raises(ValueError):
        resize_image(
            image,
            width=640,
            height=-1,
        )
