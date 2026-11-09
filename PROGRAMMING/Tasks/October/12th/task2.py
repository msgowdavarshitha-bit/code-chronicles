print("IMPORTANTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT")
print("TO display below series by getting user defined n")
#if n=4
#1 2 3 4 4 3 2 1
#No change in base condition, no change recursive function call
#need 3rd variable  accepted



def series(n,temp):
    if temp>n:
        return 

    print(temp,end=" ")
    series(n,temp+1)

    #to print or return once temp>n just like a recursive
    print(temp,end=" ")
  


n=int(input("Enter the number: "))
series(n,1)