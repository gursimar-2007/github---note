class rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return self.length*self.breadth
    def perimeter(self):
        return 2*(self.length+self.breadth)
rect=rectangle(10,5)
print(f"area: {rect.area()}")
print(f"perimeter: {rect.perimeter()}")

        
