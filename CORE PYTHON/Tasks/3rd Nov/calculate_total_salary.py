# Task 1: Function Write a function calculate_salary() that accepts basic salary, HRA, and DA, and returns the total salary.  
# Example: calculate_salary(20000, 5000, 3000) 
# Excepted Output :  Python Total Salary: 28000 

def calculate_salary(basic_salary,HRA,DA):
    total=basic_salary+HRA+DA
    return total


basic_salary=int(input("Enter the basic salary: "))
HRA=int(input("Enter the HRA: "))
DA=int(input("Enter the DA: "))

result=calculate_salary(basic_salary,HRA,DA)
print("Total salary is: ",result)