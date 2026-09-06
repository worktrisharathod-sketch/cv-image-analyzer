def generate_report(
    image_path,
    face_count,
    image_analysis,
    quality_analysis,
    output_path
):
    report = (
        "Computer Vision Analysis Report\n"
        "===============================\n\n"

        f"Input image: {image_path}\n\n"

        "1. Face Detection\n"
        "-----------------\n"
        f"Faces detected: {face_count}\n\n"

        "2. Image Analysis\n"
        "-----------------\n"
        f"Width: {image_analysis['width']} pixels\n"
        f"Height: {image_analysis['height']} pixels\n"
        f"Channels: {image_analysis['channels']}\n"
        f"Total pixels: {image_analysis['total_pixels']}\n"
        f"Average brightness: "
        f"{image_analysis['average_brightness']}\n\n"

        "3. Image Quality Analysis\n"
        "-------------------------\n"
        f"Brightness status: "
        f"{quality_analysis['brightness_status']}\n"
        f"Sharpness score: "
        f"{quality_analysis['sharpness']}\n"
        f"Sharpness status: "
        f"{quality_analysis['sharpness_status']}\n\n"

        "4. Edge Detection\n"
        "-----------------\n"
        "Canny edge detection was applied "
        "to the input image.\n"
        "Edge map saved to: output/edges.jpg\n"
    )

    with open(
        output_path,
        "w",
        encoding="utf-8"
    ) as file:
        file.write(report)