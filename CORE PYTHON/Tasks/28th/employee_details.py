class Employee:
    company_name = "Kaizentrix Global Solutions"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print()
        print("Employee Name:", self.name)
        print("Employee Salary:", self.salary)
        print("Company Name:", Employee.company_name)
        # print("---" * 30)


def createEmployee(n):
    if n == 0:
        return

    name = input("Enter the employee name: ")
    salary = int(input("Enter the salary: "))

    f1 = Employee(name, salary)

    createEmployee(n - 1)

    print("================="*5)
    print("Employee Details:")
    f1.display()


print("Welcome to Employee ID Generator")

number = int(input("Enter the number of employees: "))

createEmployee(number)