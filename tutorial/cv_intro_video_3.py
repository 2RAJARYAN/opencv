import cv2
import sys
import numpy as np

cap=cv2.VideoCapture('video/red_panda_snow.mp4') #first webcam camera
'''
*fourcc stands for Four Character Code. It’s a 4-byte identifier for the video codec used to compress frames.
*Example: "XVID" → Xvid MPEG-4 codec.
*Other common ones: "MJPG", "DIVX", "MP4V".
*It tells OpenCV how to encode the video when writing it to disk.
'''
fourcc=cv2.VideoWriter_fourcc(*"XVID")
out=cv2.VideoWriter("flipped_red_panda.avi",fourcc,25,(640,360))
#writing frames to a video file. videowrite(output_filename,fourcc,25,frame_size)
while True:
    ret,frame=cap.read()  #getting data frame by frame.
    print(frame.shape)
    # gray_scale=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    # cv2.imshow("gray scale",gray_scale)
    frame2=cv2.flip(frame,0) #do (frame,1)
    cv2.imshow("fipping",frame2)
    cv2.imshow("frame",frame)

    out.write(frame2)
    key=cv2.waitKey(30) #1ms   give illusion of video but actually we work frame by frame

    if key==27:
        break
out.release()  #close safely
cap.release()
cv2.destroyAllWindows() 











