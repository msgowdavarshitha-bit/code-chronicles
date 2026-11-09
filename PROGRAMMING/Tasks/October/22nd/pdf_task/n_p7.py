n = int(input("Enter: "))

for i in range(1, n + 1):
    
    for j in range(i, n * 2 - i + 1):
        if j <= n:
            print(j, end=" ")
        else:
            print(n * 2 - j, end=" ")
    print()


# Enter: 5
# 1 2 3 4 5 4 3 2 1 
# 2 3 4 5 4 3 2 
# 3 4 5 4 3 
# 4 5 4 
# 5 