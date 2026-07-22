import random
# =============character pool======================
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%"
n=int(input("enter the length of password YOU want to generate"))
# =============password's inititation==============
password=""
# =============password's looper===================
for i in range(n):
    index=random.randint(0,len(characters)-1)
    character=characters[index]
    password+=character
# =============password printer====================
print(password)