import cv2
import numpy as np

image = cv2.imread("input14.jpg")

if image is None:
    print("Image not found!")
else:
    points1 = np.float32([
        [50, 50],
        [400, 50],
        [400, 300],
        [50, 300]
    ])

    points2 = np.float32([
        [0, 0],
        [300, 0],
        [300, 400],
        [0, 400]
    ])

    matrix = cv2.getPerspectiveTransform(points1, points2)
    result = cv2.warpPerspective(image, matrix, (300, 400))

    cv2.imshow("Original Image", image)
    cv2.imshow("Perspective Transformation", result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
