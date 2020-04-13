#! /usr/bin/env python


def print_menu():
    print("\nPlease select an option by typing the corresponding number:")
    print("1: Add a recipe")
    print("2: Delete a recipe")
    print("3: Print a recipe")
    print("4: Print the cookbook")
    print("5: Quit\n")


def add_recipe(cookbook):
    recipe = input("Please enter the recipe name: ")
    cookbook[recipe] = {}
    cookbook[recipe]['meal'] = input("Please enter the type of meal: ")
    cookbook[recipe]['prep_time'] = int(input("Please enter the time to be cooked: "))
    cookbook[recipe]['ingredients'] = input("Please enter the ingredients: ")


def delete_recipe(cookbook):
    print("Please enter the recipe's name to be eliminated:")
    recipe = input()
    if recipe in cookbook.keys():
        del cookbook[recipe]
        print("The recipe was deleted from the cookbook")
    else:
        print("That recipe does not exist in the cookbook")


def print_recipe(cookbook):
    print("Please enter the recipe's name to get its details:")
    recipe = input()
    if recipe in cookbook.keys():
        print(f'\nRecipe for {recipe}:')
        print(f'Ingredients list: {cookbook[recipe]["ingredients"]}')
        print(f'To be eaten for {cookbook[recipe]["meal"]}.')
        print(f'Takes {cookbook[recipe]["prep_time"]} minutes of cooking.')
    else:
        print("That recipe does not exist in the cookbook")


def print_all_recipes(cookbook):
    if len(cookbook.keys()) == 0:
        print("\nThe cookbook list is empty")
        return
    for k, v in cookbook.items():
        print(f'\nRecipe for {k}:')
        print(f'Ingredients list: {v["ingredients"]}')
        print(f'To be eaten for {v["meal"]}.')
        print(f'Takes {v["prep_time"]} minutes of cooking.')


def main():
    cookbook = {
        'sandwich': {
            'ingredients': ['ham', 'bread', 'cheese', 'tomatoes'],
            'meal': 'lunch',
            'prep_time': 10,
        },
        'cake': {
            'ingredients': ['flour', 'sugar', 'eggs'],
            'meal': 'dessert',
            'prep_time': 60,
        },
        'salad': {
            'ingredients': ['avocado', 'arugula', 'tomatoes', 'spinach'],
            'meal': 'lunch',
            'prep_time': 15,
        },
    }
    option = 1
    while option != 5:
        print_menu()
        option = input()
        if not option.isnumeric() or not (1 <= int(option) <= 5):
            print("This option does not exist, please type the corresponding number")
            print("To exit, enter 5")
        else:
            option = int(option)
            if option == 1:
                add_recipe(cookbook)
            elif option == 2:
                delete_recipe(cookbook)
            elif option == 3:
                print_recipe(cookbook)
            elif option == 4:
                print_all_recipes(cookbook)
    print("Cookbook closed.")


if __name__ == '__main__':
    main()
