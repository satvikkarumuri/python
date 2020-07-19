#    ask --> o / e ; 

# if odd 
    
# loop - 0 - 10 ;	
#       o --> print odd numbers
#       e -->  print even numbers

# 3 % 2 
choice = input("print odd (o) or even (e) numbers? ")

for x in range(10):
    if choice == "o":
        if x % 2 == 1:
            print (x)

    elif choice == "e":
        if x % 2 == 0:
            print(x)

    else:
        print("invalid input")

