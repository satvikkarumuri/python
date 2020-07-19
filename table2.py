# Print multiplication table 
table = eval(input("what multiplication table do you want? "))
x=0
while x < 10:
    x+=1
    print(table," * ",  x, " =", table*x)
