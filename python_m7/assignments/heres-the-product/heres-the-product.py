from tkinter import *

root = Tk()
root.title("Here's the product")
root.geometry("400x420")

heading = Label(text="Here's the Product", fg="white", bg="#072F5F", height=1, width=300)

name_lbl = Label(text="Product name")
name_entry = Entry()

price_lbl = Label(text="Price per item")
price_entry = Entry()

qty_lbl = Label(text="Quantity")
qty_entry = Entry()


def display():
    name = name_entry.get()
    price = float(price_entry.get())
    quantity = int(qty_entry.get())
    total = price * quantity
    text_box.delete(1.0, END)
    text_box.insert(END, "Product: " + name + "\n")
    text_box.insert(END, "Price: " + str(price) + "\n")
    text_box.insert(END, "Quantity: " + str(quantity) + "\n")
    text_box.insert(END, "Total: " + str(total))


btn = Button(text="Show Product", command=display, bg="#1261A0", fg="white")
text_box = Text(height=5)

heading.pack()
name_lbl.pack()
name_entry.pack()
price_lbl.pack()
price_entry.pack()
qty_lbl.pack()
qty_entry.pack()
btn.pack(pady=10)
text_box.pack()

root.mainloop()
