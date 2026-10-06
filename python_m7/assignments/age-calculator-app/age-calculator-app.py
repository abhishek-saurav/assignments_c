from tkinter import *
from datetime import date

root = Tk()
root.title("Age Calculator App")
root.geometry("350x250")

frame = Frame(master=root, relief=SUNKEN, borderwidth=2, bg="#d0efff")
frame.grid(row=0, column=0, padx=20, pady=20)

name_lbl = Label(frame, text="Name", bg="#d0efff")
name_entry = Entry(frame)
year_lbl = Label(frame, text="Year of birth", bg="#d0efff")
year_entry = Entry(frame)

name_lbl.grid(row=0, column=0, padx=5, pady=5)
name_entry.grid(row=0, column=1, padx=5, pady=5)
year_lbl.grid(row=1, column=0, padx=5, pady=5)
year_entry.grid(row=1, column=1, padx=5, pady=5)


def calculate():
    name = name_entry.get()
    year = int(year_entry.get())
    age = date.today().year - year
    result.delete(1.0, END)
    result.insert(END, name + ", you are " + str(age) + " years old.")


btn = Button(root, text="Calculate Age", command=calculate)
result = Text(root, height=2, width=35)

btn.place(x=120, y=130)
result.place(x=20, y=180)

root.mainloop()
