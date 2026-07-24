class Student:
# init constructor for storings
    def __init__(self, name, roll, course, marks):
        try:
            self.name = name
            self.course = course
            self.roll = roll
            self.marks = marks
        except ValueError:
            print("please enter correct value")
        
# average calculation
    def calculate_average(self):
        return sum(self.marks) / len(self.marks)
# ======for displaying details========
    def display_details(self):
        print(f"roll={self.roll}")
        print(f"course={self.course}")
        print(f"marks={self.marks}")
        print(f"name={self.name}")
# str function
    def __str__(self):
        return f"Student({self.name}, Roll: {self.roll}, Course: {self.course}, Avg: {self.calculate_average()})"
# list storer

students = [
    Student("fateh", 101, "cse", [90, 91, 92]),
    Student("gursimar", 102, "ece", [94, 95, 93]),
    Student("parneeta", 103, "mechanical", [43, 61, 62]),
    Student("baljeet", 104, "chemical", [12, 91, 52]),
    Student("samay raina", 105, "printing", [93, 21, 22]),
]

for student in students:
    student.display_details()

# top = max(students)
top = students[0]
for student in students:
    if student.calculate_average() > top.calculate_average():
        top = student
print("=== Top Performing Student ===")
print(f"Highest Average: {top.calculate_average()}")
print(top)