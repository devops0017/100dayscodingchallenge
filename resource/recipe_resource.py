from flask import request
from flask_restful import Resource
from http import HTTPStatus

from models.recipe import Recipe,recipes

class RecipeListResource(Resource):

    def get(self):
        if recipes:
            data = [recipe.data for recipe in recipes if recipe.is_publish is True]
            return {'data' : data}, HTTPStatus.OK
        return {'message': 'Recipe database is empty'}, HTTPStatus.NOT_FOUND

    def post(self):
        data = request.get_json()

        recipe = Recipe(name=data['name'],
                        description=data['description'],
                        num_of_servings=data['num_of_servings'],
                        cook_time=data['cook_time'],
                        directions=data['directions'])

        recipes.append(recipe)
        return recipe.data, HTTPStatus.CREATED

class RecipeResource(Resource):

    def put(self, recipe_id):
        data = request.get_json()

        for recipe in recipes:
            if recipe_id == recipe['id']:
                recipe.name = data['name'],
                recipe.description = data['description'],
                recipe.num_of_servings=data['num_of_servings'],
                recipe.cook_time=data['cook_time'],
                recipe.directions=data['directions']

                return recipe.data, HTTPStatus.CREATED
        return {'message': 'recipe not found'}, HTTPStatus.NOT_FOUND

    def get(self,recipe_id):
        for recipe in recipes:
            if recipe_id == recipe.id and recipe.is_publish is True:
                return recipe.data, HTTPStatus.OK
        return {'message': 'recipe not found'}, HTTPStatus.NOT_FOUND

class RecipePublishResource(Resource):

    def put(self,recipe_id):
        for recipe in recipes:
            if recipe_id == recipe.id:
                recipe.is_publish =True
                return recipe.data, HTTPStatus.OK
        return {}, HTTPStatus.NO_CONTENT




