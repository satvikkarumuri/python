#    ask --> o / e ; 

# if odd 
    
# loop - 0 - 10 ;	
#       o --> print odd numbers
#       e -->  print even numbers

# 3 % 2 
choice = input("print odd (o) or even (e) numbers? ")
if choice != "o" and choice != "e":
    print ("invalid input")
    exit(100)

for x in range(10):
    if choice == "o" and x % 2 == 1 :
        print(x)
    elif choice == "e" and x % 2 == 0:
        print(x)

