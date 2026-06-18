import cv2
import numpy as np

img1=cv2.imread("image\\road.jpg")
img2=cv2.imread("image\\car.jpg")
img2_gray=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)




cv2.waitKey(0)
cv2.destroyAllWindows()