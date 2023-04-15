class Recipe_Exception(Exception):
    def __init__(self, msg):
        print(msg)
        exit(1)


class Recipe:
    __recipe_list = ["starter", "lunch", "dessert"]
    name = ""
    cooking_lvl = 0
    cooking_time = 0
    ingredients = []
    description = ""
    recipe_type = ""

    def __init__(self, p_name: str, p_cooking_lvl: int, p_cooking_time: int,
                 p_ingredients: list[str], p_description:
                 str, p_recipe_type: str):

        def parser_new_recipe():
            if len(p_name) == 0:
                raise Recipe_Exception("Name can not empty")
            if not isinstance(p_name, str):
                raise Recipe_Exception("Name must be a str")
            if p_cooking_lvl not in range(1, 5):
                raise Recipe_Exception("cooking leve not in range 1 - 5")
            if not isinstance(p_cooking_time, int):
                raise Recipe_Exception("Cooking time must be a int")
            if p_cooking_time <= 0:
                raise Recipe_Exception("Cooking time must be positive")
            if len(p_ingredients) == 0:
                raise Recipe_Exception("must be one or more ingredients")
            if not isinstance(p_ingredients, list):
                raise Recipe_Exception("ingredients must be a list")
            for i in p_ingredients:
                if not isinstance(i, str):
                    raise Recipe_Exception("Ingredient must be a str")
            if p_recipe_type not in self.__recipe_list:
                raise Recipe_Exception("the type is starter, lunch or dessert")

        parser_new_recipe()
        self.name = p_name
        self.cooking_lvl = p_cooking_lvl
        self.cooking_time = p_cooking_time
        self.ingredients = p_ingredients
        self.description = p_description
        self.recipe_type = p_recipe_type

    def __str__(self):
        res = str(self.name + "\n" + "level " + str(self.cooking_lvl) + "\n" +
                  "time " + str(self.cooking_time) + "\n" + "ingredients " +
                  str(self.ingredients) + "\n" + "description " +
                  self.description + "\n" + "type " + self.recipe_type)
        return (res)

    def get_name(self) -> str:
        return self.name

    def get_type(self) -> str:
        return self.recipe_type
