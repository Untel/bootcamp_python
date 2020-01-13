import sys
import string

cookbook = {
    'sandwich': {
        'ingredients': ('ham', 'bread', 'cheese', 'tomatoes'),
        'type': 'lunch',
        'prep_time': 10,
    },
    'cake': {
        'ingredients': ('flour', 'sugar', 'eggs'),
        'type': 'dessert',
        'prep_time': 60,
    },
    'salad': {
        'ingredients': ('avocado', 'arugula', 'tomatoes', 'spinach'),
        'type': 'lunch',
        'prep_time': 15,
    },
}

def print_recipe(key):
    print


def main(argv):

    print("Please select an option by typing the corresponding number:")
    print("1: Add a recipe")
    print("2: Delete a recipe")
    print("3: Print a recipe")
    print("4: Print the cookbook")
    print("5: Quit")
    resp = None
    while (resp not in ('1', '2', '3', '4', '5')):
        resp = input(">> ")
        if (resp not in ('1', '2', '3', '4', '5')):
            print("This option does not exist, please type the corresponding number.\nTo exit, enter 5.")
            continue

        if resp is '3':
            print_recipe('sandwich')


if __name__ == "__main__":
	main(sys.argv[1:])
