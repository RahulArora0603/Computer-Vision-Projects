import cv2
#Input Image Path by User
img_name = input("Enter image path\n")
#Converting '\' into '/':
img_name = list(img_name)
for i in img_name:
    if i=="\\":
       r = img_name.index(i)
       img_name[r] = "/"
myimg = ''.join(img_name)
#Read Image
img = cv2.imread(myimg)
coordy = int(input("Enter height in pixels.\n")) #Enter height
coordx = int(input("Enter width in pixels.\n"))  #Enter weight
new_name = input("Enter name to be saved as : ") 
#Resize image
new_img = cv2.resize(img,(coordx,coordy))
cv2.imshow("Window",new_img) #Displaying the image
cv2.imwrite(new_name , new_img) #Saving image
cv2.waitKey(0) #Keep showing until key press
cv2.destroyAllWindows()