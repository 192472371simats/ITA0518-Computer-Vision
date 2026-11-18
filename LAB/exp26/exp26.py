import cv2

def reverse_video():
    video = cv2.VideoCapture("video.mp4")

    frames = []

    while True:
        ret, frame = video.read()

        if not ret:
            break

        frames.append(frame)

    video.release()

    if len(frames) == 0:
        print("Video not found or empty")
        return

    height, width, _ = frames[0].shape

    fps = 30

    output = cv2.VideoWriter(
        "reverse_video.mp4",
        cv2.VideoWriter_fourcc(*"mp4v"),
        fps,
        (width, height)
    )

    for frame in reversed(frames):
        output.write(frame)

    output.release()

    print("Reverse video created successfully")

reverse_video()
