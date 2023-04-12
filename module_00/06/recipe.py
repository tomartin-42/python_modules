import sys

cookbook ={'sandwich' : [], 'cake' : [], 'salad' : []}

def init_sandwich():
    cookbook['sandwich'] = ['ham', 'bread', 'cheese', 'tomatoes', 'lunch', 10]

def init_cake():
    cookbook['cake'] = ['flour', 'sugar', 'eggs', 'dessert', 60]

def init_salad():
    cookbook['salad'] = ['avocado', 'arugula', 'tomatoes', 'spinach', 'lunch', 15]

def print_recipes():
    print("All recipes")
    for r in cookbook:
        print(r)

def print_one_recipe(recipe):
    print("Recipe", recipe)
    data = cookbook[recipe]
    print("Ingredient:", data[:-2])
    print("Mealt type:", data[len(data)- 2])
    print("Time:", data[len(data) - 1])

def dell_one_recipe(recipe):
    if recipe in cookbook:
        del cookbook[recipe]
        print(recipe, "Delete");

def add_recipe():
    print("New recipe")
    recipe = input("Recipe name: ")
    cookbook[recipe] = []
    print("Add ingredient: (type 'End' to end)")
    for line in sys.stdin:
        if 'End' == line.rstrip():
            break
        else:
            cookbook[recipe].append(line.rstrip())
    cookbook[recipe].append(input('Mealt type: '))
    cookbook[recipe].append(input('Time: '))

def print_all_recipes():
    for r in cookbook:
        print(r)

if __name__ == '__main__':
    init_sandwich()
    init_cake()
    init_salad()
    print_recipes()
    for r in cookbook:
        print_one_recipe(r)
    add_recipe()
