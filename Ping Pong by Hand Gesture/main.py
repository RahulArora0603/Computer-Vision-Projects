import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(3, 1280) #Here, 3 is propId(width), 1280 is the width
cap.set(4, 720) # height

#Importing all images
imgbackground = cv2.imread("Untitled design (1).png")
imgGameOver = cv2.imread("gameOver.png")
imgBall = cv2.imread("ball.png", cv2.IMREAD_UNCHANGED)
imgBat1 = cv2.imread("Bat1(1).png", cv2.IMREAD_UNCHANGED)
imgBat2 = cv2.imread("Bat2(1).png", cv2.IMREAD_UNCHANGED)

#HandDetector
detector = HandDetector(detectionCon=0.8, maxHands=2)

#Declaring variables
ballPos = [100,100]
speedX = 5
speedY = 5
gameOver = False
score = [0,0]

while True:
    _, img =  cap.read()
    imgRaw = img.copy()
    img = cv2.flip(img, 1)
    
    #Find hands
    hands, img = detector.findHands(img, flipType=False)

    # Overlaying background image
    img = cv2.addWeighted(img, 0.2, imgbackground,0.8, 0)
    
    if hands:
        for hand in hands:
            x,y,w,h = hand['bbox']
            h1, w1, _ = imgBat1.shape
            y1 = y - h1//2
            y1 = np.clip(y1, 20 , 415)

            if hand['type']=="Left":
                img = cvzone.overlayPNG(img, imgBat1, (59,y1))
                if 59 <ballPos[0]<59+w1 and y1< ballPos[1] <y1+h1:
                    speedX = -speedX
                    ballPos[0]+=15
                    score[0]+=1

            if hand['type']=="Right":
                img = cvzone.overlayPNG(img, imgBat2, (1195,y1))
                if 1195-50 <ballPos[0]<1195-30 and y1< ballPos[1] <y1+h1:
                    speedX = -speedX
                    ballPos[0]-=15
                    score[1]+=1
    #GameOver
    if ballPos[0]<40 or ballPos[0]>1200:
        gameOver = True 

    if gameOver:
        img = imgGameOver
        cv2.putText(img, str(score[1] + score[0]).zfill(2), (585,280), cv2.FONT_HERSHEY_COMPLEX, 2.5, (200,0,200), 5)                   
    else:
        #Moving the ball
        if ballPos[1]>= 500 or ballPos[1]<=10:
            speedY = -speedY
    
        ballPos[0] += speedX
        ballPos[1] += speedY
    
        #Drawing the ball
        img = cvzone.overlayPNG(img, imgBall, ballPos)

        cv2.putText(img, str(score[0]), (300,650), cv2.FONT_HERSHEY_COMPLEX, 3, (255,255,255), 5)                   
        cv2.putText(img, str(score[1]), (900,650), cv2.FONT_HERSHEY_COMPLEX, 3, (255,255,255), 5)                   

    img[580:700, 20:233] = cv2.resize(imgRaw, (213,120))    
    cv2.imshow('image', img)
    key = cv2.waitKey(1)
    if key==ord('r'):
        ballPos=[100,100]
        speedX=15
        speedy=15
        gameOver = False
        score = [0,0]
        imgGameOver = cv2.imread("gameOver.png")
    
    if key==ord('s'):
        break

cap.release()
cv2.destroyAllWindows()
