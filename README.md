# Smart Parking Vision

A computer vision project that detects parking spaces and classifies them as empty or occupied using YOLO and the PKLot dataset.

## Project Overview

Smart Parking Vision uses a YOLO object detection model to identify parking spaces in parking-lot images.

The system can:

- Detect parking spaces
- Classify spaces as empty or occupied
- Calculate total parking spaces
- Calculate empty spaces
- Calculate occupied spaces
- Calculate parking occupancy percentage
- Generate an annotated output image

## Dataset

The project uses the PKLot dataset in YOLO format.

The dataset contains two classes:

- Class 0: space-empty
- Class 1: space-occupied

Dataset split:

- Training images: 8,691
- Validation images: 2,483
- Test images: 1,242
- Total images: 12,416

## Model

The project uses YOLO11n through Ultralytics.

The trained model is stored locally at:

runs/detect/runs/smart_parking/weights/best.pt

The trained model is excluded from GitHub because model files are large.

## Model Evaluation

The trained model was evaluated on the validation dataset.

Validation results:

- Precision: 0.961
- Recall: 0.972
- mAP@50: 0.980
- mAP@50-95: 0.773

Class-wise results:

### space-empty

- Precision: 0.973
- Recall: 0.947
- mAP@50: 0.976
- mAP@50-95: 0.776

### space-occupied

- Precision: 0.950
- Recall: 0.997
- mAP@50: 0.985
- mAP@50-95: 0.769

These results are measurements from the validation dataset and do not guarantee the same performance in real-world parking environments.

The model was also used to generate predictions for all 1,242 test images.

## Project Structure

smart-parking-vision/
config/
config.yaml
parking_slots.json
data/
input/
pklot_dataset/
docs/
README.md
statement.md
models/
outputs/
src/
__init__.py
detector.py
main.py
parking.py
tests/
test_parking.py
.gitignore
README.md
requirements.txt

## Installation

Create and activate a Python virtual environment.

Install the required packages:

pip install -r requirements.txt

## Usage

The application can be executed from the project root.

Example:

python .\src\main.py --image ".\data\pklot_dataset\test\images\2013-04-16_10_20_04_jpg.rf.cf2eeba0fef298a616a157669246fabe.jpg"

A custom trained model can also be specified:

python .\src\main.py --image ".\path\to\parking_image.jpg" --model ".\path\to\best.pt"

Example output:

Smart Parking Vision
--------------------
Total spaces: 43
Empty spaces: 1
Occupied spaces: 42
Occupancy: 97.67%
Output saved to: outputs\parking_result.jpg

The annotated image is saved to:

outputs/parking_result.jpg

## Testing

The project includes automated tests for the parking summary functionality.

Run the tests using:

pytest

The test suite covers:

- Empty parking summary
- Full parking summary
- Mixed parking summary
- YOLO detection summary conversion

Expected result:

4 passed

## Example Result

For one test image, the system detected:

- Total spaces: 43
- Empty spaces: 1
- Occupied spaces: 42
- Occupancy: 97.67%

The system generated an annotated parking image as the output.

## Technologies

The project uses:

- Python 3.12
- OpenCV
- NumPy
- Pandas
- Matplotlib
- Ultralytics YOLO
- PyYAML
- Pytest

## Dataset Attribution

The PKLot dataset used in this project was obtained in YOLO format from Roboflow.

The dataset metadata identifies the license as CC BY 4.0.

Dataset source:

https://universe.roboflow.com/brad-dwyer/pklot-1tros/dataset/2

The dataset remains subject to its original license and attribution requirements.

## Limitations

The current system works with parking-lot images and uses object detection to identify parking spaces.

Performance may vary depending on:

- Camera viewpoint
- Lighting conditions
- Occlusions
- Image quality
- Parking-lot layout
- Differences between training images and real-world environments

The reported evaluation results are specific to the dataset split used for evaluation.

## Future Improvements

Possible future improvements include:

- Real-time video processing
- Parking-space tracking
- Automatic parking-slot mapping
- Web-based parking dashboard
- Historical occupancy statistics
- Multiple camera support
- Edge-device deployment

## License

This project was developed for educational purposes as a computer vision project.

The dataset remains subject to its original license and attribution requirements.