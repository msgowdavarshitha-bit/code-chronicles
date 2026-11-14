# Task 4: Multiple Inheritance – Employee + Skills → 
# Developer 
# Objective: Create a child class that inherits properties and 
# methods from two parent classes. 
# Class Structure 
#        Employee       Skills 
#            \           / 
#             \         / 
#              Developer 
# 1. Parent Class – Employee 
# Attributes: 
# ● name 
# ● employee_id 
# Method: 
# ● display_employee() – Display employee information. 
# 2. Parent Class – Skills 
# Attribute: 
# ● skill 
# Method: 
# ● display_skill() – Display the employee's skills. 
# 3. Child Class – Developer 
# Attribute: 
# ● project 
# Method: 
# ● work() – Display the project assigned to the developer. 
# Task: 
# Create a Developer object and access the properties and 
# methods from both parent classes and the child class. 
# Display: 
# ● Employee details 
# ● Skill details 
# ● Project details 
# Concept: Multiple Inheritance



class Employee:
    def display_employee(self,name,employee_id):
        self.name=name
        self.employee_id=employee_id
        print("Name of the employee: ",name)
        print("Employee Id is: ",employee_id)

class Skills:
    def display_skill(self,skill):
        self.skill=skill
        print("Skills of the employee: ",skill)


class Developer(Employee,Skills):
    def work(self,project):
        
        self.project=project 
        print("The project assigned for the developer is: ",project)



name=input("Enter the name of the employee: ")
employee_id=input("Enter the ID of the employee: ")
skills=input("Enter the skills of the employee: ")
project=input("Enter the project that has been assigned for the developer: ")


developer=Developer()
print()
print("Employee Details: (Parent 1 class)")
developer.display_employee(name, employee_id)
print()
print("Skill Details: (Parent 2 class)")
developer.display_skill(skills)
print()
print("Project Details: (Parent 3 class)")
developer.work(project)


