import sys
import signal

cookbook ={'sandwich' : {}, 'cake' : {}, 'salad' : {}}

def handler(signum, frame):
    if signum == signal.SIGINT:
        print('Cookbook closed. Goodbye !')
    exit(0)

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

def print_one_recipe():
    recipe = input('Insert recipe name: ')
    if recipe in cookbook:
        print("Recipe", recipe)
        data = cookbook[recipe]
        print("Ingredient:", data['ingredients'])
        print("Mealt type:", data['meal'])
        print("Time:", data['prep_time'])
        print()
    else:
        print('Recipe not found !')
        

def del_one_recipe():
    recipe = input('Del a recipe: ')
    if recipe in cookbook:
        del cookbook[recipe]
        print(recipe, "Delete");
    else:
        print('Recipe not found !')

def main_loop():
    select = 0
    while select != 5:
        print('Welcome to the Python Cookbook !')
        print('List of available option:')
        print('\t1: Add a recipe')
        print('\t2: Delete a recipe')
        print('\t3: Print a recipe')
        print('\t4: Print the cookbook')
        print('\t5: Quit')
        print()
        print('Please select an option:')
        select = input()
        if select == '':
            select = 0
        
        select = int(select)
        if select == 1:
            print()
            add_recipe()
            print()
        elif select == 2:
            print()
            del_one_recipe()
            print()
        elif select == 3:
            print()
            print_one_recipe()
            print()
        elif select == 4:
            print()
            print_all_recipes()
            print()
        elif select == 5:
            print()
            print('Cookbook closed. Goodbye !')
            print()
            exit(0)
        else:
            print()
            print('Sorry, this option does not exist.')
            print()


def add_recipe():
    print("New recipe")
    recipe_name = input("Recipe name: ")
    if len(recipe_name) == 0:
        print("Error: Empty name")
        return
    recipe = {'ingredients': [], 'meal': '', 'prep_time': 0}
    print("Add ingredient: (type 'End' to end)")
    for line in sys.stdin:
        if 'End' == line.rstrip() or line.rstrip() == '':
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
    if not recipe['prep_time'].isdigit():
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
    signal.signal(signal.SIGINT, handler)
    try:
        main_loop()
    except:
        pass
