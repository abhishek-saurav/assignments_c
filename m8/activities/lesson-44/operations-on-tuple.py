pasta = ("Pasta Arrabiata", "Italian", 20, "Medium")
print(pasta)          # ('Pasta Arrabiata', 'Italian', 20, 'Medium')
print(pasta[0])       # Pasta Arrabiata
print(pasta[-1])      # Medium

biryani = ("Chicken Biryani", "Indian", 45, "Hard")

all_recipes = (pasta, biryani)       # nested tuple
print(all_recipes[0][0])              # Pasta Arrabiata
print(all_recipes[1][2])              # 45
print(pasta[1:3])                     # ('Italian', 20)

for detail in pasta:
    print(" -", detail)
