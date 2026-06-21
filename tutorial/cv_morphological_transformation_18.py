import cv2 
import numpy as np

# img=cv2.imread("image/balls.jpg",cv2.IMREAD_GRAYSCALE)

# _,mask=cv2.threshold(img,250,255,cv2.THRESH_BINARY_INV)
# kernel=np.ones((11,11),np.uint8)
# dilation=cv2.dilate(mask,kernel)
# erosion=cv2.erode(mask,kernel,iterations=3)


# cv2.imshow("img",img)
# cv2.imshow("mask",mask)
# cv2.imshow("dilation",dilation)
# cv2.imshow("erosion",erosion)
# cv2.waitKey(0)
# cv2.destroyAllWindows() 

def nothing():
    pass


cap=cv2.VideoCapture(0)
cv2.namedWindow("trackbars")
cv2.createTrackbar("L-H","trackbars",0,179,nothing)  
cv2.createTrackbar("L-S","trackbars",0,255,nothing)
cv2.createTrackbar("L-V","trackbars",0,255,nothing)
cv2.createTrackbar("H-H","trackbars",179,179,nothing)
cv2.createTrackbar("H-S","trackbars",255,255,nothing)
cv2.createTrackbar("H-V","trackbars",255,255,nothing)


while True:
    _,frame=cap.read()

    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    l_h=cv2.getTrackbarPos("L-H","trackbars")
    l_s=cv2.getTrackbarPos("L-S","trackbars")
    l_v=cv2.getTrackbarPos("L-V","trackbars")
    h_h=cv2.getTrackbarPos("H-H","trackbars")
    h_s=cv2.getTrackbarPos("H-S","trackbars")
    h_v=cv2.getTrackbarPos("H-V","trackbars")

    lower_blue=np.array([l_h,l_s,l_v]) 
    upper_blue=np.array([h_h,h_s,h_v])  
    mask=cv2.inRange(hsv,lower_blue,upper_blue)  
    kernel=np.ones((5,5),np.uint8)
    erosion=cv2.erode(mask,kernel)  #src,kernel,iterations.
    dilation=cv2.dilate(mask,kernel)

    opening=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel,iterations=2) #src,operation,kernel,iteration.
    closing=cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernel)
    #morph_open,close-> open(erosion followed by distilation, USE CASE-> remove small foreground noise while preseving larger objects)
    # closing(Dilation followed by erosion, USE CASE-> close small holes inside objects, removes black spots.)
    # ther are other like top hat and black hat.
    result=cv2.bitwise_and(frame,frame,mask=mask) 

    cv2.imshow("frame",frame)
    cv2.imshow("mask",mask)
    cv2.imshow("erosion",erosion)
    cv2.imshow("dilation",dilation)
    cv2.imshow("opening",opening)
    cv2.imshow("closing",closing)
    cv2.imshow("result",result)

    key=cv2.waitKey(1)
    if key==27:
        break

cap.release()
cv2.destroyAllWindows()






'''
*A kernel (also called a structuring element or filter mask) is simply a small matrix that defines how pixel neighborhoods are processed in image operations. Think of it as a sliding window 
that moves across the image and decides how each pixel should be modified based on its neighbors.

## Kernel in Smoothing (Blurring)##
*In averaging blur, a kernel like 5 x 5 means:Take a 5 x 5 block of pixels.
*In Gaussian blur, the kernel has weights shaped like a Gaussian curve (center pixels more important).
*In median blur, the kernel replaces the center pixel with the median of the neighborhood.


## Kernel in Morphological Transformations ##
*In erosion and dilation, the kernel defines the shape used to probe the image.
*Erosion: The kernel slides over the image; if all pixels under the kernel are white, the center stays white, otherwise it becomes black.

*Dilation: If any pixel under the kernel is white, the center becomes white.The kernel defines the shape and size of the transformation.

### Types of Kernels ###
*Square/Rectangle → np.ones((5,5), np.uint8)
*Ellipse/Circle → cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))
*Cross → cv2.getStructuringElement(cv2.MORPH_CROSS, (5,5))
'''



'''
*Morphological transformations in OpenCV are shape-based image processing operations applied to binary images using a kernel (structuring element). 
*They are mainly used for noise removal, object boundary refinement, and feature extraction
*The two fundamental operations are erosion and dilation, with variants like opening, closing, gradient, and top-hat.

### Core Concept ###
*Binary Image → Foreground (white, 255) and background (black, 0).
*Kernel (Structuring Element) → A small matrix (e.g., 3x3 or 5x5) that defines how pixels are processed.
*Operation Principle → The kernel slides over the image, modifying pixels based on neighborhood values.
'''