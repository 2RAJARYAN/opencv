import cv2 
import numpy as np


# img=cv2.imread("image/simpsons.jpg")
# gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# template=cv2.imread("image/barts_face.jpg",cv2.IMREAD_GRAYSCALE)
# w,h=template.shape[::-1]   #rows as height, and cols as width
# #template matching, you usually need width first, then height (for rectangle drawing).

# result=cv2.matchTemplate(gray_img,template,cv2.TM_CCOEFF_NORMED)  #img,templete image, method(tm_ccoeff-correlation coeficient , tm_sqdiff - squared difference)

# # print(result)
# loc=np.where(result>=0.9)  #condition(all position in result where similarity>=0.9),  returns tuple of array( y,x) indices.
# # print(loc)

# for pt in zip(*loc[::-1]):  #*loc-- unpacking(passes two array separeted into zip) ,zip pair them into coordinate tuple
#     # print(pt)
#     cv2.rectangle(img,pt,(pt[0]+w,pt[1]+h),(0,255,0),3)

# cv2.imshow("img",img)
# cv2.imshow("result",result)
# cv2.waitKey(0)
# cv2.destroyAllWindows()



## may not work ##
## may give error when template size is bigger than source image (error in matchtemplate)
## template should be same as shown on camera.
cap=cv2.VideoCapture(0)
template=cv2.imread("image/pen.png",cv2.IMREAD_GRAYSCALE)
w,h=template.shape[::-1]

while True:
    _,frame=cap.read()
    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    result=cv2.matchTemplate(frame,template,cv2.TM_CCOEFF_NORMED)
    loc=np.where(result>=0.9)

    for pt in zip(*loc[::-1]):
        cv2.rectangle(frame,pt,(pt[0]+w,pt[1]+h),(0,255,0),3)

    cv2.imshow("frame",frame)
    key=cv2.waitKey(1)
    if key==27:
        break

cap.release()
cv2.destroyAllWindows()