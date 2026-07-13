class Staff:
    def __init__(self, name, salary, subject):
        if not name:
            raise ValueError("Name is missing")
        self.name = name
        self.salary = salary
        self.house = subject

    def __str__(self):
        return f"name: {self.name}, salary: {self.salary}"

    def Hcheck(self):
        match self.subject.lower():
            case "physics":
                return "your sub is भौतिक विज्ञान"
            case "chemistry":
                return "your sub is रसायन विज्ञान "
            case "english":
                return "your house is अंग्रेज़ी"
            case "engineering":
                return "your house is इंजीनियरिंग"
            case _:
                return "are you crazy?"

def get_staff():
    print("Enter Name: ", end="")
    name = input().strip()
    
    print("Enter salary: ", end="")
    salary = input().strip()
    
    print("Enter subject: ", end="")
    subject = input().strip()
    return Staff(name, salary, subject)

def main():
    staff = get_staff()
    print(staff)
    print(staff.Hcheck())

if __name__ == "__main__":
    main()