import cv2
import numpy as np

def nothing():
    pass

# img=cv2.imread("image/black_to_white.jpeg",cv2.IMREAD_GRAYSCALE)
# print(img.shape)
# print(img[0,0])
# print(img[0,250])
# print(img[0,450])

img=cv2.imread("image/red_panda.jpg",cv2.IMREAD_GRAYSCALE)
cv2.namedWindow("image")
cv2.createTrackbar("threshold value","image",128,255,nothing)

while True:
    value_threshold=cv2.getTrackbarPos("threshold value","image")
    _,threshold_binary=cv2.threshold(img,value_threshold,255,cv2.THRESH_BINARY)  #source image,thresh_value(when <=128 set to 0),max)value(when it >128 set to 255 or color number at given prostion)
    _,threshold_binary_inv=cv2.threshold(img,value_threshold,255,cv2.THRESH_BINARY_INV)  #opposite of thresold_binary
    _,threshold_trunc=cv2.threshold(img,value_threshold,255,cv2.THRESH_TRUNC)   #pixel > threshold = set to threshold value otherwise unchange
    _,threshold_zero=cv2.threshold(img,value_threshold,255,cv2.THRESH_TOZERO)   #pixel >threshold =uncange otherwise set to 0
    _,threshold_zero_INV=cv2.threshold(img,value_threshold,255,cv2.THRESH_TOZERO_INV)

#thresholding is a segmentation thechnique . converts a grayscale image into a binary or modified image based on intensity cutoff.
# usefull for -> separating foreground from background,  detecting object in simple lighting conditions,  preprocessing before contour(outline) detection or OCR.

    cv2.imshow("image",img)
    cv2.imshow("th binary",threshold_binary)
    cv2.imshow("th binary inv",threshold_binary_inv)
    cv2.imshow("th trunc",threshold_trunc)
    cv2.imshow("th zero",threshold_zero)
    cv2.imshow("th zero_inv",threshold_zero_INV)
   
    key=cv2.waitKey(100)
    if key==27:
        break


cv2.destroyAllWindows()