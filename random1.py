import random
x = random.randint(1, 1000)
number=int(input("pick a number 1 to 1000 "))
count = 1
while x != number:
    if x > number:
        print("too low, try again")
    elif x < number:
        print("too high, try again")
    number=int(input("pick a number 1 to 1000 "))
    count += 1

print ("you did it, good job! solved in", count, "steps")