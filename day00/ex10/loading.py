import sys
import string
import re
from time import sleep
import time

def ft_progress(listy):
    start_time = time.time()
    m = max(listy) + 1
    for x in listy:
        p = (x + 1) / m
        bs = 30
        eta = 0
        elap = time.time() - start_time
        eta = (elap * m / (x + 1)) #- elap
        print("ETA: %.2fs [%3d%%] [%s%s] %d/%d | elapsed time %.2fs" % (
            eta,
            round(p * 100),
            ("" if bs - p * bs == 0 else ">").rjust(round(p * bs), "="),
            "".ljust(bs - round(p * bs), " "),
            x + 1, m,
            elap
        ), end = '\r')
        yield 1

if __name__ == "__main__":
    listy = range(1000)
    ret = 0
    for elem in ft_progress(listy):
        ret += (elem + 3) % 5
        sleep(0.01)
    print()
    print(ret)