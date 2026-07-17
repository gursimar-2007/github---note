class Student:
    def __init__(self,name,roll):
        self.name = name
        self.roll = roll
    def check_name(self):
        if (len(self.name)>0 and int(self.roll)>0):
            return f"name {self.name} and {self.roll}is valid"
        else:
            return "invalid name"
class Subject(Student):
    def __init__(self, name, roll,phy_marks):
        super().__init__(name,roll)
        self.phy_marks=phy_marks
    def display_data(self):
        return f"name={self.name} and roll no={self.roll}"
    def get_marks(self):
        # phy_marks=self.marks
        return f"phy marks are{self.phy_marks}"
def main():
    name=input("name")
    roll=input("roll")
    marks=input("marks")
    student=Subject(name,roll,marks)
    print(student.display_data())
    print(student.check_name())
    print(student.get_marks())
if __name__=="__main__":
    main()

    