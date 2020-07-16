name=input("what is your name? ")
while name != "":
    for x in range(10):
        print(name, end=" ")
    print("")
    name = input("enter a different name or press ENTER to exit ")
    print("")
print("thanks for playing")
