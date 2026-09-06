import cv2


def draw_detections(image, detections):
    result = image.copy()

    for x, y, width, height in detections:
        cv2.rectangle(
            result,
            (x, y),
            (x + width, y + height),
            (0, 255, 0),
            2
        )

    return result


def save_image(image, output_path):
    success = cv2.imwrite(
        output_path,
        image
    )

    if not success:
        raise IOError(
            f"Could not save image: {output_path}"
        )