class student:
    def __init__(self,name,roll,marks):
        self.name=name
        self.roll=roll
        self.marks=marks
        # pass
    def display(self):
        print(f"name={self.name}")
        print(f"roll no={self.roll}")
        print(f"marks={self.marks}")
s1=student("gursimar",15,90)
s1.display()