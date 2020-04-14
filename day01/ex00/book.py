from recipe import Recipe
from datetime import datetime


class Book:
    def __init__(self, name):
        if type(name) != str:
            raise TypeError("Invalid type for book name")
        elif len(name) == 0:
            raise ValueError("Invalid book name")
        self.name = name
        self.creation_date = datetime.now()
        self.last_update = datetime.now()
        self.recipe_list = {'starter': [], 'lunch': [], 'dessert': []}

    def get_recipe_by_name(self, name):
        """Print a recipe with the name `name` and return the instance"""
        for recipes in self.recipe_list.values():
            for recipe in recipes:
                if recipe.name == name:
                    print(recipe)
                    return recipe

    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        if type(recipe_type) != str:
            raise TypeError("Invalid argument by recipe type")
        elif (len(recipe_type) == 0
                or recipe_type not in self.recipe_list.keys()):
            raise ValueError("Invalid type for recipe")
        return [recipe.name for recipe in self.recipe_list[recipe_type]]

    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        if type(recipe) != Recipe:
            raise TypeError("Invalid recipe argument")
        self.recipe_list[recipe.recipe_type].append(recipe)
        self.last_update = datetime.now()

    def __str__(self):
        return f'{self.name} - updated {self.last_update: %Y%m%d %H:%M:%S}'
