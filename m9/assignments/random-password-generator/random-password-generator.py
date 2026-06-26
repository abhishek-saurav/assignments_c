from tkinter import *
import random
import string

root = Tk()
root.title("Random Password Generator")
root.geometry("400x300")
root.configure(bg="light gray")

Label(root, text="Password Generator", font=("Arial", 18, "bold"), bg="light gray").pack(pady=20)

Label(root, text="Password Length:", font=("Arial", 12), bg="light gray").pack()

length_entry = Entry(root, font=("Arial", 12), width=10)
length_entry.pack(pady=5)

result_label = Label(root, text="", font=("Arial", 12), bg="light gray", fg="blue")
result_label.pack(pady=10)

def generate_password():
    length = int(length_entry.get())
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ""
    for i in range(length):
        password += random.choice(characters)
    result_label.config(text=password)

Button(root, text="Generate", font=("Arial", 12), command=generate_password).pack(pady=10)

root.mainloop()
