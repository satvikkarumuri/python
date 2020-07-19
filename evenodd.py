#    ask --> o / e ; 

# loop - 0 - 10 ;	
#       o --> print odd numbers
#       e -->  print even numbers

# 3 % 2 
choice = input("print odd (o) or even (e) numbers? ")
for x in range(1):
    if choice == "o":
        print("your numbers are", 1, 3, 5, 7, 9)
    elif choice == "e":
        print("your numbers are", 0, 2, 4, 6, 8)
    else:
        print("invalid input")

