import cv2
import mediapipe as mp
import math

# ==========================
# CONSTANTS
# ==========================
KNOWN_FACE_WIDTH = 0.15      # meters
FOCAL_LENGTH = 700           # pixels (adjust later)

# Smoothing
previous_depth = 0
previous_angle = 0
SMOOTHING_FACTOR = 0.8

# ==========================
# MEDIAPIPE
# ==========================
mp_face_detection = mp.solutions.face_detection

face_detection = mp_face_detection.FaceDetection(
    model_selection=0,
    min_detection_confidence=0.5
)

# ==========================
# WEBCAM
# ==========================
cap = cv2.VideoCapture(0)

while cap.isOpened():

    success, frame = cap.read()

    if not success:
        break

    image_height, image_width, _ = frame.shape

    image_center_x = image_width // 2
    image_center_y = image_height // 2

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = face_detection.process(rgb)

    # Draw camera center line
    cv2.line(
        frame,
        (image_center_x, 0),
        (image_center_x, image_height),
        (255, 255, 0),
        2
    )

    if results.detections:

        for detection in results.detections:

            bbox = detection.location_data.relative_bounding_box

            x = int(bbox.xmin * image_width)
            y = int(bbox.ymin * image_height)
            w = int(bbox.width * image_width)
            h = int(bbox.height * image_height)

            # Face center
            face_center_x = x + w // 2
            face_center_y = y + h // 2

            # Draw bounding box
            cv2.rectangle(
                frame,
                (x, y),
                (x + w, y + h),
                (0, 255, 0),
                2
            )

            # Draw face center
            cv2.circle(
                frame,
                (face_center_x, face_center_y),
                5,
                (0, 0, 255),
                -1
            )

            # Draw horizontal deviation line
            cv2.line(
                frame,
                (image_center_x, face_center_y),
                (face_center_x, face_center_y),
                (255, 0, 255),
                2
            )

            # -------------------------
            # DEPTH
            # -------------------------
            if w > 0:
                raw_depth = (FOCAL_LENGTH * KNOWN_FACE_WIDTH) / w
            else:
                raw_depth = previous_depth

            depth = (
                SMOOTHING_FACTOR * previous_depth
                + (1 - SMOOTHING_FACTOR) * raw_depth
            )

            previous_depth = depth

            # -------------------------
            # ANGLE
            # -------------------------
            raw_angle = math.degrees(
                math.atan(
                    (face_center_x - image_center_x) / FOCAL_LENGTH
                )
            )

            angle = (
                SMOOTHING_FACTOR * previous_angle
                + (1 - SMOOTHING_FACTOR) * raw_angle
            )

            previous_angle = angle

            # -------------------------
            # DISPLAY
            # -------------------------
            cv2.putText(
                frame,
                "MONOCULAR FACE DISTANCE ESTIMATOR",
                (20, 30),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (255,255,255),
                2
            )

            cv2.putText(
                frame,
                f"Face Width : {w} px",
                (20,70),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0,255,0),
                2
            )

            cv2.putText(
                frame,
                f"Depth : {depth:.2f} m",
                (20,105),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (255,0,0),
                2
            )

            cv2.putText(
                frame,
                f"Angle : {angle:.2f} deg",
                (20,140),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0,0,255),
                2
            )

            # Status
            cv2.putText(
                frame,
                "STATUS : TRACKING",
                (20,175),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0,255,255),
                2
            )

    else:

        cv2.putText(
            frame,
            "STATUS : NO FACE DETECTED",
            (20,40),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0,0,255),
            2
        )

    cv2.imshow("HackTronix - Face Distance Estimation", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()