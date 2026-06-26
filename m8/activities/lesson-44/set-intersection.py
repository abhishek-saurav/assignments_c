pasta_ingredients = {"tomato", "garlic", "olive oil", "chilli", "pasta"}
biryani_ingredients = {"garlic", "tomato", "onion", "chicken", "rice", "spices"}

only_pasta = pasta_ingredients.difference(biryani_ingredients)
unique_to_each = pasta_ingredients.symmetric_difference(biryani_ingredients)
print("Only in Pasta:", only_pasta)
# {'olive oil', 'chilli', 'pasta'}
print("Not shared:", unique_to_each)
# {'olive oil', 'spices', 'onion', 'chicken', 'chilli', 'pasta', 'rice'}
