import cv2
import numpy as np
from other import stackImages as SI
#empty
def empty(a):
    pass
#video capturing
cap = cv2.VideoCapture(0)
width = 680
height = 480
cap.set(3,width)
cap.set(4,height)
cap.set(10,120)
#Trackerbar
cv2.namedWindow("Trackbar")
cv2.resizeWindow("Trackbar",640,280)
cv2.createTrackbar("h_max","Trackbar",179,179,empty)
cv2.createTrackbar("h_min","Trackbar",0,179,empty)
cv2.createTrackbar("s_max","Trackbar",255,255,empty)
cv2.createTrackbar("s_min","Trackbar",0,255,empty)
cv2.createTrackbar("v_max","Trackbar",255,255,empty)
cv2.createTrackbar("v_min","Trackbar",0,255,empty)
#loop
while True:
    success, img = cap.read()
    imgHsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    h_max = cv2.getTrackbarPos("h_max", "Trackbar")
    h_min = cv2.getTrackbarPos("h_min", "Trackbar")
    s_max = cv2.getTrackbarPos("s_max", "Trackbar")
    s_min = cv2.getTrackbarPos("s_min", "Trackbar")
    v_max = cv2.getTrackbarPos("v_max", "Trackbar")
    v_min = cv2.getTrackbarPos("v_min", "Trackbar")
    lower = np.array([h_min, s_min, v_min])
    uper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imgHsv, lower, uper)
    imgResult = cv2.bitwise_and(img, imgHsv, mask=mask)
    imgblank = np.zeros_like(img)
    imgstack = SI.StackImage(0.6,([img,imgResult],[mask,imgblank]))
    cv2.imshow("Output",imgstack)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
