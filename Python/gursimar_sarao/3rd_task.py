import random
def play_game():
    number = random.randint(1, 100)
    guess=False
    i=0


    while not guess:
        i+=1
        try:
            n = int(input(f"Attempt {i} Enter your guess (1-100): "))
            if number == n:
                print("Thank you, done!")
                guess=True

           
            elif number<n<=number+ 10:
                print("Too high, but close")
            elif n > number + 10:
                print("too high!")
            elif number - 10 <= n< number:
                print("too ow but close")
            else:
                print("too low")
        except ValueError:
            print("enter a correct one")
            i-=1



        while True:
            play = input("\nDo you want to play again? (Y/N): ").strip().lower()
            if play == "y":
                print("new game")
                break  
            elif play == "n":
                print("Thanks for playing! Goodbye.")
                return  
            else:
                print("Please enter 'Y' for Yes or 'N' for No.")

play_game()