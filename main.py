import random
import time

rps = ["Rock", "paper", "scissors"]
answer = random.choice(rps)
answer.lower()
player_answer = (input("Rock paper or scissors?\n"))
player_answer.lower()


while True:
    if answer == player_answer:
        print(f"You both answered {answer}, tie.")
        break
    elif answer == "rock":
        if player_answer == "scissors":
            print("Rock beats scissors! You lost :(")
            break
        else:
            print("Paper beats rock! You won :)")
            break
    elif answer == "paper":
        if player_answer == "rock":
            print("Paper beats rock! You lost :(")
            break
        else:
            print("Scissors beat paper! You won :)")
            break
    elif answer == "scissors":
        if player_answer == "rock":
            print("Rock beats scissors! You won :)")
            break
        else:
            print("Scissors beat paper! You lost :(")
            break

time.sleep(5)
