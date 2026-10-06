from tkinter import *

root = Tk()
root.title('Login App')
root.geometry('400x400')

frame = Frame(master=root, height=200, width=360, bg='#d0efff')

lbl1 = Label(frame, text='Full Name', bg='#d0efff')
lbl2 = Label(frame, text='Email Id', bg='#d0efff')
lbl3 = Label(frame, text='Enter Password', bg='#d0efff')

name_entry = Entry(frame)
email_entry = Entry(frame)
pass_entry = Entry(frame, show="*")


def display():
    name = name_entry.get()
    greet = "Hey " + name + ", your account has been created!"
    textbox.insert(END, greet)


textbox = Text(root, height=3, width=40)
btn = Button(root, text="Create Account", command=display)

frame.place(x=20, y=20)
lbl1.place(x=20, y=20)
name_entry.place(x=150, y=20)
lbl2.place(x=20, y=80)
email_entry.place(x=150, y=80)
lbl3.place(x=20, y=140)
pass_entry.place(x=150, y=140)
btn.place(x=140, y=240)
textbox.place(x=20, y=290)

root.mainloop()
