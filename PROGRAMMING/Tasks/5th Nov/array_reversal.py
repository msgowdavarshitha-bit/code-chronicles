# https://www.hackerrank.com/challenges/reverse-array-c/problem

# Sample Input 1

# 7
# 1 13 15 20 12 13 2 
# Sample Output 1

# 2 13 12 20 15 13 1 

def intArr(n):
    l1=[]
    for i in range(1,n+1):
        n=int(input("Enter the element: "))
        l1.append(n)
    return l1

def reverseArray(arr):
    return arr[::-1]


n=int(input("Enter the size of the array: "))
arr=intArr(n)
print(arr)
result_array=reverseArray(arr)
print(result_array)