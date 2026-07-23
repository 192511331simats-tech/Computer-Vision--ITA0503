import cv2

video = cv2.VideoCapture(r"C:\Users\SANJAY J\Downloads\13088713_2160_3840_30fps.mp4")

# Create resizable windows
cv2.namedWindow("Original Video", cv2.WINDOW_NORMAL)
cv2.namedWindow("Slow Motion", cv2.WINDOW_NORMAL)
cv2.namedWindow("Fast Motion", cv2.WINDOW_NORMAL)

while video.isOpened():
    ret, frame = video.read()

    if not ret:
        break

    cv2.imshow("Original Video", frame)
    cv2.imshow("Slow Motion", frame)
    cv2.imshow("Fast Motion", frame)

    cv2.waitKey(30)
    cv2.waitKey(100)
    key = cv2.waitKey(10)

    if key & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
