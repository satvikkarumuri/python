import random

print("paper beats rock")
print("rock beats scissors")
print("scissors beats paper")

item=["rock", "paper", "scissors"]

player = input("Choose rock, paper or scissors or type quit to exit ")
player = player.lower()

while player != "quit":
    computer = random.choice(item)
    if player == computer:
        print("it is a tie!")
    elif player == "rock":
        if computer == "paper":
            print("you lose!")
        if computer == "scissors":
            print("you win!")

    elif player == "scissors":
        if computer == "rock":
            print("you lose")
        if computer == "paper":
            print("you win!")

    elif player == "paper":
        if computer == "rock":
            print("you win!")
        if computer == "scissors":
            print("you lose")

    else:
        print("error")
    player = input("Choose rock, paper or scissors or type quit to exit ")
    player = player.lower()