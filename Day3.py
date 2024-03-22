#Part 1
import re

original_recipes: set = set()
wanted_recipes: set = set()
wanted_recipes_buffer: set = set()
ingredients: set = set()

find_recipe = re.compile(r'(.+) =')
find_ingredients = re.compile(r'(?:\=|\+) ([^\n+]+)')

with open("Day3Input.txt", "r", encoding = "utf-8") as f:
  recipe = f.readline()[8:-1].split(', ')[0]
  original_recipes.add(recipe)
  wanted_recipes.add(recipe)

# While we still have any wanted_recipes
while len(wanted_recipes) >= 1:
  # Iterate through all wanted_recipes
  for wanted_recipe in wanted_recipes:
    # For each wanted_recipe, iterate through each line of the input
    with open("Day3Input.txt", "r", encoding = "utf-8") as f:
      for line in f.readlines():
        recipe = re.findall(find_recipe, line)
        # If recipe is empty, continue to the next line
        if not recipe:
          continue
        # If the current recipe is a wanted_recipe
        if recipe[0] in wanted_recipes:
          # Read the rest of the line to find all ingredients used
          ingredients_used = map(str.strip,re.findall(find_ingredients, line))
          # For each ingredient on the line
          for ingredient in ingredients_used:
            # Add the ingredient as a wanted recipe and to the ingredient list
            if ingredient not in ingredients:
              wanted_recipes_buffer.add(ingredient)
              ingredients.add(ingredient)
  # After iterating through the entire wanted_recipes, move the ones in the buffer into this main one
  wanted_recipes.clear()
  for recipe in wanted_recipes_buffer:
    wanted_recipes.add(recipe)
  wanted_recipes_buffer.clear()

print(original_recipes)
print(ingredients)
print(len(ingredients))

print("Part 2")

# Part 2

original_recipes: set = set()
wanted_recipes: set = set()
wanted_recipes_buffer: set = set()
ingredients: set = set()

with open("Day3Input.txt", "r", encoding = "utf-8") as f:
  recipes = f.readline()[8:-1].split(', ')
  for recipe in recipes:
    original_recipes.add(recipe)
    wanted_recipes.add(recipe)

# While we still have any wanted_recipes
while len(wanted_recipes) >= 1:
  # Iterate through all wanted_recipes
  for wanted_recipe in wanted_recipes:
    # For each wanted_recipe, iterate through each line of the input
    with open("Day3Input.txt", "r", encoding = "utf-8") as f:
      for line in f.readlines():
        recipe = re.findall(find_recipe, line)
        # If recipe is empty, continue to the next line
        if not recipe:
          continue
        # If the current recipe is a wanted_recipe
        if recipe[0] in wanted_recipes:
          # PART 2 DIFFERENCE: remove the current recipe if it is present
          ingredients.discard(recipe[0])
          # Read the rest of the line to find all ingredients used
          ingredients_used = map(str.strip,re.findall(find_ingredients, line))
          # For each ingredient on the line
          for ingredient in ingredients_used:
            # Add the ingredient as a wanted recipe and to the ingredient list
            if ingredient not in ingredients:
              wanted_recipes_buffer.add(ingredient)
              ingredients.add(ingredient)
  # After iterating through the entire wanted_recipes, move the ones in the buffer into this main one
  wanted_recipes.clear()
  for recipe in wanted_recipes_buffer:
    wanted_recipes.add(recipe)
  wanted_recipes_buffer.clear()

print(original_recipes)
print(ingredients)
print(len(ingredients))
