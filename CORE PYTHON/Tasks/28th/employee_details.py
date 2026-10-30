
class Employee:
    company_name = "Kaizentrix Global Solutions"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("Employee Name:", self.name)
        print("Employee Salary:", self.salary)
        print("Company Name:", Employee.company_name)
        print("---" * 30)


print("Welcome to Employee ID Generator")

number = int(input("Enter the number of employees: "))

for i in range(1, number + 1):
    name = input("Enter the employee name: ")
    salary = int(input("Enter the salary: "))

    f1 = Employee(name, salary)

    print("==="*30)
    print("Employee details:")
    f1.display()
