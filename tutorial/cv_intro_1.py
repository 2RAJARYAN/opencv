import cv2
import sys  #provides access to system-specific parameters and function

image_path='image/red_panda.jpg'
window_title="Red panda image"
#load the image from the specified file
image=cv2.imread(image_path)
### convert it in to `gray scale`
gray_image=cv2.cvtColor(src=image,code=cv2.COLOR_BGR2GRAY)


if image is None:
    print(f"error: could not read the image file at {image_path}")
    print(f"please check the file path and ensure the image format is supported.")
    sys.exit()

### show the gray image
# cv2.imshow("Gray panda",gray_image )

# cv2.imshow(window_title,image)
#wait indefinitely until the user presses any key on the windows
# print(f"press any key while the '{window_title}' window is active to close it.")
# cv2.waitKey(0)

#close all the windows opened by opencv
# cv2.destroyAllWindows()

cv2.imwrite("image/gray panda.jpg",gray_image)

print("image window closed script finished.")