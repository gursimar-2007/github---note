# while True:
    
#     if n == 0:
#         print("THE NUMBER YOU HAVE ENTERED IS zero please enter a better one :")
#         # No break here, so it asks for a number again
#     elif n < 0:
#         print("The number is negative. Please enter a positive number.")
#         # No break here, so it loops back
#     elif n % 2 == 0:
#         print("your number is even")
#         break  # Exits the loop
#     else:
#         print("the number you have entered is odd")
#         break  # Exits the loop
# while True:
#     n = int(input("ENTER YOUR NUMBER: "))
#     if n==0:
#         print("the number is zero")
#     elif n>0:
#         print("the number you have entered is positive")
#     elif n<0:
#         print("the number you have entered is negative")
# n1=int(input("enter your first number"))
# n2=int(input("enter your second number"))
# n3=int(input("enter your third number"))
# if(n1>n2):
#     if(n1>n3):
#         print(f"greatest:{n1} ")
# elif (n2>n3):

#     print(f"greatest:{n2}")
# else:

#     print(f"greatest:{n3}
# while True:
#     leap=int(input("enter the year you want to check"))
#     if (leap%4==0 and leap%100!=0) or leap%400==0:
#         print("its a leap year")
#     else:
#         print("its not a leap year")
op=input("enter your number")
a=int(input("enter the first number"))
b=int(input("enter the second number"))


match op:
    case '+':
        c=a+b
        print(f"the number is {c}")
    case '-':
        c=a-b
        print(f"the number is {c}")
    case '*':
        c=a*b
        print(f"the number is {c}")
    case '/':
        if a==0 or b==0:
            print
        c=a/b
        
        print(f"the number is {c}")








