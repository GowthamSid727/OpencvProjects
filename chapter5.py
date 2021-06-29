import cv2
import numpy as np

img = cv2.imread("Resources/card.jpg")

height=350
width=250
pst1 = np.float32([[292,387],[352,241],[512,468],[568,322]])
pst2 =np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(pst1,pst2)
warpimg = cv2.warpPerspective(img,matrix,(width,height))
cv2.imshow("Output",img)
cv2.imshow("Warp img",warpimg)
cv2.waitKey(0)