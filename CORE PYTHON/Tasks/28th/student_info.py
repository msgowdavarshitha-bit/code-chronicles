print("1.Create a class Student with: Instance variables: name, age, course Constructor to initialize them Instance method display() to display student details Create two objects and display their details.")


class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def display(self):
        print("Name of the student:", self.name)
        print("Age of the student:", self.age)
        print("Course of the student:", self.course)
        print()


n = int(input("Enter the number of students: "))

for i in range(1, n + 1):
    print("----" * 20)
    name = input("Enter name: ")
    age = int(input("Enter the age: "))
    course = input("Enter the course name: ")

    d1 = Student(name, age, course)

    print("Details of student", i)
    d1.display()
