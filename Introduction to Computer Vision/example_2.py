# Import library - OpenCV
import cv2

# read an image
img = cv2.imread("sampleImg.jpg")

# color to gray image
grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# save an image
cv2.imwrite("graySampleImg.png", grayImg)

# display an image until u close
cv2.imshow("Orig", img)
cv2.imshow("Gray", grayImg)
cv2.waitKey(0)
cv2.destroyAllWindows()
