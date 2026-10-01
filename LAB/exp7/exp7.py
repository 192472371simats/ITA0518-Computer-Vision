import cv2

video = cv2.VideoCapture("video.mp4")

print("Playing video in SLOW MOTION...")

while True:

    ret, frame = video.read()

    if not ret:
        break

    cv2.imshow("Slow Motion", frame)

    key = cv2.waitKey(100)

    if key == ord('q'):
        video.release()
        cv2.destroyAllWindows()
        exit()

video.release()
cv2.destroyAllWindows()

video = cv2.VideoCapture("video.mp4")

print("Playing video in FAST MOTION...")

while True:

    ret, frame = video.read()

    if not ret:
        break

    cv2.imshow("Fast Motion", frame)

    key = cv2.waitKey(10)

    if key == ord('q'):
        break

video.release()

cv2.destroyAllWindows()
