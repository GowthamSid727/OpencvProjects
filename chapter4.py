import cv2
import numpy as np
img = np.zeros((512,512,3),np.uint8)
#img[:] = 0,255,0
#line
cv2.line(img,(0,0),(img.shape[0],img.shape[1]),(0,255,0),3)
#rectangle
#cv2.rectangle(img,(0,400),(200,100),(255,0,0),cv2.FILLED)
#circle
cv2.circle(img,(50,450),(30),(0,255,0),3)
#text
cv2.putText(img,"Hello world",(200,100),cv2.FONT_ITALIC,1,(0,255,0),3)

cv2.imshow("output",img)
cv2.waitKey(0)