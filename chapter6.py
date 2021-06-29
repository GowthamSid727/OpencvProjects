import cv2
import numpy as np
from other import stackImages as SI

width = 640
height = 480
cap = cv2.VideoCapture(0)
cap.set(3,width)
cap.set(4,height)
while True:
    success,img = cap.read()
    kernel = np.ones((5, 5), np.uint8)
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(img, (7, 7), 0)
    imgCanny = cv2.Canny(img, 100, 200)
    imgDilation = cv2.dilate(imgCanny, kernel, iterations=1)
    imgerode = cv2.erode(imgDilation, kernel, iterations=1)

    imgstack = SI.StackImage(0.6,([img,imgGray,imgBlur],[imgCanny,imgDilation,imgerode]))
    cv2.imshow("Stacked Image",imgstack)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break


