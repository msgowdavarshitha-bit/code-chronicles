
# nums=[2,433,0,1]

# arr=[0]*(len(nums)+1)

# print(arr)


def intArr():
    l1=[]
    while True:
        try:
            n=int(input("Enter the element: "))
            l1.append(n)
        except Exception as e:
            return l1

def missing_element(arr):
    n=len(arr)
    sum=0
    for i in range(0,n):
        sum+=arr[i]
        total=n*(n+1)//2
    return total-sum 

arr=intArr()
result=missing_element(arr)
print(result)