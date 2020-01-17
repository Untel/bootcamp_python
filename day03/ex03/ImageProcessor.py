import sys
from PIL import Image
import numpy as np

class ImageProcessor():
    def load(self, path):
        self.arr = np.array(Image.open(path))
        return self.arr

    def display(self, arr):
        return Image.fromarray(arr).show()

# imp = ImageProcessor()
# arr = imp.load("../resources/42AI.png")
# print(arr)
# imp.display(arr)
