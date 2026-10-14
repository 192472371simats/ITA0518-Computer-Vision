import cv2
import numpy as np

image = cv2.imread("input16.jpg")

if image is None:
    print("Image not found!")
else:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Sobel filters
    sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

    sobel_x = cv2.convertScaleAbs(sobel_x)
    sobel_y = cv2.convertScaleAbs(sobel_y)

    result = cv2.addWeighted(sobel_x, 0.5, sobel_y, 0.5, 0)

    # Resize all outputs to fit the desktop
    size = (350, 250)

    original_small = cv2.resize(image, size)
    x_small = cv2.resize(sobel_x, size)
    y_small = cv2.resize(sobel_y, size)
    result_small = cv2.resize(result, size)

    cv2.imshow("1. Original Image", original_small)
    cv2.imshow("2. Sobel X", x_small)
    cv2.imshow("3. Sobel Y", y_small)
    cv2.imshow("4. Sobel Result", result_small)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
