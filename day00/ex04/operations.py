import sys
import string


def main(argv):
    if len(argv) > 2:
        print("InputError: too many arguments\n")
        print("Usage: python operations.py\nExample:\n\tpython operations.py 10 3")
        return
    elif len(argv) < 2:
        print("Usage: python operations.py\nExample:\n\tpython operations.py 10 3")
        return
    try:
        a = int(argv[0])
        b = int(argv[1])
    except ValueError:
        print("InputError: only numbers\n")
        print("Usage: python operations.py\nExample:\n\tpython operations.py 10 3")
        return
    print("Sum:         " + str(a + b))
    print("Difference:  " + str(a - b))
    print("Product:     " + str(a * b))
    if (b == 0):
        print("Quotien:     ERROR (div by zero)")
        print("Remainder:   ERROR (modulo by zero)")
    else:
        print("Quotien:     " + str(a / b))
        print("Remainder:   " + str(a % b))
        
if __name__ == "__main__":
	main(sys.argv[1:])
