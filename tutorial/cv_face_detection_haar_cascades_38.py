import cv2
import sys
import numpy as np

def nothing():
    pass

cap=cv2.VideoCapture(0) 
face_cascade=cv2.CascadeClassifier("video\haarcascade_frontalface_default.xml")  #The XML file contains a pre-trained face detection model
cv2.namedWindow("frame")
# cv2.createTrackbar("scale","frame",11,20,nothing)
cv2.createTrackbar("neighbours","frame",11,20,nothing)

while True:
    _,frame=cap.read() 
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # scale=cv2.getTrackbarPos("scale","frame")
    neighbours=cv2.getTrackbarPos("neighbours","frame")

    faces=face_cascade.detectMultiScale(gray,1.3,neighbours)  #image, scaling factor(This controls image pyramid scaling.), neighbours(Controls false positives.)

    # print(faces)
    for rect in faces:
        (x,y,w,h)=rect
        frame=cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2) #return [[x,y,w,h],[x,y,w,h]]


    cv2.imshow("frame",frame)


    key=cv2.waitKey(1) 
    if key==27:
        break

cap.release()
cv2.destroyAllWindows() 











