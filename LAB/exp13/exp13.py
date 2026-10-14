import cv2
import numpy as np
image = cv2.imread("input13.jpg")
if image is None:
    print("Error: image.jpg not found")
else:
    rows, cols = image.shape[:2]
    points1 = np.float32([
        [50, 50],
        [200, 50],
        [50, 200]
    ])
    points2 = np.float32([
        [80, 80],
        [220, 60],
        [100, 220]
    ])
    matrix = cv2.getAffineTransform(points1, points2)
    result = cv2.warpAffine(image, matrix, (cols, rows))
    cv2.imshow("Original Image", image)
    cv2.imshow("Affine Transformation", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
