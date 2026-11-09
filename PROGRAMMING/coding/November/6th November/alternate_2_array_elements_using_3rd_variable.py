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
    result=[]*(n1+n2)
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