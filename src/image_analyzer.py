import cv2


def analyze_image(image):
    height, width, channels = image.shape

    gray_image = cv2.cvtColor(
        image,
        cv2.COLOR_BGR2GRAY
    )

    average_brightness = gray_image.mean()

    return {
        "width": width,
        "height": height,
        "channels": channels,
        "total_pixels": width * height,
        "average_brightness": round(
            float(average_brightness),
            2
        )
    }