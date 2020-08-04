starSign= input("What is your star sign or click type exit to leave? ")
while starSign != "exit":
    starSign.lower()
    if starSign ==  "aries":
        print("In the morning, I begin again")
    elif starSign == "taurus":
        print("Safety is a place only in my mind")
    elif starSign == "gemini":
        print("You can have all of me, not half of me")
    else:
        print("error")
    starSign= input("What is your star sign or click type exit to leave? ")
