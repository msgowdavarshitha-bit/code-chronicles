print("Write a program to check the target element present in the array")
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
            return True
    else:
        return False



arr=intArr()
target=int(input("ENter the value you want to search"))

print("CReated array: ",arr)
a=linearSearch(arr,target)
if linearSearch(arr,target):
    print("Found",target)
else:
    print("Not found",target)
