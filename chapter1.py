import cv2
print("Package imported")
#image reading.....
#img = cv2.imread("Resources/d.jpg")
#cv2.imshow("Output",img)
#cv2.waitKey(1000)

#video reading....
#vid = cv2.VideoCapture("Resources/test.mp4")
#print("file readed")
#while True:
#    success, img = vid.read()
#    cv2.imshow("Output",img)
#    if cv2.waitKey(1) & 0xFF == ord('q'):
#        break

#Webcam reading...
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
#cap.set(10, 100)
while True:
    success, img = cap.read()
    cv2.imshow("Output",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
