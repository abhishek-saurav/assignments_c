from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

root = Tk()
root.title("Denomination Calculator")
root.config(bg="#E3F2FD")
root.geometry("400x450")

img = Image.open("app_img.jpg")
img = img.resize((300, 300))
photo = ImageTk.PhotoImage(img)
img_lbl = Label(root, image=photo)
img_lbl.pack(pady=10)

welcome_lbl = Label(
    root,
    text="Welcome! Let's count your notes.",
    bg="#E3F2FD",
    font=("Arial", 12),
)
welcome_lbl.pack()


def msg():
    answer = messagebox.showinfo(
        "Denomination Calculator",
        "Do you want to calculate denominations?",
    )
    if answer == "ok":
        topwin()


btn = Button(root, text="Let's get started!", command=msg)
btn.place(x=140, y=400)


def topwin():
    top = Toplevel()
    top.title("Calculator")
    top.config(bg="#FFF3E0")
    top.geometry("350x350")

    lbl = Label(top, text="Enter total amount", bg="#FFF3E0")
    entry = Entry(top)

    heading = Label(top, text="Number of notes", bg="#FFF3E0")
    l1 = Label(top, text="2000 :", bg="#FFF3E0")
    l2 = Label(top, text="500 :", bg="#FFF3E0")
    l3 = Label(top, text="100 :", bg="#FFF3E0")
    t1 = Entry(top)
    t2 = Entry(top)
    t3 = Entry(top)

    def calculator():
        try:
            amount = int(entry.get())
            note2000 = amount // 2000
            amount %= 2000
            note500 = amount // 500
            amount %= 500
            note100 = amount // 100
            t1.delete(0, END)
            t2.delete(0, END)
            t3.delete(0, END)
            t1.insert(END, str(note2000))
            t2.insert(END, str(note500))
            t3.insert(END, str(note100))
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")

    calc_btn = Button(top, text="Calculate", command=calculator)

    lbl.place(x=40, y=30)
    entry.place(x=170, y=30)
    calc_btn.place(x=140, y=80)
    heading.place(x=120, y=130)
    l1.place(x=60, y=180)
    t1.place(x=140, y=180)
    l2.place(x=60, y=220)
    t2.place(x=140, y=220)
    l3.place(x=60, y=260)
    t3.place(x=140, y=260)

    top.mainloop()


root.mainloop()
