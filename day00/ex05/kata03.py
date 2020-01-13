import sys
import string


def main(argv):
    phrase = "The right format"
    # print("{:>42}".format(phrase))
    print(phrase.rjust(42, '-'), end = '')

if __name__ == "__main__":
	main(sys.argv[1:])
