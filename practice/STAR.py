class Checker:

    def __init__(self,name):
        self.name=name
    def checkname(self):
        if (len(self.name)>0 and len(self.age)>0):
            return f"name ={self.name}  and {self.age} is valid"
        else :
            return f"invalid name"
class Student(Checker):
    def __init__(self,name,age):
        super().__init__(name)
        # self.name=name
        self.age=age
    def displaydata(self):
        return f"name:{self.name} age:{self.age}"
def main():
    name=input()    
    age=input() 
    student=Student(name,age)
    print(student.displaydata())   
    print(student.checkname())
if __name__=="__main__":
    main()   