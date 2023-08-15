'''
import cv2
import numpy as np

def main():
    # img = cv2.imread("./img.png")

    # ex1 = img[:, 1085:2160]
    # ex2 = img[:, 0:1075]

    # cv2.imwrite("./ex1.png", ex1)
    # cv2.imwrite("./ex2.png", ex2)
    
    ex1 = cv2.imread("./ex1.png")
    ex2 = cv2.imread("./ex2.png")

    for x in range(ex1.shape[0]):
        for y in range(ex1.shape[1]):
            for k in range(3):
                if ex1[x][y][k] !=  ex2[x][y][k]:
                    ex1[x][y] = [0 , 0, 255]

    cv2.imwrite("./answer.png", ex1)
if __name__ == '__main__':
    main()

'''

from PIL import Image
im = Image.open("./mmm.jpeg")
print(im.info)