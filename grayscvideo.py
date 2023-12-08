import cv2

cap = cv2.VideoCapture(0)


mog = cv2.createBackgroundSubtractorMOG2()

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
  
    fgmask = mog.apply(gray)
    
    
    cv2.imshow('Foreground Mask', fgmask)
    if cv2.waitKey(1) == ord('q'):
        break
        
cap.release()
cv2.destroyAllWindows()