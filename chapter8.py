import cv2
import numpy as np
from other import stackImages as SI
def getcontour(img):
    contour, hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contour:
        area = cv2.contourArea(cnt)
        if(area>500):
            peri = cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            print(len(approx))
            objlen = len(approx)
            x,y,w,h = cv2.boundingRect(approx)
            if objlen==3:objname="Tri"
            elif objlen==4:
                aspectratio = w/float(h)
                if aspectratio>0.95 and aspectratio<1.05:
                    objname="Square"
                else:
                    objname="Rect"
            elif objlen >5:objname="Circle"
            else:objname="None"
            cv2.rectangle(imgContour,(x,y),(x+w,y+h),(255,0,0),2)
            cv2.putText(imgContour,objname,((x+(w//2)-10),(y+(h//2)-10)),cv2.FONT_HERSHEY_COMPLEX,0.6,(0,0,255))

img = cv2.imread("Resources/shapes.png")
imgContour = img.copy()
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),1)
imgCanny = cv2.Canny(imgBlur,50,50)
imageblank = np.zeros_like(img)
getcontour(imgCanny)
imgstack = SI.StackImage(0.8,([img,imgGray,imgBlur],[imgCanny,imgContour,imageblank]))
cv2.imshow("Stacked Image",imgstack)
cv2.waitKey(0)