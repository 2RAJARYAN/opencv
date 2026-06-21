import cv2
import numpy as np

def nothing():
    pass


cap=cv2.VideoCapture(0)
cv2.namedWindow("trackbars")
cv2.createTrackbar("L-H","trackbars",0,179,nothing)  ## l=lower / h =higher(upper) saturation
cv2.createTrackbar("L-S","trackbars",0,255,nothing)
cv2.createTrackbar("L-V","trackbars",0,255,nothing)
cv2.createTrackbar("H-H","trackbars",179,179,nothing)
cv2.createTrackbar("H-S","trackbars",255,255,nothing)
cv2.createTrackbar("H-V","trackbars",255,255,nothing)


while True:
    _,frame=cap.read()

    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    #hsv= Hue, Saturation, and Value.
    # Hue (0–179) → the actual color (red, green, blue, etc.).
    # Saturation (0–255) → intensity of the color (0 = gray, 255 = pure color).
    # Value (0–255) → brightness (0 = black, 255 = full brightness).
    # In BGR, separating colors is tricky because brightness affects all three channels.
    # In HSV, you can isolate colors more easily by focusing on Hue, while Saturation and Value let you control intensity and brightness.


    l_h=cv2.getTrackbarPos("L-H","trackbars")
    l_s=cv2.getTrackbarPos("L-S","trackbars")
    l_v=cv2.getTrackbarPos("L-V","trackbars")
    h_h=cv2.getTrackbarPos("H-H","trackbars")
    h_s=cv2.getTrackbarPos("H-S","trackbars")
    h_v=cv2.getTrackbarPos("H-V","trackbars")

    lower_blue=np.array([l_h,l_s,l_v])  #lower bound
    upper_blue=np.array([h_h,h_s,h_v])  #upper bound
    mask=cv2.inRange(hsv,lower_blue,upper_blue)  #create binary mask - pixels within the hsv range(white) and outside black(0)
    result=cv2.bitwise_and(frame,frame,mask=mask)  #apply mask to original frame keeping only the detected object

    cv2.imshow("frame",frame)
    cv2.imshow("mask",mask)
    cv2.imshow("result",result)

    key=cv2.waitKey(1)
    if key==27:
        break

cap.release()
cv2.destroyAllWindows()   