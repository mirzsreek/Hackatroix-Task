# Adaptive Ball Detection using YOLOv11

## Overview
Adaptive Ball Detection is a computer vision project that detects sports balls in real time using the YOLOv11 object detection model. The system works with both images and a live webcam feed, making it suitable for sports analytics, training systems, and AI-based tracking applications.

## Features
- Real-time ball detection using webcam
- Detects sports balls in images
- Fast YOLOv11-based inference
- Bounding box visualization
- Easy to use and extend

## Technologies Used
- Python
- YOLOv11
- OpenCV
- Ultralytics
- PyTorch

## Project Structure

Adaptive Ball Detection/
│
├── main.py
├── requirements.txt
├── README.md
├── yolo11n.pt
├── src/
│   ├── app.py
│   └── best.pt
├── sports-ball.yolov11/
├── runs/

## Installation

```bash
pip install -r requirements.txt
```

## Run

```bash
python main.py
```

## Future Improvements

- Multiple ball tracking
- Ball speed estimation
- Trajectory prediction
- Player-ball interaction analysis

## Author

Developed for Hackathon Submission.