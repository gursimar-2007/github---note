def main():
    try:
        x=int(input("enter a no. to square"))
        print("square of a no.", square(x))
    except ValueError:
        print("gdp ")

def square(x):
    return x+x
    


while True:
    if __name__=="__main__":
        main()
