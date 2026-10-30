n=int(input("Enter: "))


for i in range(1,n+1):
    for j in range(i,n+i):
        print(chr(64+j),end="")

    print()

# Enter: 4
# ABCD
# BCDE
# CDEF
# DEFG