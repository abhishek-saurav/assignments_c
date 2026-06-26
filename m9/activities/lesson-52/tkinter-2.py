from tkinter import *

root = Tk()
root.title("Tkinter Window with Button")
root.geometry("400x300")
root.configure(bg="light blue")

label = Label(root, text="Welcome to Tkinter!", font=("Arial", 16), bg="light blue")
label.pack(pady=30)

def on_click():
    label.config(text="Button Clicked!")

button = Button(root, text="Click Me", command=on_click, font=("Arial", 12))
button.pack(pady=10)

root.mainloop()
