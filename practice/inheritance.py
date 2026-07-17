class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return f"name:{self.name} age:{self.age}"
def main():
    name=input("name")
    age=input("age")
    student=Student(name,age)
    print(student)





if __name__=="__main__":
    main()
    