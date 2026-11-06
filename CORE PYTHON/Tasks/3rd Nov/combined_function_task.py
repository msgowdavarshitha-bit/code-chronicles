# Task 8: Combined Function Challenge 
# Scenario: Student Marks Processing 
# Given: marks = [35, 45, 67, 89, 90, 23, 56, 78, 99] 
# 
# Perform the following: 
# 1. Create a function to calculate the average. 
# 2. Use lambda to sort marks in descending order. 
# 3. Use filter to find marks above 60. 
# 4. Use map to convert marks into grades. 
# 5. Create a closure that checks whether a mark is a pass or fail. 
# 6. Create a decorator that displays "Marks processing started" before execution. 


marks = [35, 45, 67, 89, 90, 23, 56, 78, 99]


# 1. DECORATOR
def processing_decorator(func):

    def function(marks):
        func(marks)

    return function


# 2. CLOSURE
def check_result(pass_mark):

    def result(mark):

        if mark >= pass_mark:
            return "Pass"
        else:
            return "Fail"

    return result


# 3. MAIN FUNCTION
@processing_decorator
def process_marks(marks):

    # 1. Calculate Average
    def calculate_average(marks):
        return sum(marks) / len(marks)

    average = calculate_average(marks)


    # 2. Sort marks in descending order using lambda
    sorted_marks = sorted(marks, key=lambda x: x, reverse=True)


    # 3. Filter marks above 60
    above_60 = list(filter(lambda x: x > 60, marks))


    # 4. Convert marks into grades using map
    def calculate_grade(mark):

        if mark >= 90:
            return "A+"

        elif mark >= 80:
            return "A"

        elif mark >= 70:
            return "B"

        elif mark >= 60:
            return "C"

        elif mark >= 40:
            return "D"

        else:
            return "F"

    grades = list(map(calculate_grade, marks))


    # 5. Closure to check pass or fail
    check_pass_fail = check_result(40)

    results = list(map(check_pass_fail, marks))


    # 6. Display all results
    print("\nOriginal Marks:", marks)

    print("Average Marks:", round(average, 2))

    print("Descending Order:", sorted_marks)

    print("Marks Above 60:", above_60)

    print("Grades:", grades)

    print("Pass / Fail:", results)


# Function Call
process_marks(marks)
