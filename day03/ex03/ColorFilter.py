from ImageProcessor import ImageProcessor
import numpy as np
class ColorFilter():
    def invert(self, array):
        for row in array:
            for octet in row:
                for idx, bit in enumerate(octet):
                    octet[idx] = -(bit - 256)
        return array

    def to_green(self, array):
        for row in array:
            for octet in row:
                octet[0] = 0
                octet[2] = 0
        return array

    def to_red(self, array):
        for row in array:
            for octet in row:
                octet[1] = 0
                octet[2] = 0
        return array

    def to_blue(self, array):
        for row in array:
            for octet in row:
                octet[0] = 0
                octet[1] = 0
        return array

    def celluloid(self, array, treshold = 2):
        s = np.linspace()
        fn = (lambda a, b: 256/b if (a > 256 / b) else a)
        vec = np.vectorize(fn)
        return vec(array, treshold)

imp = ImageProcessor()
arr = imp.load("../resources/42AI.png")
cf = ColorFilter()
# imp.display(cf.to_green(arr))
# imp.display(cf.invert(arr))
imp.display(cf.celluloid(np.array(arr, dtype="uint8")))