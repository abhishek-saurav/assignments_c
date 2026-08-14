cost_price = int(input("Enter the cost price: "))
selling_price = int(input("Enter the selling price: "))

if selling_price > cost_price:
    profit = selling_price - cost_price
    print("You made a profit")
    print("Profit is Rs.", profit)
else:
    loss = cost_price - selling_price
    print("You made a loss")
    print("Loss is Rs.", loss)
