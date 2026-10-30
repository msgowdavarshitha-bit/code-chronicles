print("Write a program to print first n odd and even factors separately..")


def isFactors(n):
    i=1
    while i*i<=n:
        if n%i==0:
            print(i, end=" ")
            if i!=(n//i):
                print((n//i),end=" ")
        i+=1
    return i


n=int(input("Enter the number like how many even and odd factors you need: "))
temp=n 

series=1

print("First ",n," even factors are")
while n>0:
    if series%2==0:
        print("\nThe factors of ",series,"are: ")
        isFactors(series)
        n-=1
    series+=1 


series1=1
print("\nFirst ",temp," odd factors are")
while temp>0:
    if series1%2!=0:
        print("\nThe factors of ",series1,"are: ")
        isFactors(series1)
        temp-=1
    series1+=1