import cv2
import os


def load_image(image_path):
    if not os.path.exists(image_path):
        raise FileNotFoundError(
            f"Image file not found: {image_path}"
        )

    image = cv2.imread(image_path)

    if image is None:
        raise ValueError(
            f"Could not read the image file: {image_path}"
        )

    return image