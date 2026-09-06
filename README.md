# 📷 Monocular Face Distance & Angle Estimation

## 📌 Overview

This project estimates the **depth (distance)** and **horizontal deviation angle** of a human face using a **single monocular webcam**.

The system detects a face in real time using **MediaPipe Face Detection** and applies the **Pinhole Camera Model** to estimate the face's distance from the camera. It also computes the horizontal angle of the detected face relative to the camera's optical center.

This implementation was developed as part of the **HackTronix 2.0** Round 1 Computer Vision challenge.

---

🎯 Objective

Develop a real-time computer vision system capable of estimating:

- Face Depth (Distance from Camera)
- Horizontal Deviation Angle
- Face Width in Pixels

using only a **single RGB camera**.

---

 🛠 Technologies Used

- Python 3.12
- OpenCV
- MediaPipe Face Detection
- NumPy
- Math Library

---

## ⚙ Working Principle

 Step 1 – Capture Webcam Frame

The webcam continuously captures video frames.

### Step 2 – Face Detection

MediaPipe detects the face and returns a bounding box around it.

### Step 3 – Face Width Extraction

The width of the detected bounding box is converted from normalized coordinates to pixel values.

### Step 4 – Depth Estimation

Using the Pinhole Camera Model,

\[
Z=\frac{f\times W}{w_{px}}
\]

where

| Symbol | Description |
|---------|-------------|
| Z | Estimated depth (meters) |
| f | Camera focal length (pixels) |
| W | Average real face width (0.15 m) |
| wₚₓ | Face width in pixels |

As the face moves farther away, its apparent width decreases, resulting in a larger estimated distance.

---

### Step 5 – Horizontal Angle Estimation

The horizontal deviation angle is calculated using

\[
\theta=\arctan\left(\frac{x-c_x}{f}\right)
\]

where

| Symbol | Description |
|---------|-------------|
| x | Face center x-coordinate |
| cₓ | Image center x-coordinate |
| f | Camera focal length |

Interpretation:

- Negative Angle → Face is left of camera center
- Positive Angle → Face is right of camera center
- Approximately 0° → Face is centered

---

## ✨ Features

- Real-time webcam processing
- Fast face detection using MediaPipe
- Monocular depth estimation
- Horizontal angle estimation
- Face bounding box visualization
- Face center tracking
- Camera center reference line
- Smoothed distance and angle values
- Live status display

---

## 📊 Sample Output

```
Face Width : 214 px

Depth : 0.92 m

Angle : -7.8°

Status : TRACKING
```

---

## 📂 Project Structure

```
FaceDistanceEstimator/

│── main.py
│── README.md
│── requirements.txt
```

---

## 📈 Assumptions

- A single monocular camera is used.
- The Pinhole Camera Model is assumed.
- Average human face width is approximately **0.15 meters**.
- Camera focal length is calibrated experimentally.

---

## ⚠ Limitations

- Assumes an average face width for all users.
- Accuracy depends on camera calibration.
- Performance may vary under poor lighting conditions.
- Large head rotations can reduce estimation accuracy.

---

## 🚀 Future Improvements

- Automatic camera calibration
- Multi-face tracking
- Head pose estimation
- 3D facial landmark integration
- Higher-accuracy depth estimation using deep learning

---

 📸 Demonstration

The application performs the following in real time:

- Detects a human face
- Draws a bounding box around the face
- Computes face width in pixels
- Estimates distance from the camera
- Calculates horizontal deviation angle
- Displays live tracking information

---

👨‍💻 Author

Developed for **HackTronix 2.0 – Round 1 Submission**

Built using **Python, OpenCV, and MediaPipe**.