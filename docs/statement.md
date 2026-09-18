\# Smart Parking Vision



\## Project Title



Smart Parking Vision



\## Project Description



Smart Parking Vision is a computer vision application that detects parking spaces in parking-lot images and classifies each detected space as either empty or occupied.



The project uses the YOLO11n object detection model through the Ultralytics framework and the PKLot dataset in YOLO format.



\## Objective



The main objective of this project is to develop a computer vision system that can automatically analyze a parking-lot image and provide a parking occupancy summary.



The system identifies parking spaces and calculates:



\- Total parking spaces

\- Empty parking spaces

\- Occupied parking spaces

\- Parking occupancy percentage



It also generates an annotated image containing the detection results.



\## Dataset



The project uses the PKLot dataset in YOLO format.



The dataset contains two classes:



\- Class 0: space-empty

\- Class 1: space-occupied



Dataset split:



\- Training images: 8,691

\- Validation images: 2,483

\- Test images: 1,242

\- Total images: 12,416



\## Methodology



The project follows these main steps:



1\. Prepare the PKLot dataset in YOLO format.

2\. Configure the YOLO11n object detection model.

3\. Train the model using the training dataset.

4\. Evaluate the trained model using the validation dataset.

5\. Run predictions on parking-lot images.

6\. Count empty and occupied parking spaces.

7\. Calculate the parking occupancy percentage.

8\. Generate an annotated output image.



\## Model



The project uses YOLO11n through Ultralytics.



The trained model was evaluated using the validation dataset.



Validation results:



\- Precision: 0.961

\- Recall: 0.972

\- mAP@50: 0.980

\- mAP@50-95: 0.773



Class-wise results:



\### space-empty



\- Precision: 0.973

\- Recall: 0.947

\- mAP@50: 0.976

\- mAP@50-95: 0.776



\### space-occupied



\- Precision: 0.950

\- Recall: 0.997

\- mAP@50: 0.985

\- mAP@50-95: 0.769



These results are measurements from the validation dataset.



\## Application Output



For one test image, the application produced the following parking summary:



\- Total spaces: 43

\- Empty spaces: 1

\- Occupied spaces: 42

\- Occupancy: 97.67%



The application also generates an annotated parking-lot image.



\## Technologies Used



\- Python 3.12

\- OpenCV

\- NumPy

\- Pandas

\- Matplotlib

\- Ultralytics YOLO

\- PyYAML

\- Pytest



\## Testing



The project includes automated tests for the parking summary functionality.



The test suite covers:



\- Empty parking summary

\- Full parking summary

\- Mixed parking summary

\- YOLO detection summary conversion



The completed test suite contains 4 tests.



\## Project Structure



The project is organized into configuration, source code, tests, documentation, data, model outputs, and generated results.



Important source files include:



\- `src/detector.py` - YOLO detection functionality

\- `src/parking.py` - parking summary calculations

\- `src/main.py` - command-line application

\- `tests/test\_parking.py` - automated tests

\- `config/config.yaml` - project configuration



\## Limitations



The current system works with parking-lot images and uses object detection to identify parking spaces.



Performance may vary depending on:



\- Camera viewpoint

\- Lighting conditions

\- Occlusions

\- Image quality

\- Parking-lot layout

\- Differences between training images and real-world environments



The reported evaluation results are specific to the dataset split used for evaluation.



\## Future Improvements



Possible future improvements include:



\- Real-time video processing

\- Parking-space tracking

\- Automatic parking-slot mapping

\- Web-based parking dashboard

\- Historical occupancy statistics

\- Multiple camera support

\- Edge-device deployment



\## Dataset Attribution



The PKLot dataset used in this project was obtained in YOLO format from Roboflow.



The dataset metadata identifies the license as CC BY 4.0.



Dataset source:



https://universe.roboflow.com/brad-dwyer/pklot-1tros/dataset/2



The dataset remains subject to its original license and attribution requirements.



\## Conclusion



Smart Parking Vision demonstrates the use of object detection for automated parking-space analysis.



The system can detect and classify parking spaces, calculate occupancy information, and generate an annotated result image from a parking-lot image.

