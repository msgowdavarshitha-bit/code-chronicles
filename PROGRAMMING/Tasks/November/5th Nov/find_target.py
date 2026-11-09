# Given a List of Distinct N number a1,a2,a3........an.

# Find The Position Of Number K In The Given List.

# Input Format

# First Line Take Input Value Of N

# Second Line Take Input N Space Separated Integer Value

# Third Line Take Input Value Of K

# Constraints

# 0 < N < 100001

# 0 < ai < 10^10

# 0 < K < 10^10

# Output Format

# Position Of K In The Given List.

# Print -1 if element is not found.

# Sample Input 0

# 5
# 1 2 3 4 5
# 4
# Sample Output 0

# 3


def intArr(n):
    l1=[]
    for i in range(1,n+1):
        n=int(input("Enter the element: "))
        l1.append(n)
    return l1

def findElement(arr,target):
    for i in range(0,len(arr)):
        if arr[i]==target:
            return i


n=int(input("Enter the size of the array: "))
arr=intArr(n)

target=int(input("Enter the target: "))
result=findElement(arr,target)
print(result)