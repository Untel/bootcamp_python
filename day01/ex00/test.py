# from book import Bookfrom
from recipe import Recipe
from book import Book
from time import sleep

cake = Recipe("Cake", 1, 90, [], "dessert")
lol = Recipe("lol", 2, 60, [], "starter")
book = Book("Yo")
book.add_recipe(cake)
book.add_recipe(lol)
print(book)
print(book.get_recipes_by_types("dessert"))