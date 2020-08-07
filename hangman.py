import random

# List of words in the game
secret_words = ["Cat", "Dog", "Fish", "Parrot", "Hamster", "Frog"]

# Create empty list for answer
answer = []
# ----------------------------

# Shuffle words
random.shuffle(secret_words)

# Get first word from the list after shuffle
secret = secret_words[0]

# Player starts
# Fill answer with '_'
for letter in range (len(secret)):
    letter = answer.append("_")
print(answer)

y = 0
for x in answer:
    guess = input("guess a letter A through Z: ")
    answer[y] = guess
    y = y + 1
    print (answer)

# list to string conversion
answer_str = ""
answer_str = answer_str.join(answer)

# Compare final result
if answer_str.lower() == secret.lower():
    print("You did it, the word is", ''.join(secret), "!")
else:
    print("That is wrong, try again ")
