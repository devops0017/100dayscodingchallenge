from flask import Flask, jsonify, request
from http import HTTPStatus

app = Flask(__name__)

recipes = [
    {
        'id': 1,
        'name': 'Egg Salad',
        'description': 'This is a lovely egg salad recipe.'
    },
    {
        'id': 2,
        'name': 'Tomato Pasta',
        'description': 'This is a lovely tomato pasta recipe.'
    }
]

@app.route("/")
def hello():
    return 'Recipe book'

@app.route('/recipes', methods=['GET'])
def get_recipe():
    return jsonify({'data':recipes})

@app.route('/recipes', methods=['POST'])
def create_recipe():
    data = request.get_json()
    name = data.get('name')
    description = data.get('description')

    recipe = {
        'id' : len(recipes) + 1 ,
        'name' : name ,
        'description' :  description
    }

    recipes.append(recipe)

    return jsonify({'data':recipe}) , HTTPStatus.CREATED


@app.route('/recipes/<int:recipe_id>', methods=['GET'])
def get_specific_recipe(recipe_id):
    for recipe in recipes:
        if recipe_id == recipe['id']:
            return jsonify(recipe)
    return jsonify({'message': 'recipe not found'}), HTTPStatus.NOT_FOUND


if __name__ == '__main__':
    app.run()