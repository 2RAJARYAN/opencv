import cv2 
import numpy as np

#line detection is use in robotics,shpae recogination.object boundaries etc.
#coner detection is for object motion tracking ,3d modeling, object recogination.

# img=cv2.imread("image\squares.jpg")
# gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


# corners=cv2.goodFeaturesToTrack(gray,50,0.1,10) #img, maxCorners(maximum no of corners to return), qualityLevel(minimum quality of corner (0-1, 0.1 means corners must have at least 10% of the best corner's quality.)), minDistance(minimum distance between detected corners.(prevent corners from clusturing too close together)).
# # other parameter are mask, blocksize, useharrisdetector,k(harris detector)
# corners=np.int32(corners)
# # print(corners)

# for corner in corners:
#     x,y=corner.ravel() #flatten the array from multi to one dimensional.
#     cv2.circle(img,(x,y),3,(0,0,255),-1)

# cv2.imshow("img",img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

def nothing(): #callback function when trackbar value changes.
    pass

cap=cv2.VideoCapture(0)
cv2.namedWindow("frame")
cv2.createTrackbar("quality","frame",1,100,nothing)
while True:
    _,frame=cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    quality=cv2.getTrackbarPos("quality","frame")
    quality=quality/100 if quality>0 else 0.01
    corners=cv2.goodFeaturesToTrack(gray,80,quality,10)
    if corners is not None:
        corners=np.int32(corners)

        for corner in corners:
            x,y=corner.ravel() 
            cv2.circle(frame,(x,y),3,(0,0,255),-1)

    cv2.imshow("frame",frame)

    key=cv2.waitKey(1)
    if key==27:
        break

cap.release()
cv2.destroyAllWindows()
