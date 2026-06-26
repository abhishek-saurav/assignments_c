fruits = ["apple", "mango", "banana", "grapes"]

fruits.append("orange")   # Add to end
# ['apple', 'mango', 'banana', 'grapes', 'orange']

fruits.remove("mango")    # Remove by value
# ['apple', 'banana', 'grapes', 'orange']

fruits.pop(1)             # Remove by index  (removes 'banana')
# ['apple', 'grapes', 'orange']

fruits.sort()             # Sort alphabetically
# ['apple', 'grapes', 'orange']

fruits.reverse()          # Reverse the order
# ['orange', 'grapes', 'apple']

fruits.clear()            # Remove all items
# []
