import cv2

image = cv2.imread("input12.jpg")

rotated = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)

cv2.imshow("Original Image", image)

cv2.imshow("270 Degree Clockwise", rotated)

cv2.waitKey(0)

cv2.destroyAllWindows()
