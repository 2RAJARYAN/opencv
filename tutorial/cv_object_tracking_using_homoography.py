import cv2
import numpy as np

img=cv2.imread("image/ultimo_book.png",cv2.IMREAD_GRAYSCALE)
cap=cv2.VideoCapture("video/ultimo_book.mp4")

## feature 
sift=cv2.xfeatures2d.SIFT_create()
kp_img,desc_image=sift.detectAndCompute(img,None)  #desc-->A keypoint tells us where an interesting feature is located.A descriptor is a vector of 128 numbers
# img=cv2.drawKeypoints(img,kp_img,img)   #query image

## feature matching
index_params=dict(algorithm=0,trees=5)  #algo=0 mean FLANN_INDEX_KDTREE , trees mean number of kd tree.
search_params=dict()  #default , but sometimes checks=50
flann=cv2.FlannBasedMatcher(index_params,search_params)  
'''
*flann--Fast Library for Approximate Nearest Neighbors
*FLANN builds a search tree so nearest descriptors can be found quickly.
*

'''

while True:
    _,frame=cap.read()
    gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    kp_grayframe,desc_grayframe=sift.detectAndCompute(gray_frame,None)
    # gray_frame=cv2.drawKeypoints(gray_frame,kp_grayframe,gray_frame)
    matches=flann.knnMatch(desc_image,desc_grayframe,k=2)  #for every descriptor in desc_img find k=2 nearst descriptor in desc_grayframe.
    #KD- k dimension tree(binary tree). 
    #flann is designed for speed with high dimesional data.
    #KD‑Tree provides an efficient way to approximate nearest neighbors . bulid mutiple kd tree -> during search travels the tree, returns nearest matches much faster.

    good_points=[]
    for m,n in matches:  #m-best matches ,n-second best matches
        # print(m,n)
        if m.distance<0.6*n.distance:   #distance-- euclidean distance
            good_points.append(m)


    # img3=cv2.drawMatches(img,kp_img,gray_frame,kp_grayframe,good_points,gray_frame)

    #### Homography
    '''
    ## why need homography 
    *suppose book is place in front of camera now camera or book moves ,tilt to detect that we need homography.
    *we need mathmatical transformation describing-
        *translation, rotation, scaling, perspecitve distortion
    '''

    if len(good_points)>10:
        query_pts=np.float32([kp_img[m.queryIdx].pt for m in good_points]).reshape(-1,1,2)  #ponts for reference image  ,m.queryIdx-Index of feature in reference image.
        # print(query_pts)  
        train_pts=np.float32([kp_grayframe[m.trainIdx].pt for m in good_points]).reshape(-1,1,2)   #pointst for video 

        matrix,mask=cv2.findHomography(query_pts,train_pts,cv2.RANSAC,5.0)  #RANSAC automatically removes outliers. without it homography become wrong.
        # 5.0-- is maximum reporjection error.
        matches_mask=mask.ravel().tolist()

        #perspective transformation
        h,w=img.shape  #define book size.
        pts=np.float32([[0,0],
                        [0,h],
                        [w,h],
                        [w,0]]).reshape(-1,1,2)  #define corner
        dst=cv2.perspectiveTransform(pts,matrix) #apply homography to corner.

        homography=cv2.polylines(frame,[np.int32(dst)],True,(255,0,0),3)  #draw the polygon.
        
        cv2.imshow("hoomography",homography)
    else:
        cv2.imshow("homograhy",gray_frame)

    # cv2.imshow("img",img)
    # cv2.imshow("img3",img3)
    # cv2.imshow("gray frame",gray_frame)

    key=cv2.waitKey(1)
    if key==27:
        break

cap.release()
cv2.destroyAllWindows()