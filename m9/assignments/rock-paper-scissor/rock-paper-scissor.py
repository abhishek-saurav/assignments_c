import random

choices = ["rock", "paper", "scissor"]

player = input("Enter your choice (rock/paper/scissor): ").lower()
computer = random.choice(choices)

print(f"Computer chose: {computer}")

if player == computer:
    print("It's a tie!")
elif (player == "rock" and computer == "scissor") or \
     (player == "paper" and computer == "rock") or \
     (player == "scissor" and computer == "paper"):
    print("You win!")
else:
    print("Computer wins!")
