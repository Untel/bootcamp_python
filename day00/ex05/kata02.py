import sys
import string


def main(argv):
    t = (3,30,2019,9,25)
    print("%02d/%02d/%d %02d:%02d" % (t[-2], t[-1], t[-3], t[0], t[1]))
if __name__ == "__main__":
	main(sys.argv[1:])
