import cv2
import numpy as np

image = cv2.imread(r"C:\Users\SANJAY J\Downloads\CV image.jpg")

rows, cols, ch = image.shape

pts1 = np.float32([[50, 50], [400, 50], [50, 400], [400, 400]])
pts2 = np.float32([[10, 100], [300, 50], [100, 300], [350, 350]])

matrix = cv2.getPerspectiveTransform(pts1, pts2)

transformed_image = cv2.warpPerspective(image, matrix, (cols, rows))

cv2.namedWindow("Original Image", cv2.WINDOW_NORMAL)
cv2.namedWindow("Perspective Transformed Image", cv2.WINDOW_NORMAL)

cv2.imshow("Original Image", image)
cv2.imshow("Perspective Transformed Image", transformed_image)

cv2.imwrite(r"C:\Users\SANJAY J\Downloads\perspective_transformed.jpg", transformed_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
