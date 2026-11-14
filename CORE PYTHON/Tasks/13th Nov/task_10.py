# Task 10: KGS Software Company – Employee Management System Question: Concept: Inheritance + Constructor + super() + Method Overriding Develop a simple employee management system for Kaizentrix Global Solutions (KGS). Create a parent class Employee with the following attributes: ● name ● employee_id ● salary Methods: ● display_details() ● work() 
# Create three child classes:              Employee            /    |    \     Developer  Tester  HR 1. Developer Class Additional attributes: ● programming_language ● project Override the work() method. Expected Output: Arun is developing the Employee Portal using Python 2. Tester Class Additional attribute: ● testing_tool Override the work() method. Expected Output: None None                                                                                                                                   Priya is testing the Employee Portal using Selenium 3. HR Class Additional attribute: ● department Override the work() method. Expected Output: Meena is managing the HR department Requirements: 1. Implement __init__() in the parent and child classes. 2. Use super() to initialize parent class attributes. 3. Implement parent and child class attributes. 4. Override the work() method in all three child classes. 5. Display employee details. 6. Create objects for Developer, Tester, and HR. 7. Demonstrate how inheritance reduces code duplication. 

class Employee:
    def __init__(self,name,employee_id,salary):
        self.name=name
        self.employee_id=employee_id
        self.salary=salary

    def display_details(self):
        print("Name of the employee: ",self.name)
        print("ID of the employee: ",self.employee_id)
        print("Salary of the employee: ",self.salary)

    def work(self):
        print("Employee is working")


class Developer(Employee):
    def work(self):
        