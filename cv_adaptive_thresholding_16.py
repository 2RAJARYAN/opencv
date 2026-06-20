import cv2 
import numpy as np

img=cv2.imread("image/book_page.jpg")  #the image have different lightning so simple threshold do not work.

_,threshold=cv2.threshold(img,150,255,cv2.THRESH_BINARY)

img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
adaptive_thresh_mean_c=cv2.adaptiveThreshold(img_gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,5)
adaptive_thresh_gaus=cv2.adaptiveThreshold(img_gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,15,12)
'''
*src → Input image (must be grayscale).
*maxValue → Value to assign to pixels that pass the threshold (usually 255 → white).
*adaptiveMethod → How the threshold is calculated for each pixel:
    *cv2.ADAPTIVE_THRESH_MEAN_C → threshold is the mean of neighborhood values minus C.
    *cv2.ADAPTIVE_THRESH_GAUSSIAN_C → threshold is a weighted sum (Gaussian window) of neighborhood values minus C.
*thresholdType → Type of thresholding (usually cv2.THRESH_BINARY).
*blockSize → Size of neighborhood (odd number, e.g. 11, 15). Defines how many pixels around each pixel are considered.
*C → Constant subtracted from the mean/weighted sum. Fine‑tunes the threshold.

#### USE CASE ####
*OCR preprocessing → makes text clearer for recognition.
*Document scanning → removes shadows and uneven lighting.
*Medical imaging → highlights regions of interest.
'''

cv2.imshow("img",img)
cv2.imshow("adaptive_thresh_mean",adaptive_thresh_mean_c)
cv2.imshow("adaptive_thresh_gaus",adaptive_thresh_gaus)
cv2.imshow("binary_threshold",threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()