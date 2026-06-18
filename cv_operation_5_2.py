import cv2
import numpy as np

image=cv2.imread("image/red_panda.jpg")
print(image.shape) #heigth, width, channel
he,wi,ch=image.shape

roi=image[200:he,0:wi]



cv2.imshow("panda",image)
cv2.imshow("roi",roi)
cv2.waitKey(0)
cv2.destroyAllWindows()