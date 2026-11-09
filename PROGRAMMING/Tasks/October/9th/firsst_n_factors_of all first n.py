print("Program to display all the factors of first n numbers")
# count=4  
#Factors 1->1 , factors 2 ->1 2.... factors 4-> 1 2 4


def factors(n):
    i=1

    while i*i<=n:
        if n%i==0:
            print(i,end=" ")
            if i!=(n//i):
                print((n//i),end=" ")
        i+=1
    


n=int(input("Enter till where you want the factors: "))
series=1

while n>0:
    print("\nfactors of the",series,":",end=" ")
    factors(series)
    n-=1
    series+=1
