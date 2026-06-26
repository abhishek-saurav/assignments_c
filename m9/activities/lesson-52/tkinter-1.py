from tkinter import *

root = Tk()
root.title("My First Tkinter Window")
root.geometry("400x300")

label = Label(root, text="Hello, Tkinter!", font=("Arial", 20))
label.pack(pady=50)

root.mainloop()
