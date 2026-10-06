import random
import tkinter as tk
from tkinter import ttk, messagebox

root = tk.Tk()
root.title("Rock Paper Scissor App")
root.geometry("350x250")

choices = ["Rock", "Paper", "Scissor"]
player_score = 0
computer_score = 0

frame = ttk.Frame(root)
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

heading = ttk.Label(frame, text="Rock Paper Scissor", font=("Arial", 16, "bold"))
heading.grid(row=0, columnspan=2, pady=10)

choice_var = tk.StringVar()
choice_lbl = ttk.Label(frame, text="Your choice:")
dropdown = ttk.Combobox(
    frame,
    textvariable=choice_var,
    state="readonly",
    values=("Rock", "Paper", "Scissor")
)
dropdown.current(0)
score_lbl = ttk.Label(frame, text="You 0 - 0 Computer")


def play():
    global player_score, computer_score
    player = choice_var.get()
    computer = random.choice(choices)

    for i, name in enumerate(choices):
        if name == player:
            player_index = i
        if name == computer:
            computer_index = i

    if player_index == computer_index:
        outcome = "It's a tie!"
    elif (player_index - computer_index) % 3 == 1:
        outcome = "You win!"
        player_score += 1
    else:
        outcome = "Computer wins!"
        computer_score += 1

    score_lbl.config(text=f"You {player_score} - {computer_score} Computer")
    messagebox.showinfo(
        "Result",
        f"You chose {player}\nComputer chose {computer}\n\n{outcome}"
    )


play_btn = ttk.Button(frame, text="Play", command=play)

choice_lbl.grid(row=1, column=0, padx=5, pady=5)
dropdown.grid(row=1, column=1, padx=5, pady=5)
play_btn.grid(row=2, columnspan=2, pady=10)
score_lbl.grid(row=3, columnspan=2)

root.mainloop()
