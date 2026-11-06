# Encapsulation: Employee Salary
#  Create an Employee class. 
# employee = Employee("Priya", 30000) 
# 
# 
# Requirements: 
# name → public 
# __salary → private 
# Create get_salary() 
# Create set_salary(new_salary) 
# 
# Salary cannot be set to a negative value. 
# 
# example: 
# employee.set_salary(35000) 
# print(employee.get_salary()) 
# Expected: 35000 

# If: employee.set_salary(-5000) 
# Output: Invalid salary 


class Employee:

    def __init__(self,name,salary):
        self.name=name
        self.__salary=salary

    def setdata(self,new_salary):
        if new_salary>0:
            self.__salary=new_salary
        else:
            print("Invalid salary")


    def getdata(self):
        return self.__salary



name=input("Enter the name of the employee: ")
salary_new=int(input("Enter new salary: "))
employee=Employee(name,35000)
employee.setdata(salary_new)
result=employee.getdata()
print(result)




print("==========="*5)
print("Output: ")


#o/p 1
# Enter the name of the employee: Raama
# Enter new salary: 10000000000 
# 10000000000


#o/p 2
# Enter the name of the employee: Seetha
# Enter new salary: -200
# Invalid salary
# 35000