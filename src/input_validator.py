import os


SUPPORTED_EXTENSIONS = [
    ".jpg",
    ".jpeg",
    ".png",
    ".bmp"
]


def validate_image_path(image_path):
    if not os.path.exists(image_path):
        raise FileNotFoundError(
            f"Image file not found: {image_path}"
        )

    extension = os.path.splitext(
        image_path
    )[1].lower()

    if extension not in SUPPORTED_EXTENSIONS:
        raise ValueError(
            "Unsupported image format. "
            "Use JPG, JPEG, PNG, or BMP."
        )

    return True