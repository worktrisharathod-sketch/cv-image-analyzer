import cv2


def analyze_quality(image):
    gray_image = cv2.cvtColor(
        image,
        cv2.COLOR_BGR2GRAY
    )

    average_brightness = gray_image.mean()

    sharpness = cv2.Laplacian(
        gray_image,
        cv2.CV_64F
    ).var()

    if average_brightness < 60:
        brightness_status = "Too Dark"
    elif average_brightness > 200:
        brightness_status = "Too Bright"
    else:
        brightness_status = "Good"

    if sharpness < 100:
        sharpness_status = "Blurry"
    else:
        sharpness_status = "Sharp"

    return {
        "brightness_status": brightness_status,
        "sharpness": round(float(sharpness), 2),
        "sharpness_status": sharpness_status
    }