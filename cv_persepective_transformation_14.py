import cv2 
import numpy as np

cap=cv2.VideoCapture(0)

while True:
    _,frame=cap.read()
    # print(frame.shape)

    cv2.circle(frame,(130,250),5,(0,24,205),-1)   
    #frame(image to draw),(x,y)(center), 5(radius in pixel), (0,24,255)(color in bgr format),-1(thickness)(negative fill the cirlce)
    cv2.circle(frame,(430,220),5,(0,255,0),-1)
    cv2.circle(frame,(100,400),5,(130,0,255),-1)
    cv2.circle(frame,(530,380),5,(130,35,155),-1)

    pt1=np.float32([[130,250],  #source point(given by user keep same as what you put in above cirlce points)
                   [430,220],
                   [100,400],
                   [530,380]])
    pt2=np.float32([[0,0],    #destination points (where you want those corners mapped in transformed image)
                   [500,0],
                   [0,600],
                   [400,600]])
    #pt1,2 define how the perspective should be wraped
    matrix=cv2.getPerspectiveTransform(pt1,pt2)
    #getperspectivetransform ->compute transformation matrix that maps the quadrilateral defined by pt1 into tectangle defined by pt2. 
    result=cv2.warpPerspective(frame,matrix,(500,600))
    #apply the perspective transformation to the frame.  frame, matrix, size of ouptut image, 

    cv2.imshow("frame",frame)
    cv2.imshow("perspective",result)
    key=cv2.waitKey(1)
    if key==27:
        break

cap.release()
cv2.destroyAllWindows()

