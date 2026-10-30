class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)
        print()


def createStudent(n):
    if n == 0:
        return

    name = input("Enter name: ")
    age = int(input("Enter age: "))
    course = input("Enter course: ")

    s = Student(name, age, course)

    createStudent(n - 1)    #i used recursion so that after creation of multiple objects and then display

    print("Student Details:")
    s.display()


n = int(input("Enter number of students: "))

createStudent(n)