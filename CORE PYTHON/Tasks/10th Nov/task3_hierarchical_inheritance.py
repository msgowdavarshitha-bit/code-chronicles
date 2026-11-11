# Task 5: Hierarchical Inheritance – E-Commerce Product → Electronics / Clothing 
# # Objective: Create multiple child classes that inherit common product details from a parent class while implementing category-specific methods. 
# 
# Class Structure                  Product                
#                                 /       \          
#                           Electronics   Clothing 
# 
# 1. Parent Class – Product 
# Attributes: ● product_name ● price 
# Method: ● display_product() – Display the common product information. 
# 
# 2. Child Class – Electronics 
# Attribute: ● warranty 
# Methods: ● display_warranty() – Display the warranty period. 
#          ● check_warranty() – Display warranty availability. 
# 
# 
# 3. Child Class – Clothing 
# Attribute: ● size 
# Methods: ● display_size() – Display the clothing size. 
#          ● check_size() – Display the available size. 
# 
# 
# Task: 
# ● Create an Electronics object for an electronic product. 
# ● Create a Clothing object for a clothing product. 
# ● Access the common properties and methods inherited from the Product class. 
# ● Access the category-specific properties and methods of both child classes. 
# ● Display the complete information of both products. Concept: Hierarchical Inheritance

class Employee:
    def display_employee(self,name,employee_id,salary):
        self.name =name 
        self.employee_id=employee_id
        self.salary=salary
        print("Name of the employee: ",name)
        print("EMployee ID: ",employee_id)
        print("Employee salary: ",salary)

class Developer(Employee):
    def write_code(self,programming_language):
        self.programming_language=programming_language
        print("The programming language used by the developer: ",programming_language)


class SeniorDeveloper(Developer):
    def review_code(self, experience):
        self.experience= experience
        print("Display the senior developer's code review details: ", experience)

name=input("Enter the name of the employee: ")
employee_id=int(input("Enter the employee ID of the employee: "))
salary=int(input("Enter the salary of the employee: "))
programming_language=input("ENter the programming language developer knows: ")
experience=int(input("Enter senior developer reviews: "))


SeniorDeveloper=SeniorDeveloper()
SeniorDeveloper.display_employee(name,employee_id,salary)
SeniorDeveloper.write_code(programming_language)
SeniorDeveloper.review_code(experience)