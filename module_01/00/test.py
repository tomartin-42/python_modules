from book import Book
from recipe import Recipe

if __name__ == '__main__':
    b = Book()
    t = Recipe("hola", 4, 5, ['one'], "a", "lunch")
    u = Recipe("adios", 1, 1, ['uno', 'dos'], "dld", "starter")
    w = Recipe("hello", 2, 2, ['dos', 'tres'], "lll", "starter")
    b.add_recipe(t)
    b.add_recipe(u)
    b.add_recipe(w)
    b.get_recipe_by_name("hola")
    b.get_recipe_by_name("hello")
    b.get_recipes_by_types("starter")
    print(w.__dict__)
    print()
    print(str(w))
