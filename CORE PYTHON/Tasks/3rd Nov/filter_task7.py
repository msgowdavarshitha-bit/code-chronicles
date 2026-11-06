# Task 6: Filter Scenario: Number Filtering Given a list of numbers: 
# numbers = [12, 45, 67, 23, 89, 90, 34, 100, 15] Use filter() and lambda to: 
# ● Filter even numbers. 
# ● Filter numbers greater than 50. 
# ● Filter numbers divisible by 5. 
# ● Filter numbers between 20 and 80. 


numbers = [12, 45, 67, 23, 89, 90, 34, 100, 15]

def even_check(n):
    if n%2==0:
        return True
    else:
        return False

def greater_than_50(n):
    if n>50:
        return True
    else:
        return False


def divisible_by_5(n):
    if n%5==0:
        return True
    else:
        return False

def between_20_80(n):
    if n>20 and n<80:
        return True
    else:
        return False



print("Original list is: ",numbers)
even=list(filter(even_check,numbers))
print("Even numbers of the list: ",even)

greater_50=list(filter(greater_than_50,numbers))
print("The numbers greater than 50 are: ",greater_50)

factor_of_5=list(filter(divisible_by_5,numbers))
print("The numbers which are divisible by 5 are: ",factor_of_5)


bw_20_80=list(filter(between_20_80,numbers))
print("The numbers between 20 to 80 are: ",bw_20_80)
