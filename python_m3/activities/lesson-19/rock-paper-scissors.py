import random

while True:
    player = input("Choose rock, paper, or scissors: ")
    number = random.randint(1, 3)
    if number == 1:
        computer = "rock"
    elif number == 2:
        computer = "paper"
    else:
        computer = "scissors"
    print(f"You chose {player}, the computer chose {computer}")
    if player == computer:
        print("It's a tie")
    elif player == "rock" and computer == "scissors":
        print("You win")
    elif player == "paper" and computer == "rock":
        print("You win")
    elif player == "scissors" and computer == "paper":
        print("You win")
    else:
        print("You lose")
    again = input("Play again? (y/n): ")
    if again != "y":
        break
