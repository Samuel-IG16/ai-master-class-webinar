# import OpenCV and imutils library
import cv2
import imutils

# read an image
img = cv2.imread("sample2.jpg")

# resize an image
resizeImg = imutils.resize(img, width=100)

# save an image
cv2.imwrite("resizedImage.jpg", resizeImg)
