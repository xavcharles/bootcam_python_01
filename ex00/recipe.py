class Recipe:
    def __init__(self, name:str, level:int, cooktime:int, ingredients:list, recipe_type:str, description:str=None):
        if not name.strip():
            raise ValueError("Name cannot be empty")
        if not level in range(1,6):
            raise ValueError("level range is from 1 to 5")
        if cooktime < 0:
            raise ValueError("cooking time cannot be negative")
        if recipe_type not in ["starter", "lunch", "dessert"]:
            raise ValueError("there are 3 valid recipe types : starter, lunch or dessert")
        if not (bool(ingredients) and all(ingredients) and len(set(map(type, ingredients))) == 1):
            raise ValueError("The ingredient list is either empty, or has an empty element, or has different types")
        # print("test1")
        self.name = name
        self.cooking_lvl = level
        self.cooking_time = cooktime
        self.ingredients = ingredients
        self.descripton = description
        self.recipe_type = recipe_type

    def __str__(self):
        """Returns the string to print with the recipe’s info"""
        txt = f"""
Recipe : {self.name}, cooking level = {self.cooking_lvl}
Needs to cook for {self.cooking_time} minutes
Ingredients : {', '.join(self.ingredients)}        
"""
        if (self.descripton):
            txt += f"""Description : {self.descripton}
"""
        txt += f"""Recipe type : {self.recipe_type}
"""
        return txt