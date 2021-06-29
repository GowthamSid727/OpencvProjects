import cv2

img = cv2.imread("Resources/Mazda.jpg")
print(img.shape)
imgresize = cv2.resize(img,(500,400))
print(imgresize.shape)
imgcrop = img[0:250,0:500]
cv2.imshow("original img",img)
cv2.imshow("Resized image",imgresize)
cv2.imshow("Croped image",imgcrop)
cv2.waitKey(0)
