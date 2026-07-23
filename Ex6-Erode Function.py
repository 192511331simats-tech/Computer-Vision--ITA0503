import cv2
import numpy as np

image = cv2.imread(r"C:\Users\SANJAY J\Downloads\CV image.jpg")

if image is None:
    print("Error: Image not found!")
    exit()

image = cv2.resize(image, (0, 0), fx=0.25, fy=0.25)

kernel = np.ones((5, 5), np.uint8)

eroded_image = cv2.erode(image, kernel, iterations=1)

cv2.imshow("Original Image", image)
cv2.imshow("Eroded Image", eroded_image)

cv2.imwrite("eroded_image.jpg", eroded_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
