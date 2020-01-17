import sys

def ft_reduce(fn, args):
    prev = args[0]
    for i in args[1:]:
        prev = fn(prev, i)
    return prev

# a = [1, 2, 3]
# print(ft_reduce(lambda prev, acc: prev + acc, a)
# a = [True, True, False]
# print(ft_reduce(lambda prev, acc: prev and acc, a))
