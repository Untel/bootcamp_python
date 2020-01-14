import sys
import string

class Recipe:
    # def __new__(name, cooking_lvl, cooking_time, ingredients, recipe_type, description = None):

    def __init__(self, name, cooking_lvl, cooking_time, ingredients, recipe_type, description = None):
        self.set_name(name)
        self.set_cooking_lvl(cooking_lvl)
        self.set_cooking_time(cooking_time)
        self.set_ingredients(ingredients)
        self.set_recipe_type(recipe_type)
        if description != None:
            self.set_description(description)

    def get_name(self):
        return self.name

    def set_name(self, name):
        if name.isprintable():
            self.name = name
        else:
            raise ValueError("Error, name is unprintable")

    def get_cooking_lvl(self):
        return self.cooking_lvl

    def set_cooking_lvl(self, cooking_lvl):
        if type(cooking_lvl) is int:
            self.cooking_lvl = cooking_lvl
        elif type(cooking_lvl) is str and cooking_lvl.isdigit():
            self.cooking_lvl = int(cooking_lvl)
        else:
            raise ValueError("Error, cooking level is not a digit")

    def get_cooking_time(self):
        return self.cooking_time

    def set_cooking_time(self, cooking_time):
        if type(cooking_time) is int:
            self.cooking_time = cooking_time            
        elif type(cooking_time) is str and cooking_time.isdigit():
            self.cooking_time = int(cooking_time)
        else:
            raise ValueError("Error, cooking time is not a digit")

    def get_ingredients(self):
        return self.ingredients

    def set_ingredients(self, ingredients):
        if type(ingredients) is list:
            self.ingredients = ingredients            
        else:
            raise ValueError("Error, ingredients arg is not a list")

    @staticmethod
    def is_allowed_recipe_type(recipe_type):
        return recipe_type in ["starter", "lunch","dessert"]

    def get_recipe_type(self):
        return self.recipe_type

    def set_recipe_type(self, recipe_type):
        if Recipe.is_allowed_recipe_type(recipe_type):
            self.recipe_type = recipe_type
        else:
            raise ValueError("Error, recipe_type can only be starter, lunch or dessert")

    def get_description(self):
        return self.description

    def set_description(self, description):
        if description.isprintable():
            self.description = description
        else:
            raise ValueError("Error, description is unprintable")

    def __str__(self):
        """Return the string to print with the recipe info"""
        txt = "Name: " + self.get_name() + "\n"
        txt += "Cooking level: " + str(self.get_cooking_lvl()) + "\n"
        txt += "Cooking Time: " + str(self.get_cooking_time()) + "\n"
        txt += "Ingredients: " + str(self.get_ingredients()) + "\n"
        txt += "Recipe type: " + self.get_recipe_type() + "\n"
        return txt
