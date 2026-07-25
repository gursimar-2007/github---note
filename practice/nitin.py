# while True:
#     if name=="nitin":
#         with open("freindsname.txt","w") as file:
#             pass
#     else:
#         with open ("freindsname.txt","a") as file:
#             file.write(f"{name}\n")
while True:
    name=input("enter the name").lower()
    with open ("freindsname.txt","a") as file:
            file.write(f"{name}\n")

    while True:
        ask =input("\nDo you want to enter again? (Y/N): ").strip().lower()
        if ask == "y":
            print("new")
            with open ("freindsname.txt","a") as file:
                    file.write(f"{name}\n")
            break  
        elif ask == "n":
            print("Thanks Goodbye.")
            break
                    
        else:
            print("Please enter 'Y' for Yes or 'N' for No.")
    print("--- Friends List ---")
    with open("freindsname.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            print(line.strip())

# while
# with open a
    #input
    # write
    # if coti
