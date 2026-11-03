print("WAP to find the smallest element in the array ALONG WITH index")

#Contraints :_ what are the inputs they can give us


def arr():
    arr=[]
    while True:
        try:
            n=int(input("Enter the element: "))
            arr.append(n)
        except Exception as e:
            return arr

def fineElem(l1):
    min_element=2**31
    min_element_index=-1
    for i in range(0,len(l1)):
        if l1[i]<min_element:
            min_element=l1[i]
            min_element_index=i
    return min_element,min_element_index


a=arr()
res1,res2=fineElem(a)
print("The minimum valued element is",res1)
print("The index the minimum element found",res2)

