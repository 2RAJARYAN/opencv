import cv2 
import numpy as np
import matplotlib.pylab as plt 

img=cv2.imread("image/red_panda.jpg")
rows,cols,ch=img.shape

print("heights: ",rows)
print("width: ",cols)


scaled_img=cv2.resize(img,None,fx=2,fy=1)

matrix_t=np.float32([[1,0,50],
                   [0,1,50]])
translated_img=cv2.warpAffine(img,matrix_t,(cols,rows))

matrix_r=cv2.getRotationMatrix2D((cols/2,rows/2),90,0.5)
rotation_img=cv2.warpAffine(img,matrix_r,(cols,rows))

cv2.imshow("original image",img)
cv2.imshow("scaled image",scaled_img)
cv2.imshow("traslated image",translated_img)
cv2.imshow("rotation img",rotation_img)
cv2.waitKey(0)
cv2.destroyAllWindows()