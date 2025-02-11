from book import Book
from recipe import Recipe
import datetime

def main():
    recipe1 = Recipe("Sandwitch", 1, 5, ["ham", "bread", "cheese", "tomatoes"], "lunch")
    recipe2 = Recipe("Cake", 4, 30, ["flour", "sugar", "eggs"], "dessert")
    recipe3 = Recipe("Salad", 2, 10, ["avocado", "arugula", "tomatoes", "spinach"], "lunch")

    print(str(recipe1))
    print(str(recipe2))
    print(str(recipe3))

    book1 = Book("book1", datetime.datetime, datetime.datetime, {"lunch" : [recipe1,], 
                                                                 "dessert" : [recipe2,],
                                                                 "starter" : [None,]})
    print("-------------------------------------------")
    book1.get_recipe_by_name("Cake")
    print(book1.get_recipes_by_types("lunch"))
    book1.add_recipe(recipe3)
    print(book1.get_recipes_by_types("lunch"))





main()