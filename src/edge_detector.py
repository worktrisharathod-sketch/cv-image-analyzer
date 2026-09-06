import cv2


def detect_edges(image):
    gray_image = cv2.cvtColor(
        image,
        cv2.COLOR_BGR2GRAY
    )

    blurred_image = cv2.GaussianBlur(
        gray_image,
        (5, 5),
        0
    )

    edges = cv2.Canny(
        blurred_image,
        50,
        150
    )

    return edges