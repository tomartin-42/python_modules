import sys

cookbook ={'sandwich' : {}, 'cake' : {}, 'salad' : {}}

def init_sandwich():
    cookbook['sandwich'] = {'ingredients': ['ham', 'bread', 'cheese', 'tomatoes'],
                            'meal': 'lunch',
                             'prep_time': 10}

def init_cake():
    cookbook['cake'] = {'ingredients': ['flour', 'sugar', 'eggs'],
                        'meal': 'dessert',
                         'prep_time': 60}

def init_salad():
    cookbook['salad'] = {'ingredients': ['avocado', 'arugula', 'tomatoes', 'spinach'],
                         'meal': 'lunch',
                          'prep_time': 15}

def print_recipes():
    print("All recipes")
    for r in cookbook:
        print(r)

def print_one_recipe(recipe):
    print("Recipe", recipe)
    data = cookbook[recipe]
    print("Ingredient:", data['ingredients'])
    print("Mealt type:", data['meal'])
    print("Time:", data['prep_time'])
    print()

def dell_one_recipe(recipe):
    if recipe in cookbook:
        del cookbook[recipe]
        print(recipe, "Delete");

def add_recipe():
    print("New recipe")
    recipe_name = input("Recipe name: ")
    if len(recipe_name) == 0:
        print("Error: Empty name")
        return
    recipe = {'ingredients': [], 'meal': '', 'prep_time': 0}
    print("Add ingredient: (type 'End' to end)")
    for line in sys.stdin:
        if 'End' == line.rstrip():
            break
        else:
            recipe['ingredients'].append(line.rstrip())
    if recipe['ingredients'] == []:
        print("Error: Empty ingredient")
        return
    recipe['meal'] = input('Mealt type: ')
    if len(recipe['meal']) == 0:
        print("Error: Empty meal type")
        return
    recipe['prep_time'] = input('Time: ')
    if isinstance(recipe['prep_time'], int):
        print("Error: Time must be an integer")
        return
    if int(recipe['prep_time']) < 0:
        print("Error: Time must be positive")
        return
    cookbook[recipe_name] = recipe 

def print_all_recipes():
    for r in cookbook:
        print(r)

if __name__ == '__main__':
    init_sandwich()
    init_cake()
    init_salad()
    print_recipes()

    add_recipe()
    for r in cookbook:
        print_one_recipe(r)
