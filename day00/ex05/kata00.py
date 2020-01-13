import sys
import string


def main(argv):
    t = (19,42,21)
    print("The 3 numbers are: " + ", ".join(map(str, t)))
        
if __name__ == "__main__":
	main(sys.argv[1:])
