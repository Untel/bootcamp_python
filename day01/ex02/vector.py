import sys
import string

class Vector:
    def __init__(self, values):
        if type(values) is list:
            self.values = values
        elif type(values) is int:
            self.values = [float(value) for value in range(values)]
        elif type(values) is tuple:
            self.values = [float(value) for value in range(values[0], values[1])]
        else:
            raise Exception("Wrong value type")
        self.size = len(self.values)

    def __mul__(self, per):
        if type(per) is int or type(per) is float:
            return Vector([value * per for value in self.values])
        elif type(per) == Vector:
            return Vector([x * y for x, y in zip(self.values, per.values)])
        else:
            raise Exception("Cannot multiply a Vector by something else than int or float")

    def __rmul__(self, per):
        return self.__mul__(per)

    def __add__(self, per):
        if type(per) is int or type(per) is float:
            return Vector([value + per for value in self.values])
        elif type(per) == Vector:
            return Vector([x + y for x, y in zip(self.values, per.values)])
        else:
            raise Exception("Cannot add a Vector by something else than int or float")

    def __radd__(self, per):
        return self.__add__(per)        

    def __sub__(self, per):
        if type(per) is int or type(per) is float:
            return Vector([value - per for value in self.values])
        elif type(per) == Vector:
            return Vector([x - y for x, y in zip(self.values, per.values)])
        else:
            raise Exception("Cannot sub a Vector by something else than int or float")

    def __rsub__(self, per):
        return self.__sub__(per)

    def __truediv__(self, per):
        if type(per) is int or type(per) is float:
            return Vector([value / per for value in self.values])
        elif type(per) == Vector:
            return Vector([x / y for x, y in zip(self.values, per.values)])
        else:
            raise Exception("Cannot multiply a Vector by something else than int or float")

    def __rtruediv__(self, per):
        return self.__truediv__(per)

    def __str__(self):
        return "Size: " + str(self.size) + " // " + str(self.values)

    def __repr__(self):
        return {
            'size': self.size,
            'values': self.values
        }