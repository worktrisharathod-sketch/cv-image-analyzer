import sys

from src.image_loader import load_image
from src.input_validator import validate_image_path

from src.detectors.face_detector import detect_faces

from src.image_analyzer import analyze_image
from src.quality_analyzer import analyze_quality
from src.edge_detector import detect_edges

from src.utils.image_utils import (
    draw_detections,
    save_image
)

from src.reporting.report_generator import (
    generate_report
)


def main():
    if len(sys.argv) > 1:
        input_path = sys.argv[1]
    else:
        input_path = "input/test.jpg"

    output_image_path = "output/result.jpg"
    output_edges_path = "output/edges.jpg"
    output_report_path = "output/report.txt"

    try:
        validate_image_path(input_path)

        image = load_image(input_path)

        faces = detect_faces(image)

        image_analysis = analyze_image(image)

        quality_analysis = analyze_quality(image)

        edges = detect_edges(image)

        result_image = draw_detections(
            image,
            faces
        )

        save_image(
            result_image,
            output_image_path
        )

        save_image(
            edges,
            output_edges_path
        )

        generate_report(
            input_path,
            len(faces),
            image_analysis,
            quality_analysis,
            output_report_path
        )

        print()
        print("================================")
        print(" COMPUTER VISION ANALYZER")
        print("================================")
        print()
        print("Analysis completed successfully.")
        print()
        print(f"Input image: {input_path}")
        print(f"Faces detected: {len(faces)}")
        print(
            f"Image size: "
            f"{image_analysis['width']} x "
            f"{image_analysis['height']}"
        )
        print(
            f"Average brightness: "
            f"{image_analysis['average_brightness']}"
        )
        print(
            f"Brightness status: "
            f"{quality_analysis['brightness_status']}"
        )
        print(
            f"Sharpness status: "
            f"{quality_analysis['sharpness_status']}"
        )
        print()
        print(f"Result image: {output_image_path}")
        print(f"Edge image: {output_edges_path}")
        print(f"Report: {output_report_path}")
        print()

    except (
        FileNotFoundError,
        ValueError,
        IOError,
        RuntimeError
    ) as error:
        print()
        print(f"Error: {error}")
        print(
            "Please check the input image "
            "and try again."
        )


if __name__ == "__main__":
    main()