print("WAP to create a integer costomized array")
print("WAP to to check the item/elemnt present in the customizzed user defined array")


print()
print("WAP to create a integer costomized array")
def custArr():
    l1=[]
    while True:
        try:
            n=int(input("ENter: "))
            l1.append(n)
        except Exception as e:
            return l1

arr=custArr()
print("Array created: ",arr)



print("================"*3)
print("WAP to to check the item/elemnt present in the customizzed user defined array")

def intArr():
    l2=[]
    while True:
        try:
            n=int(input("Enter: "))
            l2.append(n)
        except Exception as e:
            return l2

arr=intArr()
num=int(input("Enter the element y want to search: "))
for i in arr:
    if i==num:
        print("Found")
        break
    else:
        print("Not found")