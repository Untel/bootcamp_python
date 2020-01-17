import sys
from PIL import Image
import numpy as np
from ImageProcessor import ImageProcessor

class ScrapBooker():
    def crop(self, array, dimensions, position):
        w, h, x = array.shape
        if w < position[0] + dimensions[0] or h < position[1] + dimensions[1]:
            print("ERROR")
            return None
        return array[position[0]:position[0] + dimensions[0],
            position[1]:position[1] + dimensions[1]]

    def thin(self, array, n, axis):
        return np.delete(array, np.arange(n - 1, array.shape[axis], n), axis)
   
    def juxtapose(self, array, n, axis):
        return np.concatenate([array] * n, axis)

    def mosaic(self, array, dim):
        return np.tile(array, (dim[0], dim[1], 1))

# ip = ImageProcessor()
# img = ip.load("../resources/42AI.png")
# sb = ScrapBooker()
# # new = sb.crop(img, (100, 100), (100, 100))
# # new = sb.thin(img, 4, 0)
# # new = sb.juxtapose(img, 4, 1)
# new = sb.mosaic(img, (4, 2))
# if new is not None:
#     ip.display(new)
