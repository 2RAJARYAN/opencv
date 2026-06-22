import cv2 
import numpy as np

cap=cv2.VideoCapture(0)

#create old frame
_,frame=cap.read()
old_gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

## lUCAS KANADE PARAMETERS
lk_params=dict(winSize=(15,15),
               maxLevel=2,
               criteria=(cv2.TERM_CRITERIA_EPS|cv2.TERM_CRITERIA_COUNT,10,0.03))
#winSize(size of search window around each point),maxlevel(number of pyramid levels used),criteria(stoping condition)
 
def select_point(event,x,y,flags,params):
    global point,point_selected,old_points
    if event==cv2.EVENT_LBUTTONDOWN:
        point=(x,y)
        point_selected=True
        old_points=np.array([[x,y]],dtype=np.float32)

cv2.namedWindow("frame")
cv2.setMouseCallback("frame",select_point)

point_selected=False
point=()             
old_points=np.array([[]])
while True:
    _,frame=cap.read()
    gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    if point_selected is True:
        cv2.circle(frame,point,5,(0,0,255),2)
        new_points,status,error=cv2.calcOpticalFlowPyrLK(old_gray,gray_frame,old_points,None,**lk_params)
        #old_gray(previous grayscale), gray_frame(current frame), cold_points(points you want to track(select with mouse), mask(none), dictionary of parameeters(lucan kanade))
        old_gray=gray_frame.copy()
        old_points=new_points
        # print(new_points)
        x,y=new_points.ravel() 
        cv2.circle(frame,(int(x),int(y)),5,(0,255,0),-1)

    #here we going to make pyramid
    # first_level=cv2.pyrDown(frame)
    # second_level=cv2.pyrDown(first_level)

    cv2.imshow("frame",frame)
    # cv2.imshow("first level",first_level)
    # cv2.imshow("second level",second_level)
    key=cv2.waitKey(1)
    if key==27:
        break

cap.release()
cv2.destroyAllWindows()

'''
### Lucas–Kanade optical flow ###
*It is a classic algorithm that tracks motion of points 
between frames by assuming displacement is small and nearly constant within a local neighborhood. 

## role of pyramid levels
*Image Pyramid: A set of progressively downsampled versions of the image 
*Lucas–Kanade assumes small motion. If an object moves a lot between frames, the algorithm may fail.
*By starting at a coarse (small) resolution, large displacements appear smaller and easier to track.
'''