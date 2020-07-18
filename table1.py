# Print multiplication table 
table = eval(input("what multiplication table do you want? "))

for x in range (10):
    x+=1
    print(table," * ",  x, " =", table*x)
