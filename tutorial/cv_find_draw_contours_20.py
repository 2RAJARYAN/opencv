import cv2 
import numpy as np 

cap=cv2.VideoCapture(0)

while True:
    _,frame=cap.read()
    frame=cv2.GaussianBlur(frame,(5,5),0)
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)  #make color detection easier than bgr.

    lower_blue=np.array([30,86,0])  #to find this value print hsv[x.y] , choose range around that value.
    upper_blue=np.array([121,255,255])
    mask=cv2.inRange(hsv,lower_blue,upper_blue)  #inrange-- create a binary mask :pixels inside range white(255),others--black(0)

    contours,_=cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)  #img,mode(contour retrieval mode, contour approximation method,)
    #OUTPUT-- contours and hierarchy.
    # print(contours)
    for contour in contours:
        area=cv2.contourArea(contour)
    # print(area)
        if area>7000:
            cv2.drawContours(frame,contour,-1,(0,255,0),3)

    # cv2.drawContours(frame,contours,-1,(0,255,0),3)
    cv2.imshow("frame",frame)
    cv2.imshow("mask",mask)


    key=cv2.waitKey(1)
    if key==27:
        break


cap.release()
cv2.destroyAllWindows()