import sys
import string
import re
from random import randint

def main(argv):
    print("This is an interactive guessing game!")
    print("You have to enter a number between 1 and 99 to find out the secret number.")
    print("Type 'exit' to end the game.\nGood luck!\n")
    num = randint(1, 99)
    tries = 0
    while True:
        print("What's your guess between 1 and 99?")
        ans = input(">> ")
        tries += 1
        if ans == 'exit':
            print("Sad, number was %d x(. Goodbye!" % (num))
            return
        if ans.isdigit() is False:
            print("That's not a number.")
        ans = int(ans)
        if ans > num:
            print("Too high!")
        elif ans < num:
            print("Too low!")
        else:
            if num is 42:
                print("yo")
            break
    print("Congratulations, you've got it!")
    print("You won in %d attempts!" % (tries))

if __name__ == "__main__":
	main(sys.argv[1:])
