week1 = 250
week2 = 180
week3 = 320
week4 = 210

total = week1 + week2 + week3 + week4
average = total / 4
print("Total pocket money :", total)
print("Average per week   :", average)

days = 28
spend_per_day = total / days
print("Spending per day   :", spend_per_day)

cost_per_book = 75
books = total // cost_per_book
leftover = total % cost_per_book
print("Books affordable   :", books)
print("Money left over    :", leftover)

last_month = 900
print("More than last month?  :", total > last_month)
print("Less than last month?  :", total < last_month)
print("Same as last month?    :", total == last_month)
print("At least as much?      :", total >= last_month)

total += 150
print("After birthday gift:", total)

total -= 90
print("After bus pass     :", total)

books = total // cost_per_book
leftover = total % cost_per_book
print("Final books affordable :", books)
print("Final money left over  :", leftover)
