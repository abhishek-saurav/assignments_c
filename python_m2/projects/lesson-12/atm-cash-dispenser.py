denominations = [500, 200, 100, 50, 20, 10]

count_500 = 0
count_200 = 0
count_100 = 0
count_50 = 0
count_20 = 0
count_10 = 0
customers_served = 0
total_dispensed = 0

serving = True
while serving:
    name = input("Enter customer name: ")
    amount = int(input("Enter withdrawal amount: "))

    if amount <= 0 or amount % 10 != 0:
        print("Invalid amount.")
        continue

    remaining = amount
    idx = 1
    while idx <= 6:
        value = denominations[idx - 1]
        notes = remaining // value
        remaining = remaining % value
        if idx == 1:
            count_500 += notes
        elif idx == 2:
            count_200 += notes
        elif idx == 3:
            count_100 += notes
        elif idx == 4:
            count_50 += notes
        elif idx == 5:
            count_20 += notes
        else:
            count_10 += notes
        idx += 1

    total_dispensed += amount
    customers_served += 1
    print("Dispensed", amount, "to", name)

    next_customer = input("Is there a next customer? (yes/no): ")
    if next_customer != "yes":
        serving = False

counts = [count_500, count_200, count_100, count_50, count_20, count_10]

print("")
print("===== DAILY DENOMINATION REPORT =====")
for slot in range(1, 7):
    total = counts[slot - 1]
    print(denominations[slot - 1], "note x", total, ":", end=" ")
    for note in range(total):
        print("=", end="")
    print()

print("Customers served:", customers_served)
print("Total dispensed:", total_dispensed)
print("=======================================")
