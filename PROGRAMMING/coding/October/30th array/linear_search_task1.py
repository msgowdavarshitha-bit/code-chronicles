def intArr():
    lst=[]   #to store it 
    while True:
        try:
            n=int(input("Enter the element: "))
            lst.append(n)
        except Exception as e:
            return lst


#make sure to search the element that is linear search maintain different function
def linearSearch(a,target):
    for i in range(0,len(a)):
        if target==a[i]:
            return True
        else:
            return False


a=intArr()  #store it in a variable

target=int(input("Enter the target: "))
result=linearSearch(a,target)
print(result)