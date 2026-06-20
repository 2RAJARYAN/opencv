import cv2 
import numpy as np

# img=cv2.imread("image/sea_beach.jpg",cv2.IMREAD_GRAYSCALE)
# img=cv2.GaussianBlur(img,(11,11),0)  #(11,11) odd number only
# sobelx=cv2.Sobel(img,cv2.CV_64F,1,0)  #img, cv2.CV_64F(output image depth{64 float, avoids overflow})
# sobely=cv2.Sobel(img,cv2.CV_64F,0,1)

## 1,0 → derivative order in x direction (detects vertical edges).
## 0,1 → derivative order in y direction (detects horizontal edges)

# laplacian=cv2.Laplacian(img,cv2.CV_64F,ksize=5)

# canny=cv2.Canny(img,100,150)  #img,lower_threshold, upper_threshold

# cv2.imshow("img",img)
# cv2.imshow("sobelx",sobelx)
# cv2.imshow("sobely",sobely)
# cv2.imshow("laplacian",laplacian)
# cv2.imshow("canny",canny)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

'''
*Edges = regions of rapid intensity change.
*They represent object boundaries and are crucial for segmentation, recognition, and tracking.
*different model like sobel,laplacian, canny.
'''

cap=cv2.VideoCapture(0)

while True:
    _,frame=cap.read()
    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    blurred_frame=cv2.GaussianBlur(frame,(5,5),0)

    laplacian=cv2.Laplacian(frame,cv2.CV_64F,ksize=5)
    canny=cv2.Canny(frame,100,150)

    cv2.imshow("frame",frame)
    cv2.imshow("laplacian",laplacian)
    cv2.imshow("canny",canny)

    key=cv2.waitKey(1)
    if key==27:
        break

cap.release()
cv2.destroyAllWindows()
