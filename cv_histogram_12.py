import numpy as np
import cv2 
import matplotlib.pyplot as plt

# img=np.zeros((100,100),np.uint8)
# cv2.rectangle(img,(0,50),(100,100),(255),-1)
# cv2.circle(img,(50,50),25,127,thickness=-1)

# img=cv2.imread("image/sea.jpg",cv2.IMREAD_GRAYSCALE)
img=cv2.imread("image/sea_beach.jpg")
b,g,r=cv2.split(img)


cv2.imshow("b",b)
cv2.imshow("g",g)
cv2.imshow("r",r)
# cv2.imshow("img",img)

plt.hist(b.ravel(),256,[0,256])
plt.hist(g.ravel(),256,[0,256])
plt.hist(r.ravel(),256,[0,256])

# plt.hist(img.ravel(),256,[0,256])
plt.show()
# cv2.waitKey(0)
# cv2.destroyAllWindows()


