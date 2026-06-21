import cv2
import numpy as np

image=cv2.imread("image\\red_panda.jpg")
shape=image.shape
print(shape)
blue=(255,0,0)  #bgr
red=(0,0,255)
green=(0,255,0)
violet=(100,0,180)
yellow=(0,180,180)
white=(255,255,255)

cv2.line(image,(50,30),(450,35),blue,thickness=5)
cv2.circle(image,(240,200),23,red,-1)  #-1 to fill the circle.
cv2.rectangle(image,(50,60),(450,95),green,-1)
cv2.ellipse(image,(250,150),(80,20),8,5,360,violet,-1) 
#enter (250,150), axes (80,20), angle = 8°, start = 5°, end = 360°, color = violet, filled_shape.

points=np.array([[[120,230],[400,230],[320,250],[240,200]]],np.int32)
cv2.polylines(image,[points],True,yellow,thickness=3)
font=cv2.FONT_HERSHEY_TRIPLEX
cv2.putText(image,"panda",(20,100),font,4,white)

cv2.imshow("red panda",image)
cv2.waitKey(0)  #wait indefinite for a key press.
cv2.destroyAllWindows()
