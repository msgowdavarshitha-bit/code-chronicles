def isLeapYear(n):
    return ((n%400!=0 and n%4==0) or (n%400==0))
n=int(input("Enter a year: "))
if isLeapYear(n):
    print("Leap year")
else:
    print("Not a leap year")


