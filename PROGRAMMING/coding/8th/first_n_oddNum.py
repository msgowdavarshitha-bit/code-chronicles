
print("Write a program to print first n odd numbers")

def isOddNumbers(n):

    if n%2!=0:
        return n
    

count=int(input("Enter the number: "))
series=1
print("The first",count,"odd numbers are: ")
while count>0:
    if isOddNumbers(series):
        print(series,end=" ")
        count-=1
    series+=1

    # if not isOddNumbers(series):
    #     continue
    #Not necessary needed 



