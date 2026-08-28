def due_amount(total, paid):
    return total - paid

total = float(input("Enter the total amount: "))
paid = float(input("Enter the amount paid: "))
print("Amount still due:", due_amount(total, paid))
