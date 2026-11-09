
print("TO display below series by getting user defined n")
#if n=4
#4 3 2 1 1 2 3 4
#No change in base condition, no change recursive function call
#3rd variable not accepted


def series(n):
    if n<=0:
        return 
    print(n,end=" ")
    series(n-1)

    
    print(n,end=" ")
    
 
   


n=int(input("Enter the number: "))
series(n)