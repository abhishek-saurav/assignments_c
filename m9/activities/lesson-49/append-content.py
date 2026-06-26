file = open("bucket-list.txt", "a")
file.write("4. Travel to Japan\n")
file.write("5. Run a 5K marathon\n")
file.close()
print("2 more items added!")

file = open("bucket-list.txt", "r")
print(file.read())
file.close()
