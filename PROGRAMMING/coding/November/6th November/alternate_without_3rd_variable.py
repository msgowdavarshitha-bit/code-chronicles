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
    for k in range(0,n1+n2):
        if k<n1+n2:
            if i<n1 and k%2==0:
                # arr1.insert(k,arr1[i])    since i'm inserting into the arr1, no need to add that just insert the arr2 elements 
                #If you i add this line again the arr1 elements are repeated which is wrong 
                i+=1
            elif j<n2 and k%2!=0:
                arr1.insert(k,arr2[j])
                j+=1
            else:
                if i<n1:
                    # arr1.insert(k,arr1[i])
                    #  since i'm inserting into the arr1, no need to add that just insert the arr2 elements 
                    #If you i add this line again the arr1 elements are repeated which is wrong 
                    i+=1
                elif j<n2:
                    arr1.insert(k,arr2[j])   
                    j+=1             
arr1=intArr()
arr2=intArr()
mergeArr(arr1,arr2)
print(arr1)
