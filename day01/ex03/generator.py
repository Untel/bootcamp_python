import sys
from random import shuffle

def generator(text, sep=" ", option=None):
    '''Option is an optional arg, sep is mandatory'''
    print("Opt = ", option)
    if type(text) is str and option in ["shuffle", "ordered", "unique", None]:
        words = text.split(sep)
        if option == "shuffle":
            shuffle(words)
        elif option == "ordered":
            words.sort()
        elif option == "unique":
            words = list(set(words))
        for word in words:
            yield word
        return
    print("ERROR")

for word in generator(sys.argv[1], sys.argv[2], sys.argv[3]):
    print(word)