import sys
import string


def main(argv):
    if (len(argv) > 0):
        print(" ".join(argv).swapcase()[::-1])

if __name__ == "__main__":
    main(sys.argv[1:])
