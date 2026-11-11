# def intArr():
#     l1=[]
#     while True:
#         try:
#             n=int(input("Enter the element: "))
#             l1.append(n)
#         except Exception as e:
#             return l1

# def mergeArr(arr1,arr2):
#     n1=len(arr1)
#     n2=len(arr2)
#     result=[]*(n1+n2)
#     for i in range(0,n1):
#         for j in range(0,n2):
#             for k in range(0,n1+n2):
#                 if k<(n1+n2):
#                     if i<n1 and k%2==0:
#                         result.append(arr1[i])
#                     elif j<n2 and k%2!=0:
#                         result.append(arr2[j])
#                     else:
#                         if i<n1:
#                             result.append(arr1[i])
#                         elif j<n2:
#                             result.append(arr2[j])
#     return result


# arr1=intArr()
# arr2=intArr()
# final_array=mergeArr(arr1,arr2)
# print(final_array)
#in above i have taken 3 loops i,j,k nested loop  so make it simpler and structured
#Use k for the number of cycles, i and j for looping (arr1 and arr2 respectively)



def intArr():
    l1=[]
    while True:
        try:
            n=int(input("Enter the element: "))
            l1.append(n)
        except Exception as e:
            return l1

def mergeArr(arr1,arr2):
    i,j=0,0
    n1=len(arr1)
    n2=len(arr2)
    result=[]
    for k in range(0,n1+n2):
        if k<(n1+n2):
            if i<n1 and k%2==0:
                result.append(arr1[i])
                i+=1
            elif j<n2 and k%2!=0:
                result.append(arr2[j])
                j+=1
            else:
                if i<n1:
                    result.append(arr1[i])
                    i+=1
                elif j<n2:
                    result.append(arr2[j])
                    j+=1
    return result


arr1=intArr()
arr2=intArr()
final_array=mergeArr(arr1,arr2)
print(final_array)



# Enter the element: 1
# Enter the element: 2
# Enter the element: 3
# Enter the element: 4
# Enter the element: 
# Enter the element: 9
# Enter the element: 8
# Enter the element: 7
# Enter the element: 
# [1, 9, 2, 8, 3, 7, 4]