def __init__(self,name,age,house):
    if not name:
        raise ValueError("name is missing")
    self.name=name
    self.age=age
    self.house=house
def __str__(self):
    return f"name:{self.name} age:{self.age}"
def Hcheck(self):
    match self.house:
        case "blue":
            return "your house is neela"
        case "green":
            return "your house is hara"
        case "red":
            return "your house is laal"
        case "yellow":
            return "your house is peela"
def main():
    student=get_students()
    print(student)
    print(student.Hcheck())
def get_students():
    name=input()
    age=input()
    house=input()
    return students(name,age,house)
if __name__=="__main__":
    main()