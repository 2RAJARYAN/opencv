import cv2
import numpy as np

video=cv2.VideoCapture("video/mouth_cleaning.mp4")
_,first_frame=video.read()
x=450
y=360
width=120
height=115
cut_out=first_frame[y:y+height,x:x+width]
# cv2.imshow("first",cut_out)
hsv_cut=cv2.cvtColor(cut_out,cv2.COLOR_BGR2GRAY)
cut_hist=cv2.calcHist([hsv_cut],[0],None,[180],[0,180])
# print(sorted(cut_hist[0])) #here some of the value is more than 255 so 
cut_hist=cv2.normalize(cut_hist,cut_hist,0,255,cv2.NORM_MINMAX)

term_criteria=(cv2.TERM_CRITERIA_EPS|cv2.TERM_CRITERIA_COUNT ,10,1)  #type (combination of flag(term_criteria_eps etc)), maxcount, epsilon(minimum required acccuracy)
#Defines when the iterative algorithm (MeanShift here) should stop
##now use real camera
cap=cv2.VideoCapture(0)

while True:
    # _,frame=video.read()
    _,frame=cap.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    mask=cv2.calcBackProject([hsv],[0],cut_hist,[0,180],1)

    _,track_window=cv2.meanShift(mask,(x,y,width,height),term_criteria)  #mask, initial window (cut out) , stopping condition(term_criteria)
    # print(track_window)
    x,y,w,h=track_window
    cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.imshow("first frame",first_frame)
    cv2.imshow("cut_out frame",cut_out)

    cv2.imshow("mask",mask)
    cv2.imshow("frame",frame)
    # cv2.imshow("frame",first_frame)

    key=cv2.waitKey(60)
    if key==27:
        break


video.release()
cv2.destroyAllWindows()