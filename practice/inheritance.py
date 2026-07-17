class Checkerr:
    def __init__(self,name):
        self.name = name
    def check_name(self):
        if (len(self.name)>0):
            return f"name={self.name} is valid"
        else:
            return f"invalid name"
class Student(Checkerr):
    def __init__(self,name,age):
        super().__init__(name)
        # self.name=name
        self.age=age
    def display_data(self):
        return f"name:{self.name} age:{self.age}"
def main():
    name=input("name")
    age=input("age")
    student=Student(name,age)
    print(student.display_data())
    print(student.check_name())
if __name__=="__main__":
    main()
    