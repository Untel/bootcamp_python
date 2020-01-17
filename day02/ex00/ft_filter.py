import sys

def ft_filter(fn, lst):
    return [el for el in lst if fn(el)]

# a = [1, 2, 3]
# print(ft_filter(lambda el: el == 2, a))
