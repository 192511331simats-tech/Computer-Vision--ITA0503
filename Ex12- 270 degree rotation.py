import cv2

# Read the image
image = cv2.imread(r"C:\Users\SANJAY J\Downloads\CV image.jpg")

if image is None:
    print("Image not found!")
else:
    flipped_image = cv2.flip(image, 1)
    rotated_image = cv2.rotate(flipped_image, cv2.ROTATE_90_COUNTERCLOCKWISE)
    cv2.namedWindow("Original Image", cv2.WINDOW_NORMAL)
    cv2.namedWindow("Rotated 270-degree Clockwise Along Y-axis", cv2.WINDOW_NORMAL)
    cv2.imshow("Original Image", image)
    cv2.imshow("Rotated 270-degree Clockwise Along Y-axis", rotated_image)
    cv2.imwrite(r"C:\Users\SANJAY J\Downloads\rotated_image_270.jpg", rotated_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
