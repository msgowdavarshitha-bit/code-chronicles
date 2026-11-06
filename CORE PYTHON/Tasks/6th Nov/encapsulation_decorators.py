print("using decorator function")
class Employee:

    def __init__(self,name,salary):
        self.name=name
        self.__salary=salary

    @property
    def setter_getter(self):
        return self.__salary

    @setter_getter.setter
    def setter_getter(self,new_salary):
        if new_salary>0:
            self.__salary=new_salary
        else:
            print("Invalid salary")
name=input("Enter the name of the employee: ")
new_salary=int(input("Enter the salary new salary of the employee: "))
employee=Employee(name,30000)
employee.setter_getter=new_salary
result=employee.setter_getter
print("The salary of the employee: ",result)



print("==========="*5)
print("Output: ")


#o/p 1
# using decorator function
# Enter the name of the employee: Varshitha M S
# Enter the salary new salary of the employee: 80000
# The salary of the employee:  80000


#o/p 2
# using decorator function
# Enter the name of the employee: Varsha
# Enter the salary new salary of the employee: -199
# Invalid salary
# The salary of the employee:  30000