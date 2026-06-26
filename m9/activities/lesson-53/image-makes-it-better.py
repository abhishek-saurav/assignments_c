from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Image Display")
root.geometry("400x400")
root.configure(bg="white")

upload = Image.open("app_img.jpg")
upload = upload.resize((300, 300))
image = ImageTk.PhotoImage(upload)

label = Label(root, image=image, bg="white")
label.place(x=50, y=30)

root.mainloop()
