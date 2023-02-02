# import OpenCV library
import cv2

# initialize the camera
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# reading the frame from the camera
while True:
    check, frame = cap.read()
    cv2.imshow("VideoStream", frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

# releasing the camera
cap.release()

# close all windows
cv2.destroyAllWindows()
