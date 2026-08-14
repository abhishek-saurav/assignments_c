name = input("Enter your name: ")
book = input("Enter your favourite book: ")

age = 31
fine_amount = 12.5
books_issued = 4
is_member = True

print("Name:", name, "-> type:", type(name))
print("Book:", book, "-> type:", type(book))
print("Age:", age, "-> type:", type(age))
print("Fine Amount:", fine_amount, "-> type:", type(fine_amount))
print("Books Issued:", books_issued, "-> type:", type(books_issued))
print("Is Member:", is_member, "-> type:", type(is_member))

age_text = str(age)
fine_text = str(fine_amount)
books_text = str(books_issued)
member_text = str(is_member)

print("Age as text:", age_text, "-> type:", type(age_text))
print("Fine as text:", fine_text, "-> type:", type(fine_text))
print("Books as text:", books_text, "-> type:", type(books_text))
print("Member as text:", member_text, "-> type:", type(member_text))

first_two = name[0:2]
last_two = book[-2:]
card_code = first_two + last_two
print("First 2 letters of name:", first_two)
print("Last 2 letters of book:", last_two)
print("Card Code:", card_code)

reversed_name = name[::-1]
print("Reversed Name:", reversed_name)

card_line_1 = "CARD HOLDER: " + name.upper()
card_line_2 = "SCHOOL: St. Alberts | AGE: " + age_text
card_line_3 = "BOOKS ISSUED: " + books_text + " | FINE: Rs. " + fine_text
card_line_4 = "MEMBER ACTIVE: " + member_text
card_line_5 = "CARD CODE: " + card_code.upper()

print("")
print("===== STUDENT LIBRARY CARD =====")
print(card_line_1)
print(card_line_2)
print(card_line_3)
print(card_line_4)
print(card_line_5)
print("================================")
