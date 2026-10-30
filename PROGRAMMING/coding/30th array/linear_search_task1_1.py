#To create user defined array
def intArr():
    lst=[]
    while True:
        try:
            n=int(input("Enter the element: "))
            lst.append(n)
        except Exception as e:
            return lst

#To search the target in the array
def linearSearchIndex(a,target):
    for i in range(0,len(a)):
        if target==a[i]:
            return i
        else:
            return -1

a=intArr()