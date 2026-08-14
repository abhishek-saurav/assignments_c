amount = int(input("Enter the amount in rupees: "))

notes500 = amount // 500
amount = amount % 500

notes100 = amount // 100
amount = amount % 100

notes50 = amount // 50
amount = amount % 50

notes10 = amount // 10
amount = amount % 10

print("500 rupee notes:", notes500)
print("100 rupee notes:", notes100)
print("50 rupee notes :", notes50)
print("10 rupee notes :", notes10)
print("Amount left    :", amount)
