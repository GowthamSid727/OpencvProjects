import cv2
import numpy as np


cap = cv2.VideoCapture(0)
width = 540
height = 280
cap.set(3,width)
cap.set(4,height)
cap.set(10,150)

myColors = [[32,0,0,162,226,175],
            [85,77,0,110,255,255]]
myColorsValues=[[0,0,0],
                [255,0,0]]
myPoints=[]
def findColors(img,myColors,myColorValues):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    count = 0
    newPoints=[]
    for clr in myColors:
        lower =np.array(clr[0:3])
        uper = np.array(clr[3:6])
        mask = cv2.inRange(imgHSV, lower, uper)
        x,y =getContour(mask)
        #cv2.imshow("img", mask)
        cv2.circle(imgResult,(x,y),10,myColorsValues[count],cv2.FILLED)
        if x!=0 and y!=0:
            newPoints.append([x,y,count])
        count+=1
    return  newPoints
def getContour(img):
    x,y,w,h=0,0,0,0
    contour, hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contour:
        area = cv2.contourArea(cnt)
        if area>500:
            #cv2.drawContours(imgResult,cnt,-1,(0,255,0),3)
            length = cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt,0.02*length,True)
            x, y, w, h = cv2.boundingRect(approx)
    return x+w//2, y
def drawCanvas(myPoints,myColorsValues):
    for myPoint in myPoints:
        cv2.circle(imgResult,(myPoint[0],myPoint[1]),10,(myColorsValues[myPoint[2]]),cv2.FILLED)
while True:
    success, img = cap.read()
    imgResult = img.copy()
    newPoints = findColors(img, myColors,myColorsValues)
    for newP in newPoints:
        if len(newPoints)!=0:
            myPoints.append(newP)
        if len(myPoints)!=0:
            drawCanvas(myPoints,myColorsValues)
    cv2.imshow("Output",imgResult)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
