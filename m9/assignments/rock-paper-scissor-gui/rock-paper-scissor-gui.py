from tkinter import *
import random

choices = ["rock", "paper", "scissor"]

root = Tk()
root.title("Rock Paper Scissor")
root.geometry("400x350")
root.configure(bg="light yellow")

Label(root, text="Rock Paper Scissor", font=("Arial", 18, "bold"), bg="light yellow").pack(pady=15)

result_label = Label(root, text="Make your choice!", font=("Arial", 13), bg="light yellow")
result_label.pack(pady=10)

computer_label = Label(root, text="", font=("Arial", 12), bg="light yellow")
computer_label.pack()

def play(player):
    computer = random.choice(choices)
    computer_label.config(text=f"Computer chose: {computer}")
    if player == computer:
        result_label.config(text="It's a tie!", fg="blue")
    elif (player == "rock" and computer == "scissor") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissor" and computer == "paper"):
        result_label.config(text="You win!", fg="green")
    else:
        result_label.config(text="Computer wins!", fg="red")

def play_rock():
    play("rock")

def play_paper():
    play("paper")

def play_scissor():
    play("scissor")

Button(root, text="Rock", font=("Arial", 12), width=10, command=play_rock).pack(pady=5)
Button(root, text="Paper", font=("Arial", 12), width=10, command=play_paper).pack(pady=5)
Button(root, text="Scissor", font=("Arial", 12), width=10, command=play_scissor).pack(pady=5)

root.mainloop()
