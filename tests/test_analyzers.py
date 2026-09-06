import numpy as np

from src.image_analyzer import analyze_image
from src.quality_analyzer import analyze_quality
from src.edge_detector import detect_edges


def create_test_image():
    return np.zeros(
        (100, 100, 3),
        dtype=np.uint8
    )


def test_image_analysis():
    image = create_test_image()

    result = analyze_image(image)

    assert result["width"] == 100
    assert result["height"] == 100
    assert result["channels"] == 3
    assert result["total_pixels"] == 10000


def test_quality_analysis():
    image = create_test_image()

    result = analyze_quality(image)

    assert "brightness_status" in result
    assert "sharpness" in result
    assert "sharpness_status" in result


def test_edge_detection():
    image = create_test_image()

    result = detect_edges(image)

    assert result.shape == (100, 100)