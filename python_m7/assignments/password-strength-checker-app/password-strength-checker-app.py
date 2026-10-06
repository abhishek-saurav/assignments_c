from tkinter import *

root = Tk()
root.title("Password Strength Checker App")
root.geometry("350x200")

lbl = Label(root, text="Enter a password")
entry = Entry(root, show="*")


def check():
    password = entry.get()
    score = 0
    has_digit = False
    has_upper = False
    has_lower = False
    has_symbol = False

    for ch in password:
        if ch.isdigit():
            has_digit = True
        elif ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch in "!@#$%^&*":
            has_symbol = True

    if len(password) >= 8:
        score += 1
    if has_digit:
        score += 1
    if has_upper:
        score += 1
    if has_lower:
        score += 1
    if has_symbol:
        score += 1

    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Medium"
    else:
        strength = "Strong"

    top = Toplevel()
    top.geometry("220x100")
    top.title("Result")
    result = Label(top, text="Password strength: " + strength)
    result.pack(pady=30)


btn = Button(root, text="Check Strength", command=check)

lbl.pack(pady=15)
entry.pack()
btn.pack(pady=15)

root.mainloop()
