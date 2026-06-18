import cv2
import numpy as np

def nothing(x):  #do nothing
# Trackbars require a callback, but if you don’t need one, you define nothing() to do nothing.
    pass


cap=cv2.VideoCapture(0)

cv2.namedWindow("frame")  #create window name frame, add befor trackbar window. give control of properties
cv2.createTrackbar("test","frame",50,500,nothing) #trackbar name, window to attach it to, initial value, maximum value, callback function when slider changes.
cv2.createTrackbar("color/gray","frame",0,1,nothing) #toggle between color and grayscale.


while True:
    _,frame=cap.read()  # read return two value rel(_),frame , rel-> boolean true if a frame read, false otherwise.
    #frame= actual image(numpy array)

    test=cv2.getTrackbarPos("test","frame")  #read current position of trackbar(test).
    font=cv2.FONT_HERSHEY_COMPLEX
    cv2.putText(frame,str(test),(20,100),font,4,(0,0,255))
    #frame, text string, position, font, font scale, color

    n=cv2.getTrackbarPos("color/gray","frame")
    if n==0:
        pass
    else:
        frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    cv2.imshow("frame",frame)

    key=cv2.waitKey(1)
    if key==27:  #press esc
        break

cap.release()  #free the camera resource.
cv2.destroyAllWindows()