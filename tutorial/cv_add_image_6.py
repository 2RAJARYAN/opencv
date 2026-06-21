import cv2
import numpy as np

img1=cv2.imread("image\\road.jpg")
img2=cv2.imread("image\\car.jpg")
img2_gray=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)


print(img1[0,0])  #rows and columns
print(img2[0,0])

weighted=cv2.addWeighted(img1,1,img2,0.5,0)  #img1,weight_img1,img2,weight_img2,scalar added to the result(like brightness adjustment(or like bias))
ret,mask=cv2.threshold(img2_gray,240,255,cv2.THRESH_BINARY_INV)
'''
Parameters:
*img2_gray → Source image (must be single‑channel, usually grayscale).
*240 → Threshold value. (any ther value than 240)
    *Any pixel intensity greater than 240 will be set to 0 (because of THRESH_BINARY_INV).
    *Any pixel intensity less than or equal to 240 will be set to 255.
*255 → Maximum value to assign when condition is met.
*cv2.THRESH_BINARY_INV → Inverse binary thresholding type.
*Normal THRESH_BINARY: pixels above threshold → max value, below → 0.
*Inverse THRESH_BINARY_INV: pixels above threshold → 0, below → max value.

**Return values:
*ret → The threshold value used (here, 240).
*mask → The resulting binary image (black and white
'''


sum=cv2.add(img2,img2,mask=mask)
# sum=cv2.add(img1,img2)

cv2.imshow("sum",sum)
cv2.imshow("threshold",mask)
cv2.imshow("weighted",weighted)
cv2.imshow("img_2 gray",img2_gray)
cv2.imshow("road",img1)
cv2.imshow("car",img2)
cv2.waitKey(0)
cv2.destroyAllWindows()