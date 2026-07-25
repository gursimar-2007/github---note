# # while True:
# #     if name=="nitin":
# #         with open("freindsname.txt","w") as file:
# #             pass
# #     else:
# #         with open ("freindsname.txt","a") as file:
# #             file.write(f"{name}\n")
# while True:
#     name=input("enter the name").lower()
#     with open ("freindsname.txt","a") as file:
#             file.write(f"{name}\n")

#     while True:
#         ask =input("\nDo you want to enter again? (Y/N): ").strip().lower()
#         if ask == "y":
#             print("new")
#             with open ("freindsname.txt","a") as file:
#                     file.write(f"{name}\n")
#             break  
#         elif ask == "n":
#             print("Thanks Goodbye.")
#             False
                    
#         else:
#             print("Please enter 'Y' for Yes or 'N' for No.")
#     print("--- Friends List ---")
#     with open("freindsname.txt", "r") as file:
#         lines = file.readlines()
#         print(lines.strip())
        # for line in lines:

while True:
    name = input("Enter the name: ").strip().lower()

    with open("freindsname.txt", "a") as file:
        file.write(f"{name}\n")

    while True:
        ask = input("Do you want to enter again? (Y/N): ").strip().lower()
        if ask in ("y", "n"):
            break
        print("Please enter 'Y' for Yes or 'N' for No.")

    if ask == "n":
        print("Thanks! Goodbye.\n")
        break

print("--- Friends List ---")
with open("freindsname.txt", "r") as file:
    lines = file.readlines()
    print(lines)
    # for line in lines: