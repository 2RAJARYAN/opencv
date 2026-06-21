import cv2 
import numpy as np

# img=cv2.imread("image/lines.png")
# gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #convert gray because need to relies on edges for detection line so we use canny(and canny use single channel grayscales.)
# edges=cv2.Canny(gray,75,150)  

# lines=cv2.HoughLinesP(edges,1,np.pi/180,30,maxLineGap=90)
# #Parameter of HoughLinesP--> image,rho(resolution of rdistance in pixels), theta(resolution of angel in radians), threshold(minimun number of votes to detect a line.),...
# # ... , minLineLength(minimum length of line to accept), maxLineGap(maximum gap betweeen line segments to treate them as a single line.)
# # HoughLines--> return infinite lines it require more cpu, where as HoughLinesP--> return some points based on probabilistic , easlier to compute(more efficient)
# # print(lines)
# for line in lines:
#     x1,y1,x2,y2=line[0]
#     cv2.line(img,(x1,y1),(x2,y2),(0,255,0),3)


# cv2.imshow("img",img)
# cv2.imshow("edges",edges)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

'''
*Hough Line Transform-- it is technique to detect geometric shapes(lines,circle) in an image.
*it works by transforming points in the image space into a parameter space (ρ, θ for lines).


'''

video=cv2.VideoCapture("video/road.mp4")

while True:
    ret,ori_frame=video.read() #ret tell ture or false . if video is running->true
    if not ret:
        video=cv2.VideoCapture("video/road.mp4")
        continue
    
    frame=cv2.GaussianBlur(ori_frame,(5,5),0)
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    low_yellow=np.array([10,94,140])
    up_yellow=np.array([48,255,255])
    mask=cv2.inRange(hsv,low_yellow,up_yellow)
    edges=cv2.Canny(mask,75,150)
    lines=cv2.HoughLinesP(edges,1,np.pi/180,50,maxLineGap=50)
    if lines is not None:
        for line in lines:
            x1,y1,x2,y2=line[0]
            cv2.line(frame,(x1,y1),(x2,y2),(0,255,0),5)
    
    cv2.imshow("frame",frame)
    cv2.imshow("edges",edges)

    key=cv2.waitKey(30)
    if key==27:
        break

video.release()
cv2.destroyAllWindows()

