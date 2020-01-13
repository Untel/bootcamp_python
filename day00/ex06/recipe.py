import sys
import string
from collections import OrderedDict

cookbook = {
    'sandwich': {
        'ingredients': ['ham', 'bread', 'cheese', 'tomatoes'],
        'type': 'lunch',
        'prep_time': 10,
    },
    'cake': {
        'ingredients': ['flour', 'sugar', 'eggs'],
        'type': 'dessert',
        'prep_time': 60,
    },
    'salad': {
        'ingredients': ['avocado', 'arugula', 'tomatoes', 'spinach'],
        'type': 'lunch',
        'prep_time': 15,
    },
}

def print_recipe(key):
    print("Recipe for " + key)
    print("Ingredients list: ", cookbook[key]['ingredients'])
    print("To be eaten for " + cookbook[key]['type'] + ".")
    print("Takes %d minutes of cooking." % (cookbook[key]['prep_time']))

def choose_recipe():
    resp = None
    print("Choose a recipe to print:")
    choices = { str(idx + 1): key for idx, key in enumerate(cookbook.keys()) }
    choices[str(len(cookbook) + 1)] = 'back'
    while resp not in choices.keys():
        for idx, key in choices.items():
            print(idx + ": " + key)
        resp = input(">> ")
        if resp not in choices.keys():
            resp = None
            print("This recipe does not exist, please type the corresponding number.")
            continue
        if choices[resp] is 'back':
            return None
    return choices[resp]

def main(argv):

    resp = None
    while resp not in ('1', '2', '3', '4', '5'):
        print("Please select an option by typing the corresponding number:")
        print("1: Add a recipe")
        print("2: Delete a recipe")
        print("3: Print a recipe")
        print("4: Print the cookbook")
        print("5: Quit")
        resp = input(">> ")
        if (resp not in ('1', '2', '3', '4', '5')):
            print("This option does not exist, please type the corresponding number.\nTo exit, enter 5.")
            continue

        if resp is '1':
            key = input(">> Name: ")
            meal_type = input(">> Type: ")
            time_prep = input(">> Time to prepare (in minutes): ")
            while time_prep.isnumeric() == False:
                time_prep = input(">> Please enter a numeric value: ")
            time_prep = int(time_prep)
            ingredients = []
            to_add = None
            while to_add is not "":
                if to_add is not None:
                    ingredients.append(to_add)
                to_add = input(">> Add an ingredient (leave empty to finish): ")
            cookbook[key] = {
                'ingredients': ingredients,
                'type': meal_type,
                'prep_time': time_prep,
            }

        if resp is '2':
            key = choose_recipe()
            if key is None:
                continue
            del cookbook[key]

        if resp is '3':
            key = choose_recipe()
            if key is None:
                continue
            print_recipe(key)

        if resp is '4':
            for key in cookbook.keys():
                print_recipe(key)

        if resp is not '5':
            resp = None
            print("---")
        else:
            print("Good bye!")

if __name__ == "__main__":
	main(sys.argv[1:])
