# # 13195


# def isPrime(n):
#     # current_max_element,current_index=-2**31,-1

#     if n<2:
#         return False

#     count=0
#     arr=[]
#     i=1

#     while i*i<=n:
#         if n%i==0:
#             arr.append(i)
#             count+=1

#             if i!=(n//i):
#                 arr.append(n//i)
#                 count+=1
#         i+=1
#     return max(arr)


# n=13195
# print(isPrime(n))



def largest_prime_factor(n):
    largest = 1
    while n % 2 == 0:
        largest = 2
        n //= 2
    i = 3
    while i * i <= n:
        while n % i == 0:
            largest = i
            n //= i
        i += 2
    if n > 1:
        largest = n
    return largest


t = int(input("Enter the input: "))
for _ in range(t):
    print(largest_prime_factor(int(input())))