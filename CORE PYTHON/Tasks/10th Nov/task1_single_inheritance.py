# Task 1: Single Inheritance – Person → Student 
# Objective: Create a child class that inherits properties and methods from a parent class. 
# Class Structure         Person           |         
# 
# Student 1. Parent Class – Person 
# Attributes: ● name ● age 
# Method: ● display_person() – Display the person's name and age. 
# 
# 2. Child Class – Student Attributes: 
# ● student_id 
# ● course 
# Method: ● display_student() – Display the student's ID and course details. 
# 
# 
# 
# 
# Task: Create a Student object and display the complete student information by accessing the properties and methods of both the parent and child classes. Concept: Single Inheritance 



#METHOD 01
class Person:

    def display_person(self,name,age):
        self.name=name
        self.age=age
        print("Name of the person: ",name)
        print("Age of the person: ",age)

class Student(Person):

    def display_student(self,student_id,course):
        self.student_id=student_id
        self.course=course
        Person.display_person(self,name,age)
        print("Student ID is: ",student_id)
        print("Course details: ",course)
        

name=input("Enter the name of the person/student: ")
age=int(input("Enter the age of the person/student"))
student_id=input("Enter the student ID")
course=input("Enter the course name: ")


Student=Student()
Student.display_student(student_id,course)







#METHOD 02
class Person:

    def display_person(self,name,age):
        self.name=name
        self.age=age
        print("Name of the person: ",name)
        print("Age of the person: ",age)

class Student(Person):

    def display_student(self,student_id,course):
        self.student_id=student_id
        self.course=course
        # Person.display_person(self,name,age)
        print()
        print("Student ID is: ",student_id)
        print("Course details: ",course)
        

name=input("Enter the name of the person/student: ")
age=int(input("Enter the age of the person/student"))
student_id=input("Enter the student ID")
course=input("Enter the course name: ")


Student=Student()
Student.display_person(name,age)
Student.display_student(student_id,course)

