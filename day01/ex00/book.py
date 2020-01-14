import sys
import string
from recipe import Recipe
from datetime import datetime

class Book:
    def __init__(self, name):
        self.set_name(name)
        self.recipe_list = {
            'starter': [],
            'lunch': [],
            'dessert': [],
        }
        self.update_last_update()
        self.creation_date = self.last_update
    def get_name(self):
        return self.name

    def set_name(self, name):
        if name.isprintable():
            self.name = name
        else:
            raise ValueError("Error, name is unprintable")

    def get_last_update(self):
        return self.last_update

    def get_creation_date(self):
        return self.creation_date

    def update_last_update(self):
        self.last_update = datetime.today()

    def get_recipe_by_name(self, name):
        """Print a recipe with the name `name` and return the instance"""
        for rtype in self.recipe_list:
            for recipe in self.recipe_list[rtype]:
                if recipe.name == name:
                    print(recipe)
                    return recipe
        print("Input Error : No such recipe\n")
        return None
    
    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        if Recipe.is_allowed_recipe_type(recipe_type):
            print("lst is", self.recipe_list[recipe_type])
            return list(map(lambda recipe: recipe.name, self.recipe_list[recipe_type]))
        else:
            raise Exception("Wrong recipe type")
        return None
    
    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        if type(recipe) == Recipe:
            self.recipe_list[recipe.get_recipe_type()].append(recipe)
            self.update_last_update()
            return True
        else:
            raise Exception("Cannot add a non recipe type")
        return False

    def __str__(self):
        """Return the string to print with the recipe info"""
        txt = "Name: " + self.get_name() + "\n"
        txt += "Creation date: " + str(self.get_creation_date()) + "\n"
        txt += "Last update: " + str(self.get_last_update()) + "\n"
        txt += "Recipes: " + str(self.recipe_list) + "\n"
        return txt
