# import OpenCV library, time and imutils
import cv2, time, imutils

# cam id
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
time.sleep(1)

firstFrame = None
area = 500

# read frame from camera
while True:
    check, frame = cam.read()
    text = "Normal"
    frame = imutils.resize(frame, width=500)    # resize

    grayFrame  = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)    # color 2 Gray scale image

    gaussianFrame = cv2.GaussianBlur(grayFrame, (21, 21), 0)    # smoothened

    if firstFrame is None:
        firstFrame  = gaussianFrame   # capturing 1st frame on 1st iteration
        continue

    frameDiff = cv2.absdiff(firstFrame, gaussianFrame)  # absolute diff b/w 1st frame and current frame
    
    threshFrame = cv2.threshold(frameDiff, 25, 255, cv2.THRESH_BINARY)[1]   # binary
    
    threshFrame = cv2.dilate(threshFrame, None, iterations=2)
    
    cnts = cv2.findContours(threshFrame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    cnts = imutils.grab_contours(cnts)
    for c in cnts:
        if cv2.contourArea(c) < area:
            continue
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        text = "Moving Object detected"
    print(text)
    cv2.putText(frame, text, (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    cv2.imshow("cameraFeed", frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

cam.release()
cv2.destroyAllWindows()
