def values_taker():
    try:
        # taking values from user
        name=input("enter your name please")
        roll=int(input("enter your roll number please"))
        subjects=["physics","chemistry","hindi","maths","english"]
        marks=[]
        # for loop for taking marks
        for subject in subjects:
            num=int(input("enter you marks"))
            if num>100 or num<0:
                print("wrong values")
                break
            else:
                marks.append(num)
# error handling
    except ValueError:
        print("wrong value")
    for i in range(len(marks)-1):
        print(f"{marks[i]}",end=",")
        # calculating total avg percentage
    total=sum(marks)
    average=total/len(marks)
    print(f"{average:.2f}")
    lowest=min(marks)
    highest=max(marks)
    print(f"your lowest marks are{lowest} and highest marks are{highest}")
    return name,roll,total
    # ===================grading system===============================
def grader(total_marks):
    # percentage and grade giving
    percentage=(total_marks/500)*100
    print(f"your percentage is {percentage}")
    if percentage>=90 or percentage<=100:
        print("A+")
    elif percentage>=80 or percentage<=89:
        print("A")
    elif percentage>=70 or percentage<=79:
        print("B")
    elif percentage>=60 or percentage<=69:
        print("c")
    elif percentage>=50 or percentage<=59:
        print("D")
    elif percentage<50:
        print("F")
name,roll,total=values_taker()
grader(total)
