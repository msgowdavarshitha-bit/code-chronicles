
print("Count digits")
print("write a program to count the number of digits present in a given number")
# 1<=n<=10*5


def countDigit(n):
    count=0 #is a helper variable
    while n>0:
        n=n//10 #n//=10    #to remove the last digit of the number
        count+=1
    return count
nu=int(input("Enter the number: "))
result=countDigit(nu)
print("The digits count of ",nu,"is ",result)



print("To keep the updated value for the next cycle store it in same variable")
#eg
#count=count+1
print("If we dont need a updated value for the next cycle then store it in temporary variable")