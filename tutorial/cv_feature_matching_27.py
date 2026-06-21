import cv2 
import numpy as np

#use own image.
img1=cv2.imread("image/book.jpeg",cv2.IMREAD_GRAYSCALE)
img2=cv2.imread("image/person_holding_book.jpeg",cv2.IMREAD_GRAYSCALE)

#ORB detector
orb=cv2.ORB_create()
kp1,des1=orb.detectAndCompute(img1,None)
kp2,des2=orb.detectAndCompute(img2,None)

## Brute force matching
bf=cv2.BFMatcher(cv2.NORM_HAMMING,crossCheck=True)

# for d in des1:
#     print(d)

matches=bf.match(des1,des2)
matches=sorted(matches,key=lambda x:x.distance)
# print(len(matches))
matches_result=cv2.drawMatches(img1,kp1,img2,kp2,matches[:30],None,flags=2)
for m in matches:
    print(m.distance)



cv2.imshow("img1",img1)
cv2.imshow("img2",img2)
cv2.imshow("matching result",matches_result)
cv2.waitKey(0)
cv2.destroyAllWindows()



'''
#BFMatcher (Brute Force Matcher) is an OpenCV class used to match feature descriptors between two images.

### parameter it takes
*normType → Defines how distance between descriptors is measured.
    *cv2.NORM_HAMMING → for binary descriptors like ORB, BRIEF.
    *cv2.NORM_L2 → for float descriptors like SIFT, SURF.

*crossCheck (True/False) →
    *If True, only matches where descriptor A’s best match is descriptor B, and descriptor B’s best match is descriptor A are kept.
    *If False, one‑way matches are allowed (more matches, but less strict).

'''

'''
# drawMatches

*cv2.drawMatches is used to visualize matches between two images.

### parameters

*img1, kp1 → First image and its keypoints.
*img2, kp2 → Second image and its keypoints.
*matches → List of DMatch objects (the actual matches).
*outImg → Output image (can be None, OpenCV creates one).
*matchColor → Color for match lines (default green).
*singlePointColor → Color for keypoints not in matches.
*flags → Drawing options (e.g., cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS).


'''


