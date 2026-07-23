import cv2
import numpy as np

# Read the image
image = cv2.imread(r"C:\Users\SANJAY J\Downloads\CV image.jpg")

if image is None:
    print("Image not found!")
else:
    kernel = np.ones((5, 5), np.uint8)
    dilated = cv2.dilate(image, kernel, iterations=1)
    cv2.namedWindow("Original Image", cv2.WINDOW_NORMAL)
    cv2.namedWindow("Dilated Image", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Original Image", 600, 400)
    cv2.resizeWindow("Dilated Image", 600, 400)
    cv2.imshow("Original Image", image)
    cv2.imshow("Dilated Image", dilated)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
