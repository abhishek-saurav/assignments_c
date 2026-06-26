from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Virus Scanner")
root.geometry("400x200")
root.configure(bg="white")

label = Label(root, text="System Status: Scanning...", font=("Arial", 14), bg="white")
label.pack(pady=30)

def check_virus():
    messagebox.showwarning("Alert!", "Virus Detected! Please take action.")

button = Button(root, text="Scan System", font=("Arial", 12), command=check_virus)
button.pack(pady=10)

root.mainloop()
