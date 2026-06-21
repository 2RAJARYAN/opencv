import cv2 
import numpy as np 

img1=cv2.imread("image/baseball_ball.png")
img1=cv2.resize(img1,(1000,1000))
img2=cv2.imread("image/football_ball.jpg")
img2=cv2.resize(img2,(1000,1000))

footbase_ball=np.hstack((img1[:,:500],img2[:,500:]))

### Gaussian pyramid ####
layer=img1.copy()
gaussian_pyramid_1=[layer]
for i in range(6):
    layer=cv2.pyrDown(layer)
    # cv2.imshow(str(i),layer)
    gaussian_pyramid_1.append(layer)

##### Laplacian pyramid
layer=gaussian_pyramid_1[5]
cv2.imshow("6",layer)
laplacian_pyramid_1=[layer]
for i in range(5,0,-1):
    size=(gaussian_pyramid_1[i-1].shape[1],gaussian_pyramid_1[i-1].shape[0])
    gaussian_expanded_1=cv2.pyrUp(gaussian_pyramid_1[i],dstsize=size)
    laplacian_1=cv2.subtract(gaussian_pyramid_1[i-1],gaussian_expanded_1)   
    laplacian_pyramid_1.append(laplacian_1)

### Gaussian pyramid ####
layer=img2.copy()
gaussian_pyramid_2=[layer]
for i in range(6):
    layer=cv2.pyrDown(layer)
    # cv2.imshow(str(i),layer)
    gaussian_pyramid_2.append(layer)

##### Laplacian pyramid
layer=gaussian_pyramid_2[5]
cv2.imshow("6",layer)
laplacian_pyramid_2=[layer]
for i in range(5,0,-1):
    size=(gaussian_pyramid_2[i-1].shape[1],gaussian_pyramid_2[i-1].shape[0])
    gaussian_expanded_2=cv2.pyrUp(gaussian_pyramid_2[i],dstsize=size)
    laplacian_2=cv2.subtract(gaussian_pyramid_2[i-1],gaussian_expanded_2)   
    laplacian_pyramid_2.append(laplacian_2)

## laplacian pyramid of foot baseball ##
footbase_ball_pyramid=[]
n=0
for img1_lap,img2_lap in zip(laplacian_pyramid_1,laplacian_pyramid_2):
    n+=1
    col,row,ch=img1_lap.shape

    laplacian=np.hstack((img1_lap[:,:int(col/2)],img2_lap[:,int(col/2):]))
    cv2.imshow(str(n),laplacian)
    footbase_ball_pyramid.append(laplacian)

## reconstruct the pyramid
footbase_ball_reconstruct=footbase_ball_pyramid[0]
for i in range(1,6):
    size=(footbase_ball_pyramid[i].shape[1],footbase_ball_pyramid[i].shape[0])
    footbase_ball_reconstruct=cv2.pyrUp(footbase_ball_reconstruct,dstsize=size)  ##pyrUp/down-->except the size argument in form of (width,height)
    footbase_ball_reconstruct=cv2.add(footbase_ball_pyramid[i],footbase_ball_reconstruct)
'''
#### This process reconstructs the original image because:
*Gaussian pyramid = smooth versions.
*Laplacian pyramid = details lost at each step.
*Adding them back in reverse order restores the original.



# Gaussian pyramids create progressively smaller, blurred versions of an image, 
  while Laplacian pyramids capture the details lost at each step of downsampling.

'''



cv2.imshow("football reconstructed",footbase_ball_reconstruct)

cv2.imshow("img1",img1)
cv2.imshow("img2",img2)
# cv2.imshow("footbase_ball",footbase_ball)
cv2.waitKey(0)
cv2.destroyAllWindows()


