import random

while True:
    rps = ["ROCK", "PAPER", "SCISSORS"]
    computer_answer = random.choice(rps).lower()
    player_answer = (input("Rock paper or scissors?\n")).lower()

    if computer_answer == player_answer:
        print(f"You both answered {computer_answer}, tie.")

    elif computer_answer == "rock":
        if player_answer == "scissors":
            print("Rock beats scissors! You lost :(")
        else:
            print("Paper beats rock! You won :)")

    elif computer_answer == "paper":
        if player_answer == "rock":
            print("Paper beats rock! You lost :(")
        else:
            print("Scissors beat paper! You won :)")
    elif computer_answer == "scissors":
        if player_answer == "rock":
            print("Rock beats scissors! You won :)")
        else:
            print("Scissors beat paper! You lost :(")

    replay = int(input("Would you like to play again? Yes[1], No[2]\n"))
    if replay != 1:
        break


