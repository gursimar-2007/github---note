class Employee():
    def __init__(self, name, id, salary):
        self.name = name
        self.id = id
        # Convert salary to a float so Python can do math on it
        self.salary = float(salary)

class Salary(Employee):
    # Cleaned up the parameters since they are calculated inside the class automatically
    def __init__(self, name, id, salary):
        # Correctly pass name, id, and salary to the parent Employee class
        super().__init__(name, id, salary)
        self.ta = 0
        self.da = 0
        self.AS = 0
        self.ts = 0
        self.hra = 0 # Fixed the syntax typo here
        
    def display_data(self):
        return f"Name: {self.name} | Base Salary: ${self.salary:.2f} | ID: {self.id}"
    
    # Removed the unused parameters from the function definition
    def calculations(self):
        self.hra = 0.15 * self.salary
        self.ta = 0.10 * self.salary
        self.da = 0.05 * self.salary
        self.ts = self.salary + self.ta + self.da + self.hra

    def display_detailed_salary(self):
        return (
            f"\n--- Salary Breakdown for {self.name} (ID: {self.id}) ---\n"
            f"Base Salary: ${self.salary:.2f}\n"
            f"HRA (House Rent Allowance): ${self.hra:.2f}\n"
            f"TA (Travel Allowance): ${self.ta:.2f}\n"
            f"DA (Dearness Allowance): ${self.da:.2f}\n"
            f"-------------------------------------\n"
            f"Gross Total Salary: ${self.ts:.2f}"
        )

def main():
    name = input("Enter name: ")
    salary = input("Enter salary: ")
    emp_id = input("Enter ID: ") # Changed prompt text to make more sense than 'marks'
    
    # Match the new cleaner parameter list
    employee = Salary(name, emp_id, salary)
    
    print(employee.display_data())
    
    # Run the math setup
    employee.calculations()
    
    # Display the final breakdown
    print(employee.display_detailed_salary())    

if __name__ == "__main__":
    main()