import sys
import string
import re
from time import sleep, time

def ft_progress(listy):
    m = max(listy) + 1
    for x in listy:
        p = (x + 1) / m
        print("p is", p)
        print("\rETA: xx [% 3d%%] %s" % (
            round(p * 100),
            (">".rjust(round(p * 100), "="))
        ))
        # sys.stdout.flush()
        yield 1

if __name__ == "__main__":
    listy = range(1000)
    ret = 0
    for elem in ft_progress(listy):
        ret += (elem + 3) % 5
        sleep(0.01)
    print()
    print(ret)
