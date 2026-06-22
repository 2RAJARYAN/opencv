import cv2
import numpy as np

cap=cv2.VideoCapture("video/highway.mp4")
# _,first_frame=cap.read()
# first_gray=cv2.cvtColor(first_frame,cv2.COLOR_BGR2GRAY)
# first_gray=cv2.GaussianBlur(first_gray,(5,5),0)


subtracter=cv2.createBackgroundSubtractorMOG2(history=20,varThreshold=50,detectShadows=True) #history(number of frame), varthreshold(threshold), detectShadow(enable shadow detection)
#create background subtraction modle using mog2(mixture of gaussians)
while True:
    ret,frame=cap.read()
    # gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    # gray_frame=cv2.GaussianBlur(gray_frame,(5,5),0)
    # difference=cv2.absdiff(first_gray,gray_frame)  # compute the absolute difference between two images pixel by pixel
    # _,difference=cv2.threshold(difference,80,255,cv2.THRESH_BINARY)
    
    # cv2.imshow("frame",frame)
    # cv2.imshow("first frame",first_frame)
    # cv2.imshow("difference",difference)

    #### MOG2 ####
    if ret is False:
        cap=cv2.VideoCapture("video/highway.mp4")
        continue
    mask=subtracter.apply(frame)


    cv2.imshow("frame",frame)
    cv2.imshow("mask",mask)

    key=cv2.waitKey(20)
    if key==27:
        break

cap.release()
cv2.destroyAllWindows()
