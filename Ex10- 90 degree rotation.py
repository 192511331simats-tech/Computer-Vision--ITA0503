import cv2

# Load the image
img = cv2.imread(r"C:\Users\SANJAY J\Downloads\CV image.jpg")
if img is None:
    print("Image not found!")
else:
    rotated_img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
    cv2.namedWindow("Original Image", cv2.WINDOW_NORMAL)
    cv2.namedWindow("Rotated Image", cv2.WINDOW_NORMAL)
    cv2.imshow("Original Image", img)
    cv2.imshow("Rotated Image", rotated_img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
