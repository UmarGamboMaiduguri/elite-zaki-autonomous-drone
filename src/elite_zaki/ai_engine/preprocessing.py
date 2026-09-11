"""
Image preprocessing utilities for Elite Zaki.
"""

from pathlib import Path

import cv2
import numpy as np


def load_image(image_path: str | Path) -> np.ndarray:
    """
    Load an image from disk.

    Args:
        image_path: Path to the image file.

    Returns:
        Image represented as a NumPy array.

    Raises:
        FileNotFoundError: If the image cannot be loaded.
    """

    path = Path(image_path)

    image = cv2.imread(str(path))

    if image is None:
        raise FileNotFoundError(
            f"Unable to load image: {path}"
        )

    return image


def resize_image(
    image: np.ndarray,
    width: int = 640,
    height: int = 480,
) -> np.ndarray:
    """
    Resize an image to the requested dimensions.

    Args:
        image: Input image.
        width: Target width.
        height: Target height.

    Returns:
        Resized image.
    """

    if width <= 0 or height <= 0:
        raise ValueError("Width and height must be positive.")

    return cv2.resize(image, (width, height))
