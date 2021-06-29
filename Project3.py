import cv2
##################################
ncascade = cv2.CascadeClassifier("Resources/haarcascade_licence_plate_rus_16stages.xml")
#img = cv2.imread("Resources/friends.jpg")
minarea = 0
count = 1
#####################################
cap = cv2.VideoCapture(0)
width=640
height=480
cap.set(3,width)
cap.set(4,height)

#imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
while True:
    success, img = cap.read()
    plates = ncascade.detectMultiScale(img, 1.1, 5)
    for(x,y,w,h) in plates:
        area = w*h
        if area>minarea:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            cv2.putText(img,"Number Plate",(x,y),cv2.FONT_HERSHEY_COMPLEX_SMALL,0.6,(255,0,255),1)
            imgroi = img[y:y+h,x:x+w]
            cv2.imshow("ROI",imgroi)
    cv2.imshow("Result",img)
    if cv2.waitKey(1) & 0xFF==ord('s'):
        cv2.imwrite("Resources/Saved_sample/"+str(count)+".jpg",imgroi)
        cv2.rectangle(img,(0,240),(640,300),(0.255,0),cv2.FILLED)
        cv2.putText(img,"SCAN SAVED",(150,265),cv2.FONT_HERSHEY_COMPLEX_SMALL,2,(0,0,255),1)
        cv2.imshow("Result",img)
        cv2.waitKey(500)
        count+=1