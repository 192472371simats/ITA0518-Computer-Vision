import cv2
import numpy as np

image = cv2.imread("input23.jpg")

if image is None:
    print("Image not found!")
else:
    kernel = np.ones((5, 5), np.uint8)

    tophat = cv2.morphologyEx(
        image, cv2.MORPH_TOPHAT, kernel
    )

    cv2.imshow("Original Image", image)
    cv2.imshow("Top-Hat Operation", tophat)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
