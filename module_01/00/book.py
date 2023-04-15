from datetime import datetime
from copy import deepcopy
from recipe import Recipe


class Book_exception(Exception):
    def __init__(self, msg):
        print(msg)
        exit(1)


class Book:
    last_update = datetime
    creation_date = datetime
    recipes_list = {'starter': [], 'lunch': [], 'dessert': []}

    def __init__(self):
        self.last_update = self.creation_date = datetime.today()

    def get_recipe_by_name(self, name):
        """
        Prints a recipe with the name \texttt{name} and returns the instance
        """
        for ty in self.recipes_list:
            for re in self.recipes_list[ty]:
                if re.get_name() == name:
                    print(self.creation_date)
                    print(self.last_update)
                    print(str(re))

    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        for r in self.recipes_list[recipe_type]:
            print("----------------------------------")
            print(str(r))
            print("----------------------------------")

    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        if not isinstance(recipe, Recipe):
            raise Book_exception("Recipe is not a Recipe obj.")
        self.recipes_list[recipe.get_type()].append(deepcopy(recipe))
        self.last_update = datetime.today()
