import random

number = random.randint(1, 100)


for i in range(1, 7):
    n = int(input(f"Attempt {i}/6 - Enter your guess (1-100): "))
    if number == n:
        print("Thank you, done!")
        break  
    elif number < n <= number + 10:
        print("Too high, but close!")
    elif n > number + 10:
        print("too high!")
        
        
    
    elif n < number - 10:
        print("too low")

