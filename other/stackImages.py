import cv2
import numpy as np
def StackImage(scale,imgArr):
    rows = len(imgArr)
    cols = len(imgArr[0])
    rowsAvail = isinstance(imgArr[0],list)
    width = imgArr[0][0].shape[1]
    height = imgArr[0][0].shape[0]
    if rowsAvail:
        for x in range(0,rows):
            for y in range(0,cols):
                if imgArr[x][y].shape[:2] == imgArr[0][0].shape[:2]:
                    imgArr[x][y] = cv2.resize(imgArr[x][y],(0,0),None,scale,scale)
                else:
                    imgArr[x][y] = cv2.resize(imgArr[x][y], (imgArr[0][0].shape[1],imgArr[0][0].shape[0]), None, scale, scale)
                if len(imgArr[x][y].shape) == 2:
                    imgArr[x][y] = cv2.cvtColor(imgArr[x][y],cv2.COLOR_GRAY2BGR)
        imgblank = np.zeros((height,width),np.uint8)
        hor = [imgblank]*rows
        hor_con = [imgblank]*rows
        for x in range(0,rows):
            hor[x]=np.hstack(imgArr[x])
        ver = np.vstack(hor)
    else:
        for x in range(0,rows):
            if imgArr[x].shape[:2] == imgArr[0].shape[:2]:
                imgArr[x] = cv2.resize(imgArr[x],(0,0),None,scale,scale)
            else:
                imgArr[x] = cv2.resize(imgArr[x], (imgArr[0].shape[1], imgArr[0].shape[0]), None, scale, scale)
            if len(imgArr[0].shape)==2:
                imgArr[x]=cv2.cvtColor(imgArr[x],cv2.COLOR_GRAY2BGR)
        hor = np.hstack(imgArr)
        ver=hor
    return ver