l=[]

def append_demo(n):
    for i in range(1,n+1):
        num=int(input("Enter the elements: "))
        l.append(num)

    print("The even elements in the list are: ")
    for j in l:
        if j%2==0:
            print(j,end=" ")
    

n=int(input("Enter the number of elements you want to enter: "))
append_demo(n)



#Append is a predefined function that is used to add the element at the end of the list 