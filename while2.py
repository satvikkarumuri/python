import turtle

family =[]

name    =   turtle.textinput("family names", "input your name or press ENTER to exit")

while name != "":
    family.append (name)
    name=turtle.textinput("family names", "input your name or press ENTER to exit")

print(family)