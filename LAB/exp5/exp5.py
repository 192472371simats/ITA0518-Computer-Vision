import cv2
import matplotlib.pyplot as plt

def analyze_histogram(image):

    colors = ('b', 'g', 'r')

    for i, color in enumerate(colors):
        histogram = cv2.calcHist([image], [i], None, [256], [0, 256])

        plt.plot(histogram, color=color)

    plt.title("Color Histogram")
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Number of Pixels")

    plt.show()


image = cv2.imread("input5.jpg")

analyze_histogram(image)
