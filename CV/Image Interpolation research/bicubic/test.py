from PIL import Image
import numpy as np

i = Image.open('new.png')
nlist = np.array(i)
print(nlist)