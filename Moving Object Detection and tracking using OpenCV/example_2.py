# import OpenCV library
import cv2

# read an image
img = cv2.imread("sampleImg.jpg")

# blur an image
gaussianBlurImg = cv2.GaussianBlur(img, (25, 25), 0)

# save an image
cv2.imwrite("gaussianSampleImg.jpg", gaussianBlurImg)
