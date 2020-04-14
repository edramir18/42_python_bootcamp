import sys
from functools import reduce


class Recipe:
    RECIPE_TYPES = ['starter', 'lunch', 'dessert']

    def __init__(self, name, lvl, time, ingredients, description, recipe_type):
        self.name = name
        self.cooking_lvl = lvl
        self.cooking_time = time
        self.ingredients = ingredients
        self.description = description
        self.recipe_type = recipe_type
        self.validate()

    def validate(self):
        if (
            type(self.name) != str
            or type(self.cooking_lvl) != int
            or type(self.cooking_time) != int
            or type(self.ingredients) != list
            or type(self.recipe_type) != str
            or (type(self.description) != str and self.description is not None)
        ):
            raise TypeError("The type of the argument is incorrect")
        elif len(self.name) == 0:
            raise ValueError("The name of recipe is incorrect")
        elif not (1 <= self.cooking_lvl <= 5):
            raise ValueError("The cooking level provided is incorrect")
        elif self.cooking_time < 0:
            raise ValueError("The cooking time provided is incorrect")
        elif len(self.ingredients) == 0:
            raise ValueError("The list of ingredients can't be empty")
        elif not reduce(lambda r, k: r and type(k) == str,
                        self.ingredients, True):
            raise TypeError("The ingredients list has invalid values")
        elif self.recipe_type not in self.RECIPE_TYPES:
            raise ValueError("The type of recipes is not valid")

    def __str__(self):
        """ Return the string to print with the recipe info"""
        return f'{self.name} ({self.cooking_lvl}) - {self.recipe_type}'
