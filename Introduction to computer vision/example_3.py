# Import library - OpenCV
import cv2

# read an image
img = cv2.imread("sample2.jpg")

# color to grayscale
grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# threshold the image
threshImg = cv2.threshold(grayImg, 185, 255, cv2.THRESH_BINARY)[1]

# save an image
cv2.imwrite("threshsample2.png", threshImg)

# display an image until u close
cv2.imshow("Thresh", threshImg)
cv2.waitKey(0)
cv2.destroyAllWindows()
