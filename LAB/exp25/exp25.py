
import cv2
from ultralytics import YOLO

# Load the pretrained object recognition model
model = YOLO("yolov8n-oiv7.pt")

# Read the input image
image = cv2.imread("watch_scene.jpg")

if image is None:
    print("Error: watch_scene.jpg not found.")

else:
    # Perform general object detection
    results = model.predict(
        source=image,
        conf=0.20,
        verbose=False
    )

    output = image.copy()
    watch_found = False

    # Examine detected objects
    for result in results:
        for box in result.boxes:
            class_id = int(box.cls[0])
            label = result.names[class_id]
            confidence = float(box.conf[0])

            # Select the watch object
            if label.lower() == "watch":
                x1, y1, x2, y2 = map(
                    int, box.xyxy[0].tolist()
                )

                cv2.rectangle(
                    output, (x1, y1), (x2, y2),
                    (0, 255, 0), 3
                )

                cv2.putText(
                    output,
                    "Watch: " + str(round(confidence, 2)),
                    (x1, max(y1 - 10, 20)),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7, (0, 255, 0), 2
                )

                watch_found = True

    if watch_found:
        print("Watch detected successfully.")
    else:
        print("Watch not detected in this image.")

    # Resize output to fit the screen
    h, w = output.shape[:2]
    scale = min(800 / w, 600 / h, 1.0)
    output = cv2.resize(
        output, None, fx=scale, fy=scale
    )

    cv2.imshow("Watch Object Recognition", output)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
