import datetime
from recipe import Recipe

class Book:
    def __init__(self, name:str, last_update:datetime, creation_date:datetime, recipes_list:dict):
        if not name.strip():
            raise ValueError("Name cannot be empty")
        if not last_update:
            raise ValueError("Date of last update cannot be empty")
        if not creation_date:
            raise ValueError("Creation date cannot be empty")
        self.name = name
        self.last_update = datetime.datetime
        self.creation_date = self.last_update
        self.recipes_list = recipes_list

    def get_recipe_by_name(self, name):
        """Prints a recipe with the name \texttt{name} and returns the instance"""
        for keys in self.recipes_list.keys():
            print(f"key = {keys}")
            lst = self.get_recipes_by_types(keys)
            print(lst)
            for i in range(len(lst)):
                if (lst[i] == name):
                    print(str(self.recipes_list[keys][i]))
                    return self.recipes_list[keys][i]
#... Your code here ...
    
    def get_recipes_by_types(self, recipe_type):
        """Gets all recipes names for a given recipe_type """
        lst = []
        for i in range(len(self.recipes_list[recipe_type])):
            # print(f"rec.name = {self.recipes_list[recipe_type][i].name}")
            lst.append(self.recipes_list[recipe_type][i].name)
        return lst
#... Your code here ...
    
    def add_recipe(self, recipe):
        """Adds a recipe to the book and updates last_update"""
        if not isinstance(recipe, Recipe):
            raise TypeError("new recipe must be an instance of the class Recipe")
        for keys in self.recipes_list.keys():
            if recipe.recipe_type == keys:
                self.recipes_list[keys].append(recipe)
                self.last_update = datetime.datetime

            

#... Your code here ...