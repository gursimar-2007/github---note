while True:
    n = int(input("ENTER YOUR NUMBER: "))
    
    if n == 0:
        print("THE NUMBER YOU HAVE ENTERED IS zero please enter a better one :")
        # No break here, so it asks for a number again
    elif n < 0:
        print("The number is negative. Please enter a positive number.")
        # No break here, so it loops back
    elif n % 2 == 0:
        print("your number is even")
        break  # Exits the loop
    else:
        print("the number you have entered is odd")
        break  # Exits the loop
