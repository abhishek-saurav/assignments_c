from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Length Converter App")
root.geometry("350x300")

lbl = Label(root, text="Enter length in meters")
entry = Entry(root)
result = Label(root, text="", justify=LEFT)


def convert(event=None):
    try:
        meters = float(entry.get())
        centimeters = meters * 100
        kilometers = meters / 1000
        feet = meters * 3.28084
        inches = meters * 39.3701
        result.config(
            text="Centimeters: " + str(centimeters) + "\n"
            + "Kilometers: " + str(kilometers) + "\n"
            + "Feet: " + str(feet) + "\n"
            + "Inches: " + str(inches)
        )
    except ValueError:
        messagebox.showwarning("Alert", "Please enter a valid number.")


btn = Button(root, text="Convert", command=convert)
root.bind("<Return>", convert)

lbl.pack(pady=10)
entry.pack()
btn.pack(pady=10)
result.pack()

root.mainloop()
