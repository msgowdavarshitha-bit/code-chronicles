class EmployeeID:
    employee_count = 1000
    company_name="Kaizentrix Global Solutions"


    def __init__(self,n,d):
        self.name=n
        self.department=d
      


    def generate_employee_id(self):
        EmployeeID.employee_count+=1
        employee="EMPKGS"+str(EmployeeID.employee_count)
        return employee



print("=====================Welcome to employee ID generator=======================")
number=int(input("Enter the number of employee you want to generate ID's: "))


for i in range(1,number+1):
    n=input("Enter the employee name: ")
    d=input("Enter the employee department: ")


    print("--"*30)
    f1=EmployeeID(n,d)

    print("Employee details....")  
    print("Company name: ",EmployeeID.company_name)  
    print("Employee Name: ",f1.name)
    print("Employee Department: ",f1.department)
    print("Employee ID: ",f1.generate_employee_id())
    print("===="*30)