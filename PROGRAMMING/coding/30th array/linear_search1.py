print("Write a program to check the target element present in the array along with where it is index")
def intArr():
    l1=[]
    while True:
        try:
            n=int(input("ENter: "))
            l1.append(n)
        except Exception as e:
            return l1

def linearSearch(arr,target):
    for i in range(0,len(arr)):
        if target==arr[i]:
            return i
    else:
        return -1   #BCZ we dont have the negative indexing 



arr=intArr()
target=int(input("ENter the value you want to search"))

a=linearSearch(arr,target)
if linearSearch(arr,target):
    print("Found",target,"at",a)
else:
    print("Not found",target)
