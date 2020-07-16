# pizza cost calculator
quantity = eval (input("how many pizzas? "))
price = eval (input("what is the price of each pizza? "))

subtoatal = quantity * price

tax = subtoatal*0.08
total = tax+subtoatal
print("your tax is", tax)
print("your total bill is", total)