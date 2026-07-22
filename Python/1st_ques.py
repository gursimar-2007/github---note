# try:
#     subjects=[]
#     for i in range(1,6):
#         marks=int(input("enter your marks please"))
#         if marks<0 or marks>100:
#             raise ValueError("invalid")
#         subjects.append(marks)
#     total=sum(subjects)
#     percentage=(total/500)*100
#     average=total/len(subjects)
#     print(f"{total},{average},{percentage}")
#     if(percentage>=90 and percentage<=100):
#         print("your grade is A please proceed")
#     elif(percentage>=80 and percentage<90):
#         print("your grade is B please proceedd")
#     elif(percentage>=70 and percentage<80):
#         print("your grade is C please proceed")
#     elif(percentage>=60 and percentage<70):
#         print("your grade is D please proceed")
#     elif(percentage<60):
#         print("your grade is F please proceed with caution")
# except ValueError:
#     print("unethical")
    

# ======================================================================2nd question=====================================================
acc_bal=10000
withdrawal=acc_bal
while acc_bal>0:
        withdrawal=int(input("enter withdrawal amount please"))
        acc_bal-=withdrawal
        print(acc_bal)
if (withdrawal>10000 or withdrawal<0):
    print("invalid input please reverify")
       
elif(withdrawal>acc_bal or withdrawal==0):
    print("SBI ON LUNCh BREAK")
else:
     acc_bal-=withdrawal
     print(f"TRANSACTION SUCCESSFUL YOU ACC BALANCE IS NOW {acc_bal}")
    
    # ===========================================3rd question===============================================













# =============================================4th question=============================================================
# try:
# units=int(input("enter the number of units"))
# bill = 0
    
# if units <= 100:
#         bill = units*5
#         print(bill)
# elif units <= 200:
#         bill= (100*5)+((units-100)*7)
#         print(bill)
# else:
#         bill= (100*5)+(100*7)+((units-200)*10)
#         print(bill)
# except ValueError:
# print("not efined")
# =================================================5th questions====================================

# import random

# number = random.randint(1, 100)


# for i in range(1, 7):
#     n = int(input(f"Attempt {i}/6 - Enter your guess (1-100): "))
#     if number == n:
#         print("Thank you, done!")
#         break  
#     elif number < n <= number + 10:
#         print("Too high, but close!")
#     elif n > number + 10:
#         print("too high!")
        
        
    
#     elif n < number - 10:
#         print("too low")


