
recipes = []


def get_recipe_id():
    if recipes:
        last_recipe_id = recipes[-1]
        return last_recipe_id + 1
    return 1

class Recipe:

    def __init__(self, name, description, num_of_servings, cook_time, directions):
        self.id = get_recipe_id()
        self.name = name
        self.description = description
        self.num_of_servings = num_of_servings
        self.cook_time = cook_time
        self.directions = directions
        self.is_publish = False

    @property
    def data(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'num_of_servings': self.num_of_servings,
            'cook_time': self.cook_time,
            'directions': self.directions
        }