import cv2
import time
from ultralytics import YOLO

# Load your trained model
model = YOLO("src/best.pt")

# Open webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

prev_time = 0

while True:
    # Read frame
    ret, frame = cap.read()

    if not ret:
        break

    # Run detection
    results = model(frame, conf=0.25)

    # Draw detections
    annotated_frame = results[0].plot()

    # Calculate FPS
    current_time = time.time()
    fps = 1 / (current_time - prev_time) if prev_time != 0 else 0
    prev_time = current_time

    # Display FPS
    cv2.putText(
        annotated_frame,
        f"FPS: {fps:.2f}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    # Display title
    cv2.putText(
        annotated_frame,
        "Adaptive Ball Detection",
        (20, 80),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (255, 0, 0),
        2
    )

    # Show webcam
    cv2.imshow("Adaptive Ball Detection", annotated_frame)

    # Press Q to exit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()