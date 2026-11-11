# Task 3: Multilevel Inheritance – Employee → Developer → SeniorDeveloper 
# 
# Objective: Create a chain of inheritance where a child class becomes the parent class for another class. 
# 
# Class Structure        Employee  
#                           |       
#                        Developer         
#                            |     
#                       SeniorDeveloper 
# 
# 
# 1. Parent Class – Employee 
# Attributes: ● name ● employee_id ● salary 
# Method: ● display_employee() – Display employee details. 
# 
# 
# 2. Child Class – Developer
#  Attribute: ● programming_language 
# Method: ● write_code() – Display the programming language used by the developer. 
# 
# 
# 3. Child Class – SeniorDeveloper 
# Attribute: ● experience 
# Method: Task: ● review_code() – Display the senior developer's code review details. 
# 
# 
#Task
# Create a SeniorDeveloper object and access the properties and methods inherited from all three classes. 
# 
# Display: 
# ● Employee information 
# ● Developer information 
# ● Senior Developer information 
# 
# 
# Concept: Multilevel Inheritance 

class  Employee:
    def display_employee(self,name,employee_id):
        self.name=name
        self.employee_id=employee_id
        print()
        print("Name of the employee: ",name)
        print("EMployee ID: ",employee_id)

class Skills(Employee):
    def display_skill(self,skill):
        self.skill=skill
        print("Skill of the employee: ",skill)


class Developer(Skills):
    def work(self,project):
        
        self.project=project
        print("EMployee assigned project: ",project)


name=input("Enter the name of the employee: ")
employee_id=int(input("Enter the employee id: "))
skill=input("Enter the employee skills: ")
project=input("ENter the project name the employee assigned to: ")
Developer=Developer()
Developer.display_employee(name,employee_id)
Developer.display_skill(skill)
Developer.work(project)

#NOTE:-
#Python doesn't support multiple inheritance