#! /usr/bin/env python3

from recipe import Recipe
from book import Book


def test_recipe(name, lvl, time, ingredients, description, recipe_type):
    try:
        recipe = Recipe(name, lvl, time, ingredients, description, recipe_type)
    except ValueError as v:
        print(f'Wrong value: {v}')
    except TypeError as t:
        print(f'Wrong type: {t}')
    else:
        print(recipe)


def main():
    ingredients = ['flour', 'eggs', 'milk']
    test_recipe('cake', 1, 10, ingredients, 'A delicious dessert', Recipe.RECIPE_TYPES[2])
    test_recipe('cake', 1, 10, ingredients, None, Recipe.RECIPE_TYPES[2])
    test_recipe('', 1, 10, ingredients, 'A delicious dessert', Recipe.RECIPE_TYPES[2])
    test_recipe(None, 1, 10, ingredients, 'A delicious dessert', Recipe.RECIPE_TYPES[2])
    test_recipe('cake', None, 10, ingredients, 'A delicious dessert', Recipe.RECIPE_TYPES[2])
    test_recipe('cake', '2', 10, ingredients, 'A delicious dessert', Recipe.RECIPE_TYPES[2])
    test_recipe('cake', 6, 10, ingredients, 'A delicious dessert', Recipe.RECIPE_TYPES[2])
    test_recipe('cake', 1, -4, ingredients, 'A delicious dessert', Recipe.RECIPE_TYPES[2])
    test_recipe('cake', 1, 10, [1, 3, 'Hola'], 'A delicious dessert', Recipe.RECIPE_TYPES[2])
    test_recipe('cake', 1, 10, ingredients, 300, Recipe.RECIPE_TYPES[2])
    test_recipe('cake', 1, 10, ingredients, 'A delicious dessert', 'Dinner')

    cake = Recipe('cake', 1, 10, ingredients, 'A delicious dessert', Recipe.RECIPE_TYPES[2])
    book = Book("Libro")
    print(book)
    book.add_recipe(cake)
    print(book)
    print(book.get_recipe_by_name(cake.name))
    print(book.get_recipes_by_types(cake.recipe_type))
    print(book.get_recipes_by_types(Recipe.RECIPE_TYPES[0]))


if __name__ == '__main__':
    main()
