from pathlib import Path

from ultralytics import YOLO


class ParkingDetector:
    def __init__(self, model_path):
        model_path = Path(model_path)

        if not model_path.exists():
            raise FileNotFoundError(
                f"Model file not found: {model_path}"
            )

        self.model = YOLO(str(model_path))

    def predict(self, image_path, conf=0.25):
        """
        Run parking-space detection on an image.
        """
        return self.model.predict(
            source=str(image_path),
            conf=conf,
            verbose=False,
        )