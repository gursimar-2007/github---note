class Employee():
    def __init__(self,name,id,salary):
        self.name=name
        self.id=id
        self.salary=salary
class Salary(Employee):
    def __init__(self, name, id,hra,ta,da,AS,ts):
        super().__init__(name, id,Salary)
        self.ta=ta
        self.da=da
        self.AS=AS
        self.ts=ts
        self.hra=hra
    def display_data(self):
        return f" {self.name} and {self.salary} and id is {self.id}"
    def calculations(self,hra,ta,da,AS,ts):
        hra=(0.15*self.salary)
        ta=(0.15*self.salary)
        self.da=(0.15*self.salary)
        self.ts=(0.15*self.salary)
        self.=(0.15*self.salary)
        print(hra)
def main():
    name=input("name")
    salary=input("salary")
    id=input("marks")
    employee=Employee(name,id,salary)
    print(employee.display_data())
    print(employee.check_name())
    print(employee.get_marks())    
if __name__=="__main__":
    main()

        