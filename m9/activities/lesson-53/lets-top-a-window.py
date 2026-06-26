from tkinter import *

root = Tk()
root.title("Main Window")
root.geometry("400x250")

label = Label(root, text="This is the Main Window", font=("Arial", 14))
label.pack(pady=30)

def open_top():
    top = Toplevel(root)
    top.title("Top Window")
    top.geometry("300x200")
    top_label = Label(top, text="This is the Top Window!", font=("Arial", 12))
    top_label.pack(pady=40)

button = Button(root, text="Open Top Window", font=("Arial", 12), command=open_top)
button.pack(pady=10)

root.mainloop()
