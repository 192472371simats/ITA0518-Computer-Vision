import cv2

image = cv2.imread("input9.jpg")

small = cv2.resize(image, (300, 200))

big = cv2.resize(image, (800, 600))

cv2.imshow("Original Image", image)

cv2.imshow("Smaller Image", small)

cv2.imshow("Bigger Image", big)

cv2.waitKey(0)

cv2.destroyAllWindows()
