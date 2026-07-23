side1=int(input("enter first side"))
side2=int(input("enter enter second side"))
side3=int(input("enter third side"))
if(side1==side2==side3):
    print("equilateral")
elif(side1==side2 or side2==side3 or side3==side1 ):
    print("isosceles")
else:
    print("scalene")




