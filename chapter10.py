import cv2
import numpy as np

circles = np.zeros((4,2),np.int)

counter=0
def findpointer(event,x,y,flags,param):
    global counter
    if event == cv2.EVENT_LBUTTONDOWN:
        circles[counter]=x,y
        counter=counter+1
        #print(x,y)

img = cv2.imread("Resources/card.jpg")
while True:
    if counter==4:
        height=350
        width=250
        pst1 = np.float32([circles[0],circles[1],circles[2],circles[3]])
        pst2 =np.float32([[0,0],[width,0],[0,height],[width,height]])
        matrix = cv2.getPerspectiveTransform(pst1,pst2)
        warpimg = cv2.warpPerspective(img,matrix,(width,height))
        cv2.imshow("Output Warp",warpimg)
    for i in range(0,4):
        cv2.circle(img,circles[i],2,(0,0,255),cv2.FILLED)
    cv2.imshow("Output",img)
    cv2.setMouseCallback("Output",findpointer)
    cv2.waitKey(1)