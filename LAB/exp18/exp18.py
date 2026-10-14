import cv2

image = cv2.imread("input18.jpg")

if image is None:
    print("Image not found!")
else:

    roi = image[50:200, 50:200]

    result = image.copy()

    h, w = roi.shape[:2]

    x = 0
    y = 0

    result[y:y+h, x:x+w] = roi

    cv2.imshow("Original Image", image)
    cv2.imshow("Cropped ROI", roi)
    cv2.imshow("ROI Copied and Pasted", result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
