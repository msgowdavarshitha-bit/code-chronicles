print("10-11-2026")
print("Merge sort")

#IMPORTANT:--
# NOTE :-
#it works on the principle of divide and conquer rule

#3 parts Merge sort
#1. divide the array to its least form
#2. Start merging the array into 3rd temporary memory
#3. update the sorted values from 3rd memory to input memory


def intArr():
    l1=[]
    while True:
        try:
            n=int(input("Enter the element: "))
            l1.append(n)
        except Exception as e:
            return l1


#2.merge in 3rd m/m and update it in a original arr[]

def mergeSortMerging(arr,start,mid,end):
    i,j=start,(mid+1)
    res=[]

    #cycles
    for k in range(0,(mid+end)+1):
        if i<=mid and j<=mid:
            if arr[i]<arr[j]:
                res.append(arr[i])
                i+=1
            else:
                res.append(arr[j])
                j+=1
        else:
            #for extra values
            if i<=mid:
                res.append(arr[i])
                i+=1
            else:
                res.append(arr[j])
                j+=1

    #update the original array
    for k in range(0,len(res)):
        arr[start]=res[k]
        start+=1


# Divide the array
def mergeDivision(arr,start,end):
    #base condition
    if start>=end:
        return

    mid=(start+end)//2
    #LHS division
    mergeDivision(arr,start,mid)

    #RHS division
    mergeDivision(arr,(mid+1),end)

    #merging
    mergeSortMerging(arr,start,mid,end)


arr=intArr()
print("Un-Sorted array: ",arr)
mergeDivision(arr,0,len(arr)-1)
print("Sorted array: ",arr)







print("=============================================================="*2)

print("10-11-2026")
print("Merge sort")

# NOTE: Merge sort works on the divide and conquer principle
# 1. Divide the array down to single elements
# 2. Merge the pieces into a 3rd temporary list
# 3. Copy the sorted values from the temporary list back into the original array


def intArr():
    l1 = []
    while True:
        try:
            n = int(input("Enter the element: "))
            l1.append(n)
        except ValueError:      # type a non-number (e.g. just press Enter) to stop
            return l1


# Merge arr[start..mid] and arr[mid+1..end] using a temp list
def mergeSortMerging(arr, start, mid, end):
    i, j = start, mid + 1
    res = []

    for k in range(end - start + 1):
        if i <= mid and j <= end:
            if arr[i] <= arr[j]:
                res.append(arr[i])
                i += 1
            else:
                res.append(arr[j])
                j += 1
        else:
            # one half is exhausted, copy the remaining values
            if i <= mid:
                res.append(arr[i])
                i += 1
            else:
                res.append(arr[j])
                j += 1

    # update the original array
    for k in range(len(res)):
        arr[start] = res[k]
        start += 1


# Divide the array
def mergeDivision(arr, start, end):
    # base condition: 0 or 1 element
    if start >= end:
        return

    mid = (start + end) // 2

    mergeDivision(arr, start, mid)        # left half
    mergeDivision(arr, mid + 1, end)      # right half
    mergeSortMerging(arr, start, mid, end)  # merge both halves


arr = intArr()
print("Un-Sorted array: ", arr)
mergeDivision(arr, 0, len(arr) - 1)
print("Sorted array: ", arr)