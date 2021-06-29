import cv2
facecascade = cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")
#img = cv2.imread("Resources/friends.jpg")
cap = cv2.VideoCapture(0)
width=640
height=480
cap.set(3,width)
cap.set(4,height)
#imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
while True:
    success, img = cap.read()
    faces = facecascade.detectMultiScale(img, 1.1, 5)
    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    cv2.imshow("Output",img)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
