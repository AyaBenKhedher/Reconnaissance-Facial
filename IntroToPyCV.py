import cv2 as cv
import numpy as np
import sys

face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')


cap = cv.VideoCapture(0)

while True:
     _,img = cap.read()

     gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    
     faces = face_cascade.detectMultiScale(gray, 1.1,4)
    
     for(x, y, w, h) in faces:
         cv.rectangle(img, (x,y),(x+w, y+h),(255,0,0), 2)
         cv.putText(img,str("Face Detected"),(400,70),cv.FONT_HERSHEY_PLAIN,2,(0,255,0),2)
        
     cv.imshow('img', img)
     
     k = cv.waitKey(30) & 0xff
     if k==27:    
        break
        
cap.release()
cv.destroyAllWindows()
     


        
    
