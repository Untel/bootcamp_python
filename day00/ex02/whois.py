import sys
import string


def main(argv):
	if len(argv) > 1:
		print("ERROR")
		return
	elif len(argv) == 0:
		return
	try:
		num = int(argv[0])
	except ValueError:
		print("ERROR")
		return
	if (num == 0):
		print("I'm Zero.")
	elif num % 2 == 1:
		print("I'm Odd.")
	else:
		print("I'm Even.")

if __name__ == "__main__":
	main(sys.argv[1:])
