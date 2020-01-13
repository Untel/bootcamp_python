import sys
import string
import re

def main(argv):
    if len(argv) is not 2 or argv[0].isprintable() == False or argv[1].isdigit() == False:
        print("ERROR")
        return
    # delimiters_str = string.punctuation + string.whitespace
    # print("delimiters_str", delimiters_str)
    # delimiters_array = [char for char in delimiters_str]
    # print("delimiters_array", delimiters_array)
    # delimiters = "|".join(delimiters_array)
    # print("delimiters", delimiters)
    # elms = argv[0].split(delimiters)
    elms = re.findall(r"[\w']+", argv[0])
    filtered = [el for el in elms if len(el) > int(argv[1])]
    # filtered = filter(lambda x: len(x) > int(argv[1]), elms)
    print(filtered)

if __name__ == "__main__":
	main(sys.argv[1:])
