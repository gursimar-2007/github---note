while True:
    n=int(input("ENTER YOUR NUMBER"))
    if n%2==0:
        print("your number is even")
        break
    elif n%2!=0:
        print("the number you have entered is odd")
        break
    elif n==0:
        print("THE NUMBER YOU HAVE ENTERED IS zero please enter a better one :")
    elif n<0:
        print("The number is negative")    