
print("WAP to create a string costomized array")
def custArr():
    l1=[]
    while True:
        n=input("ENter: ")
        if n=="":
            return l1
        l1.append(n)

arr=custArr()
print("Array created: ",arr)
