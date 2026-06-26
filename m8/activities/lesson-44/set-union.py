pasta_ingredients = {"tomato", "garlic", "olive oil", "chilli", "pasta"}
biryani_ingredients = {"garlic", "tomato", "onion", "chicken", "rice", "spices"}

all_ingredients = pasta_ingredients.union(biryani_ingredients)
common = pasta_ingredients.intersection(biryani_ingredients)
print("All ingredients:", all_ingredients)
print("Common:", common)  # {'garlic', 'tomato'}
