import cv2
import numpy as np
from copy import deepcopy

image = cv2.imread("iu.jpg")
bimg = deepcopy(image)
sp = image.shape
bbimg = deepcopy(image)

kernel1d = cv2.getGaussianKernel(5, 7)
kernel2d = np.outer(kernel1d, kernel1d.transpose())
print(kernel2d)

for x in range(2, sp[0]-2):
    for y in range(2, sp[1]-2):

        for p in range(3):
            sum = 0
            bsum =0

            for i in range(5):
                for j in range(5):
                    sum += image[x+i-2][y+j-2][p] * (1-kernel2d[i][j])
                    bsum += image[x+i-2][y+j-2][p]
            bimg[x][y][p] = sum // 25
            bbimg[x][y][p] = bsum // 25

cv2.imshow("Original", image)
cv2.imshow("Blurred", bimg)
cv2.imshow("Blurred2", bbimg)
cv2.waitKey(0)
cv2.destroyAllWindows()
