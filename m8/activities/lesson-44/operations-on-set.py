pasta_ingredients = {"tomato", "garlic", "olive oil", "chilli", "pasta", "garlic"}
print(pasta_ingredients)        # garlic appears only once
print(len(pasta_ingredients))   # 5, not 6

pasta_ingredients.add("parmesan")
pasta_ingredients.discard("chilli")
print(pasta_ingredients)
# {'olive oil', 'parmesan', 'tomato', 'garlic', 'pasta'}
