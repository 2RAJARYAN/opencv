import cv2 
import numpy as np

img=cv2.imread("image/orange.jpg",cv2.IMREAD_GRAYSCALE)
# img=cv2.resize(img,(600,600))  #(width,height)
# img=cv2.GaussianBlur(img,(7,7),0)

#apply fouier transform

f=np.fft.fft2(img)
fshift=np.fft.fftshift(f)
magnitude_spectrum=20*np.log(np.abs(fshift)+1)

# magnitude_spectrum=20*np.log(np.abs(f))
# print(magnitude_spectrum.dtype)
# magnitude_spectrum=magnitude_spectrum.astype(np.uint8)

#### can use cv2.normalize--minmax , for uint8 to do their job

magnitude_spectrum=cv2.normalize(magnitude_spectrum,None,0,255,cv2.NORM_MINMAX).astype(np.uint8)
# magnitude_spectrum=np.asarray(magnitude_spectrum,dtype=np.uint8)

 

cv2.imshow("magniture spectrum",magnitude_spectrum)
cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()




'''
#Fourier transform
*The Fourier Transform is a mathematical tool that converts a signal from the time (or spatial) domain 
into the frequency domain, showing which frequencies make up the original signal
*it decomposes any waveform into a sum of sine and cosine waves of different frequencies and amplitudes.

## Application of fourier transform
* signal processing, image processing, physics/engineering, communications.
'''