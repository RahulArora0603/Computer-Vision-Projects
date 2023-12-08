import cv2

img = cv2.imread('Mark-Zuckerberg.jpg')
resize_image = cv2.resize(img,(300,300))

cv2.imshow("Window", resize_image)
cv2.waitKey('q')