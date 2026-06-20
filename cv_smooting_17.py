import cv2 
import numpy as np

img=cv2.imread("image/lake.jpg")

averaging=cv2.blur(img,(5,5))  #img, kernal size(width x height)  #simple smoothen but blur the edges
gaussian=cv2.GaussianBlur(img,(5,5),0) #img,kernel size , sigma(standard deviation);0 mean let opencv calculate automatically  #better edge presevation than simple averaging
median=cv2.medianBlur(img,5)  #img, kernal size(odd integer) ## each pixel replace by the median of it's neighorhood  #exvellent for removing "salt and pepper" noise while keeping  edges sharp.
bilateral=cv2.bilateralFilter(img,9,355,350)  #img, diameter of pixel neighborhood, sigmacolor(filter strenght vased on color difference), sigmaSpace (filter strength based on spatial distance).
#smooths noise while preseving sharp edges 

cv2.imshow("original image",img)
cv2.imshow("averaging image",averaging)
cv2.imshow("gaussian image",gaussian)
cv2.imshow("median image",median)
cv2.imshow("bilateral image",bilateral)
cv2.waitKey(0)
cv2.destroyAllWindows()