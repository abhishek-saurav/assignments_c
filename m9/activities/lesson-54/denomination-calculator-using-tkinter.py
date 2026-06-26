from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

root = Tk()
root.title("Denomination Counter")
root.configure(bg="light blue")
root.geometry("650x400")

upload = Image.open("app_img.jpg")
upload = upload.resize((300, 300))
image = ImageTk.PhotoImage(upload)
label = Label(root, image=image, bg="light blue")
label.place(x=180, y=20)

label1 = Label(root,
    text="Hey User! Welcome to Denomination Counter Application.",
    bg="light blue")
label1.place(relx=0.5, y=340, anchor=CENTER)

def topwin():
    top = Toplevel(root)
    top.title("Denomination Counter")
    top.geometry("400x350")
    top.configure(bg="light blue")

    Label(top, text="Enter Amount:", font=("Arial", 12), bg="light blue").place(x=50, y=40)
    amount_entry = Entry(top, font=("Arial", 12), width=15)
    amount_entry.place(x=180, y=40)

    result_label = Label(top, text="", font=("Arial", 11), bg="light blue", justify=LEFT)
    result_label.place(x=50, y=110)

    def calculate():
        amount = int(amount_entry.get())
        denominations = [500, 200, 100, 50, 20, 10, 5, 2, 1]
        result = ""
        for d in denominations:
            count = amount // d
            amount = amount % d
            if count > 0:
                result += f"{d} x {count}\n"
        result_label.config(text=result)

    Button(top, text="Calculate", font=("Arial", 12), command=calculate).place(x=180, y=75)

def msg():
    MsgBox = messagebox.showinfo(
        "Alert", "Do you want to calculate the denomination count?")
    if MsgBox == "ok":
        topwin()

button1 = Button(root, text="Start", font=("Arial", 12), command=msg)
button1.place(relx=0.5, y=375, anchor=CENTER)

root.mainloop()
