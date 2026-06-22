import cv2 
import numpy as np
import matplotlib.pyplot as plt 

original_image=cv2.imread("image/goalkeeper.jpg")
hsv_original=cv2.cvtColor(original_image,cv2.COLOR_BGR2HSV)
cut_out=cv2.imread("image/pitch_ground.jpg")
hsv_cut_out=cv2.cvtColor(cut_out,cv2.COLOR_BGR2HSV)
hue,saturation,value=cv2.split(hsv_cut_out)

# for h in hue:
#     print(h)

#histogram cut out
#to get histogram we need only 2 channel of hsv (hue and saturation)
cut_hist=cv2.calcHist([hsv_cut_out],[0,1],None,[180,256],[0,180,0,256])
#image,channels([0,1] h and s),mask(optional mask),histSize(number of bins([180,256],[hue,saturation])),ranges(hue range 0-180 and saturation 0-256)
mask=cv2.calcBackProject([hsv_original],[0,1],cut_hist,[0,180,0,256],1) 

#filtering remove noise 
kernel=cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5)) 
# for k in kernel:
#     print(k)
mask=cv2.filter2D(mask,-1,kernel)
_,mask=cv2.threshold(mask,80,255,cv2.THRESH_BINARY)

mask=cv2.merge((mask,mask,mask))  #convet graymask(1 channel) into 3 channel so that it combine with colors.
result=cv2.bitwise_and(original_image,mask)

cv2.imshow("result",result)
cv2.imshow("mask",mask)
cv2.imshow("original image",original_image)
cv2.imshow("cut out image",cut_out)
cv2.waitKey(0)
cv2.destroyAllWindows()

# plt.imshow(cut_hist)
# plt.show()


'''
### Histogram backprojection → finds regions in one image that match the color distribution of another.


#### cv2.calcHist → Computes histogram. Parameters:
    *images → list of images.
    *channels → which channels to use ([0,1] = Hue + Saturation).
    *mask → optional mask (None = whole image).
    *histSize → number of bins ([180,256]).
    *ranges → value ranges ([0,180,0,256] for Hue 0–180, Saturation 0–256).

    
### cv2.calcBackProject → Finds pixels in hsv_original that match histogram of cut_out. Parameters:
    *images → list of images.
    *channels → channels used ([0,1]).
    *hist → histogram reference.
    *ranges → same as histogram.
    *scale → multiplier (usually 1).


### cv2.getStructuringElement → Creates kernel for morphology. Parameters:
    *shape (e.g., cv2.MORPH_ELLIPSE).
    *ksize (kernel size, e.g., (5,5)).

### cv2.filter2D → Convolves image with kernel. Parameters:
    *src (input image).
    *ddepth (output depth, -1 = same as input).
    *kernel (filter matrix).
'''