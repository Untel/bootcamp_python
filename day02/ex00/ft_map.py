import sys

def ft_map(fn, lst):
    return [fn(el) if fn else el for el in lst]
# a = [1, 2, 3]
# print(ft_map(lambda x: x * 2, a))