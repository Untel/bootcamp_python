import numpy as np
from collections.abc import Iterable

class NumPyCreator():
    def from_list(self, lst):
        return np.array(lst) if type(lst) == list else None

    def from_tuple(self, tpl):
        return np.array(tpl) if type(tpl) == tuple else None

    def from_iterable(self, itr):
        return np.array([x for x in itr]) if isinstance(itr, Iterable) else None

    def from_shape(self, shape, value=0):
        return np.full(shape, value)

    def random(self, shape):
        return np.random.rand(shape[0], shape[1])

    def identity(self, n):
        return np.identity(n)


npc = NumPyCreator()
print(list(npc.from_list([[1,2,3],[6,3,4]])))
print(list(npc.from_tuple(("a", "b", "c"))))
print(list(npc.from_iterable(range(5))))
shape=(3,5)
print(npc.from_shape(shape, value=1))
print(npc.random(shape))
print(npc.identity(4))
