import random
suits = ["hearts", "clovers", "spades", "diamonds"]
faces = ["two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
"jack", "king", "queen", "ace"]

keepGoing=True
while keepGoing:
    computerS = random.choice(suits)
    playerS = random.choice(suits)
    computerF = random.choice(faces)
    playerF = random.choice(faces)
    print("computer got",computerS,"and",computerF)
    print("You got",playerS,"and",playerF)
    if faces.index(computerF) > faces.index(playerF):
        print("you lose :(")
    elif faces.index(computerF) < faces.index(playerF):
        print("you win :)")
    else:
        print("it is a draw :|")

    awnser=input("click enter to continue or click anything else to exit ")
    keepGoing= (awnser == "")