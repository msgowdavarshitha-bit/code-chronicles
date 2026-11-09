print("DATE:- 13-10-2026")
print("Write a program to count the number of digits using recursion")


def countRecur(n,count):
    if n<=0:
        return count

    n//=10
    count+=1
    return countRecur(n,count)

n=int(input("Enter the number: "))
re=countRecur(n,0)
print("The number of counts are: ",re)


print()
print("Use the return to update the value instead of passing the expression")

def countRecur(n,count):
    if n<=0:
        return count
    
    return countRecur(n//10,count+1)   #instead of using count+=1 and n//10 making an expression and passing it to function is a extra work so instead perform the updation while passing the arguments while returning with each function call



n=int(input("Enter the number: "))
re=countRecur(n,0)
print("The number of counts are: ",re)



print()
print("If the condition to be checked once then it should outside/ before the function call only in recursive function ")
print("Use the return to update the value instead of passing the expression")

def countRecur(n,count):
    if n<=0:
        return count
    
    return countRecur(n//10,count+1)   #instead of using count+=1 and n//10 making an expression and passing it to function is a extra work so instead perform the updation while passing the arguments while returning with each function call



n=int(input("Enter the number: "))
if n<0:
    n=n*-1
re=countRecur(n,0)
print("The number of counts are: ",re)
