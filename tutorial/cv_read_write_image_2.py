import cv2
import sys 
import numpy as np

image_path='image/red_panda.jpg'
img=cv2.imread(image_path)

if img is None:
    print(f"Error could not read the image file at {image_path}")
else:
    print("successfully, load the file")
    print(f"image dimension {img.shape}")

#### cv2.imread() -filename .flags(interger,optional) 
"""
For cv2.IMREAD_COLOR,-> it's typically a 3D array of shape (height, width, 3), representing BGR channels.
For cv2.IMREAD_GRAYSCALE,-> it's a 2D array of shape (height, width).
For cv2.IMREAD_UNCHANGED,-> it could be 2D or 3D, potentially with 4 channels
                            (e.g., BGRA) if the image has transparency.
"""
img_gray=cv2.imread('image/red_panda.jpg',cv2.IMREAD_GRAYSCALE)
if img_gray is not None:
    print(f"Grayscale image dimensions: {img_gray.shape}") 

img_rgba = cv2.imread('image/red_panda.jpg', cv2.IMREAD_UNCHANGED)
if img_rgba is not None:
    print(f"Image dimensions (with alpha?): {img_rgba.shape}") # Might show (height, width, 4)

processed=cv2.cvtColor(src=img,code=cv2.COLOR_BGR2HSV)
output_path="image/processed.png"
success=cv2.imwrite(output_path,processed)

if success:
    print(f"image successfully saved to {output_path}")
else:
    print(f"Error could not save image to {output_path}")

if img_gray is not None:
    cv2.imwrite('photo_grayscale.jpg',img_gray)
"""
Understanding cv2.imwrite():

* filename (string): The first argument is the desired path and filename for the output image. 
    The file format is determined by the extension you provide (e.g., .jpg, .png, .bmp, .tif). 
    OpenCV uses this extension to encode the image appropriately.
    
* img (NumPy array): The second argument is the image data (the NumPy array) you want to save.

* params (optional): You can provide optional parameters to control the saving process, 
    such as the compression quality for JPEG files. This is more advanced and often not needed for basic tasks.

* Return Value: The function returns True if the image was saved successfully and False otherwise 
    (e.g., invalid path, incorrect permissions, unsupported file extension).
"""

