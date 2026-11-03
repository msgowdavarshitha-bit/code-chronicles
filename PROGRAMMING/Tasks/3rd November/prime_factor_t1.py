# 13195


def isPrime(n):
    # current_max_element,current_index=-2**31,-1

    if n<2:
        return False

    count=0
    arr=[]
    i=1

    while i*i<=n:
        if n%i==0:
            arr.append(i)
            count+=1

            if i!=(n//i):
                arr.append(n//i)
                count+=1
        i+=1
    return max(arr)


n=13195
print(isPrime(n))