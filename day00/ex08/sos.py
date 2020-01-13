import sys
import string
import re

MORSE_CODE_DICT = {
    'A':'.-', 'B':'-...', 
    'C':'-.-.', 'D':'-..', 'E':'.', 
    'F':'..-.', 'G':'--.', 'H':'....', 
    'I':'..', 'J':'.---', 'K':'-.-', 
    'L':'.-..', 'M':'--', 'N':'-.', 
    'O':'---', 'P':'.--.', 'Q':'--.-', 
    'R':'.-.', 'S':'...', 'T':'-', 
    'U':'..-', 'V':'...-', 'W':'.--', 
    'X':'-..-', 'Y':'-.--', 'Z':'--..', 
    '1':'.----', '2':'..---', '3':'...--', 
    '4':'....-', '5':'.....', '6':'-....', 
    '7':'--...', '8':'---..', '9':'----.', 
    '0':'-----'
}

def to_morse_letter(letter):
    new_letter = MORSE_CODE_DICT[letter]
    return new_letter

def to_morse_word(word):
    letter_arr = [char for char in word]
    new_word = map(to_morse_letter, letter_arr)
    return " ".join(list(new_word))

def main(argv):
    if len(argv) == 0
        return
    txt = " ".join(argv).upper()
    words = re.findall(r"[\w']+", txt)
    test = "".join(words)
    if test.isalnum() is False:
        print("ERROR")
        return
    # print("Word list", words)
    parsed = map(to_morse_word, words)
    print(" / ".join(list(parsed)))

if __name__ == "__main__":
	main(sys.argv[1:])
