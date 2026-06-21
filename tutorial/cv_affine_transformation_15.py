import cv2 
import numpy as np

img=cv2.imread("image/grid.jpg")
cols,rows,ch=img.shape
cv2.circle(img,(83,90),5,(0,0,255),-1)
cv2.circle(img,(447,90),5,(0,0,255),-1)
cv2.circle(img,(83,470),5,(0,0,255),-1)

pts1=np.float32([[83,90],
                 [447,90],
                 [83,470]])
pts2=np.float32([[83,90],
                 [447,90],
                 [173,470]])
matrix=cv2.getAffineTransform(pts1,pts2)
result=cv2.warpAffine(img,matrix,(cols,rows))
'''
An affine transform is a type of geometric transformation in computer vision that preserves points, straight lines, and parallelism. 
It’s more general than simple translation or rotation, because it can also include scaling, shearing, and reflection — 
but it does not preserve angles or lengths (so circles may become ellipses).
'''
cv2.imshow("img",img)
cv2.imshow("result_img",result)
cv2.waitKey(0)
cv2.destroyWindow()

