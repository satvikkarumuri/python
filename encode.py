# Take input
name = input("type in a sercet word ")
name = name.upper()

output = " "

# Loop word and write logic
for letter in name:
    a_value = ord(letter) + 13
    if a_value > 90:
        a_value -= 26
    
    new_letter = chr(a_value)
    output += new_letter

# Print result
print(output)