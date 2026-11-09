
print("TO display below series by getting user defined n")
#if n=4
#4 3 2 1 1 2 3 4
#No change in base condition, no change recursive function call
#3rd variable not accepted


print("IMPORTANTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT")
print("TO display below series by getting user defined n")
#if n=4
#1 2 3 4 4 3 2 1
#No change in base condition, no change recursive function call
#need 3rd variable  accepted


print()
print("Write a program to reverse an integer(+ve) number using recursion ")

def reverse(n,rev):
    if n<=0:
        return rev
    digit=n%10
    rev=(rev*10)+digit
    n=n//10
    return reverse(n,rev)

n=int(input("Enter the number u want to reverse: "))
print(reverse(n,0))



