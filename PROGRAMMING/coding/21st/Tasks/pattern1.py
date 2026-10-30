n=int(input("Enter the number: "))

count = n * (n + 1) // 2  #use this formula 

for i in range(n,1-1,-1):
    for j in range(1,i+1):
        print(count,end=" ")
        count-=1
     
    print() 



n = int(input("Enter the number: "))

count = 0
for i in range(n, 1-1, -1):
    count += i

for i in range(n, 1-1, -1):
    for j in range(1,i+1):
        print(count, end=" ")
        count -= 1
    print()


# Enter the number: 4
# 10 9 8 7 
# 6 5 4 
# 3 2 
# 1 