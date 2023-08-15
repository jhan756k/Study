import cv2

img = cv2.imread("./new.png") 
print(img)
print()
size = img.shape
dimension = (size[0], size[1])
new_dimension = (int(dimension[1]*0.5), int(dimension[0]*0.5))
resized_img = cv2.resize(img, new_dimension, interpolation=cv2.INTER_NEAREST)
print(resized_img)

'''
[
    [ [10 10 10],[40 40 40]  ],
    [ [30 30 30], [20 20 20] ]
]
'''

'''
[
    [[10 10 10]]
]
'''