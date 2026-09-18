import argparse
from pathlib import Path

from detector import ParkingDetector
from parking import summarize_detections


DEFAULT_MODEL = (
    Path(__file__).resolve().parent.parent
    / "runs"
    / "detect"
    / "runs"
    / "smart_parking"
    / "weights"
    / "best.pt"
)


def main():
    parser = argparse.ArgumentParser(
        description="Smart Parking Vision - parking space detection"
    )

    parser.add_argument(
        "--image",
        required=True,
        help="Path to the parking image",
    )

    parser.add_argument(
        "--model",
        default=str(DEFAULT_MODEL),
        help="Path to the trained YOLO model",
    )

    parser.add_argument(
        "--conf",
        type=float,
        default=0.25,
        help="Confidence threshold",
    )

    parser.add_argument(
        "--output",
        default="outputs/parking_result.jpg",
        help="Path for the annotated output image",
    )

    args = parser.parse_args()

    image_path = Path(args.image)

    if not image_path.exists():
        raise FileNotFoundError(
            f"Input image not found: {image_path}"
        )

    detector = ParkingDetector(args.model)
    results = detector.predict(
        image_path,
        conf=args.conf,
    )

    result = results[0]

    if result.boxes is None or len(result.boxes) == 0:
        class_ids = []
    else:
        class_ids = result.boxes.cls.cpu().numpy()

    summary = summarize_detections(
        result.names,
        class_ids,
    )

    output_path = Path(args.output)
    output_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    annotated_image = result.plot()
    result.save(filename=str(output_path))

    print("\nSmart Parking Vision")
    print("--------------------")
    print(f"Total spaces: {summary.total_spaces}")
    print(f"Empty spaces: {summary.empty_spaces}")
    print(f"Occupied spaces: {summary.occupied_spaces}")
    print(
        f"Occupancy: {summary.occupancy_percentage:.2f}%"
    )
    print(f"Output saved to: {output_path}")


if __name__ == "__main__":
    main()