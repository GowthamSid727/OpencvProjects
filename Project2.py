import cv2
import numpy as np
######################
width = 640
height = 480
#######################
#cap = cv2.VideoCapture('https://192.168.0.100:8080/video')
#cap.set(3,width)
#cap.set(4,height)


def preproceesing(img):
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imgblur = cv2.GaussianBlur(imgGray,(7,7),1)
    imgCanny = cv2.Canny(imgblur,300,300)
    kernel = np.ones((5,5),np.uint8)
    imgDilation = cv2.dilate(imgCanny,kernel,iterations=1)
    return imgDilation
def getContours(img):
    biggest =  np.array([])
    maxarea = 0
    contour, Hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contour:
        area = cv2.contourArea(cnt)
        if area>500:
            peri = cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt,0.2*peri,True)
            if area>maxarea and len(approx)==4:
                biggest = aprrox
                print(biggest)
                maxarea = area
        cv2.drawContours(imgcon, cnt, -1, (255, 0, 0), 10)
    return biggest
def reorder(myPoints):
    myPoints = myPoints.reshape((4,2))
    myPointsNew = np.zeros((4,1,2),np.uint32)
    add = myPoints.sum(1)
    myPointsNew[0] = myPoints[np.argmin(add)]
    myPointsNew[3] = myPoints[np.argmax(add)]
    diff = np.diff(myPoints,axis=1)
    myPointsNew[1] = myPoints[np.argmin(diff)]
    myPointsNew[2] = myPoints[np.argmax(diff)]
    return myPointsNew
def getwarp(img,biggest):
    biggest = reorder(biggest)
    pst1 = np.float32(biggest)
    pst2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
    matrix = cv2.getPerspectiveTransform(pst1, pst2)
    warpimg = cv2.warpPerspective(img, matrix, (width, height))
    return warpimg
img = cv2.imread("Resources/p.jpg")
img = cv2.resize(img,(width,height))
imgcon = img.copy()
imgpre = preproceesing(img)
biggest = getContours(imgpre)
print(biggest)
#imgwarp = getwarp(imgcon,biggest)
cv2.imshow("Ouput",imgcon)
cv2.waitKey(0)
#while True:
#    success, img = cap.read()
#    img = cv2.resize(img,(width,height))
#    imgcon = img.copy()
#    imgpre = preproceesing(img)
#    getwarp(imgcon,getContours(imgpre))
#    cv2.imshow("Ouput",imgcon)
#    if cv2.waitKey(1) & 0xFF == ord('q'):
#    break