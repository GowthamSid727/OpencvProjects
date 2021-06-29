import cv2
import numpy as np
from other import stackImages as SI
def empty(x):
    pass
img = cv2.imread("Resources/Mazda.jpg");
cv2.namedWindow("Trackbar")
cv2.resizeWindow("Trackbar",640,240)
cv2.createTrackbar("h_max","Trackbar",179,179,empty)
cv2.createTrackbar("h_min","Trackbar",0,179,empty)
cv2.createTrackbar("s_max","Trackbar",255,255,empty)
cv2.createTrackbar("s_min","Trackbar",129,255,empty)
cv2.createTrackbar("v_max","Trackbar",255,255,empty)
cv2.createTrackbar("v_min","Trackbar",0,255,empty)

while True:
    imgHsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    h_max = cv2.getTrackbarPos("h_max","Trackbar")
    h_min = cv2.getTrackbarPos("h_min", "Trackbar")
    s_max = cv2.getTrackbarPos("s_max", "Trackbar")
    s_min = cv2.getTrackbarPos("s_min", "Trackbar")
    v_max = cv2.getTrackbarPos("v_max", "Trackbar")
    v_min = cv2.getTrackbarPos("v_min", "Trackbar")
    lower = np.array([h_min,s_min,v_min])
    uper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imgHsv,lower,uper)
    imgResult = cv2.bitwise_and(img,imgHsv,mask=mask)
    Result = SI.StackImage(0.6,([img,imgHsv],[mask,imgResult]))
    cv2.imshow("Result", Result)
    if cv2.waitKey(1)&0xFF==ord('q'):
        break
