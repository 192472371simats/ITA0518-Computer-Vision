import cv2

image = cv2.imread("lena.jpg")
logo = cv2.imread("logo.png", cv2.IMREAD_UNCHANGED)

if image is None or logo is None:
    print("Image or logo not found!")
else:
    # Resize logo
    logo = cv2.resize(logo, (100, 100))

    # Use the top-right corner for the watermark
    h, w = image.shape[:2]
    x = w - 110
    y = 10

    # Handle transparent PNG logos
    if logo.shape[2] == 4:
        overlay = image.copy()
        alpha = logo[:, :, 3] / 255.0

        for c in range(3):
            overlay[y:y+100, x:x+100, c] = (
                alpha * logo[:, :, c]
                + (1 - alpha) * image[y:y+100, x:x+100, c]
            )

        image = overlay
    else:
        image[y:y+100, x:x+100] = logo[:, :, :3]

    cv2.imshow("Watermarked Image", image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
