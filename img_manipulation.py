import cv2
import random
import numpy as np


img =  cv2.imread('IMG_7880[1].jpg', -1)
#CHANGE COLOR OF IMAGE
for i in range(100):
    for j in range(img.shape[1]):
        img[i][j] = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]     
#COPY ONE PART OF IMAGE AND PASTE TO ANOTHER PART
'''tag = img[50:70 , 60:90]
img[10:30 , 65:95] = tag'''


#height, width = 780, 920
#b, g, r = 0x3E, 0x88, 0xE5  # orange
#image = np.zeros((height, width, 3), np.uint8)
#image[:,:,0]= b
#image[:,:,1]= g
#image[:,:,2]= r
#img[100:110, 100:110,:]= [100,165,0]


cv2.imshow("A New Image", img)
cv2.waitKey(0)
#cv2.imshow('Image', img)
#cv2.waitKey(0)
cv2.destroyAllWindows() 

