text = input("type in a text and I will give you a acronym ")

abb = []
words = text.split()
for word in words:
    letter = word[0].upper()
    abb.append(letter)


add=''.join(abb)
print(add)

