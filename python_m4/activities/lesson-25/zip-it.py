items = ["pencil", "eraser", "notebook", "sharpener"]
counts = [12, 7, 8, 5]

paired = list(zip(items, counts))
print("Paired:", paired)

inventory = {item: count for item, count in zip(items, counts)}
print("Inventory:", inventory)
