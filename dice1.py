import random

dice = [0, 0, 0, 0, 0]
x = input ("click enter to start the game, or type exit to leave the game ")

while x != "exit":
    
    for i in range (5):
        dice[i] = random.randint(1, 6)

    print("You got", dice)
    dice.sort()

    if dice[0] == dice[4]:
        print("yatzee! ")
    elif (dice[0] == dice[3]) or (dice[1] == dice[4]):
        print("four of a kind")
    else:
        print("you lost")
    x = input ("type exit to leave the game, or click enter to play again ")
    