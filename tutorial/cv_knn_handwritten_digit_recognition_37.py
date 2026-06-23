import cv2 
import numpy as np

digits=cv2.imread("image/digits.png",cv2.IMREAD_GRAYSCALE)
test_digits=cv2.imread("image/test_digits.png",cv2.IMREAD_GRAYSCALE)

rows=np.vsplit(digits,50)
cells=[]
for row in rows:
    row_cells=np.hsplit(row,50)
    # cv2.imshow("row cell 0",row_cells[0])
    # break
    for cell in row_cells:
        cell=cell.flatten() #convert 2d to 1d
        cells.append(cell)
        # print(cell)
        # cv2.imshow("cells",cell)
        # break
cells=np.array(cells,dtype=np.float32)



k=np.arange(10)
# print(k)
cells_labels=np.repeat(k,250)
# for c in cells_labels:
#     print(c)
test_digits=np.vsplit(test_digits,50)
test_cells=[]
for d in test_digits:
    d=d.flatten()
    test_cells.append(d)

test_cells=np.array(test_cells,dtype=np.float32)
## use knn algo
knn=cv2.ml.KNearest_create()
knn.train(cells,cv2.ml.ROW_SAMPLE,cells_labels)

ret,result,neighbours,dist=knn.findNearest(test_cells,k=1)

print(result)

# cv2.imshow("cell",cells[220])
# cv2.imshow("rows",rows[0])
# cv2.imshow("test_digits",test_digits[0])
# cv2.imshow("digits",digits)
# cv2.waitKey(0)
# cv2.destroyAllWindows()