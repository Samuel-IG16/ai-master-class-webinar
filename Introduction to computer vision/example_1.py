# Import library - OpenCV
import cv2

# read an image
img = cv2.imread("sample2.jpg")

# save an image
cv2.imwrite("sample2Copy.png", img)

# display an image until u close
cv2.imshow("Python LOGO", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
