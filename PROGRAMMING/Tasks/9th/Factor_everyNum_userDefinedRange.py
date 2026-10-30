print("#to display all the factors of each and every number present in the user defined range")
# s=8 and s=12   factors of 8 :- 1 2 4 8  , factors of 9:- 1 3 9....., factors of 12:- 1 2 3 4 6 12 


def countFactors(n):
    i=1
    while i*i<=n:
        if n%i==0:
            print(i,end=" ")
            if i!=(n//i):
                print((n//i),end=" ")
        i+=1

n1=int(input("Enter the first number: "))
n2=int(input("Enter the second number: "))
for i in range(n1,n2+1):
    print("\nthe factors of",i,"are",end=" ")
    if countFactors(i):
        print(i,end=" ")