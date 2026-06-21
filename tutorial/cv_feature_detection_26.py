#install opencv-contrib-python
import cv2 
import numpy as np

img=cv2.imread("image/book.jpeg",cv2.IMREAD_GRAYSCALE)  #use your own image.

sift=cv2.xfeatures2d.SIFT_create()
# surf=cv2.xfeatures2d.SURF_create()
orb=cv2.ORB_create(nfeatures=15000)
# # kp=sift.detect(img,None)  #kp is key points
# keypoints,descriptors=sift.detectAndCompute(img,None)
# img=cv2.drawKeypoints(img,keypoints,None)

# keypoints,descriptors=surf.detectAndCompute(img,None)   ###surf is non free algo . gives error####
# img=cv2.drawKeypoints(img,keypoints,None)

keypoints,descriptors=orb.detectAndCompute(img,None)   ###surf is non free algo . gives error####
img=cv2.drawKeypoints(img,keypoints,None)

cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''
Feature detection in computer vision is the process of finding distinctive points, edges, corners, or regions in an image that can be
reliably identified and used for tasks like object recognition, tracking, and image matching
'''