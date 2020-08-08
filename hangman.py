import random

# ------------------ VARIABLES -------------------------------

# List of words in the game
secret_words = ["cat", "dog", "fish", "parrot", "hamster", "frog"]

# Create empty list for answer
answer = []
# -------------------- END VARIABLES -----------------------------


# ------------------ FUNCTIONS -------------------------------
def setDisplay():
    # Fill answer with '_'
    for letter in range (len(secret)):
        answer.append("_")
    print(answer)



# def setBlankValue(position, letter):
#     answer[position] = letter

def setBlankValue(letter):
    index = secret.find(letter)
    if index < 0:
        print("that is wrong, try again ")
        exit()
    else:
        answer [index] = letter


def fillAnswer ():
    y = 0
    for x in answer:
        guess = input("guess a letter A through Z: ")
        setBlankValue(guess)
        y = y + 1
        print (answer)

# ------------------END FUNCTIONS -------------------------------


# ------------------------ MAIN LOGIC -------------------------
# Shuffle words
random.shuffle(secret_words)

# Get first word from the list after shuffle
secret = secret_words[0]

# Player starts
setDisplay()
fillAnswer()

# list to string conversion
answer_str = ""
answer_str = answer_str.join(answer)

# Compare final result
if answer_str.lower() == secret.lower():
    print("You did it, the word is", ''.join(secret), "!")
else:
    print("That is wrong, try again ")
# ------------------------ END MAIN LOGIC -------------------------
