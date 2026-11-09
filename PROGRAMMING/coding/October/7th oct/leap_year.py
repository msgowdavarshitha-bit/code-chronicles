print("Leap year")
print("Write a program to check whether it is leap year or not")

year=int(input("Enter the year: "))
if (year%100!=0 and year%4==0) or (year%400==0):
    print("It is a leap year",year)
else:
    print("It is not a leap year",year) 


print("Write a program to check whether it is a leap year or not using customized value given by the user")
#identify the major logic
#declare the function and include the parameter that is input to it
#include the function declaration
#include o/p statements
#pass the required value --> Function call


def isLeapYear(year):
    if (year%100!=0 and year%4==0) or (year%400==0):
        return True 
    else:
        return False 
year=int(input("Enter a year: "))
if isLeapYear(year):
    print("It is a leap year")
else:
    print("It is not a leap year")




print("*******"*5)
print("Optimized code")
a=2002
print((a%100!=0 and a%4==0) or (a%400==0))
b=2004
print((b%100!=0 and b%4==0) or (b%400==0))


print("***"*10)
print("Write a program to display all the leap year present in a user defined range")

def isLeapYear(year):
    return ((year%100!=0 and year%4==0) or (year%400==0))


year1=int(input("Enter a start year: "))
year2=int(input("Enter a end year: "))
if year1>year2:
    print("Invalid input")
else:
    for i in range(year1,year2+1):
        if isLeapYear(i):
            print(i,end=" ")


print("\n****")
print("write a program to print all leap year and non leap year present in a user defined range separately")

def isLeapYear(year):
    return ((year%100!=0 and year%4==0) or (year%400==0))


year1=int(input("Enter a start year: "))
year2=int(input("Enter a end year: "))
if year1>year2:
    print("Invalid input")
else:
    print("\nLeap years")
    for i in range(year1,year2+1):
        if isLeapYear(i):
            print(i,end=" ")
    print("\nNon leap year")
    for i in range(year1,year2+1):
        if not isLeapYear(i):
            print(i,end=" ")




