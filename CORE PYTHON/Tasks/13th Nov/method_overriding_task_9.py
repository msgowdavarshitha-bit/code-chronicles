#  Task 9: Method Overriding – Employee Roles
# 
#  Concept: Inheritance + Method Overriding 
# 
# Question: Create a parent class Employee with the following method:
#  class Employee:
#   def work(self):         
#       print("Employee is working") 
# 
# Create the following child classes: 
# ● Developer 
# ● Tester 
# ● Manager 
# 
# Each child class must override the work() method with its own implementation. 
# 
# Expected Output: 
# Developer → Writing code Tester → Testing application Manager → Managing team 
# 
# Requirements: 
# 1. Create all three child classes. 
# 2. Override the work() method in each child class. 
# 3. Create objects for all three classes. 
# 4. Call the work() method using each object. 


class Employee:     
    def work(self):         
        print("Employee is working") 

class Developer(Employee):
    def work(self):
        print("Developer → Writing code ")

class Tester(Employee):     
    def work(self):         
        print("Tester → Testing application ")

class Manager(Employee):     
    def work(self):         
        print("Manager → Managing team")

d=Developer()
t=Tester()
m=Manager()

d.work()
t.work()
m.work()

# Developer → Writing code 
# Tester → Testing application 
# Manager → Managing team