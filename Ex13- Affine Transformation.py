import cv2
import numpy as np

image = cv2.imread(r"C:\Users\SANJAY J\Downloads\CV image.jpg")

rows, cols, ch = image.shape

pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
pts2 = np.float32([[10, 100], [200, 50], [100, 250]])

matrix = cv2.getAffineTransform(pts1, pts2)
transformed_image = cv2.warpAffine(image, matrix, (cols, rows))
cv2.namedWindow("Original Image", cv2.WINDOW_NORMAL)
cv2.namedWindow("Affine Transformed Image", cv2.WINDOW_NORMAL)
cv2.imshow("Original Image", image)
cv2.imshow("Affine Transformed Image", transformed_image)
cv2.imwrite(r"C:\Users\SANJAY J\Downloads\affine_transformed.jpg", transformed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
