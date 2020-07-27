import random

dice = [0, 0, 0, 0, 0]

for i in range (5):
    dice[i] = random.randint(1, 6)

print("you got", dice)
dice.sort()

if dice[0] == dice[4]:
    print("yatzee! ")
elif (dice[0] == dice[3]) or (dice[1] == dice[4]):
    print("four of a kind")
else:
    print("you lost")