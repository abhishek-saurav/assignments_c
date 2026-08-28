stock = {"pencil": 12, "eraser": 0, "notebook": 8}
item = "eraser"

print("Checking stock for", item)
if stock[item] == 0:
    print(item, "is out of stock! Stopping the program.")
    exit()

print(item, "is available:", stock[item])
