import cv2
import matplotlib.pyplot as plt

# Read the image
image = cv2.imread("input4.jpg")

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply histogram equalization
equalized = cv2.equalizeHist(gray)

# Calculate histograms
original_hist = cv2.calcHist([gray], [0], None, [256], [0, 256])
equalized_hist = cv2.calcHist([equalized], [0], None, [256], [0, 256])

# Create one window with 4 sections
plt.figure(figsize=(10, 8))

# Original image
plt.subplot(2, 2, 1)
plt.imshow(gray, cmap="gray")
plt.title("Original Grayscale Image")
plt.axis("off")

# Original histogram
plt.subplot(2, 2, 2)
plt.plot(original_hist)
plt.title("Original Histogram")
plt.xlabel("Pixel Intensity")
plt.ylabel("Number of Pixels")
plt.xlim([0, 256])

# Equalized image
plt.subplot(2, 2, 3)
plt.imshow(equalized, cmap="gray")
plt.title("Histogram Equalized Image")
plt.axis("off")

# Equalized histogram
plt.subplot(2, 2, 4)
plt.plot(equalized_hist)
plt.title("Equalized Histogram")
plt.xlabel("Pixel Intensity")
plt.ylabel("Number of Pixels")
plt.xlim([0, 256])

# Adjust spacing
plt.tight_layout()

# Display everything
plt.show()
