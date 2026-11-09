n=int(input("Enter number: "))

count=1
result=1 # lowercase
alpha = 96

for i in range(1,n+1):
    for j in range(1,n+1):
        print(chr(alpha + count), end=" ")
        count += 1

        if count > 26:
            count = 1
            result *= -1
            if result < 0:
                alpha = 64
            else:
                alpha = 96

    print()