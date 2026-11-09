
def intArr():
    l2=[]
    for i in range(1,6):
        n=int(input("Enter: "))
        l2.append(n)
    for j in l2:
        if j%2==0:
            print(j,end=" ")
arr=intArr()


#we can do this using different function for array and check even seperately