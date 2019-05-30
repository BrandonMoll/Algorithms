#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  max_quantity = 0
  for ing in recipe:
    if len(recipe) > len(ingredients):
      break
    if ingredients[ing]/recipe[ing] < 1:
      max_quantity = 0
      break
    elif math.floor(ingredients[ing]/recipe[ing]) >= 1 and max_quantity == 0:
      max_quantity = math.floor(ingredients[ing]/recipe[ing])
    elif math.floor(ingredients[ing]/recipe[ing]) >= 1 and math.floor(ingredients[ing]/recipe[ing]) < max_quantity:
      max_quantity = math.floor(ingredients[ing]/recipe[ing])
    
  return max_quantity


# if __name__ == '__main__':
#   # Change the entries of these dictionaries to test 
#   # your implementation with different inputs
#   recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
#   ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
#   print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))

recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
ingredients = { 'milk': 201, 'butter': 101, 'flour': 51 }

print(recipe_batches(recipe, ingredients))