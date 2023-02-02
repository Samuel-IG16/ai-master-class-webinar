# Import library - OpenCV
import cv2

# read an image
img = cv2.imread("sampleImg.jpg")

# save an image
cv2.imwrite("sampleImgCopy.png", img)

# display an image until u close
cv2.imshow("Python LOGO", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
