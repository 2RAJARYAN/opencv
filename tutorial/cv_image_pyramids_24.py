import cv2 
import numpy as np 

img=cv2.imread("image/hand.jpg")

# first_layer=cv2.pyrDown(img)
# second_layer=cv2.pyrDown(first_layer)


#### Gaussian pyramid ####
# A Gaussian pyramid is created by repeatedly applying cv2.pyrDown, which: Blurs the image slightly.

layer=img.copy()
gaussian_pyramid=[layer]
for i in range(6):
    layer=cv2.pyrDown(layer)
    # cv2.imshow(str(i),layer)
    gaussian_pyramid.append(layer)

# cv2.imshow("0",gaussian_pyramid[0])
# cv2.imshow("4",gaussian_pyramid[4])
# cv2.imshow("img",img)
# # cv2.imshow("first_layer",first_layer)
# # cv2.imshow("second_layer",second_layer)
# cv2.waitKey(0)
# cv2.destroyAllWindows()



##### Laplacian pyramid
#A Laplacian pyramid stores the difference between consecutive Gaussian levels.


# first_layer=cv2.pyrDown(img)
# # cv2.imshow("first layer",first_layer) #shrinking image lead to some loss in data.

# expanded_image=cv2.pyrUp(first_layer)
# laplacian=cv2.subtract(img,expanded_image)


# # cv2.imshow("expanded image",expanded_image)
# cv2.imshow("laplacian",laplacian)


layer=gaussian_pyramid[5]
cv2.imshow("6",layer)
laplacian_pyramid=[layer]
for i in range(5,0,-1):
    size=(gaussian_pyramid[i-1].shape[1],gaussian_pyramid[i-1].shape[0])
    #cv2.pyrup expands an image but you must tell it the exact size you want.
    #shape returns (rows,col,channels) . so by doing shape[0] give height(row) and shape[1] give width col
    gaussian_expanded=cv2.pyrUp(gaussian_pyramid[i],dstsize=size)
    laplacian=cv2.subtract(gaussian_pyramid[i-1],gaussian_expanded)   #this will going to generate error beacuse of shape.so add a variable called size.
    laplacian_pyramid.append(laplacian)
    cv2.imshow(str(i),laplacian)

cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''
Image pyramids are used to represent images at multiple resolutions, making them essential for tasks 
like multi‑scale  object detection, image blending, compression, and efficient processing.
'''
