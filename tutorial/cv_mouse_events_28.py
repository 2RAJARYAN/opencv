import cv2
import numpy as np

point1=()
point2=()
drawing=False

def mouse_drawing(event,x,y,flags,params):
    global point1, point2,drawing
    # print(event)
    # if event ==cv2.EVENT_LBUTTONDOWN:
    #     print("left click")
    #     print(x,y)
    # elif event==cv2.EVENT_LBUTTONDBLCLK:
    #     print("double click")
    #     print(x,y)
    # if event==cv2.EVENT_LBUTTONDOWN:
    #     print("left click")
    #     # cv2.circle(frame,(x,y),50,(0,0,255),-1)
    #     circles.append((x,y))

    if event== cv2.EVENT_LBUTTONDOWN:
        # print("left click")
        if drawing is False:
            drawing=True
            point1=(x,y)
        else:
            drawing=False
    elif event==cv2.EVENT_MOUSEMOVE:
        # print("mouse move",x,y)
        # point2=(x,y)
        if drawing is True:
            point2=(x,y)


cap=cv2.VideoCapture(0)
cv2.namedWindow("frame")
cv2.setMouseCallback("frame",mouse_drawing)

# circles=[]
while True:
    _,frame=cap.read()  
    
    # for center_position in circles:
    #     # print(center_position)
    #     cv2.circle(frame,center_position,5,(0,0,255),-1)

    if point1 and point2:
        cv2.rectangle(frame,point1,point2,(0,255,0))

    cv2.imshow("frame",frame)
    key=cv2.waitKey(1) #this is where all event is detected 
    if key==27:
        break
    # elif key==ord("d"):
    #     circles=[]
    # cv2.imshow("frame",frame)     

cap.release()
cv2.destroyAllWindows() 