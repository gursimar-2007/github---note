# username should not bve more than 12 characters
# username must not have any digits
# username must not contain any digitsd
username = input("PLEASE ENTER A USERNAME")
counter = username.count
digicount = username.isdigit
spacecount = username.find(" ")
if (counter>=12):
    print("USERNAME CANNOT BE MORE THAN 12 WORDS")
elif (digicount==True):
    print("YOUR USERNAME CONTAINS DIGIT")
elif(spacecount!=0):
    print("YOUR USERNAME CANNOT HAVE SPACES")    