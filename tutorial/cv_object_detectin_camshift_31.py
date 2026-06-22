import cv2 
import numpy as np

img=cv2.imread("image/gray_cover.jpg")
cut_out= img[252:395,354:455]   #if you have not the exact value use x,y,heigth,width.[y:y+height,x:x+width].
x=354
y=252
width=455-x
height=395-y
hsv_cut=cv2.cvtColor(cut_out,cv2.COLOR_BGR2HSV)
cut_hist=cv2.calcHist([hsv_cut],[0],None,[180],[0,180])
cap=cv2.VideoCapture(0)
term_criteria=(cv2.TERM_CRITERIA_EPS|cv2.TERM_CRITERIA_COUNT ,10,1) 
while True:
    _,frame=cap.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    mask=cv2.calcBackProject([hsv],[0],cut_hist,[0,180],1)
    #creates a probability image showing how well each pixel in a target image matches a reference histogram

    ret,track_window=cv2.CamShift(mask,(x,y,width,height),term_criteria)
    # print(ret)
    pts=cv2.boxPoints(ret)
    pts=np.int32(pts)
    cv2.polylines(frame,[pts],True,(255,0,0))

    cv2.imshow("mask",mask)
    cv2.imshow("frame",frame)
    key=cv2.waitKey(1)
    if key==27:
        break


cap.release()
cv2.destroyAllWindows()